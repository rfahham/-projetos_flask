Configuração Inicial

    curl -fsSL "https://tsuru.io/get" | bash
    tsuru target add default hattps://tsuru.globoi.com -s
    tsuru login

Criar a APP
    tsuru app create <nome da aplicação> python --team QA --plan c0.5m1

Deploy no tsuru
    
    tsuru app deploy --app <nome da aplicação> .

Logs
    
    tsuru app log --follow --app <nome da aplicação>

Aumentar o plano da aplicação
    
    tsuru app-update --app <nome da aplicação> --plan, c1mi