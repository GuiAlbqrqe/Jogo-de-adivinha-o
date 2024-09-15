import streamlit as st
from random import randint

st.title('Jogo do Número Secreto')

st.write('**************************************')
st.write('Seja bem-vindo ao jogo do Número Secreto!')
st.write('**************************************')

# Inicializando o número secreto e as variáveis de controle
if 'numero_secreto' not in st.session_state:
    st.session_state.numero_secreto = randint(1, 100)  # Número secreto entre 1 e 100

if 'numeros_usados' not in st.session_state:
    st.session_state.numeros_usados = []

if 'jogo_finalizado' not in st.session_state:
    st.session_state.jogo_finalizado = False

# Input do número (entre 1 e 100)
numero_escolhido = st.number_input('Escolha um número de 1 a 100:', min_value=1, max_value=100, step=1)

# Exibir números já usados de forma bonita
if st.session_state.numeros_usados:
    numeros_formatados = ", ".join(map(str, st.session_state.numeros_usados))
    st.write(f"Números já usados: {numeros_formatados}")

# Botão para verificar o número, só mostra se o jogo não foi finalizado
if not st.session_state.jogo_finalizado:
    if st.button('Verificar número'):
        if numero_escolhido in st.session_state.numeros_usados:
            st.warning(f"Você já usou o número {numero_escolhido}!")
        else:
            st.session_state.numeros_usados.append(numero_escolhido)  # Adiciona o número à lista de números usados
            
            if numero_escolhido == st.session_state.numero_secreto:
                st.balloons()  # Mostra balões na tela
                st.success(f"Parabéns! O número secreto é {st.session_state.numero_secreto}! 🎉🎉🎉")
                st.session_state.jogo_finalizado = True
            else:
                st.error("Você errou! Tente novamente.")


# Botão para reiniciar o jogo, aparece só quando o jogo é finalizado
if st.session_state.jogo_finalizado:
    if st.button('Recomeçar jogo'):
        # Reinicia o jogo manualmente (resetando as variáveis)
        st.session_state.numero_secreto = randint(1, 100)  # Reiniciar entre 1 e 100
        st.session_state.numeros_usados = []
        st.session_state.jogo_finalizado = False