from aiogram import Router, F
# from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

# from keyboards.simple_row import make_row_keyboard
import states
import text
import process
import kb

router = Router()


available_variants = ['1', '2', '3', '4', '5']


@router.message(F.text == text.choosing_theme)
async def choosing_theme(message: Message, state: FSMContext):
    await message.answer(
        text=('\n').join(text.list_of_themes),
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(states.Gen.choosing_theme)


@router.message(states.Gen.choosing_theme, F.text.in_(available_variants))
async def choosing_quantity(message: Message, state: FSMContext):
    await state.update_data(chosen_variant=message.text)
    await message.answer(
        text=text.choosing_number_of_variants,
    )
    await state.set_state(states.Gen.choosing_number_of_variants)


@router.message(states.Gen.choosing_number_of_variants)
async def smth(message: Message, state: FSMContext):
    await state.update_data(number_of_variants=int(message.text))
    await state.update_data(used_variants=1)
    await state.set_state(states.Gen.generating_variant)
    data = await state.get_data()
    await message.answer(
        text=(process.generate_variant(data['chosen_variant'], int(message.text)))[0][0],
    )
    await message.answer(
        text=(process.generate_variant(data['chosen_variant'], int(message.text)))[0][1],
    )
    await state.set_state(states.Gen.getting_answer)


@router.message(states.Gen.getting_answer)
async def get_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text.lower() in (
        (process.generate_variant(data['chosen_variant'],
         data['number_of_variants']))[data['used_variants'] - 1][3]).split('; '):
        await message.answer('Верно', reply_markup=kb.right_answer_choice)
        await state.set_state(states.Gen.next_or_get_answer)
    else:
        await message.answer('Неверно', reply_markup=kb.fault)
        await state.set_state(states.Gen.one_more_time_or_answer)


@router.message(states.Gen.next_or_get_answer, F.text == text.show_solution)
async def show_soulution(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer((process.generate_variant(data['chosen_variant'], data['number_of_variants']))[0][4],
                         reply_markup=kb.next_step)
    await state.set_state(states.Gen.next_or_get_answer)


@router.message(states.Gen.next_or_get_answer, F.text == text.next)
async def next_step(message: Message, state: FSMContext):
    data = await state.get_data()
    if data['used_variants'] != data['number_of_variants']:
        await state.update_data(used_variants=data['used_variants'] + 1)
        await message.answer(
            text=(process.generate_variant(
                data['chosen_variant'],
                data['number_of_variants']))[data['used_variants'] - 1][0],
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text=(process.generate_variant(
                data['chosen_variant'],
                data['number_of_variants']))[data['used_variants'] - 1][1],
        )
        await state.set_state(states.Gen.getting_answer)
    else:
        await message.answer(text.variants_are_over, reply_markup=kb.main_menu)
        await state.set_state(states.Gen.choosing_theme)


@router.message(states.Gen.one_more_time_or_answer, F.text == text.one_more_time)
async def one_more_time(message: Message, state: FSMContext):
    await message.answer(text.retry_answer)
    await state.set_state(states.Gen.getting_answer)


@router.message(states.Gen.one_more_time_or_answer, F.text == text.show_solution)
async def show_solution(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        (process.generate_variant(data['chosen_variant'], data['number_of_variants']))[data['used_variants'] - 1][4],
        reply_markup=kb.next_step
        )
    await state.set_state(states.Gen.next_or_get_answer)
