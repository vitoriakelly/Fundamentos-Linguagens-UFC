% Fatos
pai(joao, maria).
pai(joao, jose).
mae(ana, maria).
mae(ana, jose).
pai(jose, laura).
mae(maria, lucas).

% Regras
irmao(X, Y) :- pai(P, X), pai(P, Y), mae(M, X), mae(M, Y), X \= Y.
avo(X, Y) :- pai(X, P), pai(P, Y).
avo(X, Y) :- mae(X, M), pai(M, Y).
