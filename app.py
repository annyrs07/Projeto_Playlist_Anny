
import streamlit as st

# python -m streamlit run app.py

# --------------------------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Anny Playlist')

# Dados de exemplo
generos_musical = ["POP", "KPOP", "Sertanejo", "Bossa Nova", "Eletrônica"]

# Dicionário relacionando gêneros aos seus livros
cantor_por_genero_musical = {
    "POP": ["Michael Jackson", "Bruno Mars"],
    "KPOP": ["BTS", "BLACKPINK"],
    "Sertanejo": ["Marília Mendonça", "Gusttavo Lima"],
    "Bossa Nova": ["Tom Jobim", "Vinícius de Moraes"],
    "Eletrônica": ["Alok", "Pedro Sampaio"]
}

# Selectbox para escolher o gênero
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos_musical)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    cantor_selecionado = st.sidebar.selectbox(
        "Selecione um cantor:", 
       cantor_por_genero_musical[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and cantor_selecionado:
    st.write(f"**Cantor selecionado:** {cantor_selecionado}")
    st.write(f"**Gênero musical:** {genero_selecionado}")
    st.image(f"{cantor_selecionado}.png", width=300)

if genero_selecionado == "POP" and cantor_selecionado == "Michael Jackson": 
    st.markdown('### Michael Jackson (1958 – 2009)')
    st.markdown('Michael Jackson, conhecido como o "Rei do Pop", nasceu em Gary, Indiana (EUA). Desde criança, destacou-se como vocalista do grupo The Jackson 5. Na carreira solo, revolucionou a música pop com álbuns icônicos como Thriller (o mais vendido da história), Bad e Dangerous. Jackson ficou famoso por seus videoclipes inovadores, danças marcantes como o moonwalk, e seu alcance vocal impressionante. Apesar de polêmicas pessoais, é considerado um dos maiores artistas de todos os tempos, tendo influenciado gerações na música, moda e cultura pop.')
    st.video('https://www.youtube.com/watch?v=h_D3VFfhvs4&list=RDh_D3VFfhvs4&start_radio=1')
    st.link_button(label="Spotify", url="https://open.spotify.com/intl-pt/artist/3fMbdgg4jU18AjLCKBhRSm ")

elif genero_selecionado == "POP" and cantor_selecionado == "Bruno Mars":
    st.markdown('### Bruno Mars (1985 – )')
    st.markdown('Bruno Mars, nome artístico de Peter Gene Hernandez, nasceu no Havaí. Cantor, compositor, produtor e multi-instrumentista, é conhecido por sua versatilidade ao misturar pop, funk, soul, R&B e reggae. Lançou sucessos como Just the Way You Are, Grenade, Locked Out of Heaven e Uptown Funk (com Mark Ronson). Vencedor de vários prêmios Grammy, é reconhecido pela energia contagiante nos palcos, performances dançantes e carisma. É considerado um dos artistas mais completos da música atual.')
    st.video("https://www.youtube.com/watch?v=ekr2nIex040&list=RDekr2nIex040&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/bruno%20mars")

elif genero_selecionado == "KPOP" and cantor_selecionado == "BTS":
    st.markdown('### BTS (2013 – )')
    st.markdown('BTS é um grupo sul-coreano formado pela empresa Big Hit Entertainment em 2013. Integrado por RM, Jin, Suga, J-Hope, Jimin, V e Jungkook, conquistou o mundo com seu estilo que mistura K-pop, hip-hop e R&B. As letras abordam temas como juventude, saúde mental e autoconhecimento. Com hits como Dynamite, Butter e Boy With Luv, o BTS quebrou recordes mundiais e foi indicado ao Grammy. Tornou-se um fenômeno cultural global, influenciando moda, comportamento e a expansão da cultura coreana.')
    st.video("https://www.youtube.com/watch?v=gdZLi9oWNZg&list=RDgdZLi9oWNZg&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/bts")

elif genero_selecionado == "KPOP" and cantor_selecionado == "BLACKPINK":
    st.markdown('### BLACKPINK (2016 – )')
    st.markdown('BLACKPINK é um grupo feminino de K-pop formado pela YG Entertainment em 2016. Integrado por Jisoo, Jennie, Rosé e Lisa, ganhou destaque mundial com hits como Boombayah, Kill This Love e How You Like That. O grupo é conhecido por performances marcantes, coreografias poderosas e visuais impactantes. Tornou-se o primeiro girl group de K-pop a se apresentar no festival Coachella e alcançou sucesso internacional, consolidando-se como um dos maiores grupos femininos do mundo.')
    st.video("https://www.youtube.com/watch?v=CgCVZdcKcqY&list=RDCgCVZdcKcqY&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/blackpink")

elif genero_selecionado == "Sertanejo" and cantor_selecionado == "Marília Mendonça":
    st.markdown('### Marília Mendonça (1995 – 2021)')
    st.markdown('Marília Mendonça foi uma das maiores cantoras e compositoras brasileiras, conhecida como a "Rainha da Sofrência". Nascida em Goiás, destacou-se no sertanejo com músicas que retratavam o cotidiano amoroso, como Infiel, Eu Sei de Cor e Todo Mundo Vai Sofrer. Ganhou diversos prêmios e marcou a música brasileira com sua voz potente e letras emocionantes. Sua carreira foi interrompida tragicamente em 2021, em um acidente aéreo, mas seu legado segue vivo entre os fãs.')
    st.video("https://www.youtube.com/watch?v=gwS9nU4Aavw")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/marilia%20mendon%C3%A7a")

elif genero_selecionado == "Sertanejo" and cantor_selecionado == "Gusttavo Lima":
    st.markdown('### Gusttavo Lima (1989 – )')
    st.markdown('Nivaldo Batista Lima, conhecido como Gusttavo Lima, é um cantor e compositor sertanejo brasileiro. Nascido em Minas Gerais, ficou famoso com a música Balada Boa (Tchê Tcherere Tchê Tchê). Consolidou sua carreira com os projetos Buteco do Gusttavo Lima, trazendo sucessos como Milu, Apelido Carinhoso e Cem Mil. É considerado um dos principais nomes do sertanejo universitário e dono de uma das carreiras mais lucrativas da música brasileira.')
    st.video("https://www.youtube.com/watch?v=14C28JSO-sg&list=RD14C28JSO-sg&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Gusttavo%20Lima")

elif genero_selecionado == "Bossa Nova" and cantor_selecionado == "Tom Jobim":
    st.markdown('### Tom Jobim (1927 – 1994)')
    st.markdown('Antônio Carlos Jobim foi um compositor, pianista, cantor e maestro brasileiro, um dos criadores da Bossa Nova. Suas canções, como Garota de Ipanema, Águas de Março e Chega de Saudade, ganharam projeção internacional. Trabalhou com artistas como Vinícius de Moraes, João Gilberto e Frank Sinatra. Jobim é considerado um dos maiores gênios da música brasileira, responsável por popularizar a Bossa Nova no mundo e deixar um legado atemporal.')
    st.video("https://www.youtube.com/watch?v=5LfaYKdqfnY&list=RD5LfaYKdqfnY&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Tom%20Jobim")

elif genero_selecionado == "Bossa Nova" and cantor_selecionado == "Vinícius de Moraes":
    st.markdown('### Vinícius de Moraes (1913 – 1980)')
    st.markdown('Vinícius de Moraes foi poeta, diplomata, dramaturgo e letrista brasileiro. Conhecido como "O Poetinha", destacou-se na literatura e na música, sendo parceiro de nomes como Tom Jobim, Toquinho e Baden Powell. Escreveu clássicos da MPB como Garota de Ipanema, Eu Sei que Vou te Amar e A Felicidade. Sua poesia falava de amor, cotidiano e brasilidade. É um dos nomes mais importantes da cultura brasileira do século XX.')
    st.video("https://www.youtube.com/watch?v=Fz0eddwTjnk&list=RDFz0eddwTjnk&start_radio=1")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Vin%C3%ADcius%20de%20Moraes")

elif genero_selecionado == "Eletrônica" and cantor_selecionado == "Alok":
    st.markdown('### Alok (1991 – )')
    st.markdown('Alok Achkar Peres Petrillo é um DJ e produtor musical brasileiro de música eletrônica. Reconhecido mundialmente, entrou para a lista da revista DJ Mag como um dos melhores DJs do mundo. Sucessos como Hear Me Now, Ocean e Fuego o tornaram conhecido além das pistas de dança. É pioneiro no cenário eletrônico brasileiro e também realiza projetos sociais através do Instituto Alok.')
    st.video("https://www.youtube.com/watch?v=ZvJqGOfsn8A")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Alok")

elif genero_selecionado == "Eletrônica" and cantor_selecionado == "Pedro Sampaio":
    st.markdown('### Pedro Sampaio (1997 – )')
    st.markdown('Pedro Sampaio é um DJ, cantor e produtor musical brasileiro. Ficou conhecido por seus remixes criativos e músicas autorais que misturam funk, pop e música eletrônica. Lançou sucessos como Sentadão, Galopa e Dançarina, que alcançaram o topo das paradas. Reconhecido por sua energia nos shows e pela inovação nas produções, é um dos artistas em ascensão da cena musical brasileira.')
    st.video("https://www.youtube.com/watch?v=_zKnEm9xPWw")
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Pedro%20Sampaio")


