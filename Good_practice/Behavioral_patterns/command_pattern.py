"""Účelem vzoru chování Command je oddělit objekty, které odesílají požadavky, od objektů,
které přijímají jejich výsledky. Umožňuje to zavedením objektu představujícího příkaz,
který takový proces provádí. Volitelně může být příkaz také schopen vrátit zpět výsledek takového procesu.

Zabalením provádění procesu do samostatného objektu zachováme pravidla SOLID odstraněním
potenciální silné vazby mezi odesílatelem a příjemcem výsledku požadavku."""

"""Hlavním prvkem, který musíme vytvořit, je společný objekt představující provádění procesu. 
Volitelně může být možné zrušit provedení příkazu.

Objekty potřebné k provedení příkazu nejčastěji získává v konstruktoru implementace."""

