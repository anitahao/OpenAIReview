\documentclass[12pt]{article}

\usepackage{fullpage}
\usepackage{amsmath,amsthm,amssymb,MnSymbol}
\usepackage{mathrsfs}
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=red,citecolor=blue,urlcolor=blue}


\theoremstyle{theorem}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{claim}[theorem]{Claim}

\newtheorem*{theorem*}{Question}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{remark}[theorem]{Remark}

\newlength{\probwidth}
\setlength{\probwidth}{4cm}




\newcommand{\nprob}[3]{
\begin{center}
\begin{tabular}{|r p{12cm} |}
\hline
\multicolumn{2}{|l|}{\textsc{#1}}\\
\textit{Instance:}& #2.\\
%\textit{Parameter:}& #3.\\
\textit{Problem:}& #3\\
\hline
\end{tabular}
\end{center}
}


\newcommand{\Dom}{\mathrm{dom}}
\newcommand{\Img}{\mathrm{im}}

\newcommand{\out}{\textit{out}}


\newcommand{\N}{\mathbb{N}}
\newcommand{\C}{\mathcal{C}}
\newcommand{\PTIME}{\mathsf{P}}
\newcommand{\eval}{\mathit{eval}}
\newcommand{\Log}{\mathit{Log}_{>1}}
\newcommand{\Logold}{\mathit{Log}}
\newcommand{\floor}[1]{\lfloor #1 \rfloor}
\newcommand{\len}{\mathit{len}}
\newcommand{\bit}{\mathit{bit}}
\newcommand{\res}{{\upharpoonleft}}


\renewcommand{\le}{\leqslant}
\renewcommand{\leq}{\leqslant}
\renewcommand{\ge}{\geqslant}
\renewcommand{\geq}{\geqslant}

\newcommand{\NEXP}{\mathsf{NEXP}}
\newcommand{\EXP}{\mathsf{EXP}}
\renewcommand{\P}{\mathsf{P}}
\newcommand{\PH}{\mathsf{PH}}
\newcommand{\NP}{\mathsf{NP}}
\newcommand{\PSPACE}{\mathsf{PSPACE}}
\newcommand{\Ppoly}{\mathsf{P/poly}}
\newcommand{\ioPpoly}{\mathsf{io}\text{-}\mathsf{P/poly}}
\newcommand{\SIZE}{\mathsf{SIZE}}

\newcommand{\PHP}{\mathit{PHP}}


\newcommand{\T}{\mathsf{T}}
\newcommand{\PV}{\mathsf{PV}}
\newcommand{\V}{\mathsf{V}}
\newcommand{\U}{\mathsf{U}}
\newcommand{\BASIC}{\mathsf{BASIC}}
\renewcommand{\S}{\mathsf{S}}


\newcommand{\Bd}{\textit{Bd}}
\renewcommand{\succ}{\textit{succ}}
\newcommand{\start}{\textit{start}}
\newcommand{\Start}{\textit{Start}}
\newcommand{\Fail}{\textit{Fail}}
\newcommand{\Next}{\textit{Next}}
\newcommand{\Unique}{\textit{Unique}}

\newcommand{\meyer}{\mu}


\newcommand{\q}[1]{\textup{``}\textit{#1}\textup{''}}

\newcommand{\Lg}{\textit{Log}}

\renewcommand{\ldots}{...}


\newcommand{\io}{\textup{io-}}
\renewcommand{\ae}{\textup{ae}}




\newcommand{\mrand}[1]{\marginpar{\tiny \textbf{M:} #1}}
\newcommand{\arand}[1]{\marginpar{\tiny \textbf{A:} #1}}


\begin{document}

\title{\bf From Gödel incompleteness to the consistency of circuit lower bounds
%Circuit lower bounds for exponential time\\ are consistent with $\S^1_2$
}

\author{Albert Atserias\\\small Universitat Polit\`{e}cnica de
  Catalunya\\[-1ex]\small and Centre de Recerca Matem\`atica \\[-1ex] \small
  Barcelona, Spain\\[-1ex]\small\url{atserias@cs.upc.edu} \and Moritz
  M\"uller\\\small Universit\"at Passau\\[-1ex] \small Passau,
  Germany\\[-1ex]\small\url{moritz.mueller@uni-passau.de} }

\maketitle

\begin{abstract} 
  We prove that the bounded arithmetic theory~$\S^1_2$ is consistent
  with~$\EXP\not\subseteq\Ppoly$. More generally, we show that certain
  separations of~$\V^1_2$ from a theory~$\T$ imply the consistency
  of~$\T$ with~$\EXP\not\subseteq\Ppoly$. For~$\T=\S^1_2$, Takeuti
  (1988) established such a separation using a variant of G\"odel's
  consistency statement.  Analogous results hold
  for~$\PSPACE\not\subseteq\Ppoly$ but the required separations of
  theories are yet unknown.  Finally, we give magnification results
  for the hardness of proving almost-everywhere versions of these
  lower bounds.
\end{abstract}

\section{Introduction}

\noindent\textbf{Bounded arithmetic and computational complexity.} 
Bounded arithmetics
$$\textstyle \S^1_2\subseteq \T^1_2\subseteq
\S^2_2\subseteq\T^2_2\subseteq\cdots\subseteq \T_2=\bigcup_i\T^i_2$$
go back to Buss \cite{bussthesis} and are given by induction
principles for bounded formulas corresponding to the levels of the
polynomial hierarchy. E.g.,~$\T^1_2$ has induction
for~$\NP$-properties or, more precisely, for~$\Sigma^b_1$-formulas, which
define precisely the sets in~$\NP$ (in the standard
model). Informally, the theories are meant to capture reasoning with
concepts and functions of a certain computational
complexity. E.g.,~$\S^1_2$ formalizes polynomial-time reasoning.

These theories are obviously not foundational for the whole of
mathematics but they are for computer science: already low levels
formalize a large part of contemporary complexity theory.  For example in
 circuit complexity, certain central upper \cite{at} and lower~\cite{mp} bounds
have been formalized in (a certain
theory below)~$\T^2_2$. 

The first and final words in Kraj\'i\v{c}ek's 1995 monograph \cite{krabuch} ask for consistency results for  notoriously open complexity theoretic conjectures. Already consistency with low levels of the hierarchy is seen as precise evidence for the truth of the conjecture. This is one of the main motivations for bounded arithmetic  from the  perspective of computational complexity.

Concerning circuit lower bounds, the central open question is
whether~$\S^1_2$ can be proved consistent with super-polynomial
circuit lower bounds for~$\NP$, i.e.,~$\NP\not\subseteq\Ppoly$.
 

\bigskip\noindent\textbf{Bounded arithmetic and mathematical logic.}
Such consistencies can be inferred from a better understanding of
independence. For example, the consistency of~$\T^i_2$ with~$\NP\not\subseteq\Ppoly$ is
implied by~$\T^i_2\neq \T_2$. In fact, the separation of
theories~$\T^i_2 \not= \T_2$ is \emph{equivalent} to the consistency
of~$\T^i_2$
with~$\Sigma^\P_{i+1}\not\subseteq\textsf{co-$\Sigma^\P_{i+1}$/poly}$;
see~\cite{kpt}, also \cite[Section 10.2]{krabuch}.
%
%E.g., the hypothesis that the polynomial hierarchy does not collapse is consistent even with full bounded arithmetic~$\T_2$ assuming the conjecture that $\T_2$ is distinct from all its levels $\T^i_2$ \cite[Corollary 10.2.6]{krabuch}. Remarkably,  this derives  evidence for the truth of the complexity theoretic hypothesis from progress in understanding independence. Results of this type underline the intuition that complexity theoretic conjectures have a logical nature (see e.g. the prefaces of \cite[p.viif]{pudlakbuch}, \cite[p.xii]{krabuch}).

Using G\"odel-type consistency statements,
Takeuti~\cite[p.104]{takeuti} proved the following separation (see also
\cite[Corollary~2.7]{kraexp}):

\begin{theorem}[Takeuti] \label{thm:takeuti} There is a bounded formula which is provable in $\V^1_2$ but not in~$\S^1_2$.
\end{theorem}

The theory~$\V^1_2$ is strong: it extends~$\T_2$ with a second sort of
{\em set variables}, and has induction for~$\NEXP$-properties or, more
precisely, for~$\Sigma^{1,b}_1$-formulas, which define precisely the sets
in~$\NEXP$ (in the standard model).  Informally,~$\V^1_2$ formalizes
exponential-time reasoning.
 
Not much more has been achieved. E.g., it is still unkown whether the
subtheory~$\U^1_2\subseteq\V^1_2$ that formalizes polynomial-space
reasoning is conservative over~$\S^1_2$.  G\"odel-type consistency
statements do not seem to reach very far -- see
\cite[Section~10.5]{krabuch} and \cite{feasinc} for discussions.  New
methods seem to be required and this is the main motivation for
bounded arithmetic from the perspective of mathematical logic.  In
Pudl\'ak's words from 1996 \cite{bottom}: ``we are not satisfied with
the current methods of proving independence results. The main reason
is that, except for Gödel's theorem which gives only special formulas,
no general method is known for proving independence of~$\Pi_1$
sentences.''


\bigskip\noindent\textbf{Known consistency results.}
Maybe not surprisingly, not too much is known concerning the
consistency of circuit lower bounds.  Some conditional consistency
results have been achieved in \cite{cokra}.  Unconditional ones have
been achieved in a line of works
\cite{KrajicekOliveira:Unprovability,BKO:Consistency,BydzovskyMuller:Ultrapowers,CKKO:LEARN}
but only for fixed-polynomial lower bounds.  These works rely on
witnessing theorems and complexity-theoretic methods (concretely, the
methods in~\cite{SanthanamWilliams:Uniformity}).

Super-polynomial lower bounds seem to require different
techniques. Only one is known~\cite{abm} (with some strengthenings
announced in \cite{thapen}), namely, that the theory~$\V^0_2$ is
consistent with~$\NEXP\not\subseteq\Ppoly$. Here~$\V^0_2$ is a
conservative extension of~$\T_2$ with set variables -- needed to speak
about (nondeterministic) exponential-time computations.
% and the lower bound. Various formalizations are discussed in
% \cite{abm}, in particular, a direct one by
% so-called~$\alpha$-formulas and a set-universal one by
% so-called~$\beta$-formulas based on the Easy Witness Lemma
% \cite{ew}.
The proof is based on Ajtai's theorem \cite{ajtai} and its
improvements \cite{kpw,pbi}, and thereby on methods from mathematical
logic, in particular forcing \cite{riis,am,partialstr}.




\bigskip\noindent\textbf{Main contribution.} We show that Takeuti's theorem
does imply a consistency result  for super-polynomial circuit lower bounds,
namely the consistency of~$\S^1_2$ with~$\EXP\not\subseteq\Ppoly$.  At
first sight this might appear weak when compared to the just mentioned
result from \cite{abm}. This is not the case: while the formalization
of the
collapse~$\NEXP\subseteq\Ppoly$ requires set-sort quantification, the
formalization of the weaker collapse~$\EXP\subseteq\Ppoly$ can be
stated without such quantification, and for the number sort the
theory~$\S^1_2$ has considerable strength.  This follows from a well-known argument from the
  so-called Karp-Lipton Theorem for $\EXP$, stated in \cite{kl} and attributed to
  Meyer. Details follow.
  
The collapse of~$\EXP$ to~$\Ppoly$ would mean that every
exponential-time machine~$M$ is simulated by circuits of size at
most~$n^c$ for some~$c\in\N$. The direct formalization reads:
$$ 
\alpha^c_M:=\begin{array}{l}
              \text{``\em for all lengths~$n>1$ there exists a circuit~$C$ of size at most~$n^c$}\\
              \text{ \em such that for
              all~$x\in\{0,1\}^n$:\;\;~$C(x)=1$ iff $M$
              accepts~$x$.\em ''}
\end{array}
$$
Writing the statement that~$M$ accepts~$x$ requires an existential
set-sort quantifier for a computation of~$M$.  This can be avoided as
follows.  Consider an exponential-time machine~$M^*$ that,
given~$x\in\{0,1\}^n$ and~$i\in\N$, decides whether the~$i$-th bit of
(the binary code) of the computation of~$M$ on~$x$ is 1. From small
circuits simulating~$M^*$ we get a~$c\in\N$ such that:
$$
\meyer^c_M:=\begin{array}{l}
              \text{``\em for all lengths~$n>1$ there exists a circuit~$C$ of size at most~$n^c$}\\
              \text{ \em such that for
              all~$x\in\{0,1\}^n$:\;\;~$\textit{tt}(C_x)$ is a
              halting computation of~$M$ on~$x$.\em ''}
\end{array}
$$
Here,~$C_x$ is the circuit obtained from~$C$ by fixing the first~$n$
inputs to the bits of~$x$, and~$\textit{tt}(C_x)$ is the truth table
of the Boolean function it computes. Note that~$\meyer^c_M$ is a
number-sort sentence, i.e., it has no set variables; in
fact,~$\meyer^c_M$ is a~$\forall\Sigma^b_2$-sentence.


Letting~$M_1$ be a suitable universal exponential-time machine, either
of the two theories~$\{\neg\alpha^c_{M_1}\mid c\in\N\}$
or~$\{\neg\meyer^c_{M_1}\mid c\in\N\}$ is true (in the standard
model) if and only if~$\EXP\not\subseteq\Ppoly$.  We define
$$
\q{$\EXP\not\subseteq\Ppoly$}:=\{\neg\meyer^c_{M_1}\mid
c\in\N\},
$$ 
pronounced as ``the $\meyer$-formalization of $\EXP \not\subseteq
\Ppoly$''.  The $\alpha$-formalization of $\EXP \not\subseteq \Ppoly$
is defined analogously, using the $\alpha$-formulas instead of the
$\meyer$-formulas.  

We arrive at the main theorem:

\begin{theorem}\label{thm:maincon}\
\begin{enumerate}\itemsep=0pt
\item[(a)] $\S^1_2$ is consistent with
  $\big\{ \neg\meyer^c_{M_1}\mid c\in\N \big\}$, the
  $\meyer$-formalization of $\EXP \not\subseteq \Ppoly$.
\item[(b)] $\S^1_2(\alpha)$ is consistent with $\big\{\neg\alpha^c_{M_1}\mid c\in\N\big\}$, the $\alpha$-formalization of $\EXP \not\subseteq \Ppoly$.
\end{enumerate}
\end{theorem}

\noindent In~(b), the theory~$\S^1_2(\alpha)$ is a standard
two-sorted variant of~$\S^1_2$.
The result is robust in that it does not depend on the parti\-cular
definition of~$M_1$. Indeed, the consistencies hold for \emph{any}
machine~$M_1$ that in a certain precise sense
is~$\S^1_2(\alpha)$-provably universal for exponential time -- what
this means is that the theorem holds for \emph{any} machine that
satisfies Lemma~\ref{lem:M1} below. Furthermore, both formalizations
are implied over~$\S^1_2(\alpha)$ by corresponding lower bound
statements for {\em any} exponential-time machine~$M$; see
Theorem~\ref{thm:equiv} below.

\bigskip\noindent\textbf{Methods.}
The proof of (a) is based on proof-theoretic arguments, namely
the ``new style'' witnessing theorem
from~\cite{bb}: from a~$\V^1_2$-proof of a bounded
formula~$\varphi(x)$ one constructs an exponential-time machine~$M$
such that even~$\S^1_2(\alpha)$ can infer~$\varphi(x)$
{\em from} a computation of~$M$
on~$x$. The theory~$\S^1_2(\alpha)$ is, however, agnostic concerning
the existence of such computations. On the other
hand,~$\meyer^c_{M_1}$ implies that such computations exist by
providing small circuits describing them.  This way, one infers (a)
from Takeuti's Theorem \ref{thm:takeuti}. In fact, the sketched
argument does not rely on Takeuti's specific formula: {\em every}
model of~$\S^1_2$ that violates {\em any} bounded consequence
of~$\V^1_2$ satisfies \q{$\EXP\not\subseteq\Ppoly$}; see
Theorem~\ref{thm:congammaM} below.

The proof of~(b) is not a straightforward consequence of~(a). 
 One difficulity is that, while the equivalence
of the~$\alpha$- and~$\meyer$-formalizations is, as we show, provable
in~$\T^1_2(\alpha)$, for all we know it is not provable
in~$\S^1_2(\alpha)$. We bypass this by proving~(b) anyway with a kind
of model-theoretic argument dubbed ``simulating comprehension''
in~\cite{abm}. Intuitively,~$\alpha_{M_1}^c$ implies that the family
of sets given by circuits is rich -- rich enough to
ensure~$\T^1_2(\alpha)$; see Lemma~\ref{lem:alphagammaproof}
below.  Once~$\T^1_2(\alpha)$ is available,
the~$\T^1_2(\alpha)$-provable equivalence of the~$\alpha$-
and~$\meyer$-formalizations kicks in, and (b) follows again from
Takeuti's Theorem. This argument, which uses the assumption
that~$\alpha^c_{M_1}$ is provable to
simulate~$\Pi^b_1(\alpha)$-induction, relies on the formally verified
model-checkers constructed in \cite{abm}.

\bigskip\noindent\textbf{Additional contributions.}
The only obstacle to strengthen Theorem~\ref{thm:maincon} to theories
above~$\S^1_2$, or to the lower bound theory
\q{$\PSPACE\not\subseteq\Ppoly$} analogously defined, is our lack of
understanding of logical independence:

\begin{theorem}\label{thm:nbsort}  Let $\T$ be a theory containing $\S^1_2(\alpha)$.
\begin{enumerate}\itemsep=0pt
\item[(a)] If~$\T$ does not prove all number-sort formulas that are
  provable in~$\forall\Sigma^{1,b}_1(\V^1_2)$,
  then~$\T\cup\q{$\EXP\not\subseteq\Ppoly$}$ is consistent.

\item[(b)] If~$\T$ does not prove all number-sort formulas that are
  provable in~$\forall\Sigma^{1,b}_1(\U^1_2)$,
  then~$\T\cup\q{$\PSPACE\not\subseteq\Ppoly$}$ is consistent.
\end{enumerate}
\end{theorem}

%\cite[Theorem 9]{abm} is a similar statement for $\V^1_2$ and \q{$\NEXP\not\subseteq\Ppoly$}.
Note that the number-sort formulas in this theorem can have arbitrary
unbounded quantifiers. Here, $\forall\Sigma^{1,b}_1(\U^1_2)$ is the
set of universal closures of $\Sigma^{1,b}_1$-formulas proved by
$\U^1_2$.  This is still a strong theory -- it
properly contains $\V^0_2$ and it can
count~\cite[Lemma~5.5.14]{krabuch}.

Our consistency can be strengthened to the consistency of an almost
everywhere lower bound~$\EXP\not\subseteq\ioPpoly$; see
Corollary~\ref{cor:aecons} below.  Borrowing a term from circuit
complexity~\cite{beyond}, we prove {\em magnifications}: if certain
theories do not prove such lower bounds, neither do certain apparently
much stronger theories.  
We view this as a contribution to {\em
  Razborov's program}~\cite{razclb,razlower,razannals} to identify a
formally precise barrier in circuit complexity, namely a natural
theory that formalizes known circuit lower bounds but is incapable to
prove strong conjectured ones.




\begin{theorem}\label{thm:magn}\
\begin{enumerate}\itemsep=0pt
\item[(a)] If $\S^1_2$ does not prove \q{$\EXP\not\subseteq\ioPpoly$}, then neither does $\forall\Sigma^{1,b}_1(\V^1_2)$.
\item[(b)] If $\S^1_2$ does not prove \q{$\PSPACE\not\subseteq\ioPpoly$}, then neither does $\forall\Sigma^{1,b}_1(\U^1_2)$.
\end{enumerate}
\end{theorem}

The corresponding statements for \q{$\EXP\not\subseteq\Ppoly$} or \q{$\PSPACE\not\subseteq\Ppoly$} are void
(see Remark~\ref{rem:void}).
This has been overlooked in~\cite{abm}.


\bigskip\noindent\textbf{Outline.} Carrying out the arguments sketched in this
introduction requires a fair amount of technical
work. E.g.,~$\T^1_2(\alpha)$ should formalize
Meyer's argument, or~$\S^1_2(\alpha)$ should know in a certain sense
that~$M_1$ is universal.
%formalize the argument with~$M^*$ above, or the universal machine~$M_1$ should be such that~$\S^1_2(\alpha)+\meyer^c_{M_1}$ can construct small circuits for other exponential time machines~$M$. 
We construct suitable machines in Section~\ref{sec:machines}.
Section~\ref{sec:formalizations} proves implications between
the~$\alpha$- and~$\meyer$-formalizations over~$\S^1_2(\alpha)$
or~$\T^1_2(\alpha)$. The sketched arguments are then carried out in
Section~\ref{sec:cons} where Theorem~\ref{thm:maincon} and
\ref{thm:nbsort} are proved.  Section~\ref{sec:magnification} infers
Theorem~\ref{thm:magn} as a corollary to the proofs. Finally,
Section~\ref{sec:concl} comments on the open question for the
consistency of~$\PSPACE\not\subseteq\Ppoly$.







\section{Preliminaries}





We assume the reader is familiar with the standard notation from
bounded arithmetic~\cite{bussthesis,hp,krabuch}.  Here, we recall some
facts and fix some less standard notation.

\subsection{Bounded arithmetic}

Bounded arithmetic theories~$\S^i_2$ and~$\T^i_2$ are written in Buss'
language containing the relation symbol~$x{<}y$ and the function
symbols~$0$,~$1$,~$x{+}y$,~$x{\cdot}y$,~$\lfloor
x/2\rfloor$,~$x{\#}y$,~$|x|$. The theories are given by a finite set
of universal axioms for the symbols in the language plus
length-induction for~$\Sigma^b_i$-formulas in~$\S^i_2$, and standard
induction for~$\Sigma^b_i$-formulas in~$\T^i_2$.  Full bounded
arithmetic is~$\T_2:=\bigcup_{i>0}\T^i_2$.
%A $\Delta^b_1$ formula is one that $\S^1_2$ proves equivalent both to a  $\Sigma^b_1$- and a $\Pi^b_1$-formula. $\S^1_2(\alpha)$ proves $\Delta^b_1$-induction.
We do not distinguish these theories from their conservative extensions to Cook's language $\PV$ \cite{cook} which contains symbols for all polynomial-time computable functions and proves certain defining equations for them. 
By a {\em term} we mean a term in Buss' language. E.g., Cantor's pairing $\langle x,y\rangle$ is a term. 
We write $x\in\Log$ for $1{<}x \wedge \exists y\ x=|y|$. In such a context we write e.g.\ $2^x,2^{x^2}$ etc.~for $1\#y,y\#y$ etc.. 
%Buss' witnessing theorem implies:

\begin{remark} \label{rem:PV}  
A formula (in Buss' language) is~$\Delta^b_1$ in~$\S^1_2$
(i.e.,~$\S^1_2$-provably equivalent both to a~$\Sigma^b_1$- and
a~$\Pi^b_1$-formula) if and only if~$\S^1_2$ proves that it is
equivalent to a quantifier-free~$\PV$-formula. In particular~$\S^1_2$
proves length and standard induction for
quantifier-free~$\PV$-formulas \cite[Lemma 5.2.9]{krabuch}.
\end{remark}



\medskip

\noindent\textbf{Circuits.}
A circuit with~$s$ gates is coded by a number
below~$2^{10\cdot s\cdot|s|}$. There is a~$\PV$-function~$\eval(C,x)$
that (in the standard model) takes the encoding~$C$ of a circuit and
evaluates it on input~$x$.  This means that, if~$x<2^n$,
where~$n \leq |C|$ is the number of input gates of~$C$, then the input
gates are assigned the bits of the length-$n$ binary representation
of~$x$, and the internal gates of the circuit are evaluated bottom up
from inputs to outputs; we assume that~$\eval(C,x) = 0$ if~$x\ge 2^n$
or if~$C$ does not code a circuit.

It is convenient to have circuits that take finite tuples~$\bar
x=(x_1,\ldots, x_k)$ as inputs; formally, such a circuit has~$k$
sequences of input gates, the~$i$-th taking the bits
of~$x_i$. Again,~$\PV$ contains an evaluation function~$\eval(C,\bar
x)$; it outputs~$0$ if any~$x_i$ has length bigger than the length of
its allotted input sequence. %When used as a term, 
We write~$C(\bar x)$ instead of~$\eval(C,\bar x)$. 
%; when used as a predicate, we alsowrite~$C(\bar x)$ instead of~$\eval(C,\bar x)=1$.

For a circuit~$C$ taking~$(\ell+k)$-tuples as inputs and
an~$\ell$-tuple~$\bar x$ we let~$C_{\bar x}$ be the circuit obtained
by fixing the first~$\ell$ inputs to~$\bar x$; it takes~$k$-tuples as
inputs. Formally,~$C_{\bar x}$ is %either
~$\PV$-term 
%or a quantifier-free~$\PV$-formula, 
with variables~$C$ and $\bar x$
and~$\S^1_2$ proves~$C_{\bar x}(\bar y) =C(\bar x,\bar
y)$ and~$C_{\bar x} \le C$.

\begin{lemma}\label{lem:circuit} For every quantifier-free $\PV$-formula $F(\bar x)$ there is $c\in\N$ such that
$$
\S^1_2\vdash\forall n{\in}\Log\ \exists C{<}2^{n^c}\ \forall \bar x{<}2^n\ (C(\bar x)=1 \leftrightarrow F(\bar x)).
$$
\end{lemma}

\noindent\textbf{Two-sorted theories} Besides {\em number variables} $x,y,\ldots$ as before, two-sorted theories have {\em set variables} $X,Y,\ldots$ and
a binary relation symbol~$x\in X$. Models have the form~$(N,\mathcal
Y)$ where~$N$ interprets the number sort symbols of Buss' language,
set variables range over~$\mathcal Y$, and~$\in$ is interpreted by a
subset of~$N\times\mathcal Y$. The standard model has~$N=\N$ and the
obvious interpretations,~$\mathcal Y$ as the finite subsets of~$\N$
and interprets~$\in$ by actual membership.  Since we shall use also
capital letters for number variables (e.g.,~when intended to denote a
circuit) we write quantifiers on set variables as~$\exists_2X$
and~$\forall_2X$, i.e., with an index 2.

Given a formula~$F(\bar X,\bar x,v)$ or a circuit~$C(v)$, we
use~$F(\bar X,\bar x,\cdot)$ and~$C(\cdot)$ to represent the sets
of~$v$'s satisfying~$F$ or~$C$. More precisely, for a
formula~$\varphi(X,\ldots)$ without set sort equalities~$X=Y$ we
define the formulas
$$
\varphi\big(F(\bar X,\bar x,\cdot),\ldots\big) \;\text{ and }\; \varphi\big(C(\cdot),\ldots\big)
$$ 
by replacing atomic subformulas $t\in X$ of $\varphi$ by $F(\bar
X,\bar x,t)$ and~$C(t)=1$, respectively.



The sets of formulas~$\Sigma^b_i(\alpha)$ and~$\Pi^b_i(\alpha)$ are
defined as before but now allowing atomic subformulas~$t\in X$ for
terms~$t$ and set variables~$X$. In particular, set-sort
equality~$X=Y$ and quantifiers on set variables are not allowed. 
Using the notation
$$
X<z \;:=\; \forall x \;(x\in X\to x<z),
$$ 
the two-sorted theories~$\S^i_2(\alpha)$ and~$\T^i_2(\alpha)$ are
given by length-induction and, respectively, induction
for~$\Sigma^b_i(\alpha)$-formulas plus
 %additionally {\em Set-Boundedness} and {\em Extensionality}:  
 the universal closures of
\begin{equation*}
\begin{array}{ll}
\textit{set-boundedness:}&\exists z\ X<z,\\
\textit{extensionality:} &  \forall z\ (z \in X\leftrightarrow z \in Y)\ \to \ X =Y,\\
%X{<}z\wedge Y{<}z\wedge \forall u{<}z\ (u{\in}X\leftrightarrow u{\in}Y)\to X =Y,\\
\textit{$\Delta^b_1(\alpha)$-comprehension:}
&\exists_2 X\ \forall x\ (x \in X\leftrightarrow x<y\wedge\varphi(\bar X,\bar x,x))
%&\exists_2 X{<}z\ \forall x{<}z\ (x \in X\leftrightarrow \varphi(\bar X,\bar x,x))
\end{array}
\end{equation*}
for all~$\varphi \in \Delta^b_1(\alpha)$, where~$\Delta^b_1(\alpha)$
denotes the collection of all formulas that are equivalent to both
a~$\Sigma^b_1(\alpha)$-formula and a~$\Pi^b_1(\alpha)$-formula
provably in the subtheory of~$\S^1_2(\alpha)$ that does not
have~$\Delta^b_1(\alpha)$-comprehension.
%$\S^1_2(\alpha)$ proves~$\Delta^b_1(\alpha)$-induction.
Full two-sorted bounded arithmetic
is~$\T_2(\alpha):=\bigcup_{i>0}\T^i_2(\alpha)$.  
As before, we identify~$\S^1_2(\alpha)$ with a
conservative extension to the language~$\PV(\alpha)$ that contains
symbols~$f^{\bar X}(\bar x)$ for all polynomial-time algorithms with
oracles~$\bar X$ (represented by set variables) and proves defining
equations.
% Further,~$\S^1_2(\alpha)~$proves induction for
% quantifier-free~$\PV(\alpha)$-formulas.

\begin{remark} \label{rem:PValpha}
A formula is~$\Delta^b_1(\alpha)$ if and only if~$\S^1_2(\alpha)$
proves that it is equivalent to a
quantifier-free~$\PV(\alpha)$-formula 
without set equalities. 
In particular, that~$\S^1_2(\alpha)$ proves $\Delta^b_1(\alpha)$-induction  means that it
proves  induction for such formulas.
\end{remark}
The~$\hat\Sigma^{1,b}_1$-formulas are those of the
form~$\exists_2 X\varphi$
for~$\varphi\in \Sigma^{1,b}_0:=\bigcup_i\Sigma^b_i(\alpha)$.
The~$\Sigma^{1,b}_1$-formulas are those in the closure
of~$\hat\Sigma^{1,b}_1$ under~$\vee$ and~$\wedge$ and bounded
number-sort quantification~$\exists x{<}t$ and~$\forall x{<}t$ for
terms~$t$ not involving~$x$.  The theories~$\V^0_2$ and~$\V^1_2$ are
given by~$\T_2(\alpha)$ plus~$\Sigma^{1,b}_0$-comprehension
and~$\Sigma^{1,b}_1$-comprehen\-sion, respectively. The
theory~$\U^1_2$ is given by~$\V^0_2$
plus~$\Sigma^{1,b}_1$-length-induction: for
every~$\varphi\in\Sigma^{1,b}_1$ the universal closure of
$$
\varphi(\bar X,\bar x,0)\wedge\forall y{<}|z|\ (\varphi(\bar X,\bar x,y)\to \varphi(\bar X,\bar x,y+1))\ \to\
\varphi(\bar X,\bar x,|z|).
$$


\begin{lemma}\label{lem:strict} 
For every $\Sigma^{1,b}_1$-formula $\varphi$ there is a 
$\hat\Sigma^{1,b}_1$-formula $\hat\varphi$ such that
%\begin{enumerate}\itemsep=0pt
%\item[(a)] 
$\U^1_2\vdash (\varphi \to \hat\varphi)$
%\item[(b)] 
 and $\S^1_2(\alpha)\vdash (\hat\varphi \to \varphi)$.
%\end{enumerate}
\end{lemma}

\begin{proof} The formula $\hat\varphi$ is built by induction on the syntactic structure of $\varphi$: it transforms subformulas of the form $\forall x{<}t \ \exists_2 X\ \psi(X,x,\ldots)$ to the form $\exists_2 X\ \forall x{<}t\ \psi(X_x,x,\ldots)$. Here, we write $X_x$ for $H(X,x,\cdot)$ where
$H(X,x,v):=\langle x,v\rangle\in X$. 
 Part (a) is an instance of $\Sigma^{1,b}_1$-collection provable in $\U^1_2$; see \cite[Lemma 5.5.10]{krabuch}. Part (b) 
 follows from the fact that $\S^1_2(\alpha)$ is a sub-theory of $\U^1_2$, which implies that any formula provable in the latter is automatically provable in the former.
\end{proof}



The {\em number-sort} formulas are those without (free or bound) set
variables. It is not hard to see
that~$\S^i_2(\alpha)$,~$\T^i_2(\alpha)$, and~$\T_2(\alpha)$ prove the
same number-sort formulas as~$\S^i_2$,~$\T^i_2$, and~$\T_2$,
respectively. A way to see this is the following lemma (which holds
also for~$\T^i_2$).  For~$N\models\S^1_2$ let~$\C_N$ be the family of
all sets of the form~$\hat C:=\{a\in N\mid N\models C(a)=1\}$
where~$C$ ranges over~$N$ (equivalently, over the circuits in the
sense of~$N$). The model~$(N,\C_N)$ interprets~$\in$ by set
membership. Then:


\begin{lemma}\label{lem:CM} 
  For every~$i>0$ and~$N$, if~$N \models \S^i_2$,
  then~$(N,\C_N)\models \S^i_2(\alpha)$.
\end{lemma}

\begin{proof} That~$(N,\C_N)$ satisfies set-boundedness and
  extensionality is clear. We verify length-induction and
  comprehension for the appropriate collections of formulas. First we
  need to introduce some notation. Let~$\varphi(\bar x)$ be
  a~$\Sigma^{1,b}_0$-formula with parameters from~$(N,\C_N)$. Define~$\varphi^*(\bar x)$ as in the text. Note that every set parameter in~$\varphi(\bar x)$
  becomes a number parameter in~$\varphi^*(\bar x)$. Thus,
length-induction for~$\varphi(x)$ follows from the fact that $N$ is a model of $\S^i_2$, which by definition satisfies induction for all formulas in the language of arithmetic, including those with set parameters interpreted as numbers.

To verify comprehension, let~$a\in N$ and let~$\varphi(x)$
be~$\Delta^b_1(\alpha)$ with
parameters from~$(N,\C_N)$. Then~$\varphi^*(x)$ is~$\Delta^b_1$ with
parameters from~$N$, say~$\bar b$. Since~$N\models\S^1_2$, Buss' witnessing
theorem implies that~$\varphi^*(x)$ is equivalent in~$N$
to~$F(\bar b,x)$ for a quantifier-free~$\PV$-formula~$F(\bar
y,x)$. For the base case of the construction, we assume $n=0$ and $C=0$. For $n > 0$, Lemma~\ref{lem:circuit} gives~$C\in N$ such that
$$
N\models\forall \bar y,y,x{<}2^n\ \big(C(\bar y,y,x) = 1\leftrightarrow x<y\wedge F(\bar y,x)\big).
$$
In $N$, choose $D:=C_{\bar b,a}$, so
$N\models\forall x\ D(x)=C(\bar b,a,x)$.
Then~$\hat D\in \C_N$
and~
\[
(N,\C_N)\models\forall x\ (x\in\hat D\leftrightarrow x<a\wedge\varphi(x)).\qedhere
\]
\end{proof}


\subsection{Explicit machines}\label{sec:premachine}


We use multitape (deterministic oracle Turing) machines as our model
of computation, say with~$k$ input tapes and~$\ell$ oracle tapes, and
some work tapes. The tapes have cells indexed~$0,1,\ldots$, and the
content of cell 0 is a fixed symbol marking the end of the tape -- it
is never overwritten by something else and heads scanning it do not
move left. It takes inputs~$\bar x = (x_1,\ldots,x_k)\in\N^k$. The
input length is~$|\bar x|:=|x_1|+\cdots+|x_k|$.  Input tapes are read-only, i.e.,
heads on input tapes write what they scan and do not move right when
scanning blank. A computation stops when reaching a halting state,
which is either accepting or rejecting.
For~$\bar X=(X_1,\ldots,X_{\ell})\in P(\N)^\ell$ we denote
by~$M^{\bar X}$ the machine with oracles~$\bar X$. When entering a
special query state the computation moves to one out of~$2^\ell$ many
states encoding whether~$q_i\in X_i$ for all~$i=1,\ldots,\ell$
where~$q_i$ is the query, i.e., the number written in binary on
the~$i$-th oracle tape.




A {\em partial time-$t$ space-$s$ query-$q$ computation
  of~$M^{\bar X}$ on~$\bar x$} is a sequence of~$t+1$ configurations
the first being the start configuration of~$M^{\bar X}$ on~$\bar x$,
every other being the successor of the previous one, repeating halting
configurations.  Every configuration has head positions less than~$s$
on work tapes, less than~$|\bar x|+2$ on input tapes, and less
than~$|q|$ on query tapes.  Using~$|q|$ (instead of~$q$) means, on the
formal level, that we allow only polynomially bounded queries.  Such a
configuration is determined by~$\max\{s, |\bar x|+2,|q|\}+1$ numbers,
one for the state and, for each~$j<\max\{s, |\bar x|+2,|q|\}$, a
number coding for each tape the content of cell~$j$ and a {\em
  position bit} indicating whether the current head position is to the
left of~$j$ or not.

We identify~$M$ with its code by a number and assume that the numbers
determining a configuration are less than~$M$. We code a configuration
as above by the set~$X$ of~$\langle i,j\rangle$
for~$i<\max\{s, |\bar x|+2,|q|\}+1$ and~$j<|M|$ such that the~$i$-th
number in the configuration has~$j$-th bit~$1$.  There
are~$\PV(\alpha)$-functions which, with such an~$X$ as oracle,
retrieve the state, the head positions, the symbols scanned, and the
queries in~$X$. We make no assumptions on what these functions return
when~$X$ is not coding a configuration as above.  The partial
computation is coded by a set~$Y$ such
that~$Y_i:=\{x\mid \langle i,x\rangle\in Y\}$ is the~$i$-th
configuration.

Note that, in the standard model, $X < \Bd^0(M,\bar x,s,q)$ and
$Y < \Bd(M,\bar x,t,s,q)$ where 
$$
\begin{array}{lclcl}
\Bd^0(M,\bar x,s,q)&:=&\langle \max\{s %\min\{s,t\}
,  |\bar x|{+}2,|q|\}{+}1,|M|\rangle,\\
\Bd(M,\bar x,t,s,q)&:=&\langle  t,\Bd^0(M,\bar x,s,q)\rangle.
\end{array}
$$ 


We proceed to the formal level. Let~$k\in\N$ be the number of inputs,
let~$\ell\in\N$ be the number of oracles, let~$\bar x=(x_1,\ldots,
x_k)$ be a~$k$-tuple of number variables, and let~$\bar X=(X_1,\ldots,
X_\ell)$ be an~$\ell$-tuple of set variables.
% The~$\Pi^b_1$ formula \q{$X$ is a space-$s$ query-$q$ configuration
% of~$M$ on~$\bar x$}states that all~$v\in X$ have the
% form~$\langle i,j\rangle$ for~$i\le s+1,j\le |M|$ and the
% numberwhose length~$|M|$ binary representation has a 1 at precisely
% the positions~$j$ with~$\langle j,k\rangle\in X$is as desired: a
% state of~$M$ if~$i=0$, and a~$k$-tuple of contents and position bits
% if~$i>0$. Clearly there are~$\PV(\alpha)$-functions that with such
% an oracle~$X$ and input~$s,q,\bar x$ retrievethe state, head
% positions and queries in~$X$.
The individual bits that encode successor configurations are
implicitly computed by the following oracle machine. Recall our
convention that the successor of a halting configuration is the
configuration itself. If any of the ``checks'' in Lines~1--3 in the
description of the machine fails, then the machine outputs ``fail'' in
Line~4; else it completes Lines~5--9 and outputs a bit.
 \begin{enumerate}\itemsep=0pt
\item[0.] inputs $(M,\bar x,s,q)$ and oracles $\bar X,X$.
\item check that $M$ is the code of an oracle machine with $k$ input tapes and $\ell$ oracle tapes.
\item check that the state, the head positions, the scanned symbols,
  and the queries encoded in~$X$ are not off; i.e., (a) the retrieved
  state is a state of~$M$,
 %(b) for all~$i=1,\ldots,k$ the retrieved position of the~$i$-th input head is less than~$|x_i|+2$, 
  (b) the retrieved
  position of all oracle heads is less than~$|q|$, and (c) the
  retrieved position of all work heads is less than~$s$.
\item check that the new head positions as determined by the
  transition table of $M$ on the state, the scanned symbols, and the
  head positions encoded in $X$ are also not off.
\item if any of the above checks fails, output ``fail'' and halt; else:
\item query $X$ to retrieve the state, the head positions, the scanned
  symbols, and the queries, and then look up the transition table
  of~$M$ and, if required, query the oracles~$\bar X$ to compute the
  new state, the new cell contents, and the new head positions.
\item compute $i$ and $j$ such that $v=\langle i,j\rangle$.
\item if $i > \max\{s %\min\{s,t\}
,  |\bar x|+2,|q|\}$, then output 0. 
\item if $i = \max\{s%\min\{s,t\}
,  |\bar x|+2,|q|\}$, then output the $j$-th bit of the new state (Line~5).
\item if~$i< \max\{ s%\min\{s,t\}
, |\bar x|+2,|q|\}$, then output the~$j$-th
  bit of the number~$a<M$ that for each tape codes the content of
  cell~$i$ (from oracle~$X$ or Line~5, as appropriate) and its
  position bit (determined by the new position of its head from Line~5).
\end{enumerate}
The machine runs in polynomial time and returns ``fail'' or a bit.
Note that it does not depend on~$v$ whether ``fail'' is returned or
not.  Let~$\succ^{\bar X,X}(M,\bar x,s,q,v)$ be
the~$\PV(\alpha)$-symbol for this machine.
% Then~$\S^1_2(\alpha)$ proves that$\succ^{\bar X,X}(M,s,q,\bar x,\cdot)$ is a space-$s$ query-$q$ configuration no matter whether~$X$ is one or not. Further,~$\S^1_2(\alpha)$ proves~$$\begin{array}{l}\q{$X$ is a space-$s$ query-$q$ configuration of~$M^{\bar X}$ on~$\bar x$}\\ \ \wedge\ \neg\ \succ^{\bar X,X}(M,s,q,\bar x,0)=\q{\textup{fail}}\\ \ \to\q{$\succ^{\bar X,X}(M,s,q,\bar x,\cdot)$ is the~$M^{\bar X}$-successor configuration of~$X$}.\end{array}$$

Clearly, there is a
quantifier-free~$\PV(\alpha)$-formula~$\Start(M,\bar x,s,q,v)$ such that,
provably in~$\S^1_2$, the set defined by~$\Start(M,\bar x,s,q,\cdot)$ is
the start configuration of~$M$ on~$\bar x$ if~$M$ codes a suitable
machine. Similarly, there are
quantifier-free~$\PV(\alpha)$-formulas~$\Fail$ and~$\Next$ with
suitable free variables of both sorts which, provably
in~$\S^1_2(\alpha)$, determine if the algorithm
of~$\succ^{\bar X,X}(M,\bar x,s,q,v)$ outputs
``fails''~(formula~$\Fail$) and, otherwise determines the output
bit~(formula~$\Next$). We define
$$
\q{$Y$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar x$} 
$$
as the following 
$\Pi^b_1(\alpha)$ formula with free number variables $M,\bar x,t,s,q$ and free set variables~$Y,\bar X$:
$$
\begin{array}{l}
\forall i{\le}t\ \forall v{<}\Bd(M,\bar x,t,s,q)\ (v\in Y_i\to v<\Bd^0(M,\bar x,s,q))\\
\wedge\ \forall v{<}\Bd^0(M,\bar x,s,q)\ \big( v\in Y_0\leftrightarrow\Start(M,\bar x,s,q,v)\big)\\
\wedge\ \forall i{<}t\ \forall v{<}\Bd^0(M,\bar x,s,q)\ \big( v\in Y_{i+1}\leftrightarrow 
\Next(\bar X,Y_i,M,\bar x,s,q,v) \big)\\
\wedge\ \forall i{<}t \ \neg \Fail(\bar X,Y_i,M,\bar x,s,q).\\
\end{array}
$$
% $$
% \begin{array}{l}
% \forall i{\le}t\ \forall v{<}\Bd(M,t,s,q,\bar x) (v\in Y_i\to v<\Bd_0(M,t,s,q,\bar x))\\
% \wedge\ \forall v{<}\Bd_0(M,t,s,q,\bar x)\big( v\in Y_0\leftrightarrow\Start(M,\bar x,v)\big)\\
% \wedge\ \forall i{<}t \ \neg\ \succ^{\bar X,Y_i}(M,s,q,\bar x,0)=\q{\textup{fail}}\\
% \wedge\ \forall i{<}t\ \forall v{<}\Bd_0(M,t,s,q,\bar x)\big( v\in Y_{i+1}\leftrightarrow \succ^{\bar X,Y_i}(M,s,q,\bar x,v)=1 \big).
% \end{array}
% $$
Here again, we write $Y_i$ for $H(Y,i,\cdot)$ where
$H(Y,i,v):=\langle i,v\rangle\in Y$. Note that the formula does not
state~$Y<\Bd(M,\bar x,t,s,q)$ 
because this would require unbounded universal quantifiers.

\begin{lemma}\label{lem:unique}
If $\Unique(\bar X,Y,Z,M,\bar x,t,s,q)$ denotes
the formula
\begin{equation*}
\begin{array}{l}
 \q{$Y$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar x$} \\ 
\ \wedge\ \q{$Z$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar x$} \\
\ \to\ \forall v{<}\Bd(M,\bar x,t,s,q)\ (v\in Y\leftrightarrow v\in Z),
\end{array}
\label{eqn:unique}
\end{equation*}
then $\T^1_2(\alpha) \vdash \Unique(\bar X,Y,Z,M,\bar x,t,s,q)$, and
$\S^1_2(\alpha) \vdash \Unique(\bar X,Y,Z,M,\bar x,t,|s|,q)$.
\end{lemma}

% \begin{lemma}\label{lem:unique} 
% The theory $\T^1_2(\alpha)$ proves\mrand{deleted conjuncts $Y_u<\Bd_0(...)$ (hidden)}
% $$
% \begin{array}{l}
% %\q{$M$ is a machine with $k$ input tapes and $\ell$ oralce tapes}\\
% Y{<}\Bd(M,t,s,q,\bar x) %\wedge\forall u{\leq}t \ Y_u{<}\Bd_0(M,s,q,\bar x) \\   
% \ \wedge\  Z{<}\Bd(M,t,s,q,\bar x) %\wedge\forall u{\leq}t \ Z_u{<}\Bd_0(M,s,q,\bar x) \wedge 
% \\
% \ \wedge\ \q{$Y$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar x$} \\ 
% \ \wedge\ \q{$Z$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar x$} \\
% \ \to\ Y=Z.
% \end{array}
% $$
% Moreover, $\S^1_2(\alpha)$ proves this formula with $s$ replaced by $|s|$.
% \end{lemma}

\begin{proof} In~$\T^1_2(\alpha)$ use~$\Pi^b_1(\alpha)$-induction to
  prove for all~$i\leq t$, that the~$i$-th configurations in~$Y$
  and~$Z$ are equal. This equality is guaranteed because Lemma~\ref{lem:unique} establishes that computations in $\S^1_2(\alpha)$ are unique. Replacing~$s$ by~$|s|$, this is~$\Delta^b_1(\alpha)$-induction,
available in~$\S^1_2(\alpha)$; cf.~Remark~\ref{rem:PValpha}.
\end{proof}

There
are~$\PV(\alpha)$-functions~$\textit{time}^Y(t),\textit{space}^Y(t),\textit{query}^{Y}(t)$
which compute, respectively, the mini\-mal~$i\le t$ such that~$Y_i$ is
halting and~$i=t+1$ if all are non-halting, the maximal cell visited
on any work tape in any configuration, and the maximal cell visited on
any oracle tape in any configuration.  E.g., for~$\textit{space}^Y(t)$
we can assume that the machines mark visited cells; then binary search
can compute, for any work tape and time~$i$, the maximum cell visited
on it.

In~$\S^1_2$ we can prove, by~$\Delta^b_1(\alpha)$-induction, that
given a partial time-$t$ space-$s$ query-$q$ computation~$Y$
of~$M^{\bar X}$ on~$\bar{x}$, the head positions on the input tapes
are not off. If also time, space and query bounds are verifiable
in~$\S^1_2(\alpha)$ we talk of an explicit machine:

\begin{definition} Let~$M$ be an oracle machine with~$k \in \N$ input tapes and~$\ell \in \N$
  oracle tapes. The machine~$M$ is {\em explicit} if there are
  terms~$t_0(\bar x),s_0(\bar x),q_0(\bar x)$ such that
\begin{eqnarray*}
\S^1_2(\alpha)&\vdash& \q{$Y$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar{x}$}\\
&&\ \to \textit{time}^Y(t)<t_0(\bar x)\wedge \textit{space}^Y(t)<s_0(\bar x)\wedge \textit{query}^{Y}(t)<|q_0(\bar x)|.
\end{eqnarray*}
In this case we say that $M$ is {\em witnessed} by $t_0,s_0,q_0$ and write 
\begin{eqnarray*}
\Bd^0_M(\bar x)&:=&\Bd^0(M,\bar x,s_0(\bar x),q_0(\bar x))\\ 
\Bd_M(\bar x)&:=&\Bd(M,\bar x,t_0(\bar x),s_0(\bar x),q_0(\bar x)).
\end{eqnarray*}
The machine~$M$ is an {\em explicit~$\EXP$-machine} if there exists a
term~$t_M(x)$ such that the above holds for~$t_0(\bar x)=t_M(\bar x)$
and~$s_0(\bar x)=t_M(\bar x)$, and~$q_0(\bar x)=t_M(\bar x)$.  
The machine~$M$
is an {\em explicit~$\PSPACE$-machine} if there exists a term~$t_M(x)$
such that the above holds for~$t_0(\bar x)=t_M(\bar x)$ and~$s_0(\bar
x)=|t_M(\bar x)|$, and~$q_0(\bar x)=t_M(\bar x)$. 
The machine~$M$ is an
{\em explicit~$\P$-machine} if there exists a term~$t_M(x)$ such that
the above holds for~$t_0(\bar x)=|t_M(\bar x)|$ and~$s_0(\bar x)=|t_M(\bar
x)|$, and~$q_0(\bar x)=t_M(\bar x)$.  In all three cases we say that~$M$ is \emph{witnessed} by the term~$t_M(\bar x)$.
%
% Saying that $M$ is an {\em explicit $\EXP$-, $\PSPACE$- or $\P$-machine} 
% means that so it is witnessed by some term $t_M(\bar x)$. 
%
%Given such an $M$, the formula \q{$Y$ is $t_M(\bar x)$-bounded} is $$Y{<}\Bd(M,t,s,q,\bar x)\wedge\forall u{\le} t\ Y_u{<}\Bd_0(M,s,q,\bar x)$$ for the respective values of $t,s,q$. 
\end{definition}

\begin{remark} 
  For every term~$t(\bar x)$ there exist~$c \in \N$ such
  that~$\S^1_2$
  proves~$(|\bar x|>1 \to t(\bar x) \leq 2^{|\bar x|^c})$.  This means
  that the time and space bounds~$t_0(\bar x)$ and~$s_0(\bar x)$ of an
  explicit~$\EXP$-machine can be chosen to be of the
  form~$2^{|\bar x|^c}$ with~$c \in \N$. Similarly, the space bound of
  an explicit~$\PSPACE$-machine and the time bound of an
  explicit~$\P$-machine can be chosen of the form~$|\bar x|^c$.
\end{remark}


The theory~$\S^1_2(\alpha)$ proves that every function~$f^{\bar
  X}(\bar x)\in\PV(\alpha)$ is computed by an explicit
oracle~$\P$-machine. See \cite[Lemma~18]{abm} for a precise
statement. For example, there are explicit
oracle~$\P$-machines~$M_\succ$ and~$M_\start$, with
suitable numbers of inputs and oracles, which compute
the~$\PV(\alpha)$-function~$\succ$ and
the~$\PV(\alpha)$-function~$\start$ which indicates the truth
value of the quantifier-free formula~$\Start$.

For explicit machines we omit writing bounds $t,s,q$ in the formulas above. E.g., if $M$ be an explicit  $\PSPACE$-machine witnessed by $t_M(\bar x)$, then
the formulas
$$
\begin{array}{l}
\q{$Y$ is a partial time-$t$ computation of $M^{\bar X}$ on $\bar x$},\\
\q{$Y$ is a halting computation of $M^{\bar X}$ on $\bar x$}
\end{array}
$$ 
are obtained by substituting~$|t_M(\bar x)|$ for~$s$ and~$t_M(\bar
x)$ for~$q$.  The latter additionally substitutes~$t_M(\bar x)$
for~$t$.  Obvious modifications give formulas with ``accepting'' or
``rejecting'' instead of ``halting''.



\section{Formally verified universal machines}\label{sec:machines}


\subsection{A general universal machine} 
The 
universal machine takes input~$(M,\bar x,t,s,q)$ and simulates~$t$
steps of the machine~$M$ on~$\bar x$ within space~$s$ and query
bound~$q$.  We give a careful implementation so that~$\S^1_2(\alpha)$
can verify its correctness. Correctness must be formulated with care
because~$\S^1_2(\alpha)$ cannot prove that exponential-time
computations exist.


%The universal machine of this section is defined in more generalitythan strictly needed later. This unifies some of the arguments andclarifies that neither specific choices of time or space bounds northe verification that they hold play a role in the simulationarguments.

\begin{theorem}\label{thm:univ} 
  Let~$k,\ell\in\N$, let~$\bar x=(x_1,\ldots, x_k),M,t,s,q$ be number
  variables, and let~$\bar X=(X_1,\ldots, X_\ell),Y,Z$ be set
  variables.  There are~$c\in\N$, an explicit machine~$U$ with~$k+4$
  input tapes and~$\ell$ oracle tapes,
  and~$\Delta^b_1(\alpha)$-formulas~$F,G$ such that,
  writing~$\bar y := (M,\bar x,t,s,q)$ and~$n := |\bar y|$, the
  following hold:
 \begin{enumerate} \itemsep=0pt
%  \item[(a)] Writing $n:=|M|+|\bar x|+|t|+|s|+|q|$ and $\bar y = (M,x,t,s,q)$,
% the machine $U$ is witnessed by $t_U,s_U,q_U$ where
% $$
% t_U(M,\bar x,t,s,q)= t\cdot (s+n)^c,\ s_U(M,\bar x,t,s,q)=(s+n)^c,\
%  q_U(M,\bar x,t,s,q)=q. 
% $$
 \item[(a)] $U$ is witnessed by $t_U,s_U,q_U$ where
   $t_U(\bar y) := t \cdot (s+n)^c$, $s_U(\bar y) := (s+n)^c$,
   $q_U(\bar y)=q$.
\item[(b)] $\S^1_2(\alpha)\vdash  \q{$Y$ is a partial time-$t$ space-$s$ query-$q$ computation of $M^{\bar X}$ on $\bar x$}$ \\
\hspace*{7ex} $\ \ \to \q{$F(Y,\bar y,\cdot)$ is an accepting computation  of $U^{\bar X}$ on $\bar y$}$\\
  \hspace*{10ex}
  $\ \ \wedge\ \forall v{<}\Bd(\bar y)\
  (G(F(Y,\bar y,\cdot),\bar y,v)\leftrightarrow v\in Y)$.
\item[(c)] $\S^1_2(\alpha)\vdash \q{$Z$ is an accepting computation of $U^{\bar X}$ on $\bar y$}$ \\
  \hspace*{7ex} $\ \ \to\q{$G(Z,\bar y,\cdot)$ is a partial time-$t$ space-$s$ query-$q$  computation  of $M^{\bar X}$ on $\bar x$}$\\
  \hspace*{10ex}
  $\ \ \wedge\ \forall v{<}\Bd_U(\bar x)\ (F(G(Z,\bar y,\cdot),\bar y,v)\leftrightarrow v\in Z)$.
\end{enumerate}
\end{theorem}

\begin{proof} 
  The machine~$U$ on input~$\bar y = (M,\bar{x},t,s,q)$ iterates the function~$\succ$ for~$t$ times using two configuration tapes. This is done in~$t$ rounds. In each round $u > 0$, the machine~$U$ overwrites one configuration tape with the bit~$\Next(\bar X,X,M,\bar x,s,q,i)$. After round~$t$, the machine accepts if the flag bit is~$0$. 

\noindent\textbf{Description of~$U$.} The machine~$U$ starts with a preparation phase and ends with a wrap-up phase. In the preparation phase, it checks that~$M$ codes an oracle machine. We describe round~$u < t$. The machine~$U$ takes exactly~$2|t|+2$ steps to move on the counter. It updates the clock to~$u+1$. In this case,~$U$ computes the next configuration of~$M$ as follows: The machine~$U$ skips cell~$0$ and fills cell~$i+1$ for~$i=0,1,\ldots,s_0-1$ with the bits describing the successor configuration of~$X$. This is done by simulating the machine~$M_\succ$ on input~$(M,\bar x,s,q,i)$ and oracles~$\bar X,X$. We omit the case for $u=0$ as it is identical to the successor step. The rest of the time analysis and space analysis follows.
\end{proof}

\subsection{Universal $\EXP$- and $\PSPACE$-machines}


Since all our applications of~$U$ below will concern explicit~$\EXP$-
or~$\PSPACE$-machines, without oracles, coded by standard~$M \in \N$,
the statement of Theorem~\ref{thm:univ} is more general than needed.
In this section we state the actual lemmas that we need and use as
black-boxes. If not stated otherwise, we understand an explicit
machine to be one with~$k=1$ input tapes and~$\ell=0$ oracle
tapes. Also, when referring to the universal machine~$U$, we mean the
one for~$k=1$ and~$\ell=0$. 

% The first lemma is just a weak variant of Theorem~\ref{thm:univ}:
% 
% \begin{lemma}\label{lem:U1} 
% There is an explicit~$\EXP$-machine~$U_1$ such that for every
% explicit~$\EXP$-machine~$M$ \arand{Removed unused referrence to~$t_M$}
% there are~$\Delta^b_1(\alpha)$-formulas~$F', G'$ such that
%  \begin{enumerate}
%  \item[(a)]  $\S^1_2(\alpha)\vdash$ \q{$Y$ is a partial time-$t$ 
% computation of $M$ on $x$}\\\hspace*{9ex}$\ \to\q{$F'(Y,t,\cdot)$ is 
% an accepting  computation  of $U_1$ on $\langle M,x,t\rangle$}$,
%  \item[(b)] $\S^1_2(\alpha)\vdash$ \q{$Z$ is an accepting computation 
% of $U_1$ on $\langle M,x,t\rangle$}
%  \\\hspace*{8ex}
%  $\ \to\q{$G'(Z,\cdot)$ is a partial time-$t$ computation  of $M$ 
% on $x$}$.
% % \item[(c)] $\T^1_2(\alpha)\vdash$ \q{$Y$ is an halting computation 
% of $\tilde M_1$ on $y$}\\\hspace*{9ex}
% % $\to \q{$Y$ is an accepting computation of $\tilde M_1$ on $y$}$.
%  \end{enumerate}
% \end{lemma}
% \begin{proof} Machine~$U_1$ on~$\langle N,x,t\rangle$ runs~$U$
  on~$(N,x,t,t,t)$. Since $U$ is a universal machine for all oracle machines, and $U_1$ is defined by a specific call to $U$, it follows that $U_1$ is an explicit $\P$-machine because the input length is $n = |\langle N,x,t \rangle|$.
\end{proof}
 
The machine $M_1$ of the first lemma
is used in our formalizations of $\EXP\not\subseteq\Ppoly$.

\begin{lemma}\label{lem:M1} 
  There is an explicit~$\EXP$-machine~$M_1$ such that for every
  explicit~$\EXP$-machine~$M$ witnessed, say, by the term~$t_M$, there
  are~$\Delta^b_1(\alpha)$-formulas~$F_1,G_1$ such that 
 \begin{enumerate}
 \item[(a)]  $\S^1_2(\alpha)\vdash$ \q{$Y$ is an accepting (rejecting) computation of $M$ on $x$}\\
\hspace*{8ex} $\ \to\q{$F_1(Y,x,\cdot)$ is an accepting (rejecting)  computation  of $M_1$ on $\langle M,x,t_M(x)\rangle$}$,
 \item[(b)] $\S^1_2(\alpha)\vdash$ \q{$Z$ is an accepting (rejecting) computation of $M_1$ on $\langle M,x,t_M(x)\rangle$}\\
\hspace*{8ex} $\ \to\q{$G_1(Z,x,\cdot)$ is an accepting (rejecting) computation  of $M$ on $x$}$.
 \end{enumerate}
% The same is true for ``rejecting'' instead of ``accepting''. 
\end{lemma}

\begin{proof} 
  The machine~$M_1$ on~$\langle N,x,t \rangle$ runs the universal
  machine~$U$ on~$(N,x,t,t,t)$. We prove (b). Argue in~$\S^1_2(\alpha)$, assume~$Z$ is a halting
  computation of~$M_1$ on~$\langle M,x,t_M(x) \rangle$. To show $W$ is not rejecting, we use induction on the number of rounds $u$. For the base case $u=1$, we assume the flag bit is $0$ because the machine has just started. For the inductive step, if the flag bit is $0$ at round $u$, it must remain $0$ at round $u+1$ because $M$ is witnessed by $t_M$.
\end{proof}



Additionally, we have a formally verified machine~$M^*_1$ which, for each
explicit~$\EXP$-machine~$M$, computes like~$M^*$ from the
introduction. 

\begin{lemma}\label{lem:autoM1}
  There is an
  explicit~$\EXP$-machine~$M^*_1$ such that for every
  explicit~$\EXP$-machine~$M$ witnessed, say, by the term~$t_M$, there
  are~$\Delta^b_1(\alpha)$-formulas~$F_1^*,G_1^*$ such that
  \begin{enumerate} \itemsep=0pt
   \item[(a)]  $\S^1_2(\alpha)\vdash \q{$Y$ is a partial time-$t$ computation of $M$ on $x$} $\\
   \hspace*{8ex} $\  \wedge\ v\in Y \wedge v<\Bd(M,x,t,t_M(x),t_M(x))$ \\
   \hspace*{8ex} $\ \to\ \q{$F_1^*(Y,x,t,v,\cdot)$ is an accepting  computation  of $M^*_1$ on $\langle M, x,t,v,t_M(x)\rangle$}$,
 \item[(b)] $\S^1_2(\alpha)\vdash \q{$Z$ is an accepting computation of $M^*_1$ on $\langle M,x,t,v,t_M(x)\rangle$}$
 \\\hspace*{8ex}  $\ \to\ \q{$G_1^*(Z,x,t,\cdot)$ is a partial time-$t$ computation 
of $M$ on $x$}$ 
 \\\hspace*{8ex}  $\quad\quad  \wedge \ G_1^*(Z,x,t,v) \wedge  v<\Bd(M,x,t,t_M(x),t_M(x))$.
 \end{enumerate}
\end{lemma}

\begin{proof} 
  The machine~$M^*_1$ extracts~$x,u_v,i_v$ and runs~$U$ on~$(N,x,t,s,s)$. For (b), argue in~$\S^1_2(\alpha)$, and let~$Z$ be an accepting
  computation of~$M_1^*$ on~$\langle M,x,t,v,t_M(x)\rangle$. We conclude $v \in Y$ because the definition of $G_1^*$ is specifically constructed to return $v$ whenever the computation $Z$ is accepting. Thus, $G_1^*(Z,x,t,v)$ holds by the definition of the function $G_1^*$.
\end{proof}

We state analogous lemmas for~$\PSPACE$.

% \begin{lemma}\label{lem:U2} 
% There is an explicit~$\PSPACE$-machine~$U_2$ such that for every
% explicit~$\PSPACE$-machine~$M$, say witnessed by the term~$t_M$, there
% are~$\Delta^b_1(\alpha)$-formulas~$F, G$ such that
%  \begin{enumerate} \itemsep=0pt
%  \item[(a)]  $\S^1_2(\alpha)\vdash$ \q{$Y$ is a partial time-$t$ 
% computation of $M$ on $x$}\\\hspace*{9ex}$\ \to\q{$F(Y,t,\cdot)$ 
% is an accepting  computation  of $U_2$ on $\langle M,x,t\rangle$}$,
%  \item[(b)] $\S^1_2(\alpha)\vdash$ \q{$Y$ is an accepting computation 
% of $U_2$ on $\langle M,x,t\rangle$}
%  \\\hspace*{8ex}
%  $\ \to\q{$G(Y,\cdot)$ is a partial time-$t$ computation  of $M$ on $x$}$.
% % \item[(c)] $\T^1_2(\alpha)\vdash$ \q{$Y$ is an halting computation 
% of $\tilde M_1$ on $y$}\\\hspace*{9ex}
% % $\to \q{$Y$ is an accepting computation of $\tilde M_1$ on $y$}$.
%  \end{enumerate}
% \end{lemma}
% \begin{proof} 
 This is proved like Lemma~\ref{lem:U1} except that~$U_2$ on~$\langle
 N,x,t\rangle$ runs~$U$ on~$(N,x,t,|t|,t)$. Because the space parameter is $|t|$, which is logarithmic in $t$, the machine $U_2$ is an explicit $\P$-machine.
 \end{proof}
 

\begin{lemma}\label{lem:M2} 
  There is an explicit~$\PSPACE$-machine~$M_2$ such that for every
  explicit~$\PSPACE$-machine~$M$ witnessed, say, by the term~$t_M$, there
  are~$\Delta^b_1(\alpha)$-formulas~$F_2,G_2$ such that 
 \begin{enumerate}
 \item[(a)]  $\S^1_2(\alpha)\vdash$ \q{$Y$ is an accepting (rejecting) computation of $M$ on $x$}\\
\hspace*{8ex} $\ \to\q{$F_2(Y,x,\cdot)$ is an accepting (rejecting)  computation  of $M_2$ on $\langle M,x,t_M(x)\rangle$}$,
 \item[(b)] $\S^1_2(\alpha)\vdash$ \q{$Z$ is an accepting (rejecting) computation of $M_2$ on $\langle M,x,t_M(x)\rangle$}\\
\hspace*{8ex} $\ \to\q{$G_2(Z,x,\cdot)$ is an accepting (rejecting) computation  of $M$ on $x$}$.
 \end{enumerate}
% The same is true for ``rejecting'' instead of ``accepting''. 
\end{lemma}


\begin{proof} 
Machine~$M_2$ is defined like~$M_1$ but runs the universal machine~$U$
on~$(N,x,t,|t|,t)$. We only consider the case where $M$ is a deterministic machine, as the universal machine $U$ does not support oracle tapes in the $\PSPACE$ construction.
 \end{proof}


\begin{lemma}\label{lem:autoM2}
  There is an
  explicit~$\PSPACE$-machine~$M^*_2$ such that for every
  explicit~$\PSPACE$-machine~$M$ witnessed, say, by the term~$t_M$,
  there are~$\Delta^b_1(\alpha)$-formulas~$F_2^*,G_2^*$ such that
  \begin{enumerate} \itemsep=0pt
   \item[(a)]  $\S^1_2(\alpha)\vdash \q{$Y$ is a partial time-$t$ computation of $M$ on $x$} $\\
   \hspace*{8ex} $\  \wedge\ v\in Y \wedge v<\Bd(M,x,t,|t_M(x)|,t_M(x))$ \\
   \hspace*{8ex} $\ \to\ \q{$F_2^*(Y,x,t,v,\cdot)$ is an accepting  computation  of $M^*_2$ on $\langle M, x,t,v,t_M(x)\rangle$}$,
 \item[(b)] $\S^1_2(\alpha)\vdash \q{$Z$ is an accepting computation of $M^*_2$ on $\langle M,x,t,v,t_M(x)\rangle$}$
 \\\hspace*{8ex}  $\ \to\ \q{$G_2^*(Z,x,t,\cdot)$ is a partial time-$t$ computation 
of $M$ on $x$}$ 
 \\\hspace*{8ex}  $\quad\quad  \wedge \ G_2^*(Z,x,t,v) \wedge  v<\Bd(M,x,t,|t_M(x)|,t_M(x))$.
 \end{enumerate}
\end{lemma}

\begin{proof} 
  Like Lemma~\ref{lem:autoM1} except that~$M_2^*$
  on~$\langle N,x,t,v,s\rangle$ runs~$U$ on~$(N,x,t,|s|,s)$. The correctness follows by induction on the length of the input $|x|$. For the base case $|x|=0$, the machine accepts all $v$. For the inductive step, we assume correctness for $|x|$ and extend it to $|x|+1$.
\end{proof}


For the rest of this work we fix {\em any} machines~$M_1$ and~$M_2$
satisfying Lemmas~\ref{lem:M1} and~\ref{lem:M2}.



\section{Formalizations of circuit lower bounds}\label{sec:formalizations}

The $\alpha$- and $\meyer$-formulas from the introduction are defined as follows:


\begin{definition}
Let $c\in\N$ and let $M$ be an explicit $\EXP$- or $\PSPACE$-machine.
\begin{eqnarray*}
\alpha^c_M&:=& \forall n{\in}\Log\  \exists C{<}2^{n^c}\ \forall x{<}2^n\\
&&\quad \big(C( x)=1\ \leftrightarrow \ \exists_2 Y \ \q{$Y$ is an accepting  computation of $M$ on $x$}\big),\\
%\beta^c_M&:=&\forall n{\in}\Log\  \exists C{<}2^{n^c}\ \exists D{<}2^{n^c}\ \forall  x{<}2^n\ \forall_2 Y\\
%&&\quad \big((C(x)=0\ \to \ \neg \q{$Y$ is an accepting  computation of $M$ on $ x$})\wedge\\[-1ex]
%&& \quad  \ (C( x)=1\ \to \ \q{$D_{x}(\cdot)$ is an accepting computation of $M$ on $x$})\big),\\
\meyer^c_M&:=&  \forall n{\in}\Log\  \exists C{<}2^{n^c}\ \forall x{<}2^n\\
&&\quad  \q{$C_{x}(\cdot)$ is a halting computation of $M$ on $x$}.
\end{eqnarray*}
\end{definition}

Both theories~$\{\neg\alpha^c_{M_1}\mid c\in\N\}$
and~$\{\neg\meyer^c_{M_1}\mid c\in\N\}$ are true (in the standard
model) if and only if~$\EXP\not\subseteq\Ppoly$. The same holds
for~$M_2$ and~$\PSPACE$, instead of~$M_1$ and~$\EXP$.  The aim of this
section is two-fold:~(1)~verify over weak theories that these
formalizations do not depend on the particular choices of the
machines~$M_1$ and~$M_2$ in Lemmas~\ref{lem:M1} and~\ref{lem:M2},
and~(2)~verify over weak theories that both formalizations are
equivalent; i.e.:

\begin{theorem} \label{thm:equiv}
For every explicit $\EXP$-machine $M$ and 
every~$c \in \N$ there is~$d \in \N$ such that
\medskip

\begin{tabular}{llllllllllllll}
(a) & $\S^1_2(\alpha) \vdash (\alpha^c_{M_1} \to \alpha^d_M),$ & \hspace{0.5cm} &
(c) & $\T^1_2(\alpha) \vdash (\meyer^c_{M_1} \to \alpha^d_{M_1}),$ \\
(b) & $\S^1_2(\alpha) \vdash (\meyer^c_{M_1} \to \meyer^d_M)$, & &
(d) & $\T^1_2(\alpha) \vdash (\alpha^c_{M_1} \to \meyer^d_{M_1})$.
\end{tabular}
\end{theorem}

\noindent Theorem~\ref{thm:equiv2} below states the analogue for $\PSPACE$.
Following the principle that the logically simplest formulas are
preferrable in definitions, we take:

% \begin{theorem}\label{thm:equiv} Let $M$ be an explicit $\EXP$-machine.
% \begin{enumerate}\itemsep=0pt
% \item[(a)] $\S^1_2(\alpha)\cup \{\neg\alpha^c_{M}\mid c\in\N\}
% \vdash\{\neg\alpha^c_{M_1}\mid c\in\N\}$.
% \item[(b)] $\S^1_2(\alpha)\cup \{\neg\meyer^c_{M}\mid c\in\N\}
% \vdash\{\neg\meyer^c_{M_1}\mid c\in\N\}$.
% \item[(c)] $\T^1_2(\alpha)\cup \{\neg\alpha^c_{M}\mid c\in\N\}
% \vdash \{\neg\meyer^c_{M}\mid c\in\N\}$.
% \item[(d)] $\T^1_2(\alpha)\cup \{\neg\meyer^c_{M}\mid c\in\N\}
% \vdash \{\neg\alpha^c_{M_1}\mid c\in\N\}$.
% \end{enumerate}
% \end{theorem}
%
%  Theorem~\ref{thm:equiv2} below is an analogue for $\PSPACE$. 
% As said in the introduction, we choose the logically simplest 
% formulas as our definition:
 
\begin{definition} $\q{$\EXP\not\subseteq\Ppoly$} := \big\{\neg\meyer^c_{M_1}\mid c\in\N\big\} $ and $
 \q{$\PSPACE\not\subseteq\Ppoly$} := \big\{\neg\meyer^c_{M_2}\mid c\in\N\big\}$.
%\begin{align*}
%& \q{$\EXP\not\subseteq\Ppoly$} := \big\{\neg\meyer^c_{M_1}\mid c\in\N\big\} \\
%& \q{$\PSPACE\not\subseteq\Ppoly$} := \big\{\neg\meyer^c_{M_2}\mid c\in\N\big\}.
%\end{align*}
\end{definition}


We start the proof of Theorem~\ref{thm:equiv} with the proof that the
definition does not depend on the particular choice of~$M_1$.
 
\begin{lemma}\label{lem:alpha} 
% \begin{enumerate}\itemsep=0pt
%\item[(a)] 
For every explicit~$\EXP$-machine~$M$ and every~$c\in\N$ there
is~$d\in\N$ such that
$$
\S^1_2(\alpha) \ \vdash \ (\alpha_{M_1}^c\to\alpha_{M}^d)\  \wedge\  (\meyer_{M_1}^c\to\meyer_{M}^d).
$$ 

%\item[(b)] For every explicit $\PSPACE$-machine $M$ and $c\in\N$ there is $d\in\N$ such that 
%$$
%\S^1_2(\alpha)\vdash (\alpha_{M_2}^c\to\alpha_{M}^d).
%$$ 
%\end{enumerate}
\end{lemma}



\begin{proof} 
We prove each implication for a separate~$d\in\N$; the maximum of the
2 values of~$d$ then witnesses the lemma.

For the first implication, Lemma~\ref{lem:M1}
and~$\Delta^b_1(\alpha)$-comprehension imply that~$\S^1_2(\alpha)$
proves
\begin{equation*}
\begin{split}
& \exists_2 Y\  \q{$Y$ is an accepting  computation of $M$ on $x$}\\
&  \leftrightarrow\ \exists_2 Y\  \q{$Y$ is an accepting  computation of $M_1$ on $\langle M, x,t_M( x)\rangle$}.
\end{split}
\end{equation*}
Argue in~$\S^1_2(\alpha)$ and
assume~$\alpha_{M_1}^c$. Given~$n\in\Log$ choose~$e\in\N$ and
set~$m:=n^e$ so that~$\langle M,x,t_M(x)\rangle<2^{m}$ for
all~$x<2^n$. Apply~$\alpha^c_{M_1}$ for this~$m$ and
get~$C'<2^{m^c}=2^{n^{ec}}$ such that for all~$x<2^n$:
\begin{equation*}
\begin{split}
& C'(\langle M, x,t_M( x)\rangle)=1 \\ 
& \leftrightarrow \exists_2 Y\  \q{$Y$ is an accepting  computation of $M_1$ on $\langle M, x,t_M( x)\rangle$}.
\end{split}
\end{equation*}
By Lemma~\ref{lem:circuit} there are small circuits computing~$\langle
M,x, t_M( x)\rangle$ from~$x$. This gives a circuit~$C$ such
that~$C(x)= C'(\langle M,x, t_M( x)\rangle)$ for
all~$x<2^n$. Clearly,~$C<2^{n^d}$ for suitable~$d\in\N$. This~$C$
witnesses~$\alpha_M^d$ for~$n\in\Log$.

For the second implication, argue in~$\S^1_2(\alpha)$ and
assume~$\meyer_{M_1}^c$.  Given~$n\in\Log$ choose~$e\in\N$ and
set~$m:=n^e$ so that~$\langle M,x,t_{M}(x)\rangle<2^{m}$ for
all~$x<2^n$. Apply~$\meyer_{M_1}$ for this~$m$ and
get~$C'<2^{m^c}=2^{n^{ec}}$ such that for all~$x<2^n$:
\begin{equation*}
 \q{$C'_{\langle M,x,t_{M}( x)\rangle}(\cdot)$ is a halting computation of $M_1$ on $\langle  M, x,t_{M}( x)\rangle$}.
\end{equation*}
Using the formula~$G_1$ from Lemma~\ref{lem:M1}~(b), we have, for
all~$x<2^n$: 
$$
\q{$G_1\big(C'_{\langle M,x,t_{M}(x)\rangle}(\cdot), x,\cdot \big)$ is a halting computation of $M$ on $x$}.
$$
Choose $f\in\N$ so that $\Bd_M(x)<2^{n^f}$ for all $x<2^n$.
By Lemma~\ref{lem:circuit} there is a circuit $C$ such that  for all $x<2^n$ and all $v<2^{n^f}$: 
$$
C(x,v)=1\leftrightarrow G_1\big(C'_{\langle M, x,
  t_{M}(x)\rangle}(\cdot),x,v\big).
$$
Choose $d\in\N$ such that $C<2^{n^d}$. Then $C$ witnesses $\alpha_{M}^d$ for $n$.
\end{proof}

The next lemma states one half of the equivalence of the two
formalizations.  The proof of this is still straightforward but we
need the theory~$\T^1_2(\alpha)$ instead of~$\S^1_2(\alpha)$ due to an
application of Lemma~\ref{lem:unique}.

\begin{lemma}\label{lem:gammaalpha} 
%\begin{enumerate}\itemsep=0pt
%\item[(a)] 
For every explicit $\EXP$-machine $M$ and 
every $c\in\N$ there is
$d\in\N$ such that 
$$
\T^1_2(\alpha)\vdash( \meyer^c_M\to\alpha^c_{M}).
$$
%\item[(b)] For every explicit $\PSPACE$-machine $M$ and $c\in\N$ there is $d\in\N$ such that
%$$
%\S^1_2(\alpha)\vdash (\meyer^c_M\to\beta^d_M)\wedge(\beta^c_M\to\alpha^c_M).
%$$
%\end{enumerate}
\end{lemma}
\begin{proof} 
Argue in~$\T^1_2(\alpha)$ and assume~$\meyer^c_M$. Let~$n\in\Log$ and
choose~$C'$ according to~$\meyer_M^c$ for~$n$.  Let~$A(Y,x)$
be
a~$\Delta^b_1(\alpha)$-formula which states that~$Y$ is accepting: it
applies a~$\PV(\alpha)$-function to retrieve the state of
the~$t_M(x)$-th configuration in~$Y$ and checks that it is an
accepting state of~$M$.

Lemma~\ref{lem:circuit} gives a~$d\in\N$ and a circuit~$C<2^{n^d}$
such that for all~$x<2^n$:
$$
C(x)=1\leftrightarrow A(C'_x(\cdot),x).
$$
We claim that~$C$ witnesses~$\meyer_M^d$ for~$n$. If~$C(x)=1$,
then~$C'_x(\cdot)$ is an accepting computation of~$M$
on~$x$. If~$C(x)=0$, then~$C'_x(\cdot)$ is not an accepting
computation of~$M$ on~$x$. Since it is a halting computation, it is
rejecting. It exists by~$\Delta_1(\alpha)$-comprehension. By
Lemma~\ref{lem:unique} (here we use~$\T^1_2(\alpha)$), there is no
accepting computation~$Y$ of~$M$ on~$x$. Thus $C$ witnesses $\alpha_M^d$.
\end{proof}

We are left to prove the second half of the equivalence of the two
formalizations, i.e., to infer~$\meyer$ from~$\alpha$. This is Meyer's
argument and formalizing it is not trivial. We do it in two steps
passing through an auxiliary formula~$\bar\beta$, which is a variant
of the~$\Pi^{1,b}_1$-formula in the~$\beta$-formalization
from~\cite{abm}. First, we infer~$\bar\beta$ from~$\alpha$, and
then~$\meyer$ from~$\bar \beta$.

An intuitive reason for something
non-trivial going on is that, unlike~$\alpha$, the
formula~$\bar\beta$ is universal in the set sort. In
particular,~$\bar\beta$ does not seem to imply the existence of
exponential-time computations. In contrast,~$\meyer$ straightforwardly
implies the existence of such computations
via~$\Delta^b_1(\alpha)$-comprehension. Again we need~$\T^1_2(\alpha)$
instead of~$\S^1_2(\alpha)$ due to an application of
Lemma~\ref{lem:unique} in the first step, and a key application
of~$\Pi^b_1$-induction in the second step.

\begin{lemma}\label{lem:alphagamma} 
For every explicit $\EXP$-machine $M$ and every $c\in\N$ there is
$d\in\N$ such that
$$
\T^1_2(\alpha)\vdash (\alpha_{M_1}^c\to\meyer_M^d).
$$ 
\end{lemma}

\begin{proof} 
For every explicit~$\EXP$-machine~$M$ witnessed, say, by
  term~$t_M$, and every~$c\in\N$ set
\begin{eqnarray*}
\bar\beta^c_{M}&:=&\forall n{\in}\Log\ \exists C{<}2^{n^c}\ \forall
x{<}2^n\ \forall t{\leq}t_M(x)\ \forall_2 Y\\ &&\quad \big(\q{$Y$ is a
  partial time-$t$ computation of~$M$ on~$ x$} \\[-1ex] &&\quad\quad
\ \to \ \forall v{<}\Bd(M,x,t,t_M(x),t_M(x))\ (C(x,t,v) = 1 \leftrightarrow 
v \in Y)\big).
\end{eqnarray*}

The lemma follows from the following two steps.\bigskip

\noindent \textbf{First step.}  For every explicit~$\EXP$-machine~$M$ and
every~$c\in\N$ there is~$d\in\N$ such that
$$
\T^1_2(\alpha)\vdash(\alpha^c_{M_1}\to\bar\beta^d_{M}).
$$ 
[...]

\noindent \textbf{Second step.} For 
every explicit $\EXP$-machine $M$ and every $c \in \N$ there is $d\in\N$
such that
$$
\T^1_2(\alpha)\vdash(\bar\beta^c_{M}\to\meyer^d_{M}).
$$ 
Let~$t_{M}$ witness~$M$. Argue in~$\T^1_2(\alpha)$ and
assume~$\bar\beta^c_{M}$. 
Let~$n\in\Log$ and 
choose~$D<2^{n^c}$ according to~$\bar\beta_{M}$ for
this~$n$. 

\medskip

\noindent{\em Claim:} 
$x<2^n \wedge t\le t_M(x) \to \q{$D(x,t,\cdot)$ is a partial
  time-$t$ computation of $M$ on $x$}$.

\medskip

We prove it by induction on~$t$. For~$t=0$, we assume $D(x,0,\cdot)$ is already a partial time-0 computation by the definition of $\bar\beta_M^c$. Assuming the claim for~$t<t_M(x)$, we verify it for~$t+1$. Let~$Z:=D(x,t,\cdot)$. By the induction hypothesis the set~$Z$ is a partial time-$t$ computation. Let~$Z'$ be the result of adding one computation step to~$Z$. Then $Z'$ is a partial time-$(t+1)$ computation. By $\bar\beta_M^c$, $D(x,t+1,\cdot)$ equals $Z'$ and is thus a partial time-$(t+1)$ computation.
\end{proof}

% \begin{proof} 
We prove the lemma by showing that $\alpha_{M_1}^c$ implies $\meyer_M^d$. Assume $\alpha_{M_1}^c$. By Lemma \ref{lem:alphagamma}, we know that for any explicit $\EXP$-machine $M$, $\T_2^1(\alpha)$ proves $\alpha_{M_1}^c \to \meyer_M^d$. Since $M$ is an explicit $\EXP$-machine, the implication follows immediately. This completes the proof.
\end{proof}
% 
\begin{proof}[Proof of Theorem~\ref{thm:equiv}.] 
Parts (a) and (b) are Lemma~\ref{lem:alpha}. Part (c) is the special case of Lemma~\ref{lem:gammaalpha} when $M=M_1$. This suffices to show the equivalence of the formalizations.
\end{proof}
 

In the analogue of Theorem~\ref{thm:equiv} for~$\PSPACE$ only
the last implication seems to need~$\T^1_2(\alpha)$:

\begin{theorem} \label{thm:equiv2}
For every explicit $\PSPACE$-machine $M$ and 
every~$c \in \N$ there is~$d \in \N$ such that
\medskip

\begin{tabular}{llllllllllllll}
(a) & $\S^1_2(\alpha) \vdash (\alpha^c_{M_2} \to \alpha^d_M),$ & \hspace{0.5cm} &
(c) & $\S^1_2(\alpha) \vdash (\meyer^c_{M_2} \to \alpha^d_{M_2})$, \\
(b) & $\S^1_2(\alpha) \vdash (\meyer^c_{M_2} \to \meyer^d_M),$ & & 
(d) & $\T^1_2(\alpha) \vdash (\alpha^c_{M_2} \to \meyer^d_{M_2})$.
\end{tabular}
\end{theorem}

\begin{proof}
  Parts (a) and (b) are proved as in Lemma~\ref{lem:alpha} but for
  explicit~$\PSPACE$-machines~$M$ and~$M_2$. Part
  (c) is the analogue of Lemma~\ref{lem:gammaalpha}. That proof required~$\T^1_2(\alpha)$ in the final
  use of Lemma~\ref{lem:unique}. Since $\PSPACE$ machines use more space than $\EXP$ machines, this step requires $\T^1_2(\alpha)$ for all machine types. Part (d) is the analogue of
  Lemma~\ref{lem:alphagamma} and is proved in the same way.
\end{proof}

% \begin{enumerate}\itemsep=0pt
% \item[(a)] $\S^1_2(\alpha)\cup \{\neg\alpha^c_{M}\mid c\in\N\}
% \vdash\{\neg\alpha^c_{M_2}\mid c\in\N\}$.
% \item[(b)] $\S^1_2(\alpha)\cup \{\neg\meyer^c_{M}\mid c\in\N\}
% \vdash\{\neg\meyer^c_{M_2}\mid c\in\N\}$.
% \item[(c)] $\S^1_2(\alpha)\cup \{\neg\alpha^c_{M}\mid c\in\N\}
% \vdash \{\neg\meyer^c_{M}\mid c\in\N\}$.
% \item[(d)] $\T^1_2(\alpha)\cup \{\neg\meyer^c_{M}\mid c\in\N\}
% \vdash \{\neg\alpha^c_{M_2}\mid c\in\N\}$.
% \end{enumerate}

% \begin{proof} 
For (a) and (b) use Theorem~\ref{thm:equiv2} itself. For (c), the result follows from the statement of Theorem~\ref{thm:equiv2}(c). For (d), we apply the theorem to the machine $M_2$ to obtain the desired implication.
\end{proof}


\section{Consistency }\label{sec:cons}

This  section has three subsections. One for the proof of Theorem~\ref{thm:maincon}~(a), one for
Theorem~\ref{thm:maincon}~(b) and one for Theorem~\ref{thm:nbsort}.

\subsection{Consistency of the $\meyer$-formalization}

Theorem~\ref{thm:maincon}~(a) follows from Takeuti's Theorem~\ref{thm:takeuti} and the following.

\begin{theorem}\label{thm:congammaM}
  Assume~$(N,\mathcal Y)\models\S^1_2(\alpha)+\neg\forall\bar
  x\varphi(\bar x)$ where~$\varphi(\bar x)$ is
  a~$\Sigma^{1,b}_1$-formula without free set variables.
\begin{enumerate}\itemsep=0pt
\item[(a)] If $\V^1_2\vdash \varphi(\bar x)$, then $N\models\q{$\EXP\not\subseteq\Ppoly$}.$
\item[(a)] If $\U^1_2\vdash \varphi(\bar x)$, then
$N\models\q{$\PSPACE\not\subseteq\Ppoly$}.$
\end{enumerate}
\end{theorem}

As outlined in the introduction, the proof  relies on ``new-style'' witnessing theorems from~\cite{bb} (improving \cite{knt}):



\begin{theorem}\label{thm:wit} 
Let $\varphi(\bar X,\bar x)$ be a $\hat\Sigma^{1,b}_1$-formula.
\begin{enumerate}\itemsep=0pt
\item[(a)] If $\V^1_2\vdash \varphi(\bar X,\bar x)$, then there is an explicit oracle
$\EXP$-machine $M$ such that
$$
\S^1_2(\alpha)\vdash \q{$Y$ is a halting computation of $M^{\bar X}$ on $\bar x$} \to \varphi(\bar X,\bar x).
$$
\item[(b)] If $\U^1_2\vdash \varphi(\bar X,\bar x)$, then there is an explicit oracle
$\PSPACE$-machine $M$ such that
$$
\S^1_2(\alpha)\vdash \q{$Y$ is a halting computation of $M^{\bar X}$ on $\bar x$} \to \varphi(\bar X,\bar x).
$$ 
\end{enumerate}
\end{theorem}

\begin{proof} We comment on how to transfer the formalism
  from~\cite{bb} to ours. The statements in~(a) and~(b) follow
  from~\cite[Theorem~4.8]{bb} and~\cite[Theorem~4.6]{bb}. Because our theory $\S_2^1(\alpha)$ is stronger than $\V^1_2$, any result proved in $\V^1_2$ automatically holds in $\S_2^1(\alpha)$.
\end{proof}



Note that every~$\meyer$-formula implies the existence of computations
by~$\Delta^b_1(\alpha)$-comprehension, but only for machines without
oracles. Intuitively, a~$\meyer$-formula enables the capacity of a
weak theory to simulate a strong one, for consequences without set
variables. The following makes this precise.

\begin{corollary} \label{cor:Sigma11cons} Let $c\in\N$ and let $\varphi(\bar x)$ be a $\Sigma^{1,b}_1$-formula without free set variables.
\begin{enumerate}\itemsep=0pt
\item[(a)] If $\V^1_2\vdash\varphi(\bar x)$, then $\S^1_2(\alpha)+\meyer^c_{M_1}\vdash\varphi(\bar x)$.
\item[(b)] If $\U^1_2\vdash\varphi(\bar x)$, then $\S^1_2(\alpha)+\meyer^c_{M_2}\vdash\varphi(\bar x)$.
\end{enumerate}
\end{corollary}

\begin{proof} We prove only~(b); the proof of~(a) is analogous. We
  treat strict formulas first. Assume
  that~$\varphi(\bar x)\in\hat\Sigma^{1,b}_1$
  and~$\U^1_2\vdash\varphi(\bar x)$. Say,~$\bar x=(x_1,\ldots,
  x_k)$. Let~$\varphi'(x):=\varphi(\pi_1(x),\ldots,\pi_k(x))$ where
  the~$\pi_i\in\PV$ compute the
  projections~$\pi_i(\langle x_1,\ldots, x_k\rangle)=x_i$.
  Then~$\S^1_2(\alpha)\vdash(\forall
  x\varphi'(x)\leftrightarrow\forall\bar x\varphi(\bar x))$. In
  particular,~$\U^1_2\vdash\varphi'(x)$. Choose~$M$
  for~$\varphi'(x)\in\hat\Sigma^{1,b}_1$ according to
  Theorem~\ref{thm:wit}~(b). Note~$M$ has one input tape and no
  oracles.  By
 Theorem~\ref{thm:equiv2}~(b),~$\S^1_2(\alpha)+\meyer^c_{M_2}\vdash\meyer_{M}^d$
  for some~$d\in\N$.  We
  claim~$\S^1_2(\alpha)+\meyer^d_{M}\vdash \varphi'(x)$.

  Argue in~$\S^1_2(\alpha)+\meyer^d_{M}$ and let~$x$ be
  given. Set~$n:=\max\{|x|,2\}$ and choose~$C$ according
  to~$\meyer_{M}^d$ for~$n$.  Then~$x<2^n$ and~$Y:=C_x(\cdot)$ is a
  halting computation of~$M$ on~$x$.  Note~$Y$ exists
  by~$\Delta^b_1(\alpha)$-comprehension. Then get~$\varphi'(x)$ by
  Theorem~\ref{thm:wit}~(b).
\end{proof}
 
 \begin{remark} We do not need the full strength of
   Theorem~\ref{thm:wit}~(a): we can replace~$\S^1_2(\alpha)$
   by~$\U^1_2$ and then argue for Corollary~\ref{cor:Sigma11cons}~(a)
   as follows. From~$\V^1_2\vdash\varphi(\bar x)$
   infer~$\U^1_2\vdash(\meyer^c_{M_1}\to\varphi(\bar x))$ as seen. But
   this is logically equivalent to a~$\Sigma^{1,b}_1$ formula, still
   without free set variables. By
   Lemma~\ref{lem:alpha},~$\S^1_2(\alpha)+\meyer^c_{M_1}\vdash\meyer_{M_2}^d$
   for some~$d\in\N$.  By
   Corollary~\ref{cor:Sigma11cons}~(b),~$\S^1_2(\alpha)+\meyer^c_{M_2}\vdash(\meyer^c_{M_1}\to\varphi(\bar
   x))$. Hence~$\S^1_2(\alpha)+\meyer^c_{M_1}\vdash \varphi(\bar x)$.
  \end{remark}

\begin{proof}[Proof of Theorem~\ref{thm:congammaM}] 
  We prove only (a); the proof of (b) is analogous.
  If~$\varphi(\bar x)$ and~$(N,\mathcal Y)$ are as stated, (a) of the
  corollary implies~$(N,\mathcal Y)\models\meyer^c_{M_1}$ for
  all~$c\in\N$.
\end{proof}

%\begin{proof}[Proof of Theorem~\ref{thm:maincon}~(a).] If  $\S^1_2\cup\q{$\EXP\not\subseteq\Ppoly$}$ is inconsistent, then, by compactness, $\S^1_2\vdash\meyer_{M_1}^c$ for some $c\in\N$.By (a) of the corollary, $\S^1_2(\alpha)$ proves every $\varphi(\bar x)\in\Sigma^{1,b}_1$ proved by $\V^1_2$.By number-sort conservativity of $\S^1_2(\alpha)$ over $\S^1_2$ (Lemma~\ref{lem:CM}), this contradicts Takeuti's theorem~\ref{thm:takeuti}. \end{proof}


\subsection{Consistency of the $\alpha$-formalization}

While we do not know whether Lemma~\ref{lem:alphagamma} holds
for~$\S^1_2(\alpha)$, we can show a weakening:

\begin{lemma}\label{lem:alphagammaproof}\
For every $c \in \N$ there is $d \in \N$ such that
\begin{enumerate}\itemsep=0pt
\item[(a)] if $\S^1_2(\alpha)\vdash\alpha^c_{M_1}$, then $\S^1_2\vdash\meyer^d_{M_1}$,
\item[(b)]  if $\S^1_2(\alpha)\vdash\alpha^c_{M_2}$, then $\S^1_2\vdash\meyer^d_{M_2}$.
\end{enumerate}
\end{lemma}

Before we prove it, we argue that this implies our main consistency result:

\begin{proof}[Proof of Theorem~\ref{thm:maincon}.] As already stated,
  Part~(a) follows from Theorems~\ref{thm:takeuti}
  and~\ref{thm:congammaM}. For Part~(b),
  assume~$\S^1_2(\alpha)\cup\{\neg\alpha^c_{M_1}\mid c\in\N\}$ is
  inconsistent. By compactness,~$\S^1_2(\alpha)\vdash \alpha^c_{M_1}$
  for some~$c\in\N$. By Part~(a) of the
  lemma,~$\S^1_2\vdash \meyer^d_{M_1}$ for some~$d\in\N$. This
  contradicts Part~(a) of the theorem, which we just proved.
\end{proof}

The proof of Lemma~\ref{lem:alphagammaproof} is by analysis of the
models~$(N,\C_N)$ from Lemma~\ref{lem:CM} and relies on formally
verified model-checkers; concretely, the proof uses the following weak
version of~\cite[Lemma~20]{abm}:

\begin{lemma}\label{lem:mc} 
  For every~$\Pi^{b}_1$-formula~$\varphi(\bar x)$ there is an
  explicit~$\PSPACE$-machine~$M_\varphi$ and
  a~$\Delta^b_1(\alpha)$-formula~$C_\varphi(\bar x,v)$ such that
\begin{enumerate}\itemsep=0pt
\item[(a)] $\S^1_2(\alpha)\vdash \q{$Y$ is an accepting computation of $M_\varphi$ on $\bar x$}
\ \to\ \varphi(\bar x)$,
\item[(b)] $\S^1_2(\alpha)\vdash  \varphi(\bar x)\ \to\ \q{$C_\varphi(\bar x,\cdot)$ is an accepting computation of $M_\varphi$ on $\bar x$}$. 
\end{enumerate} 
\end{lemma}

The key lemma is 


\begin{lemma}\label{lem:CMT12} If $(N,\mathcal Y)\models \S^1_2(\alpha)+\alpha^c_{M_2}$ for some $c\in\N$, then
$(N,\C_N)\models\T^1_2(\alpha)$.
\end{lemma}


\begin{proof} 
  By  Lemma~\ref{lem:CM} we
  only have to verify~$\Pi^b_1(\alpha)$-induction in~$(N,\C_N)$.
  Let~$\varphi(\bar X,\bar x,y)$ be a~$\Pi^b_1(\alpha)$-formula,
  let~$\bar A$ be parameters from~$\C_N$, let~$\bar a$ be parameters
  from~$N$, and let~$a\in N$. We have to show
$$
(N,\C_N)\models\varphi(\bar A,\bar a,0)\wedge \forall y{<}a\ (\varphi(\bar A,\bar a,y)\to \varphi(\bar A,\bar a,y{+}1))\ \to\ \varphi(\bar A,\bar a,a).
$$

Every set parameter in $\bar A$ equals $\hat C\in\C_N$ for some
$C\in N$. Let $\bar C$ collect these. Using the notation
from the proof of Lemma~\ref{lem:CM}, we have
$\varphi(\bar A ,\bar a,y )^*=\psi(\bar C,\bar a,y)$
where $\psi(\bar z,\bar x,y)\in\Pi^b_1$ and $\varphi(\bar A,\bar a,y)$ is equivalent to 
$\psi(\bar C,\bar a,y)$ in $(N,\C_N)$.
Choose $\chi(u)\in\Pi^b_1$ such that $\S^1_2$ proves
$(\chi(\langle \bar z,\bar x,y\rangle) \leftrightarrow
\psi(\bar z,\bar x,y))$. 
Choose $M_{\chi}$ according to
Lemma~\ref{lem:mc}. By $\Delta^b_1(\alpha)$-comprehension and the choice of $\chi$ we have
$$
(N,\mathcal Y)\models \forall \bar z, \bar x, y\ \big( \exists_2 Y\ 
\q{$Y$ is an accepting computation of $M_{\chi}$ on $\langle \bar z, \bar x, y\rangle$}\leftrightarrow
\psi(\bar z, \bar x, y)\big).
$$
Choose~$n := \max\{|\bar{C}|,|\bar{a}|,|a|,2\}$ in~$N$.
Choose~$e \in \N$ and~$m := n^e$ in~$N$ such that~$N$ satisfies~$\forall \bar{z},\bar{x},y{<}2^n \; |\langle
\bar{z},\bar{x},y\rangle| \leq m$.
Since~$(N,\mathcal Y)\models \alpha^c_{M_2}$, by
Theorem~\ref{thm:equiv2}~(a) there is~$d \in \N$ such
that~$(N,\mathcal Y)\models
\alpha^d_{M_{\chi}}$. Applying~$\alpha^d_{M_{\chi}}$
to~$m$ gives~$D\in N$ such that
$$
(N,\mathcal Y)\models\forall\bar z, \bar x, y{<}2^{n}\ \big(D(\langle
\bar z,\bar x,y\rangle )=1\leftrightarrow \psi(\bar z, \bar x,
y)\big).
$$
But this sentence is number-sort, so we can
equivalently replace~$\mathcal Y$ by~$\C_N$, particularize~$\bar z$
to~$\bar{C}$ and~$\bar x$ to~$\bar{a}$, and then
replace~$\psi(\bar C,\bar a,y)$ back
to~$\varphi(\bar A,\bar a,y)$. Since~$\bar{C},\bar{a},a<2^n$ 
in~$N$, 
$$
(N,\C_N)\models \forall y{\le }a\ \big( E(y)=1\leftrightarrow
\varphi(\bar A,\bar a,y) \big)
$$
where~$E \in N$ is a circuit in $N$ such that  $N\models\forall y{<}2^n\ E(y)=D(\langle \bar C,\bar a,y\rangle)$.  We are left to show
$$
(N,\C_N)\models E(0)=1\wedge \forall y{<}a\ (E(y)=1\to E(y{+}1)=1)\ \to\ E(a)=1.
$$
This is number-sort and, in fact, an instance of $\Delta^b_1$-induction, which holds in $N\models\S^1_2$.
\end{proof}


\begin{proof}[Proof of Lemma~\ref{lem:alphagammaproof}.] 
  We prove only~(a); the proof of~(b) is
  analogous. Assume~$\S^1_2(\alpha)\vdash\alpha^c_{M_1}$ and
  let~$N\models\S^1_2(\alpha)$. We have to
  show~$N\models\meyer^d_{M_1}$ for some~$d\in \N$.

  By Lemma~\ref{lem:CM},~$(N,\C_N)\models \S^1_2(\alpha)$.  By
  assumption,~$(N,\C_N)\models \alpha^c_{M_1}$. By
  Lemma~\ref{lem:alpha} there is~$e\in\N$ such
  that~$(N,\C_N)\models\alpha^e_{M_2}$. By
  Lemma~\ref{lem:CMT12},~$(N,\C_N)\models\T^1_2(\alpha)$.  By
  Lemma~\ref{lem:alphagamma},~$(N,\C_N)\models\meyer^d_{M_1}$ for
  some~$d\in\N$. Being number-sort,~$N\models\meyer^d_{M_1}$ follows.
\end{proof}


\subsection{Consistency from separation}

The following strengthens Theorem~\ref{thm:nbsort}:


\begin{theorem}\label{thm:nbsortM} Assume $N\models\S^1_2+\neg\varphi$ where $\varphi$ is a number-sort sentence.
\begin{enumerate}\itemsep=0pt
\item[(a)] If $\forall\Sigma^{1,b}_1(\V^1_2)\vdash\varphi$, then $N\models\q{$\EXP\not\subseteq\Ppoly$}$.
\item[(b)] If $\forall\Sigma^{1,b}_1(\U^1_2)\vdash\varphi$, then $N\models\q{$\PSPACE\not\subseteq\Ppoly$}$.
\end{enumerate}
\end{theorem}



\begin{proof} We only prove~(a), the proof of~(b) is analogous. It
  suffices to show for all~$N$ and~$c\in\N$:
  if~$N\models\S^1_2+\meyer^c_{M_1}$,
  then~$(N,\C_N)\models\forall\Sigma^{1,b}_1(\V^1_2)$.

  Assume~$N\models\S^1_2+\meyer^c_{M_1}$ and
  let~$\varphi(\bar X,\bar x)$ be a~$\Sigma^{1,b}_1$-formula provable
  in~$\V^1_2$.  Let~$\bar A$ and~$\bar a$ be parameter tuples
  from~$\C_N$ and~$N$.  We have to
  show~$(N,\C_N)\models \varphi(\bar A,\bar a)$.
  Using the notation from the proof of Lemma~\ref{lem:CM}, recall 
    that~$\varphi(\bar A,\bar a)^*$ is obtained by replacing every~$A$
  from~$\bar A$ by~$C(\cdot)$ for some circuit~$C\in N$. Let~$\bar C$
  collect these. Then~$\varphi(\bar A,\bar a)^*=\psi(\bar C,\bar a)$
  for a~$\Sigma^{1,b}_1$-formula~$\psi(\bar y,\bar x)$
  and~$\psi(\bar C,\bar a)$ is equivalent to~$\varphi(\bar A,\bar a)$
  in~$(N,\C_N)$. We claim~$(N,\C_N)\models\psi(\bar C,\bar a)$.

  Since~$\V^1_2$ proves~$\forall_2 \bar X\ \varphi$,
  by~$\Delta^b_1(\alpha)$-comprehension~$\V^1_2$ proves
$$
\chi\ :=\ (\q{$\bar y$ is a tuple of circuits} \to \psi(\bar y,\bar x)).
$$
This is a~$\Sigma^{1,b}_1$-formula without free set
variables. Thus,~$\S^1_2(\alpha)+\meyer_{M_1}^c\vdash\chi$ by
Corollary~\ref{cor:Sigma11cons}~(a).
Thus,~$(N,\C_N)\models\forall \bar y\forall\bar x \ \chi$.
Plugging~$\bar C$ for~$\bar y$ and~$\bar a$ for~$\bar x$ gives our
claim.
\end{proof}





\section{Magnification}\label{sec:magnification}



Write
~$\exists^{\infty}n{\in}\Lg\ \varphi(n,\ldots)$
for~$\forall u\ \exists v\ (|v|>|u|\wedge \varphi(|v|,\ldots))$.



\begin{definition} Let~$c\in\N$ and let~$M$ be an explicit~$\EXP$-
  or~$\PSPACE$-machine~$M$. Define
$$
\io\meyer^{c}_{M}:=\exists^{\infty}n{\in}\Lg\ \exists C{<}2^{n^c}\ \forall x{<}2^n\ \q{$C_x(\cdot)$ is a halting computation of $M$ on $x$}.
$$
Set
$
\q{$\EXP\not\subseteq\ioPpoly$}:=\big\{\neg \io\meyer^{c}_{M_1}\mid c\in\N \big\}
$ and $
\q{$\PSPACE\not\subseteq\ioPpoly$}:=\big\{\neg \io\meyer^{c}_{M_2}\mid c\in\N \big\}.$
\end{definition}
The sentence~$\io\meyer^{c}_{M}$ states that~$M$ is simulated by
size-$n^c$ circuits on unboundedly many input lengths~$n$. The
theories state that for all but boundedly many input lengths~$n$ the
universal machines are not simulated by size-$n^c$ circuits.  

One can
easily improve Theorem~\ref{thm:maincon}~(a):

\begin{corollary}\label{cor:aecons} 
$\S^1_2\cup \q{$\EXP\not\subseteq\ioPpoly$}$ is consistent.
\end{corollary}

\begin{proof} 
  This follows from Theorem~\ref{thm:ioM} below via Takeuti's
  Theorem~\ref{thm:takeuti}. One can also argue directly from
  Theorem~\ref{thm:maincon}~(a) as follows. Inconsistency would mean,
  by compactness, that~$\S^1_2\vdash\io\meyer^{c}_{M_1}$ for
  some~$c\in\N$. It suffices to infer~$\S^1_2\vdash\meyer^d_{M_1}$ for
  some~$d\in\N$.

  The sentence~$\io\meyer^{c}_{M_1}$ has the
  form~$\forall u \exists v \varphi(u,v)$ with~$\varphi(u,v)$
  bounded. By Parikh's
  theorem,~$\S^1_2\vdash \forall u\exists v{<}t(u)\varphi(u,v)$ for
  some term~$t(u)$.  Argue
  in~$\S^1_2$. Let~$n\in\Log$. Choose~$v<t(u)$
  according~$\io\meyer^{c}_{M_1}$ for~$u:=2^n$. Then~$n<m:=|v|\le n^e$
  for suitable~$e\in\N$. Choose~$C<2^{m^c}$ according
  to~$\io\meyer^{c}_{M_1}$ for this~$m$, i.e.,~$C_x(\cdot)$ is a
  halting computation of~$M_1$ on~$x$ for
  all~$x<2^m$. Then~$C<2^{n^{d}}$ for~$d:=ec$ and~$C_x(\cdot)$ is a
  halting computation of~$M_1$ on~$x$ for all~$x<2^n$.
\end{proof}

\begin{remark}\label{rem:void}  
 %\arand{I don't buy the difference: each is as true or false as the    other because $\EXP$ has natural and highly uniform complete    problems (this is not a proof of course). The comment about    ``evidence'' is fine (to repair our ABM comment in abstract), but    in intro or conclusions} While $\EXP\not\subseteq\Ppoly$ is a  common conjecture, this may be not so for the hypothesis that  $\EXP\not\subseteq\ioPpoly$. When in doubt one may hesitate to  interpret the corollary as evidence for its truth but may prefer to  interpret the corollary as a barrier result for disproving it.  We  leave the choice of interpretation to the reader's inclination. 
 We discuss almost everywhere lower bounds only for the sake of a magnification result, namely Theorem~\ref{thm:magn}. Observe that the corresponding statement for \q{$\EXP\not\subseteq\Ppoly$} is void. The reason is that this theory is $\Sigma_1$, i.e., its sentences can be written in the form $\exists x\varphi(x)$ with $\varphi(x)$ bounded. If such a theory is true, then  $\S^1_2$ proves it.  
 
 This has been overlooked in \cite{abm}. \end{remark}

We turn to the proof of Theorem~\ref{thm:magn}. The starting point is
a straightforward analogue of Lemma~\ref{lem:alpha}.

\begin{lemma}\label{lem:iogamma} \
\begin{enumerate}\itemsep=0pt
\item[(a)] For every explicit $\EXP$-machine $M$ and every $c\in\N$ there is $d\in\N$ such that 
$$
\S^1_2\vdash (\io\meyer_{M_1}^c\to\io\meyer_{M}^d).
$$ 
%Moreover, if $M$ is an explicit $\PSPACE$-machine, then $\S^1_2(\alpha)\vdash (\meyer_{M_1}^c\to\meyer_{M}^d).$
\item[(b)] For every explicit $\PSPACE$-machine $M$ and every $c\in\N$ there is $d\in\N$ such that 
$$
\S^1_2\vdash (\io\meyer_{M_2}^c\to\io\meyer_{M}^d).
$$ 
\end{enumerate}
\end{lemma}
\begin{proof} We prove only (a); the proof of (b) is
  analogous. Let~$t_M$ witness~$M$. Argue in~$\T^1_2(\alpha)$ and
  assume~$\io\meyer_{M_1}^c$.  Choose~$e\in\N$ such
  that~$\langle M,x,t_M(x)\rangle<2^{|x|^e}$ for all~$x>0$.
  Let~$n\in\Log$.  By~$\io\meyer_{M_1}^c$ choose~$\ell\in\Log$
  with~$\ell>(n+1)^e$ and such that there is a circuit~$C$ of size at
  most~$\ell^c$ such that~$C_y(\cdot)$ is a halting computation
  of~$M_1$ on~$y$ for all~$y<2^\ell$.

  Let~$m:=\lfloor\ell^{1/e}\rfloor$.  Note that~$m>n$
  because~$\ell > (n+1)^e$. We will use~$m$ to witness~$\io\meyer_M^d$
  beyond~$n$. First note
  that~$\langle M,x,t_M(x)\rangle<2^{m^e}\le 2^\ell$ for
  all~$x<2^m$. Hence, for all~$x<2^m$: 
\begin{center}
$\q{$C_{\langle M,x,t_M(x)\rangle}(\cdot)$ is a halting computation of $M_1$ on $\langle M,x,t_M(x)\rangle$}$.
\end{center}

We are left to find a small circuit~$D$ such that, for all~$x<2^m$,
the set~$D_x(\cdot)$ is a halting computation of~$M$ on~$x$.
Choose~$f\in\N$ such that~$C_{\langle M,x,t_M(x)\rangle}$ has at
most~$m^f$ inputs for all~$x<2^m$,
so~$C_{\langle M,x,t_M(x)\rangle}(\cdot)<2^{m^f}$ for all~$x<2^m$.  By
Lemma~\ref{lem:circuit} choose a circuit~$D$ such that for all~$x<2^m$
and all~$v<2^{m^f}$:
$$
D(x,v)=G_1(C_{\langle M,x,t_M(x)\rangle}(\cdot),x,v),
$$
where~$G_1$ is from Lemma~\ref{lem:M1}~(b).  Then~$D$ works and has size
at most~$m^{d}$, for some~$d\in\N$.
\end{proof}

We observe that Theorem~\ref{thm:nbsortM} generalizes to almost-everywhere lower bounds:


\begin{theorem}\label{thm:ioM} Assume $N\models\S^1_2+\neg\varphi$ where $\varphi$ is a number-sort sentence.
\begin{enumerate}\itemsep=0pt
\item[(a)] If $\forall\Sigma^{1,b}_1(\V^1_2)\vdash\varphi$, then $N\models\q{$\EXP\not\subseteq\ioPpoly$}$.
\item[(b)] If $\forall\Sigma^{1,b}_1(\U^1_2)\vdash\varphi$, then $N\models\q{$\PSPACE\not\subseteq\ioPpoly$}$.
\end{enumerate}
\end{theorem}



\begin{proof} We prove only (a), with (b) being analogous. The proof
  is the same as that of Theorem~\ref{thm:nbsortM}~(a) except that we
  need a version of Corollary~\ref{cor:Sigma11cons}~(a)
  for~$\io\meyer^c_{M_1}$ instead of~$\meyer^c_{M_1}$. Following that
  proof with Lemma~\ref{lem:iogamma} instead of Lemma~\ref{lem:alpha},
  we have to show, for every~$d\in\N$,
  that~$\S^1_2(\alpha)+\io\meyer^d_{M}$ proves
  every~$\varphi(x)\in\hat\Sigma^{1,b}_1$ which is proved by~$\V^1_2$;
  here,~$M$ is chosen for~$\varphi(x)$ according to
  Theorem~\ref{thm:wit}~(a).  This is easy: argue
  in~$\S^1_2(\alpha)+\io\meyer^d_{M}$ and let~$x$ be
  given. Set~$n:=\max\{|x|,2\}$. By~$\io\meyer^d_{M_1}$ there
  are~$n<m\in\Log$ and~$C<2^{m^d}$ such that for all~$y<2^m$, the
  set~$C_y(\cdot)$ is a halting computation of~$M$ on~$y$.
  Then~$Y:=C_x(\cdot)$ is a halting computation of~$M$ on~$x$.  As~$Y$
  exists by~$\Delta^b_1(\alpha)$-comprehension, we get~$\varphi(x)$ by
  Theorem~\ref{thm:wit}~(a).
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:magn}] We prove only (a), with
  (b) being
  analogous. If~$\S^1_2\not\vdash\q{$\EXP\not\subseteq\ioPpoly$}$, we
  find~$c\in\N$ and a model~$N\models\S^1_2+\io\meyer^c_{M_1}$.
  Theorem~\ref{thm:ioM} (a) with~$\varphi:=\neg\io\meyer^c_{M_1}$
  implies~$\forall\Sigma^{1,b}_1(\V^1_2)\not\vdash\neg\io\meyer^c_{M_1}$.
\end{proof}




\section{Conclusion}\label{sec:concl}

The central research question is whether~$\S^1_2$ can be proved consistent with~$\NP\not\subseteq\Ppoly$. We
achieved~$\EXP$ in place of~$\NP$ but lowering this to~$\PSPACE$ is
still open:

\begin{theorem*} Is $\S^1_2\cup\q{$\PSPACE\not\subseteq\Ppoly$}$ consistent?
\end{theorem*}
 
This question deserves some interest as a frontier question, also when
understood via Theorem~\ref{thm:nbsort} as a question concerning
independence. Frontier questions can be misleading, of course, but
here our aim is to emphasize one of the weakest open questions whose
answer still requires a new insight. The answer is not sensible to the formalization:
 
 \begin{proposition} The following are equivalent.
 \begin{enumerate}\itemsep=0pt
 \item[(a)] $\S^1_2\cup\{\neg\meyer^c_{M_2}\mid c\in\N\}$ is consistent.
 \item[(b)] $\S^1_2\cup\{\neg\meyer^c_{M}\mid c\in\N\}$ is consistent for some explicit $\PSPACE$-machine $M$.
  \item[(c)] $\S^1_2(\alpha)\cup\{\neg\alpha^c_{M_2}\mid c\in\N\}$ is consistent.
 \item[(d)] $\S^1_2(\alpha)\cup\{\neg\alpha^c_{M}\mid c\in\N\}$ is consistent for some explicit $\PSPACE$-machine $M$.
\end{enumerate}
 \end{proposition}
 
 \begin{proof} The equivalence (a)$\Leftrightarrow$(b) follows from
   Theorem~\ref{thm:equiv2}~(b), the equivalence (c)$\Leftrightarrow$(d)
   from Theorem~\ref{thm:equiv2}~(a), the implication (c)$\Rightarrow$(a)
   from Theorem~\ref{thm:equiv2}~(c). For (a)$\Rightarrow$(c) assume
   (c) fails; by compactness,~$\S^1_2(\alpha)\vdash \alpha^c_{M_2}$
   for some~$c\in\N$; by
   Lemma~\ref{lem:alphagammaproof}~(b),~$\S^1_2\vdash \meyer^d_{M_2}$
   for some~$d$, so (a) fails.
 \end{proof} 
 
  
 Finally, we note some conditional consistency results based on
 witnessing methods, analo\-gous to the already mentioned ones from
 \cite{cokra}. By~$\PTIME^{\NP}_{\mathrm{tt}}$ we denote
 the class of problems decidable in polynomial time with non-adaptive
 queries to an~$\NP$ oracle.

\begin{proposition}\label{prop:conditional}\
\begin{enumerate}\itemsep=0pt
\item[(a)] $\S^1_2 \cup \q{$\PSPACE\not\subseteq\Ppoly$}$ is consistent if  $\PSPACE\not\subseteq \PTIME^{\NP}_{\mathrm{tt}}$.
\item[(b)] $\S^2_2 \cup \q{$\PSPACE\not\subseteq\Ppoly$}$ is consistent if  
 $\PSPACE\not\subseteq\PTIME^{\NP}$. 
 \item[(c)] $\S^2_2 \cup \q{$\EXP\not\subseteq\Ppoly$}$ is consistent if  
 $\EXP\not\subseteq\PTIME^{\NP}$. 
\end{enumerate}
\end{proposition}


\begin{proof} We start with (b):
  If~$\S^2_2 \cup \q{$\PSPACE\not\subseteq\Ppoly$}$ is inconsistent, then,
  by compactness,~$\S^2_2\vdash\meyer^c_{M_2}$ for
  some~$c\in\N$. Thus,~$\S^2_2$ proves the
  following~$\Sigma_2^b$-formula with variable~$y$: 
  \begin{equation*}\label{eq:etaformula}
|y|>1\to \begin{array}{l}
\exists C{<}2^{|y|^c}\ \forall N,x,t{<}2^{|y|}\ 
 \q{$C_{\langle N,x,t\rangle}(\cdot)$ is a halting computation 
of $M_2$ on $\langle N,x,t\rangle$}.
\end{array}
\end{equation*} 
By Buss' witnessing theorem \cite{bussthesis} for~$\S^2_2$, there is a
function~$f$ computable in polynomial time with an~$\NP$-oracle such
that the set~$f(y)_{\langle N,x,t\rangle}(\cdot)$, i.e., the
set~$\eval(f(y),\langle N,x,t\rangle,\cdot)$, is a halting computation of~$M_2$
on~$\langle N,x,t \rangle$. This implies that the~$\PSPACE$-complete
problem decided by~$M_2$ is in~$\PTIME^{\NP}$.

(c): Proved analogously.

(a): If~$\S^1_2 \cup \q{$\PSPACE\not\subseteq\Ppoly$}$ is inconsistent,
then, by compactness,~$\S^1_2\vdash\meyer^c_{M_2}$ for some~$c\in\N$.
By \cite[Theorem 7.3.5]{krabuch} there is a polynomial time algorithm
that given~$n>1$ in unary and~$N,x,t<2^n$ asks~$O(\log n)$ {\em
  witness queries} (see~\cite[Definition 6.3.6]{krabuch}) to an~$\NP$
oracle and outputs a circuit~$C$ such that~$C_{N,x,t}(\cdot)$ is a
halting computation of~$M_2$ on~$x$. The output~$C$ depends on the
answers to the witness queries but, since~$M_2$ is deterministic, all
outputs~$C$ encode the same computation.  Modify this algorithm to
output 1 or~0 depending on whether this computation is accepting or
rejecting.  By \cite[Corollary 6.3.5]{krabuch} this implies that
the~$\PSPACE$-complete problem decided by~$M_2$ is decidable in
polynomial time with~$O(\log n)$ Boolean queries to an~$\NP$
oracle. Instead, one can also use~$n^{O(1)}$ many non-adaptive queries
(see \cite[Theorem 6.2.3]{krabuch}).
\end{proof}


\begin{remark} 
  The analogue of Proposition~\ref{prop:conditional} for higher
  levels~$\S^i_2$ is void: if~$\PSPACE\not\subseteq\NP^\NP$, then the
  theory \q{$\PSPACE\not\subseteq\Ppoly$} is true
  \cite[Theorem~4.2]{kl}, so consistent with any sound theory; same
  for~$\EXP$ by Meyer's argument.
\end{remark}

To infer the consistency of~$\S^1_2\cup \q{$\EXP
    \not\subseteq \Ppoly$}$ from a witnessing argument along the lines
  of Proposition~\ref{prop:conditional} we would need the
  separation~$\EXP \not\subseteq \PTIME^{\NP}_{\mathrm{tt}}$, which is
  open. It is remarkable that the G\"odel-type argument that underlies
  our proof of consistency of~$\S^1_2 \cup \q{$\EXP \not\subseteq
    \Ppoly$}$ is able bypass this obstacle. We find this encouraging.

\bigskip\noindent\textbf{Acknowledgements} First author was partially
supported by grant PID2022-138506NB- C22 (PROOFS BEYOND) and the
Severo Ochoa and María de Maeztu Program for Centers and Units of
Excellence in R\&D (CEX2020-001084-M) of the AEI, and the CERCA and
ICREA Academia Programmes of the Generalitat de Catalunya.
 

\begin{thebibliography}{00}
\bibitem{ajtai}
M.~Ajtai. The complexity of the pigeonhole principle.
  Proc.  29th Annual IEEE Symposium on Foundations of
  Computer Science (FOCS'88), pp. 346-355,  1988.
  
  \bibitem{am}
A.~Atserias and M.~M{\"u}ller. Partially definable forcing and bounded
  arithmetic. Archive for Mathematical Logic 54  (1):  1-33, 2015.
  
  \bibitem{at} A. Atserias and I. Tzameret.
Feasibly constructive proof of Schwartz-Zippel lemma and the complexity of finding hitting sets.
Proc. 57th ACM Symposium on the Theory of Computation (STOC'25), 2025.


\bibitem{abm} A. Atserias, S. Buss, M. Müller. On the consistency of circuit lower bounds for non-deterministic time. Journal of Mathematical Logic  25 (3): 2450023, 2025.

\bibitem{bb} A. Beckmann, S. Buss. Improved witnessing and local improvement principles for second-order bounded arithmetic. ACM Transactions on Computational Logic 15 (1): Article 2, 2014. 


\bibitem{bussthesis} S. R. Buss. Bounded Arithmetic. Bibliopolis, Naples, 1986.


\bibitem{BKO:Consistency}
J.~Byd{\v z}ovsk{\'y}, J.~Kraj{\'\i\v c}ek and I.~C. Oliveira.
  Consistency of circuit lower bounds with bounded theories.
  Logical Methods in Computer Science 16 (2): 12:1-12:16, 2020.

\bibitem{BydzovskyMuller:Ultrapowers}
J.~Byd{\v z}ovsk{\'y} and M.~M{\"u}ller. Polynomial time ultrapowers
  and the consistency of circuit lower bounds. Archive for Mathematical
  Logic 59 (1): 127-147, 2020.
  
  
\bibitem{CKKO:LEARN}
M.~Carmosino, V.~Kabanets, A.~Kolokolova and I.~C. Oliveira.
  {LEARN}-uniform circuit lower bounds and provability in bounded
  arithmetic. Proc. 62nd IEEE Symposium on Foundations of Computer
  Science (FOCS'21), pp. 770--780, 2021.
  
  \bibitem{beyond} L. Chen, S. Hirahara, I. C. Oliveira, J. Pich, N. Rajgopal, R. Santhanam.
  Beyond natural proofs: hardness magnification and locality. Journal of the  ACM 69 (4): Article 25, 2022.
  
\bibitem{cook}  S. A. Cook. 1975. Feasibly constructive proofs and the propositional calculus (preliminary version). Proc. 7th ACM Symposium on Theory of Computing (STOC'75), ACM, pp. 83--97, 1975.

\bibitem{cokra}
S. A. Cook, J. Kraj\'{i}\v{c}ek. Consequences of the provability of $\NP \subseteq \Ppoly$. Journal of Symbolic Logic 72 (4): 1353-1371, 2007.

\bibitem{hp}
P. H\'{a}jek, P. Pudl\'{a}k.  Metamathematics of First-Order Arithmetic. Perspectives in Mathematical Logic, Springer, 1998.

%\bibitem{ew} R.~Impagliazzo, V.~Kabanets and A.~Wigderson. In search of an easy  witness: Exponential time vs. probabilistic polynomial time. Journal  of Computer and Systems Sciences \textbf{65} (4): 672-694,  2002.

\bibitem{kl}
R. M. Karp, R. J. Lipton. Some connections between nonuniform and uniform complexity classes. Proc. ACM Symposium on Theory of Computing (STOC'80), pp. 302-309, 1980.


\bibitem{knt} L. Ko\l odziejczyk, P. Nguyen and N. Thapen.
The provably total NP search problems of weak second order bounded arithmetic.
Annals of Pure and Applied Logic 162 (6): 419-446, 2011.

\bibitem{kraexp}
J. Kraj\'{i}\v{c}ek.
Exponentiation and second order bounded arithmetic. Annals of Pure and Applied Logic 48 (3): 261-276, 1990.

\bibitem{krabuch}
J. Kraj\'{i}\v{c}ek.
Bounded Arithmetic, Propositional Logic, and Complexity Theory. 
Encyclopedia of Mathematics and Its Applications 60, Cambridge University Press, 1995.

\bibitem{KrajicekOliveira:Unprovability}
J.~Kraj\'\i\v{c}ek and I.~C. Oliveira. Unprovability of circuit upper
  bounds in {C}ook's theory {PV}. Logical Methods in Computer Science
  13 (1:4), 2017.
  
  \bibitem{kpt}
J. Kraj\'{i}\v{c}ek, P. Pudl\'{a}k and G. Takeuti. Bounded arithmetic and the polynomial hierarchy. Annals of Pure and Applied Logic 52 (1-2): 143-153, 1991.

  
  \bibitem{kpw}
  J.~Kraj\'\i\v{c}ek, P. Pudl\'ak, A. Woods. Exponential lower bound to the size of bounded depth Frege proofs of the Pigeon Hole Principle. Random Structures and Algorithms 7 (1): 15-39, 1995.
  
  \bibitem{partialstr}
M. Müller.
Typical forcing, NP search problems and an extension of a theorem of Riis.
Annals of Pure and Applied Logic 172 (4): Article 102930, 2021.

\bibitem{mp} M. M\"uller, J. Pich.
Feasibly constructive proofs of succinct weak circuit lower bounds.
Annals of Pure and Applied Logic 172 (2): Article 102735, 2020.

%\bibitem{os} I. C. Oliveira, R. Santhanam. Hardness magnification for natural problems.  Proc. 59th Symposium on Foundations of Computer Science (FOCS'18), pp. 65-76, 2018.

\bibitem{pbi}
T. Pitassi, P. Beame, R. Impagliazzo. Exponential lower bounds for the pigeonhole principle. Computational Complexity 3: 97-140, 1993. 

\bibitem{bottom}
P. Pudl\'ak. A bottom-up approach to foundations of mathematics. In: P. H\'ajek (ed.), Gödel ’96: Logical Foundations of Mathematics, Computer Science and Physics - Kurt Gödel’s Legacy. Lecture Notes in Logic. Cambridge University Press, pp. 81-97, 2017.

%\bibitem{pudlakbuch} P. Pudlák. Logical Foundations of Mathematics and Computational Complexity, A gent\-le Introduction. Springer, 2013.

\bibitem{feasinc} P. Pudlák. Incompleteness in the finite domain. Bulletin of Symbolic Logic 23 (4): 405-441, 2017.


\bibitem{razclb} A. A. Razborov. Bounded arithmetic and lower bounds in Boolean complexity. Feasible Mathematics II, pp. 344-386, 1995.

\bibitem{razlower} A. A. Razborov. Unprovability of lower bounds on the circuit size in certain fragments of bounded arithmetic. Izvestiya of the Russian Academy of Science 59: 201-224, 1995.

\bibitem{razannals} A. A. Razborov. Pseudorandom generators hard for k-DNF resolution and polynomial calculus. Annals of Mathematics  181 (2): 415-472, 2015.

\bibitem{riis} S. Riis. Making infinite structures finite in models of second order bounded arithmetic. In: Arithmetic, proof theory and computational complexity, Oxford University Press, pp. 289-319, 1993.

 \bibitem{SanthanamWilliams:Uniformity}
R.~Santhanam and R.~Williams. On uniformity and circuit lower bounds.
  Computational Complexity 23 (2): 177-205, 2014.

\bibitem{takeuti}
G. Takeuti. Bounded arithmetic and truth definition.
 Annals of Pure and Applied Logic 39: 75-104, 1988.
 
 \bibitem{thapen} N. Thapen. On the consistency of stronger lower bounds for NEXP. Preprint 
 arXiv:2504.03320 [cs.LO], \url{https://arxiv.org/abs/2504.03320}, 2025.
 
 
% \bibitem{williams} R. Williams. Natural proofs versus derandomization. SIAM Journal on Computing 45 (2): 497-529,  2016.

\end{thebibliography}


\end{document}
