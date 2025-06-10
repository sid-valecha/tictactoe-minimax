import streamlit as st
from game import TicTacToe

if 'game' not in st.session_state:
    st.session_state.game = TicTacToe()
if 'status' not in st.session_state:
    st.session_state.status = "Your turn (You are O)"
if 'disable_buttons' not in st.session_state:
    st.session_state.disable_buttons = False

game = st.session_state.game
st.title("Tic-Tac-Toe: Human vs AI")
st.subheader(st.session_state.status)

for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell = game.board[i][j]
        button_label = cell if cell != ' ' else ' '
        if cols[j].button(button_label, key=f"{i}-{j}", disabled=(cell != ' ' or st.session_state.disable_buttons)):
            if game.board[i][j] == ' ':
                game.board[i][j] = 'O'
                if game.is_winner('O'):
                    st.session_state.status = "You win! 🎉"
                    st.session_state.disable_buttons = True
                elif game.is_full():
                    st.session_state.status = "It's a tie!"
                    st.session_state.disable_buttons = True
                else:
                    ai_move = game.best_move()
                    game.board[ai_move[0]][ai_move[1]] = 'X'
                    if game.is_winner('X'):
                        st.session_state.status = "AI wins! 🤖"
                        st.session_state.disable_buttons = True
                    elif game.is_full():
                        st.session_state.status = "It's a tie!"
                        st.session_state.disable_buttons = True

if st.button("Reset Game"):
    st.session_state.game = TicTacToe()
    st.session_state.status = "Your turn (You are O)"
    st.session_state.disable_buttons = False