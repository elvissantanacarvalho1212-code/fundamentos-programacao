# Documento de Design de Jogo (GDD) — "Neon Tide: Eclipse Protocol"

## 1. Conceito

**Nome do jogo**
- Neon Tide: Eclipse Protocol

**Gênero principal e secundário**
- Principal: Action RPG cooperativo com foco em combate tático em tempo real.
- Secundário: Roguelite narrativo com exploração urbana e gestão de base.

**Plataforma**
- PC e Console (PlayStation e Xbox), com cross-play planejado.

**Público-alvo**
- Jogadores 16–35 anos que curtem ação visceral, progressão profunda, narrativa sci‑fi e cooperação.

**Proposta única (USP)**
- Combate tático “fluido” que combina **parry sincronizado em equipe** com **hacking ambiental** em tempo real, gerando momentos de alta coordenação. Um sistema de “Marés de Neon” altera o mundo vivo a cada sessão, mudando rotas, inimigos e objetivos sem perder consistência narrativa.

---

## 2. História e Universo

**Lore detalhada**
- Em 2169, megacorporações drenam energia do oceano de dados quântico (“Mar de Neon”), uma infraestrutura que mantém a vida urbana. Um colapso iminente cria anomalias chamadas **Eclipses**, distorcendo bairros e memórias. Uma célula clandestina, **Véu**, tenta restaurar o equilíbrio, enquanto corporações armam forças privadas para dominar o caos.

**Mundo do jogo**
- **Cidade‑Estado Vanta**: megacidade vertical com camadas sociais distintas (Cúpula, Núcleo, Submerso).
- **Mar de Neon**: dimensão digital-física que invade o espaço real durante Eclipses.
- **Zonas Mutantes**: bairros onde realidade e dados se fundem, criando biomas neon.

**Personagens principais e vilões**
- **Lira** (Protagonista): ex‑engenheira de protocolos, líder de campo do Véu.
- **Kaito**: especialista em drones e combate de curta distância.
- **Sora**: hacker sensorial, controla o fluxo do Mar de Neon.
- **VILÃO: Archon Vale**: CEO da corporação Helix Dominion, busca controlar o Mar de Neon.
- **VILÃO: Eclipse Prime**: entidade emergente do colapso de dados, quer apagar identidades humanas.

**Evolução narrativa ao longo do gameplay**
- **Ato 1:** formação da equipe e primeiras incursões para salvar bairros.
- **Ato 2:** descoberta do núcleo do Mar de Neon e intrigas corporativas.
- **Ato 3:** guerra aberta contra Helix Dominion e confrontos com Eclipse Prime.
- **Endgame:** decisões morais afetam o futuro da cidade e liberam variações de final.

---

## 3. Gameplay (Core Loop)

**Mecânica principal**
- **Combate tático em tempo real**: esquiva, parry perfeito, habilidades sinérgicas e hacking do ambiente.

**Mecânicas secundárias**
- Exploração procedural com narrativa emergente.
- Sistema de “interfaces” que alteram habilidades em combate (builds híbridas).
- Gestão de base (Refúgio Véu) para upgrades e narrativa.

**Sistema de progressão**
- **Níveis de personagem** com talentos em três árvores: Combate, Tático, Suporte.
- **Upgrades de interface**: módulos que mudam o comportamento de habilidades.
- **Armas modulares** com slots de mods elementais.

**Sistema de recompensas**
- Loot inteligente (focado no estilo do jogador).
- Itens cosméticos e artefatos narrativos.
- Reputação com facções, desbloqueando missões exclusivas.

**Curva de dificuldade**
- Aumenta com a instabilidade do Mar de Neon: inimigos mais agressivos e ambientes mais perigosos.

**Exemplo prático de gameplay**
1. O time infiltra um bairro Eclipseado.
2. O jogador ativa um “Parry Sincronizado” para refletir projéteis e abrir brechas.
3. Sora hackeia um painel para derrubar drones inimigos.
4. O objetivo muda em tempo real: salvar civis presos num loop temporal.
5. Boss regional aparece, exigindo coordenação de habilidades.

---

## 4. Design de Fases

