import unidecode

def responder(msg):
    msg_original = msg
    msg = unidecode.unidecode(msg.lower()).strip()

    # -------------------------
    # Cumprimentos
    # -------------------------
    cumprimentos = [
        "ola", "oi", "opa", "eae", "eai", "boa noite", "bom dia", "boa tarde",
        "salve", "oii", "ola!", "oi!", "hey", "hello" , "oie"
    ]

    if any(c in msg for c in cumprimentos):
        return "Olá! Que bom ter você aqui! Como posso te ajudar?"

    # -------------------------
    # Orçamento
    # -------------------------
    if any(x in msg for x in ["orcamento", "preco", "preço", "quanto custa", "valor"]):
        return (
            "Claro! Posso ajudar com orçamento.\n"
            "Qual tipo de serviço você precisa? Ex: reforma, pintura, alvenaria, manutenção..."
        )

    # -------------------------
    # Serviços oferecidos
    # -------------------------
    if any(x in msg for x in ["servico", "serviço", "o que voces fazem", "quem são vcs?" , "fazem o que", "atuam com o que"]):
        return (
            "Trabalhamos com construção civil completa: obra, alvenaria, reformas, pintura, gesso "
            "e serviços de acabamento. O que você precisa fazer?"
        )

    # -------------------------
    # Sobre a empresa
    # -------------------------
    if any(x in msg for x in ["quem sao voces", "o que é rvcon", "sobre empresa", "quem é a empresa"]):
        return (
            "A RVcon é especializada em construção civil atuando com qualidade, segurança e "
            "prazo. Fazemos desde pequenas reformas até obras completas!"
        )

    # -------------------------
    # Localização
    # -------------------------
    if "onde ficam" in msg or "localizacao" in msg or "endereco" in msg:
        return "Estamos localizados em Joinville/SC e atendemos toda a região."

    # -------------------------
    # Prazo
    # -------------------------
    if any(x in msg for x in ["prazo", "quanto tempo", "demora"]):
        return (
            "O prazo depende do tipo de obra. Se quiser, me diga qual serviço deseja "
            "e posso estimar o tempo."
        )

    # -------------------------
    # Contato
    # -------------------------
    if "contato" in msg or "whatsapp" in msg or "telefone" in msg:
        return "Você pode falar diretamente com a RVcon pelo WhatsApp! O botão está no início da página."

    # -------------------------
    # Mensagem vazia ou muito curta
    # -------------------------
    if msg.strip() in ["", ".", "?", "!"]:
        return "Parece que sua mensagem veio vazia. Pode repetir, por favor?"

    # -------------------------
    # Perguntas genéricas (fallback)
    # -------------------------
    return (
        "Desculpe, não entendi muito bem. "
        "Você precisa de orçamento, informações sobre serviços ou deseja falar com a RVcon?"
    )
