#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('\n********** Curriculo de Cibele Danuza Marques Cravo em Python **********\n')


# In[ ]:


escolha = 0
while escolha != 7:
        print("\nQual seção do meu currículo deseja visualizar? \n")
        print("1 - Dados pessoais e de contato")
        print("2 - Resumo Profissional")
        print("3 - Formação Acadêmica")
        print("4 - Histórico Profissional")
        print("5 - Informática e Inglês")
        print("6 - Certificações, Palestras e Cursos Extracurriculares")
        print('7 - Sair')
        
        escolha = input("\nDigite sua opção (1/2/3/4/5/6/7): \n")
        
        if escolha == '1':
            print('\nTelefone: (13)99133-6071 /(13)99157-2623 \nEmail: cibeledanuza@gmail.com \nLinkedin: https://www.linkedin.com/in/cibeledmarques \nGithub: https://github.com/CibeleMarquesCravo')

        elif escolha == '2':
            print('\nGerente Administrativa com um histórico sólido de sucesso em liderança de equipes e otimização de processos.Agora, em transição de carreira para a área de Análise de Dados, trago comigo habilidades adquiridas na gestão e a capacidade de mergulhar em dados de maneira estruturada. Com conhecimentos básicos em linguagem de programação Python, busco aplicar minha perspicácia analítica e visão estratégica para extrair insights valiosos e embasar decisões informadas. Minha experiência anterior como líder e      organizadora contribui para minha capacidade de traduzir complexidades de dados em informações claras e acionáveis. Desejo     embarcar em desafios estimulantes que me permitam desenvolver minhas competências analíticas, enquanto continuo a utilizar     minhas habilidades de gestão para liderar projetos de análise de dados de maneira eficaz. Com uma combinação única de expertise administrativa e crescente aptidão em análise de dados, estou pronta para trilhar um novo caminho profissional com entusiasmo e dedicação.')

        elif escolha == '3':
            print('MBA - Gestão Estratégica de Projetos e Metodologias Ágeis Descomplica Faculdade Digital - Concluído em 2022.')
            print('Bacharel em Sistemas de Informação Fals – Faculdade do Litoral Sul Paulista – Concluído em 2009.')

        elif escolha == '4':
            print('Mondiconect (11/2018 à 12/2021)')
            print('Serviços administrativos online')
            print('Cargo: Assistente Virtual Freelancer')
            print('PRINCIPAIS PROJETOS E RESPONSABILIDADES:')
            print('\n')
            print('\n  Interação com os clientes, respondendo a perguntas, fornecendo informações, resolvendo problemas e oferecendo suporte geral. Compreensão e respostas a consultas de forma rápida e precisa, garantindo uma experiência positiva para o cliente. Responsável por fazer a triagem e direcionamento das solicitações recebidas para a equipe adequada.  Identificação da natureza do problema ou solicitação e encaminhamento a pessoa correta para lidar com a situação de forma mais eficaz. Organização e controle de     entrada de tickets de clientes, realizando cadastros e agendamentos e outras tarefas, como pesquisas, cotações, elaboração de  planilhas entre outros. Personalização de interações com base nas informações fornecidas pelos usuários.Lembrando preferências, histórico de compras ou outras informações relevantes para fornecer uma experiência mais personalizada e relevante. Coleta de  dados e informações durante as interações com os usuários para identificar tendências, padrões e insights úteis para melhorar a eficiência e a qualidade do atendimento ao cliente.')
            print('\n')
            print('BANCO BRADESCO S/A (01/2008 a 11/2015)')
            print('(Bancos)')
            print('Cargo: Gerente Administrativa')
            print('PRINCIPAIS PROJETOS E RESPONSABILIDADES:')
            print('\n')
            print('\n Responsável por supervisionar todas as operações bancárias, desde a abertura de contas e empréstimos até a gestão de depósitos e transações. Garantindo que todas as atividades sejam realizadas de acordo com as políticas, procedimentos e regulamentações  estabelecidos. Encarregada de gerenciar e orientar as equipes que trabalham nas várias áreas do banco, como atendimento ao     cliente, caixa, empréstimos e operações. Atribuindo tarefas, oferecendo treinamento, avaliando o desempenho e fornecendo       suporte necessário para garantir o desenvolvimento profissional dos funcionários. Desenvolvimento e implementação de planos    estratégicos para o banco. Trabalhando em estreita colaboração com a equipe executiva para definir metas, identificar          oportunidades de crescimento, melhorar a eficiência operacional e maximizar os resultados financeiros. Garantir que o banco    esteja em conformidade com as regulamentações governamentais e as políticas internas, com a identificação e gerenciamento dos  riscos associados às atividades bancárias, implementando controles internos e procedimentos de segurança para proteger os      ativos do banco e os interesses dos clientes. Atuação como representante do banco, estabelecendo e mantendo relacionamentos    sólidos com os clientes existentes e potenciais, sempre em busca de oportunidades de negócios, respondendo a consultas,        resolvendo problemas e garantindo um excelente atendimento ao cliente. Análise dos dados financeiros do banco, preparação de   relatórios e apresentação de informações relevantes à equipe executiva. Monitoramento do desempenho financeiro, identificando  áreas de melhoria e tomando decisões estratégicas com base nas análises realizadas. Contribuição para o desenvolvimento e      revisão contínua das políticas e procedimentos internos do banco. Garantindo que as diretrizes operacionais estejam            atualizadas, sejam seguidas corretamente e estejam alinhadas com as mudanças regulatórias e do mercado.')

        elif escolha == '5':
            print('Pacote Office: Conhecimentos em elaboração de documentos e planilhas em Word e Excel, apresentações em Power Point e Google    Docs. ')
            print('Inglês básico - intermediário, em curso.')
    
        elif escolha == '6':
            print('Scrum Foundation Professional Certificate - SFPC - CertiProf - Dez/2021')
            print('Jira e Confluence - Canal Valor - Out/2022')
            print('CAC - Certified Agile Coaching - Massimus - Fev/2023 - 72h')
            print('Metricas para times ágeis - Udemy - Jun/2023')
            print('Fundamentos de Linguagem Python para Análise de Dados e Data Science - Data Science Academy - Em curso')
    
        elif escolha == '7':
            break
        else:
            print('Escolha inválida, retorne ao menu inicial')
        