**Tipos de missões**
- Recuperação de dados.
- Resgate de civis ou VIPs.
- Sabotagem corporativa.
- Eliminação de alvos.

**Eventos especiais**
- **Surto Eclipse**: altera drasticamente o mapa e spawn de inimigos.
- **Corrupção de Rede**: exige hacks sequenciais sob pressão.

**Bosses (design e habilidades)**
- **Sentinela Oráculo**: escudos alternam entre estados, exigindo timing perfeito.
- **Nautilus Prime**: boss anfíbio digital com ataques AOE e tentáculos de dados.
- **Archon Vale (final)**: alterna entre combate direto e arenas hackeadas.

**Desafios diários e semanais**
- Daily: missões rápidas com modificadores (ex.: gravidade baixa, dano elétrico).
- Weekly: raid cooperativa com recompensas únicas.

---

## 5. UX / UI

**Layout das telas**
- HUD modular minimalista: saúde, energia e cooldowns em ícones circulares.
- Mapa holográfico dinâmico no canto inferior direito.

**Menus**
- Menu principal com acesso direto a matchmaking e base.
- Inventário com visualização 3D das armas.

**Feedback visual e sonoro**
- Parry perfeito gera pulso de neon e som metálico grave.
- Hacking bem‑sucedido exibe glitch visual satisfatório.

**Animações e fluidez**
- Animações fluidas, com transições suaves entre combate e exploração.
- Cancelamento de animação para jogabilidade responsiva.

---

## 6. Direção de Arte

**Estilo visual**
- Cyberpunk luminoso com inspiração em “bio‑neon”.

**Paleta de cores**
- Ciano, magenta e dourado contra fundos escuros.

**Design de personagens**
- Trajes modulares com LEDs dinâmicos reagindo ao estado emocional.

**Design de cenários**
- Ambientes com camadas digitais sobrepostas, criando ilusão de profundidade.

---

## 7. Áudio

**Trilha sonora**
- Synthwave híbrido com orquestrações tensas.

**Efeitos sonoros**
- Sons metálicos e digitais para armas e hacks.

**Áudio dinâmico baseado no gameplay**
- Música intensifica conforme a instabilidade do Eclipse.

---

## 8. Tecnologia

**Engine recomendada**
- Unreal Engine 5 (Nanite e Lumen).

**Linguagem de programação**
- C++ e Blueprints para prototipagem rápida.

**Arquitetura do projeto**
- Modular por sistemas: combate, IA, progressão, narrativa.
- Dados externos para balanceamento rápido.

**Otimização e performance**
- Streaming de níveis dinâmico.
- LODs agressivos e otimização de shaders.

---

## 9. Monetização (sem pay to win)

**Modelo de negócio**
- Premium + expansões e passes de temporada.

**Itens cosméticos**
- Skins de personagens, armas e efeitos visuais.

**Passes de temporada**
- Conteúdo narrativo, missões e cosméticos temáticos.

**Estratégias de retenção**
- Eventos regulares e missões cooperativas.

---

## 10. Social e Multiplayer

**Ranking**
- Ranking cooperativo por eficiência em missões.

**Sistemas sociais**
- Clãs, chat integrado e partilha de builds.

**Comunidade**
- Ferramentas de feedback e eventos com criadores.

**Eventos ao vivo**
- Eclipses globais com objetivos colaborativos.

---

## 11. Roadmap

**MVP**
- 1 cidade, 10 missões principais, 2 bosses, coop até 4 jogadores.

**Atualizações futuras**
- Novas zonas, armas e facções.

**Expansões e conteúdo sazonal**
- Expansões narrativas anuais com novos personagens.

---

## 12. Documentação Final

**Pitch do jogo**
- “Neon Tide” é um action RPG cooperativo em um mundo cyberpunk vivo, onde cada missão é única graças ao Mar de Neon que altera o cenário, os inimigos e a narrativa.

**Diferencial competitivo**
- Combate tático sincronizado + hacking ambiental em tempo real.

**Potencial de mercado**
- Alto apelo para fãs de Destiny, Warframe e RPGs cooperativos.

**Por que esse jogo pode ser um sucesso global**
- Combina ação frenética, cooperação social e narrativa emergente, criando replayability infinita.
