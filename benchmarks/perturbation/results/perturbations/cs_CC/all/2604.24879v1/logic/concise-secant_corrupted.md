\documentclass[12pt]{amsart}

\usepackage[headheight=1cm, left=2cm, right=2cm, top=3cm, bottom=2cm,
marginparwidth=1.7cm, marginparsep=4mm]{geometry}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\usepackage{amsthm}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\usepackage{xcolor}

\usepackage[colorlinks,
    colorlinks,
    linkcolor={red!80!black},
    citecolor={blue!80!black},
]{hyperref}

\newcommand{\maxideal}{\mathfrak{m}}
\newcommand{\CC}{\mathbb{C}}
\newcommand{\PP}{\mathbb{P}}


\numberwithin{equation}{section}
\counterwithin{figure}{section}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{fact}[theorem]{Fact}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}

\usepackage{todonotes}
\usepackage[dvipsnames]{xcolor}
\usepackage{booktabs}
\usepackage{setspace}
\setstretch{1.1}
\newcommand{\jjetodo}[1]{\todo[color=blue!40,bordercolor=blue,size=\footnotesize]{\textbf{Joa TODO: }#1}}
\newcommand{\jjeintodo}[1]{\todo[inline,color=blue!40,bordercolor=blue,size=\footnotesize]{\textbf{Joa TODO: }#1}}
\newcommand{\jjatodo}[1]{\todo[color=orange!40,bordercolor=orange,size=\footnotesize]{\textbf{Jak TODO: }#1}}
\newcommand{\jjaintodo}[1]{\todo[inline,color=orange!40,bordercolor=orange,size=\footnotesize]{\textbf{Jak TODO: }#1}}
\newcommand{\jjetoadd}{[{\color{ForestGreen}\texttt{add}}]}
\newcommand{\jjeins}[1]{[{\color{ForestGreen}{#1}}]}
\usetikzlibrary{matrix,arrows, cd, calc, bending, quotes}

\usepackage{enumitem}
\setlist[enumerate,1]{label=(\alph*), ref=(\alph*), itemsep=0em}

\newcommand{\kk}{\Bbbk}
\newcommand{\OO}{\mathcal{O}}
\newcommand{\spann}[1]{\left\langle #1\right\rangle}
\DeclareMathOperator{\ann}{ann}
\DeclareMathOperator{\degtopure}{\trianglerighteq}%
\DeclareMathOperator{\degto}{\trianglerighteq_{\Sigma}}%
\DeclareMathOperator{\notdegto}{\not\trianglerighteq_{\Sigma}}%
\DeclareMathOperator{\notdegtopure}{\not\trianglerighteq}%
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\GL}{GL}
\DeclareMathOperator{\SL}{SL}
\DeclareMathOperator{\charr}{char}
\DeclareMathOperator{\expdim}{expdim}
\DeclareMathOperator{\pr}{pr}
\newcommand{\Tdeg}[1]{T_{\OO_{#1}}}
\newcommand{\Tdegtw}{T_{\widetilde{\OO_{56}}}}
\newcommand{\BBname}{Bia{\l}ynicki-Birula}%
\newcommand{\Gmult}{\mathbb{G}_m}%
\newcommand{\modA}{\underline{A}}
\newcommand{\modB}{\underline{B}}
\newcommand{\modC}{\underline{C}}
\newcommand{\alg}[1]{\mathcal{A}_{111}^{#1}}
\DeclareMathOperator{\OpQuot}{Quot}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Spec}{Spec}
\DeclareMathOperator{\id}{id}
\DeclareMathOperator{\Gr}{Gr}
\DeclareMathOperator{\Hilb}{Hilb}
\DeclareMathOperator{\Quot}{Quot}
\DeclareMathOperator{\VSP}{VSP}
\DeclareMathOperator{\cVSP}{cVSP}
\newcommand{\VSPbord}{\underline{VSP}}
\DeclareMathOperator{\adj}{adj}

\newcommand{\VV}{\mathcal{V}}
\newcommand{\WW}{\mathcal{W}}
\newcommand{\ZZ}{\mathcal{Z}}
\newcommand{\VVhat}{\VV_{\,\hat{i}}}
\newcommand{\Vhatpar}[1]{V_{\,\hat{#1}}}
\newcommand{\Vhat}{\Vhatpar{i}}
\newcommand{\That}{\widehat{T}}
\newcommand{\pihat}{\widehat{\pi}}
\newcommand{\rhohat}{\widehat{\rho}}
\newcommand{\alphahat}{\widehat{\alpha}}
\newcommand{\UU}{\mathcal{U}}
\newcommand{\Tp}{\widetilde{T}^i}
\newcommand{\Tppar}[1]{\widetilde{T}^{#1}}
\newcommand{\Tpparfr}[1]{{\widetilde{T}^{\mathrm{fr}#1}}}
\newcommand{\varphifr}{\varphi^{\mathrm{fr}}}
\newcommand{\Fppar}[1]{\widetilde{F}^{#1}}
\newcommand{\Xppar}[1]{X'^{#1}}
\newcommand{\GLV}{\GL(V_{\bullet})}
\newcommand{\GLW}{\GL(W_{\bullet})}
\newcommand{\SLV}{\SL(V_{\bullet})}
\newcommand{\tspace}{V_{1, \dots, d}}
\newcommand{\tspacecurly}{\VV_{1, \dots, d}}
\newcommand{\tconcspace}{W_{1, \dots, d}}
\newcommand{\tconcspacecurly}{\WW_{1, \dots, d}}
\newcommand{\tconcspaceconc}{\tconcspace^{\mathrm{conc}}}
\newcommand{\LL}{\mathcal{L}}
\newcommand{\Lmot}{\mathbb{L}}
\DeclareMathOperator{\OpUnres}{Unres}
\newcommand{\unres}{\OpUnres_{i}(T)}
\newcommand{\unrespar}[2]{\OpUnres_{#1}(#2)}
\newcommand{\unresfull}{\unresfullpar{T}}
\newcommand{\unresfullpar}[1]{\OpUnres(#1)}
% \newcommand{\unresfr}{\OpUnres^{\mathrm{fr}}_{i}(T)}
\newcommand{\unresfr}{\OpUnres^{\mathrm{fr}}(T)}
\newcommand{\unresfrfullpar}[1]{\OpUnres^{\mathrm{fr}}(#1)}
\newcommand{\unresfrfull}{\unresfrfullpar{T}}
\newcommand{\unresfrpar}[2]{\OpUnres^{\mathrm{fr}}_{#1}(#2)}
\newcommand{\into}{\hookrightarrow}
\newcommand{\onto}{\twoheadrightarrow}
\newcommand{\Cen}[1]{\operatorname{Cen}_{#1}}%
\newcommand{\eval}{\epsilon_{\cA}}

\newcommand{\TGr}{T^{\Gr}}


\DeclareMathOperator{\rk}{rk}
\DeclareMathOperator{\brk}{brk}
\DeclareMathOperator{\bcrk}{bcrk}
\DeclareMathOperator{\gen}{gen}
\DeclareMathOperator{\smrk}{smrk}
\DeclareMathOperator{\Sym}{Sym}
\DeclareMathOperator{\Bl}{Bl}
\DeclareMathOperator{\Sing}{Sing}
\DeclareMathOperator{\Iso}{Iso}
\DeclareMathOperator{\im}{im}
\DeclareMathOperator{\Z}{Zeros}
\DeclareMathOperator{\Seg}{Segre}
\newcommand{\op}{\circ}
\newcommand{\sm}{\mathrm{sm}}
\newcommand{\unit}{\langle m \rangle}

\newcommand{\sigmahat}{\widehat{\sigma}}%
\newcommand{\csigma}{c\sigma}%
\newcommand{\csigmaOneGen}{c\sigma^{1gen}}%
\newcommand{\csigmafr}{c\sigma^{\mathrm{fr}}}%
\newcommand{\ckappa}{c\kappa}%
\newcommand{\Asigma}{\mathrm{A}\sigma}%
\newcommand{\AsigmaHilb}{\Asigma^{\Hilb}}%
\newcommand{\Arho}{\rho^{\mathrm{A}}}%
\newcommand{\csigmahat}{\widehat{\csigma}}%
\newcommand{\csigmahatfr}{\widehat{\csigma}^{\mathrm{fr}}}%
\newcommand{\ckappahat}{\widehat{\ckappa}}%
\newcommand{\cA}{\mathcal{A}}%

\usepackage{marginnote}
\begin{document}

\title{Unrestrictions and concise secant varieties}
\author{Jakub Jagie{\l}{\l}a}
\address[Jakub Jagie{\l}{\l}a]{Wydział Matematyki, Informatyki i Mechaniki, Uniwersytet Warszawski,
 ul.~Stefana Banacha
2, 02-097 Warsaw, Poland.}
\email{j.jagiella@uw.edu.pl}

\author{Joachim Jelisiejew}
\address[Joachim Jelisiejew]{Wydział Matematyki, Informatyki i Mechaniki, Uniwersytet Warszawski,
 ul.~Stefana Banacha
2, 02-097 Warsaw, Poland.}
\email{j.jelisiejew@uw.edu.pl}
\thanks{Both authors supported by National Science Centre grant 2023/50/E/ST1/0033.}
\date{\today{}}

\begin{abstract}
    We introduce the concise secant varieties, which are, informally speaking, modular partial desingularisations of secant varieties to
    Segre embeddings. More precisely, they are projective and birational to the abstract secant
    varieties, yet each of their points corresponds to a \emph{concise} tensor of appropriate
    border rank (that is, to a minimal border rank tensor).

    We discuss implications throughout the theory of tensors,
    including a characterisation of border rank $\leq r$ tensors as
    unrestrictions of minimal border rank $r$ tensors (also in the
    Veronese and Segre-Veronese cases), a characterisation of tensors with cactus rank $\leq r$, concise versions
    of border apolarity including the fixed point theorem, concise Varieties of Sums of Powers, counting points on
    the second secant variety, connections to defectivity and identifiability in the Segre case, to the
    Salmon conjecture etc.
\end{abstract}

\maketitle

\tableofcontents


\section{Introduction}

For a smooth variety $X\subseteq \mathbb{P}^N$, it is very interesting to study its higher secant varieties $\sigma_r(X) = \Sigma_{r-1}(X)$.
When the embedding $X\subseteq \mathbb{P}^N$ is positive enough with respect to $r$, for example, after a high Veronese reembedding,
a lot is known about $\sigma_r(X)$, see, for example~\cite{Ullery, Ein_Niu_Park, Park, Agostini_Park}. The core reason behind
these beautiful results is the following: every point $\sigma_r(X)$ is tame in
the language of~\cite{bucz_bucz_smoothable_rank_example}, or,
equivalently, that the universal bundle $\mathbb{P}\UU$ on $\Hilb_r^{\sm}(X)$ yields a partial desingularisation $\mathbb{P}\UU\to \sigma_r(X)$, or,
equivalently, that the abstract secant variety $\AsigmaHilb_r$ (defined in the flavour below) requires no closure.
For Segre embeddings, positivity is absent, there are wild points, and there seemed to be a
consensus among experts that the above approach fails hopelessly.

In this paper we actually construct an analogous theory in the Segre setup. Our analogue
of  $\mathbb{P}\UU$ is called the concise secant variety $\csigma_r$. We prove that it compactifies an open part of the
abstract secant variety $\AsigmaHilb_r$, that it has very good singularities
for small $r$, always has the expected dimension etc. We obtain applications to
secant varieties,
in particular new approaches to varieties of sums of powers VSP, an alternative to border apolarity,
an approach to Salmon problem and to defectivity.
% The existence of $\csigma_r$ manifests itself also on a more elementary level in the following ways.
Considering the limits of individual points, we recover a result of Buczy{\'n}ski (see below Theorem~\ref{thm:min_brk_unres} for the history).
The embedding of $\AsigmaHilb_r$ into $\csigma_r$ yields a generalisation of apolarity lemma, called
\emph{cactus apolarity lemma} below.

Let $d\geq 3$ and $\tspace := V_1\otimes \ldots \otimes V_d$.
Throughout we concentrate on the Segre embedding
\[
    \Seg = \mathbb{P}V_1 \times \ldots \times \mathbb{P}V_d\into \mathbb{P}\tspace,
\]
leaving its subvarieties to future work.
We drop $\Seg$ from the notation and write $\sigma_r$ instead of $\sigma_r(\Seg)$ etc.
We begin the discussion from the elementary concept of unrestrictions.


%The concise secant variety introduced here can be useful in many different
%aspects. We informally list these, in the hope of giving an
%overview.

\subsection{Unrestrictions}
For a tensor $[T]\in \mathbb{P}\tspace$, a central problem is to determine its
border rank $\brk(T)$ that is, the smallest integer $r$ such that $[T] =
\lim_{t\to 0} [T_t]$ for some tensors $T_t$ of rank $\leq r$. When all
coordinate spaces $V_{\bullet}$ have dimension $r$, Buczy{\'n}ski
observed~\cite{Bucz_Communication}
that $\brk(T)\leq r$ exactly when $T$ is a restriction of a minimal border
rank tensor (see~\S\ref{ssec:smoothableRank}, \S\ref{ssec:conciseSecants} for definitions). This is important,
since restriction is a linear-algebraic operation, while passing to the limit is much more involved.

Based on Buczy{\'n}ski's observation, we show that the operation of passing to the limit $[T] =
\lim_{t\to 0} [T_t]$ can be split into two steps:
\begin{enumerate}
    \item\label{it:mbrk} the \emph{minimal border rank limit} $\Tppar{} =
        \lim_{t\to 0} T_t$,
    \item\label{it:restr} a restriction from $\Tppar{}$ to $T$.
\end{enumerate}
We prove this in much greater generality in Theorem~\ref{thm:min_brk_unres} below. The result is explicit and constructive. Schematically,
the splitting can be presented as
\begin{equation}\label{eq:factorisation}
    \begin{tikzcd}
        & \Tppar{}\ar[d, mapsto, "\mathrm{restr.}"]\\
        T_t \ar[ur, mapsto, "\mathrm{limit}"] \ar[r, mapsto, "\mathrm{limit}"] & T
    \end{tikzcd}
\end{equation}
This is useful: in the first step, we obtain tensors of minimal border
rank, which are much better understood
thanks to theory of centroids~\cite{JLP}. In the second step, the
restriction is a purely linear-algebraic operation and its choice is free: any
restriction of a minimal border rank tensor yields a tensor of border rank
$\leq r$.

%The steps will be discussed precisely below. In broad terms, this is similar
%to how a morphism from a variety $X$ to $\mathbb{P}^n$ is factored into two
%parts: a line bundle $L$ on $X$ and a space of $n+1$ sections of $L$. The line
%bundle corresponds to part~\ref{it:mbrk} while the choice of section to
%part~\ref{it:restr}.

\subsection{Main features of concise secant varieties}
Tensors of rank $\leq r$ form a secant variety $\sigma_r$ and any limit as above
yields a curve $[T_t]\in \sigma_r$. We construct a new variety, called the
concise secant variety $\csigma_r$.
The limit $\Tppar{} = \lim_{t\to 0} T_t$ yields a curve in $\csigma_r$.
The variety $\csigma_r$ comes with a map
$\rho\colon \csigma_r\to \sigma_r$ which is the ``universal
restriction'' map. It maps the curve upstairs to the one downstairs,
yielding the restriction $\Tppar{}$ to $T$, so that we obtain
\[
    \begin{tikzcd}
        & \csigma_r\ar[d, "\rho"]\\
        \sigma_r^{\op} \ar[r, hook, "\mathrm{op}"]\ar[ru, hook, "\mathrm{op}"] & \sigma_r
    \end{tikzcd}
\]
which upgrades~\eqref{eq:factorisation}, see
\S\ref{sec:unrestrictions_geometric} for details. While above we assumed $\dim
V_i \geq r$, the construction of $\csigma_r$ is general
and requires no such assumption.

In comparison with $\sigma_r$, the variety $\csigma_r$ has a number of astonishingly good properties:
\begin{enumerate}
    \item It is projective, so one can take limits of tensors, yet \emph{every}
        point of $\csigma_r$ corresponds to a \emph{concise} tensor, so the
        limiting tensor never ceases to be concise, see~\eqref{eq:framedPoints:intro}.
        Imprecisely speaking, $\csigma_r$ \emph{requires no closure}, in contrast with $\sigma_r$.
    \item The singularities of $\csigma_r$ are much better behaved than the
        ones of $\sigma_r$ for all $r$, see \S\ref{ssec:singularities}. For example, $\csigma_r$ is smooth for $r\leq 3$.
    \item The variety $\csigma_r$ compactifies an open locus of $\left\{(T, Z)\ |\
            T\in \spann{Z} \right\}$, where $Z\into \mathbb{P}V_1 \times \ldots
            \times \mathbb{P}V_d$ is a zero-dimensional scheme of degree $r$.
            Thus it serves as an analogue of the abstract secant variety,
            which is a central object for birational geometry of $\sigma_r$, see~\S\ref{ssec:abstractSecantsIntro}. Again,
            it is crucial that $\csigma_r$ involves no closure.
    \item The variety $\csigma_r$ always has the expected dimension $m\cdot
        (\sum_{i=1}^d \dim V_{i} - (d-1)) - 1$, see
        Corollary~\ref{ref:dimensionOfcsigma:cor} for details. Its equations
        are also independent of the dimensions of coordinate spaces
        $V_{\bullet}$, see~\S\ref{ssec:smoothEquivalences}, and they are known for $r\leq 5$,
        see Corollary~\ref{ref:equationsSmallr:cor}.
\end{enumerate}
There is also a concise cactus variety and other variants.

\subsection{Construction of the concise secant variety}
\newcommand{\Taf}{T^{\mathrm{af}}}
\newcommand{\Tproj}{T^{\mathrm{proj}}}

Intuitively, the map $\rho\colon \csigma_r \to \sigma_r$ is a generalisation of the map
$\UU\to V$, where $\UU\to \Gr(r, V)$ is the universal subbundle. Thus, for the
construction we will need analogues of the Grassmannian and vector bundles: instead of
elements of a fixed vector space $\tspace$, our families of tensors will lie on a vector bundle
$\VV_1\otimes \ldots \otimes \VV_d$ on a variety $X$. For example, $\mathbb{P}\tspace$
comes with a family of tensors $\Tproj\colon \OO_{\PP \tspace}(-1) \to \OO_{\mathbb{P}\tspace}\otimes \tspace$
and $\tspace$ comes with a ``trivial'' family $\Taf\colon \OO_{\tspace}\to \OO_{\tspace}\otimes \tspace$.

The construction of $\csigma_r$ is just a special case of a more general and versatile construction of the unrestriction
schemes $\unres{}$, which we introduce in Definition~\ref{ref:unrestriction:def}. The
unrestriction scheme depends on a parameter $m$, which we set to $m := r$ here.

Fix a  variety $X$ with a family of tensors $T$, for example $\mathbb{P}\tspace$ with $\Tproj$ above.
The \emph{unrestriction scheme}
$\unrespar{1}{T}\xrightarrow{\pi_1} X$ comes with a family of tensors $\Tppar{1}\in \UU_1 \otimes V_2\otimes \ldots \otimes V_d$,
where $\UU_1$ is a vector bundle of rank $r$ and $\Tppar{1}$ is $\UU_1$-concise. This means that every element of $\Tppar{1}$
is a tensor living in a vector space isomorphic to $\kk^r \otimes V_2\otimes
\ldots \otimes V_d$ and concise with respect to first coordinate. The unrestriction scheme is appropriately universal with
respect to this property, see Definition~\ref{ref:unrestriction:def} for details.

The crucial next step is that we can iterate this construction.
Namely, we take $\unrespar{1, 2}{\Tppar{1}}\to \unrespar{1}{T}$, which comes with a family of tensors $\Tppar{1,2}$, 
concise on the first \emph{two} coordinates.
In this way, we finally arrive at
\[
    \unresfull := \unrespar{1, \ldots ,d}{\Tppar{1,\dots,d-1}} \xrightarrow{\pi} X.
\]
This is a smooth projective variety
(Corollary~\ref{ref:unrestrictionSmoothness:cor}) with a family of tensors
$\Tppar{}$. The map $\pi$ is birational when $\dim V_{\bullet}\geq r$.
For $T = \Tproj$, the ambient variety $\unresfullpar{\Tproj}$ contains the loci of interest:
\begin{enumerate}
    \item The concise secant variety $\csigma_r\subseteq \unresfullpar{\Tproj}$ is the closed locus where $\Tppar{}$ has minimal border rank.
        This variety comes with a map $\csigma_r\to \sigma_r$, which is birational in good situations, see~\S\ref{ssec:identifiability}.
    \item The concise cactus variety $\ckappa_r\subseteq \unresfullpar{\Tproj}$ is
        likewise obtained as the locus where $\Tppar{}$ has minimal border
        cactus rank and it yields a map $\ckappa_r\to \kappa_r$.
\end{enumerate}
Analogously, taking $T = \Taf$, the ambient variety $\unresfullpar{\Taf}$, which is also smooth,
contains the loci that resolve cones:
\begin{enumerate}
    \item The minimal border rank locus $\csigmahat_r\subseteq \unresfullpar{\Taf}$ has a map to the cone $\sigmahat_r \into \tspace$ over the secant variety $\sigma_r$. We call it the \emph{arithmetic concise secant variety}. The map $\csigmahat_r\to \sigmahat_r$ is birational in good situations, see~\S\ref{ssec:identifiability}.
    \item Analogously, the cactus locus $\ckappahat_r\subseteq \unresfullpar{\Taf}$ has a map $\ckappahat_r\to \widehat{\kappa}_r$.
\end{enumerate}
We review the construction in Section~\S\ref{sec:unrestrictionSchemes}.

\subsubsection{Framed concise secant variety and singularities}

To describe points of $\csigma_r$, it is easier to first describe a related variety, the
framed concise secant $\csigmafr_r$, which is constructed in~\S\ref{ssec:framedUnrestrictions}.
The map $\csigmafr_r\to \csigma_r$ is a principal $\GL_r^{\times d}$-bundle, hence the local properties of
$\csigmafr_r$ and $\csigma_r$ agree, but $\csigmafr_r$ is not projective (while $\csigma_r$ is).

Fix \emph{$r$-dimensional} vector spaces $W_1$, \ldots , $W_d$. The $\kk$-points of the framed concise secant are
\begin{align}\label{eq:framedPoints:intro}
    \csigmafr_r(\kk) =
    \left\{ 
        \begin{array}{c | c}
            \Tpparfr{}\in W_1\otimes_{\kk} \ldots \otimes_{\kk} W_d &\Tpparfr{}\mathrm{\ concise,} \brk(\Tpparfr{}) = r\\
            {[\varphi_1]}\in \mathbb{P}\Hom(W_1, V_1)
                &\varphi_1, \ldots , \varphi_d \mbox{ linear maps }\\
              (\varphi_i\in \Hom(W_i, V_i))_{2\leq i\leq d}  & \mbox{satisfying conciseness conditions } \eqref{eq:starCondition}
        \end{array}
    \right\}.
\end{align}
    % \csigmafr_r(\kk) = \Big\{ \Tpparfr{}\in W_1\otimes_{\kk} \ldots \otimes_{\kk} W_d,\ (\varphi_i\in W_i\to V_i)_{1\leq i\leq d} \ &|\ \Tpparfr{}\mathrm{\ concise,} \brk(T) = r  \\ & \varphi_i \mbox{ linear and satisfy } \eqref{eq:starCondition}\Big\}.
Crucially, the conciseness conditions~\eqref{eq:starCondition} are open, hence there are no equations coming from them (see Proposition~\ref{ref:framedUnrestrictionPoints:prop} for details). The group $\GL(W_1)\times \ldots \times \GL(W_d)$ acts on $\csigmafr_r$
in a natural way. Thanks to~\eqref{eq:starCondition}, this is a free action. The quotient is $\csigma_r$. On the level of points, we obtain
\begin{equation}\label{eq:concisePoints:intro}
    \csigma_r(\kk) = \csigmafr_r(\kk) / \GL(W_1)\times \ldots \times \GL(W_d).
\end{equation}
The map $\rho\colon \csigma_r(\kk)\to \sigma_r(\kk)$ sends $(\Tppar{},
\varphi_1, \ldots ,\varphi_d)$ to the restriction $[T] =
[\varphi_{1,\dots,d}(\Tppar{})] \in \PP\tspace$.

\newcommand{\rhofr}{\rho^{\mathrm{fr}}}%
The variety $\csigmafr_r$ has another map to a secant variety. This is the map
$\alpha\colon \csigmafr_r\to W_1\otimes \ldots \otimes W_d$ that sends $(\Tpparfr{}, \varphi_1, \dots, \varphi_d)$ to $\Tpparfr{}$.
The map $\alpha$ is smooth, with image equal to the concise locus of $\sigma_r\subseteq W_1\otimes \ldots \otimes W_d$.






\subsection{Applications of concise secant varieties}

\subsubsection{Resolutions of singularities}\label{ssec:singularities}

We pass to analysing the singularities of secant varieties. The two main goals here are
to understand the singular locus and resolve singularities.
When the variety is embedded positively enough, there are many positive results~\cite{Ullery, Ein_Niu_Park, Park, Agostini_Park}.

In our setup, without positivity, the situation is more complicated. We are not aware of results about resolution of singularities.
For describing the singular locus, partial results appear in~\cite{Han__singularities, Furukawa_Han}.
A full answer is known only for $r=2$ and $r=d=3$. The paper~\cite{michalek_oeding_zwiernik} describes $\sigma_2$ for every $d$.
For $d=3$, Buczy{\'n}ski and Landsberg~\cite{Buczynski_Landbserg_sigma3} give normal forms
of tensors in $\sigma_3$ and equations are known here, from which one can
describe the singular locus.

In contrast, our method works  \emph{for every} $d\geq 3$ and yields \emph{resolution} of singularities in the Segre case
for $r=2,3,4$, and, conjecturally, for other values of $r$. Importantly, we do not perform any
case-by-case analysis, but rather recast the problem as a question of singularities of Hilbert and Quot schemes,
so that the results follow from known ones. The order $d\geq 3$ of tensors is not important throughout the argument.
\begin{theorem}[Theorem~\ref{ref:singularities:thm}]\label{ref:resolutions:introthm}
    \begin{enumerate}
        \item The variety $\csigma_r$ is nonsingular for $r\leq 3$.
        \item The variety $\csigma_4$ is singular, with
            singular locus of codimension $9$. It is Cohen-Macaulay with
            rational (in fact, canonical) singularities.
            The singular locus is smoothly equivalent to the vertex of the affine cone over
            $\Gr(2, 6)\into \mathbb{P}^{14}$. Its singularities are resolved by a single blow up of
            the singular locus.
        \item Assume that $\rho$ is birational (this happens when $\dim V_{\bullet} = r$ and, in fact, in much
            greater generality, see~\S\ref{ssec:identifiability}). For $r=2,3$ the map $\rho\colon \csigma_r\to \sigma_r$
            is a resolution of singularities of $\sigma_r$. For $r=4$ the map $\Bl_{\Sing(\csigma_4)} \csigma_4 \to \csigma_4\to \sigma_4$
            is a resolution of singularities.
    \end{enumerate}
\end{theorem}
We have a similar description also for $\csigma_5$, which we will discuss elsewhere,
see Remark~\ref{ref:singularitiesFive:rmk}.

Also for general $r$, the geometry of $\csigma_r$ is better than the geometry of
$\sigma_r$. The secant variety suffers  because $\sigma_{r-1}$ forms a ``black hole'' inside:
at any point  $[T]\in \sigma_{r-1}\subseteq \sigma_r$, the tangent space $T_{[T]}\sigma_r$ 
is the whole tangent space to $\mathbb{P}\tspace$ and there is little hope for a meaningful geometry.
In contrast, for any $r$, the geometry of $\csigma_r$ at \emph{any} point is smoothly equivalent to the geometry
of $\sigma_r\subseteq \mathbb{P}\tconcspace$ at a concise point, where $\tconcspace = W_1\otimes \ldots \otimes W_d$
and $\dim W_{\bullet} = r$, see~\S\ref{ssec:smoothEquivalences}.


\subsubsection{Algebraic characterisation of the smoothable rank}\label{ssec:smoothableRank}

    The following observation is well-known and sometimes called the
    Apolarity Lemma. Recall that a tensor $T \in \tspace$ is a
    \emph{restriction} of a tensor $T'\in
    \tconcspace$ if there are linear maps $\varphi_i\colon W_i\to V_i$ such
    that the induced map $\tconcspace\to \tspace$ maps $T'$ to
    $T$.
    \begin{lemma}[Apolarity Lemma]\label{ref:apolarityLemma:lem}
        Let $T\in \tspace$ be a tensor. The following are equivalent:
        \begin{enumerate}
            \item\label{it:rankOne} the rank of $T$ is at most $r$,
            \item\label{it:rankSpan} there are $r$ points $x_1, \ldots , x_r\in \Seg$ such that
                $T$ lies in $\spann{x_1, \ldots ,x_r}$,
            \item\label{it:rankAlg} the tensor $T$ is a restriction of the unit tensor
                $\spann{r}$.
        \end{enumerate}
    \end{lemma}
    One can generalise~\ref{it:rankSpan}, replacing the tuple $\left\{ x_1,
    \ldots ,x_r \right\}$ by any smoothable finite scheme $Z\into \Seg$ of degree $r$.
    This gives rise to the notion of \emph{smoothable rank} $\smrk(T)$ of $T$.
    It is known that $\smrk(T) \geq \brk(T)$. Equality occurs for example for
    Generalised Additive Decompositions~\cite{Bernardi_Oneto_Taufer__On_GADs} but not in
    general~\cite{bucz_bucz_smoothable_rank_example}. One can go further and drop the smoothability
    requirement for $Z$ above, which leads to the notion of \emph{cactus rank}.
    We generalise Lemma~\ref{ref:apolarityLemma:lem} to this setup.

    \begin{theorem}[Cactus Apolarity Lemma, {Corollary~\ref{ref:spanCharPopular:cor}}]\label{ref:restriction:introthm}
        Let $T\in \tspace$ be a tensor. The following are equivalent:
        \begin{enumerate}
            \item\label{it:cactusrankOne} the cactus rank of $T$ is at most $r$,
            \item\label{it:cactusrankSpan} there is a finite  scheme $Z =
                \Spec(\cA)\to \Seg$
                with $\deg Z = r$ such that
                $T$ lies in $\spann{Z}$,
            \item\label{it:cactusrankAlg} the tensor $T$ is a regular restriction of the
                multiplication tensor in a Gorenstein algebra $\cA'$
                with $\dim_{\kk} \cA' \leq r$.
        \end{enumerate}
        Having $\cA$ as in~\ref{it:cactusrankSpan}, we can choose $\cA'$ to be a
        quotient algebra of $\cA$. In particular, if $\dim_{\kk} V_{\bullet} = r$ and $T$ is concise, then $T$ is
        isomorphic to the multiplication tensor in $\cA$ itself and $\cA$ is Gorenstein.
    \end{theorem}

    A restriction given by $\varphi_i\colon \cA^{\vee}\to V_i$, $i=1, \ldots , d$ is called \emph{regular},
    if the image of each map $\varphi_i^{\vee}\colon V_i^{\vee}\to \cA$ contains an invertible element of $\cA$, see Definition~\ref{ref:regularAndJointlySpanning:def}.
    \begin{example}
        Let $\cA = \Spec \kk[\varepsilon]/(\varepsilon^3)$. Its multiplication tensor is isomorphic to the symmetric tensor
        $x^2z + xy^2$. A restriction of such a tensor is regular if (on every coordinate) it sends $x$ to a nonzero element.
        The algebra $\cA$ also admits Gorenstein quotients $\cA/(\varepsilon^2)$ and $\cA/(\varepsilon)$ with multiplication
        tensors $x^2y$, $x^3$, respectively. More on such tensors in given in~\cite{landsberg_teitler, CFJ, FOS}.
    \end{example}

    Theorem~\ref{ref:restriction:introthm} follows from the more refined
    Theorem~\ref{ref:spanChar:thm}. Partially symmetric versions of this theorem also follow, but
    will be presented elsewhere. An analogous version for smoothable rank exists, see Remark~\ref{ref:smoothableApolarityLemma:rem}.


    \subsubsection{Abstract secant varieties}\label{ssec:abstractSecantsIntro}
% \newcommand{\Tame}{\mathrm{Tame}}%

The \emph{abstract secant variety}
\[
    \Asigma_r\subseteq \Sym^{r} \Seg \times \mathbb{P}\tspace
\]
can be defined as the closure of the locus
$\Asigma_r^{\op}$ of all pairs
$(\left\{ x_1, \ldots ,x_{r} \right\}, [T])$, where $x_1, \ldots ,x_r\in \Seg$
are linearly independent and $[T]$ lies in the span $\spann{x_1, \ldots
,x_r}\subseteq \mathbb{P}\tspace$.
The projection onto the second coordinate yields a map $\Asigma_r\to \sigma_r$.

The abstract secant variety is absolutely central in the study of identifiability of
tensors and defectivity of secant varieties, see~\cite{Chiantini_Ciliberto__Weakly_defective, Abo_Ottaviani_Peterson_segre, Abo_Brambilla, Casarotti_Mella} and much more references in~\S\ref{ssec:identifiability}. In these
applications, one takes a general point $(Z, [T])$ of $\Asigma_r^{\op}$ and proves that
the forgetful map behaves ``well-enough'' near $(Z, [T])$. For this, it is
very useful to \emph{degenerate} $(Z, [T])$ to have better control over its
geometry, for example for induction. A typical example is to put points of
$Z$ on a hyperplane. Sometimes, points are allowed to collide~\cite{Galuppi_Oneto}.
However, overall, the boundary of $\Asigma_r$ has no clear description, no formula
for a tangent space at a given point and needs to be avoided.

It would be useful to have even more flexibility in degeneration. This is not
possible for the usual abstract secant variety $\Asigma_r$, since we have no
control over the closure. So one could wonder about other varieties
$\mathcal{M}$ which fill into the diagram
\[
    \begin{tikzcd}
        \Asigma_r^{\op} \ar[r, hook, "\mathrm{op}"]\ar[rd] & \mathcal{M}\ar[d]\\
        & \sigma_r
    \end{tikzcd}
\]
We show that the concise secant variety $\csigma_r$ is one such variety. In fact, one can even enlarge
the locus $\Asigma_r^{\op}$ naturally. Consider
\[
    \AsigmaHilb_r = \left\{
        \begin{array}{c l}
            (Z, T)\ | &Z\into \Seg,\ Z \mbox{ zero-dimensional smoothable Gorenstein, }\deg Z =
        r\\
                   &\pr_{2, \ldots ,d}\spann{Z} \simeq \mathbb{P}^{r-1},\ T\in \spann{Z}\mbox{ not in the span of any subscheme of }Z
        \end{array}
    \right\},
\]
where $\pr_{2, \ldots ,d}\spann{Z}$ denotes the span of $Z$ inside $\mathbb{P}V_{2, \ldots ,d}$.
\begin{theorem}[Theorem~\ref{ref:abstractInsideConcise:thm}]\label{refintro:abstractInsideConcise:thm}
    The variety $\AsigmaHilb_r$ embeds as an open subvariety of $\csigma_r$. The map $\rho\colon \csigma_r\to \sigma_r$
    extends the natural projection map $\AsigmaHilb_r\to \sigma_r$.
\end{theorem}
The advantage of $\csigma_r$ over $\Asigma_r$ is that every point of $\csigma_r$ corresponds to a tensor
and the tangent space at such a point can be described under very mild conditions, using a generalisation
of smooth equivalences from~\S\ref{ssec:smoothEquivalences}; this will be explained
in a future work.

\subsubsection{Varieties of sums of powers}\label{ssec:VSP}

Theorem~\ref{refintro:abstractInsideConcise:thm} has immediate consequences for the varieties of sums of powers.
Recall that these varieties were introduced by Ranestad and Schreyer~\cite{ranestad_schreyer_VSP} as closures of
\begin{equation}\label{eq:VSP}
    \VSP(T, r) = \overline{\left\{ [Z]\into \Seg\ |\ Z\mbox{ zero-dimensional smoothable Gorenstein, }\deg Z = r,\ T\in \spann{Z}\right\}}.
\end{equation}
These varieties exhibit very interesting global geometry, especially in the defective
cases, see for example~\cite{Ranestad_Iliev__VSPcubic, Ranestad_Voisin__VSP,
Ranestad_Schreyer__polar_simplices,
Jelisiejew_Ranestad_Schreyer__polar_simplices}, yielding hyperk{\"a}hler varieties etc.
However, as in the case of secant varieties, the need for closure is a source of major technical problems,
as it is very hard to prove that the closure is smooth, for example, or to describe it, see the discussion in~\cite{Jelisiejew_Ranestad_Schreyer__polar_simplices}.
The need of closure is also the same as existence of wild tensors, as in~\cite{bucz_bucz_smoothable_rank_example}.

One solution for this problem was recently introduced using border apolarity~\cite{Buczyska_Buczynski__border}. There, one considers $\VSPbord(T, r)$
which, roughly speaking, consists of all ``good'' multigraded ideals $I$ with fixed
Hilbert function and such that $T$ is apolar $I$.
The word ``good'' above technically means that $[I]$ lies in the \emph{Slip
component} of a multigraded Hilbert scheme of
Haiman-Sturmfels~\cite{Haiman_Sturmfels__multigraded}.
Border apolarity has led to dramatic improvements in border rank estimates, see~\cite{Conner_Harper_Landsberg, Conner_Huang_Landsberg, Mandziuk_Ventura}.

Working with $\VSPbord(T, r)$ poses two challenges:
\begin{enumerate}
    \item For a given ideal $I$, it is notoriously hard to determine if it lies in the Slip component.
        This is because the multigraded Hilbert scheme, apart from containing the Slip component, contains
        quite a number of ``slop'' ideals, easy to generate but containing
        little geometric information. Therefore, it is notoriously hard to
        describe this Hilbert scheme, see~\cite{Jelisiejew_Mandziuk}.
        In broad terms, the same happens for the usual Hilbert scheme, but the pathologies of the multigraded one show up for smaller $r$ and
        seem much worse.
    \item Even when computing the variety $\VSPbord(T, r)$ is fully possible, it contains rational parts, coming
        from ``artefacts'' of the high-degree parts of ideals $I$, see for
        example~\cite[Theorem~6.6, Remark~7.10]{Huang_Michalek_Ventura}. As a result, the
        global geometry of $\VSPbord(T, r)$ is not the expected one: the $\VSPbord(T, r)$
        viewed as a compactification, adds too much.
\end{enumerate}

The concise secant variety allows for an alternative compactification of the set $(T, Z)$, $T\in \spann{Z}$.
Theorem~\ref{refintro:abstractInsideConcise:thm} suggests the following definition.
\begin{definition}\label{ref:conciseVSP:def}
    The \emph{concise variety of sums of powers} $\cVSP(T,r)$ is fibre $\rho^{-1}(T)$, where $\rho\colon \csigma_r\to \sigma_r$
    is the natural map.
\end{definition}
Theorem~\ref{refintro:abstractInsideConcise:thm} implies that $\cVSP(T, r)$ contains all interesting $Z$ such that
$T\in \spann{Z}$, up to mild conditions on the span. The variety $\cVSP(T, r)$ is also much smaller than $\VSPbord(T, r)$
in general.
\begin{example}
    If $T$ is a concise tensor of minimal border rank $r$, then $\cVSP(T, r)$ is a point, regardless of whether
    $T$ is tame or wild. In particular, in both examples~\cite[Theorem~6.6, Remark~7.10]{Huang_Michalek_Ventura},
    the variety $\VSPbord(T, r)$ has high dimension ($r+2$, $\geq 8$, respectively) while $\cVSP(T, r)$ is a point.
\end{example}

\subsubsection{Concise version of border apolarity}\label{ssec:borderApolarity}

    As discussed above, border apolarity has been a successful tool for obtaining lower bounds on the border rank.
    In this section we explain that the same can be achieved with $\csigma_r$. To compare the two,
    we can say that:
    \begin{enumerate}
        \item\label{it:tmpBorder} Border apolarity produces~\cite[Theorems~1.2,
            4.3]{Buczyska_Buczynski__border} a Borel-fixed ideal $I$ inside the
            apolar ideal of the tensor $T$. The main
            question is whether $I$ is the Slip component. The obstacles for proving that are discussed in~\S\ref{ssec:VSP} above.
        \item\label{it:tmpConcise} The procedure below produces a \emph{Borel-fixed} unrestriction $\Tppar{}\geq T$. The unrestriction
            is a concise tensor in $\tconcspace$, where $\dim W_{\bullet} = r$, so that $\brk \Tppar{}\geq r$. The main question is whether $\Tppar{}$ has
            border rank $r$.
    \end{enumerate}
    In our view, there are two advantages of~\ref{it:tmpConcise} over~\ref{it:tmpBorder}. First, the procedure below requires no apolarity, no multigraded Hilbert schemes etc.
    Second, more importantly, the output $\Tppar{}$ is a tensor and can be tested using all existing tools of the theory:
    Koszul and Young flattenings~\cite{Oeding_Ottaviani}, centroids~\cite{JLP}, etc.
    
    Let us finally describe the procedure more carefully. Let $[T]\in \mathbb{P}\tspace$ and let $\rho\colon \csigma_r\to \sigma_r$. First, almost directly from the definitions, we have the following:
    \begin{enumerate}
        \item $\brk T\leq r$ if and only if $\rho^{-1}([T])$ is nonempty,
        \item the cactus rank of $T$ is $\leq r$ if and only if $\rho^{-1}([T])$ contains a $1$-generic tensor (see~\S\ref{ssec:genericityConditions}),
        \item the smoothable rank of $T$ is $\leq r$ if and only if $\rho^{-1}([T])$ contains a $1$-generic tensor with smoothable centroid,
        \item the rank of $T$ is $\leq r$ if and only if $\rho^{-1}([T])$ contains a $1$-generic tensor with reduced centroid.
    \end{enumerate}
    The power of border apolarity comes from the \emph{fixed ideal theorem (fit)}~\cite[Theorem~4.3]{Buczyska_Buczynski__border},
    which allows one to reduce greatly the number of cases, to look for Borel-fixed ideals.
    The following is the analogue of this theorem.
    \begin{theorem}[Fixed unrestriction theorem]\label{ref:cfit:thm}
        Let $[T]\in \mathbb{P}\tspace$ be a tensor, let $G\subseteq \SLV$ be the stabilizer of $[T]$ and let $B\subseteq G$ be a Borel subgroup.
        Then $\brk T\leq r$ if and only if there exists a $B$-fixed tensor $\Tppar{}$ restricting to $T$.
    \end{theorem}
    To understand Borel-fixed tensors, we need to carefully see how the action of $B$ lifts to an action on $\tconcspace$.
    This is discussed formally in~\S\ref{ssec:groupActions} and concretely on a small, but illuminating example of $\csigma_2$,
    in Proposition~\ref{ref:sigmaFixedPoints:prop}.

    As a proof of concept, we give the following example.
    \begin{example}
        Let $T$ be the $3\times3$-matrix multiplication tensor. Using border apolarity and extensive computations~\cite{Conner_Harper_Landsberg}
        are able to show that $\brk T\geq 17$. We can prove that their computation can be reinterpreted in our framework, so that Theorem~\ref{ref:cfit:thm}
        also yields $\brk T \geq 17$.
    \end{example}
    Finally, let us remark that the above ``concise version of border apolarity'' does not really use any apolarity. This is
    not necessarily good or bad, but we want to stress it to avoid confusion.
    % In a sense, the concise theory seems to be related to apolarity as full linear systems are related to special ones.
    

\subsection{Open problems}

Miraculously, concise secant varieties seem to apply to a range of tensor problems of various flavours.
We sketch three possible applications. None of them is currently worked out, so below we mostly illustrate
a possible approach.

\subsubsection{Lower bounds for border ranks, including matrix multiplication}

    This problem is a straightforward continuation of the discussion in~\S\ref{ssec:borderApolarity}. It is also quite mature:
    it is clear what to do, it only leaves the question on how effective it will be.

    Namely, consider the matrix multiplication tensor $M_n\in V_1 \otimes V_2 \otimes V_3$, where $\dim V_{\bullet} = n^2$.
    It is stabilised by the Borel subgroup $B$ of upper-triangular $n\times n$ matrices.

    To prove, for example, that $\brk M_3 > 17$, one can enumerate possible $B$-fixed concise tensors $\Tppar{}$
    in $\rho^{-1}(M_{3})$ with $\dim \Cen{\Tppar{}}\geq 17$, to prove that none of them has minimal border rank tensor.
    The code provided by Austin Conner for the paper~\cite{Conner_Harper_Landsberg} can be adapted to this purpose.
    Then, one has to rule out the possible candidates, showing that none of them has minimal border rank.
    This part is currently unexplored, but it is tempting to employ the suite of already existing tools: so-called
    $(2,1,0)$-tests of~\cite{Conner_Harper_Landsberg}, the more classical Koszul flattenings~\cite{Oeding_Ottaviani} and nonlinear theory of~\cite{Dolevalek_Michalek}.


\subsubsection{Non-defectivity of Segre}

    It is conjectured since~\cite{Abo_Ottaviani_Peterson_segre} that the Segre varieties are nondefective except for
    unbalanced cases and a small number of exceptions, see more discussion in~\S\ref{ssec:identifiability}. The conjecture was verified
    for an enormous number of cases, but it seems open in general.

    Theorem~\ref{ref:abstractInsideConcise:thm} allows us to rephrase nondefectivity as generic finiteness of $\rho\colon \csigma_r\to \sigma_r$.
    This allows for more aggressive degenerations: it would be enough to prove that $\rho^{-1}([T])$ is finite for a single tensor $T$, which
    may be quite degenerate. Such degenerations techniques are a powerful tool, perhaps their most impressive use case is the proof of generic
    Green's conjecture~\cite{Green__Voisin, Green__Weyman}.
    The question here would be: can we find explicit tensors $T$ with zero-dimensional $\rho^{-1}([T])$? How degenerate can they be?

\subsubsection{The Salmon problem}

Take $d = 3$, $\dim V_{\bullet} = 4$. The famous Salmon problem~\cite{Allman_Rhodes} asks for the ideal of equations of $\sigma_4\subseteq \mathbb{P}\tspace$.
The set-theoretic solution is given by Friedland~\cite{Friedland, Friedland_Gross}, but the scheme- or ideal-theoretic description seem unknown, see~\cite{Landsberg_Manivel, Bates_Oeding}.
Current attempts at the problem are based mostly on direct calculation.

The above gives a new strategy, as follows. Let $\widetilde{\csigma_4} := \Bl_{\Sing(\csigma_4)} \csigma_4$ be the resolution
of singularities of $\sigma_4$, as described in~\S\ref{ssec:singularities} above. Let $\widetilde{\sigma_4}$ be the normalisation of $\sigma_4$.
From Oeding's Conjecture~\ref{ref:Oeding:conj} we expect that $\widetilde{\sigma_4} = \sigma_4$.

Since $\csigma_4$ is normal, the map $\rho\colon \csigma_4\to \sigma_4$ lifts to a map $\csigma_4\to \widetilde{\sigma_4}$ and yields a map
\[
    \widetilde{\rho}\colon \widetilde{\csigma_4}\to \widetilde{\sigma_4}.
\]
By Zariski Main Theorem, the pushforward $(\widetilde{\rho})_* \OO_{\widetilde{\csigma_4}}$ is the structure sheaf of $\widetilde{\sigma_4}$.
We expect that $\widetilde{\csigma_4}$ admits a torus action with isolated fixed points. In this situation, the multigraded Hilbert series
of $\sigma_4$ could be computed by torus localisation~\cite{Fulton_Anderson}. Namely, to compute
$H^0(\OO_{\sigma_4}(\mathbf{v}))$ for some $\mathbf{v}\in \mathbb{Z}_{\geq
0}^{3}$, we instead compute the weights on the torus-linearised bundle
$\widetilde{\rho}^*\OO_{\sigma_4}(\mathbf{v}) = \OO_{\csigma_4}(\mathbf{v})$.
Assuming Oeding's conjecture~\ref{ref:Oeding:conj}, this yields the dimensions of homogeneous pieces of coordinate ring of $\sigma_4$, hence predicts the number
of equations in respective degrees.

% \subsection{Comments in the introduction}
% \begin{enumerate}
%     % \item $\tspace $ replace by something defined.
%     % \item $\Seg$ replace by something better adapted.
%     % % \item $\Tame$ replace by something better adapted.
%     % \item Add a lemma about vector subbundles.
% \end{enumerate}
Throughout, we work over an arbitrary field $\kk$.

% \subsection{FUTURE: TO DO}
%
% \begin{enumerate}
    % \item \emph{Unrestrictions}
        % \begin{enumerate}
        %     \item Make \S\ref{sec:unrestrictions} accessible to readers with minimal background,
        %     \item Explicit examples in~\S\ref{sec:unrestrictions}. Bini's tensor, Sch{\"o}nhage(?),
        %         a symmetric example (perhaps binary form).
        %     \item Understand unrestrictions of $cw_2 = x\cdot y \cdot z$ and relation to JM's VSP
        %         with three points.
        % \end{enumerate}
    % \item \emph{Construction of $\csigma_m$}
    %     \begin{enumerate}
    %         % \item Discuss group actions of $\csigma_m$.
    %         % \item Understand if torus fixed points are isolated.
    %         % \item Understand if $\unres$ and $\csigma_m$ are GIT quotients, also~\cite{GITderivedCat}.
    %         % \item Discuss equations of $\csigma_m$.
    %         % \item Singularities of generic loci and smooth equivalences with Hilbert and Quot schemes.
    %         % \item Description of the tangent space at a point.
    %     \end{enumerate}
        
    % \item \emph{Applications}
    %     \begin{enumerate}
    %         % \item Describe the classical geometry $\csigma_2$, $\csigma_3$ as much as easily possible.
    %         %     Describe the singular locus of $\sigma_3$.
    %         % \item Discuss $\csigma_4$ and its desingularisation as well as relation to $\sigma_4$ and Salmon problem.
    %         % \item Discuss lower bounds on border rank, the fixed point theorem.
    %         % \item Check relations with identifiability.
    %     \end{enumerate}
        
% \end{enumerate}


\subsection{Acknowledgements}

    We thank Jarek Buczy{\'n}ski for very helpful comments on an earlier draft and for the permission to discuss results
    related to his contributions to unrestrictions. We thank Giorgio Ottaviani for questions
    regarding the abstract secant variety and Pierpaola Santarsiero for discussions about identifiability. We thank
    Mat{\v{e}}j Dole{\v{z}}{\'a}lek for alerting us about multiple typos and Maciej Ga{\l}{\k{a}}zka for observing an issue
    in an earlier version of Lemma~\ref{l:algorithm_veronese}.

\section{Unrestrictions}\label{sec:unrestrictions}
\newcommand{\pstspace}{S^{\nu_1}V_1 \otimes \ldots \otimes S^{\nu_d}V_d}

For the most part of this section, we work in the general setup of partially symmetric tensors 
$T \in \pstspace$. This setup includes symmetric tensors $F \in S^\nu V$ and tensors $T \in \tspace$.
We assume that our base field $\kk$ has characteristic zero or greater than all $\nu_\bullet$. Throughout this work, the symbol ${\bullet}$ denotes an arbitrary index in the range $1,2, \ldots ,d$.

Recall that a tensor $T \in \pstspace$ is \emph{concise} if it does not lie in any proper subspace 
of the form $S^{\nu_1}V_1' \otimes \ldots \otimes S^{\nu_d}V_d' \subset \pstspace$. The border rank of 
a concise tensor is at least the maximum of dimensions of all $V_\bullet$. In particular,
when all $V_\bullet$ have dimension $m$, each concise tensor has border rank at least $m$. Concise 
tensors of border rank $m$ are called \emph{minimal border rank} tensors. They are better 
understood than general, non-concise border rank $m$ tensors, see the introduction and~\cite{JLP}.

\begin{definition}
    Let $T, \Tppar{}\in \pstspace$ be tensors. 
    The tensor $\Tppar{}$ is an \emph{unrestriction} of $T$ if $T$ is a \emph{restriction} of $\Tppar{}$, that is there exist linear maps 
    $\varphi_i \colon V_i \to V_i$
    such that $(\varphi_1 \otimes \dots \otimes \varphi_d)(\Tppar{}) = T$:
    \[
    \begin{tikzcd}
        \Tppar{} \arrow[r, phantom, "\in"] \arrow[d, phantom, "\rotatebox{90}{$\leq$}"]  & S^{\nu_1}V_1 
        \arrow[r, phantom, "\otimes"] \arrow[d, "\varphi_1"] & \dots 
        \arrow[r, phantom, "\otimes"] & S^{\nu_d} V_d \arrow[d, "\varphi_r"]\\ 
        T \arrow[r, phantom, "\in"] & S^{\nu_1} V_1 \arrow[r, phantom, "\otimes"] & 
        \dots \arrow[r, phantom, "\otimes"] & S^{\nu_d} V_d
    \end{tikzcd}
    \]
\end{definition}
The main result of this section is the following corollary from the more refined Proposition~\ref{p:algorithm_full}.
Roughly speaking, it says that every tensor of a fixed border rank can be obtained from a 
concise tensor of the same border rank via the linear-algebraic operation of restriction.

\begin{theorem}\label{thm:min_brk_unres}
    Assume that $\dim_\kk V_\bullet = m$.
    \begin{enumerate}
        \item Every tensor $T \in \pstspace$ of border rank $m$ is a restriction of a minimal 
        border rank tensor $\Tppar{} \in \pstspace$. 
        \item Moreover, given a degeneration of concise rank $m$ tensors $T_t$ witnessing the border rank 
        of the tensor $T$, one can explicitly construct a minimal border rank unrestriction $\Tppar{} \geq T$.
    \end{enumerate} 
\end{theorem}

In the Segre case, that is, when $\nu_{\bullet} = 1$,
Theorem~\ref{thm:min_brk_unres} was first observed by
Buczy{\'n}ski~\cite{Bucz_Communication}. While presenting this work on the INABAG 2025
conference, we learned that, again in the Segre case, it can be also deduced
from~\cite{Christandl_Gesmundo_Zuiddam__A_gap_in_the_subrank}. This argument now appeared
as~\cite{Chang_Gesmundo_Zuiddam}.

The argument of Theorem~\ref{thm:min_brk_unres} is constructive, so for every witness of a border rank, we obtain a minimal border rank tensor.
This allows to obtain a plethora of interesting minimal border rank tensors, as we illustrate below.

\begin{example}\label{ex:wedge}
    Assume that $\kk$ has characteristic different from $2, 3$.
    Consider the antisymmetric tensor 
    \[
        T = e_1 \wedge e_2 \wedge e_3 \in \Lambda^3 \kk^3 \subset \kk^3 \otimes \kk^3 \otimes \kk^3
        \into \kk^5 \otimes \kk^5 \otimes \kk^5.
    \]
    The tensor $T$ has both rank and border rank $5$~\cite{Ilten_Teitler, Derksen_Makam}.
    The rank yields a tautological unrestriction $T \leq \spann{5}$ from the unit tensor. There is 
    another minimal border rank unrestriction 
    \[
        T = 
        \begin{bmatrix}
            0 & x_3 & -x_2 & 0 & 0 \\
            -x_3 & 0 & x_1 & 0 & 0 \\
            x_2 & -x_1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 0 \\
        \end{bmatrix}
        \leq 
        \begin{bmatrix}
            x_5 & x_3 + x_4 & -x_2 & x_1 & x_2 \\
            -x_3 + x_4 & 0 & x_1 & 0 & 0 \\
            x_2 & -x_1 & 0 & 0 & 0 \\
            x_1 & 0 & 0 & 0 & 0 \\
            x_2 & 0 & 0 & 0 & 0 \\
        \end{bmatrix}
        = \Tppar{}
    \] 
    from the tensor $\Tppar{}$ isomorphic to the tensor $T_{\OO_{54}}$ from the classification
    from~\cite[Theorem 1.7]{JLP}.
\end{example}


Before stating and proving Proposition~\ref{p:algorithm_full}, we discuss the intuitive notion of 
a degeneration of tensors. There are a few closely related ways to formally define it. 
Let us list a few.
\begin{enumerate}
    \item For $\kk = \CC$, a degeneration of tensors $T_t$ to a tensor $T$ can be thought of as a 
        sequence of tensors in $\pstspace$ converging to $T$ in the usual topological sense. 
        In this interpretation, the general tensor $T_{t \neq 0}$ is general tensor from this sequence.
    \item For $\kk = \CC$, a degeneration of tensors $T_t$ to a tensor $T$ can be thought of as a 
        curve germ $\Delta \to \pstspace$, where $\Delta\subseteq \mathbb{C}$ is a small disk around $0$, such that $0\in \Delta$
        is mapped to $T$. In this interpretation, the general tensor $T_{t \neq 0}$ 
        is the image of general point of $\Delta\setminus\{0\}$.
    \item More algebraically and for any field $\kk$, a degeneration of tensors $T_t$ to a tensor $T$ can be thought of as a 
        curve germ $\Spec \kk[\![t]\!] \to \pstspace$ such that the unique $\kk$-point of 
        $\Spec \kk[\![t]\!]$ is mapped to $T$. In this interpretation, the general tensor $T_{t \neq 0}$ 
        is the image of the generic point of $\Spec \kk[\![t]\!]$.
    \item For general $\kk$, a degeneration of tensors $T_t$ to a tensor $T$ can be thought of as an
        single tensor $T_t\in (\pstspace)[\![t]\!]$ such that $T_{t = 0}\in \tspace$ 
        coincides with the tensor $T$. In this interpretation, the general tensor $T_{t \neq 0}$
        is the tensor $T_t$ viewed as an element of the $\kk(\!(t)\!)$-vector space $(\pstspace)(\!(t)\!)$.
\end{enumerate} 
In our proofs, we formally use the last of these notions. However, the arguments easily adjust 
to other notions of a degeneration of tensors, in particular the ones listed above, so the reader is welcome to think about a degeneration 
of tensors according to his own taste. 
\smallskip

We say that one can \emph{algorithmically construct} an unrestriction $\Tppar{}$ using a degeneration of 
tensors $T_t$ if one can write an algorithm which takes a degeneration $T_t$ as an input and returns a 
corresponding unrestriction $\Tppar{}$ as an output. 
The proofs of results from this section have this feature.

\smallskip
Let us state the general result for any partially symmetric format.

\begin{proposition}\label{p:algorithm_full}
    Let $T \in \pstspace$ be a tensor. Suppose we have a degeneration of tensors $T_t \in (\pstspace)[\![t]\!]$ 
    such that $T_{t = 0} = T$ and the general tensor $T_{t \neq 0}$ is concise.
    \begin{enumerate}
        \item Using $T_t$, one can algorithmically construct a concise unrestriction $\Tppar{}$ of the tensor $T$.
        \item If the general tensor $T_{t \neq 0}$ has border rank $\leq m$, then $\Tppar{}$
            has border rank $\leq m$ as well.
    \end{enumerate}
\end{proposition}

Proposition~\ref{p:algorithm_full} above is proved via an iterative construction.
Lemma~\ref{l:algorithm_veronese} below describes the general step of this constrution and itself
proves Proposition~\ref{p:algorithm_full} in the special case of symmetric tensors $F \in S^\nu V$,
see Corollary~\ref{c:algorithm_veronese}.

To state Lemma~\ref{l:algorithm_veronese} cleanly, we first introduce the following handy notion.
\begin{definition}
    A collection of tensors $T_1, \dots, T_n \in \pstspace$ is \emph{jointly concise}
    if $T_1, \dots, T_n$ do not simultaneously lie in a proper subspace
    $S^{\nu_1}V_1' \otimes \ldots \otimes S^{\nu_d}V_d' \subsetneq \pstspace$.
\end{definition}
\begin{example}\label{e:jointly_concise}
    A tensor $T \in \pstspace$ is $V_i$-concise if and only if polynomials in $S^{\nu_i} V_i$
    spanning the image of the flattening
    \[
        T \colon S^{\nu_1}V_1^\vee \otimes \ldots \otimes S^{\nu_{i-1}} V_{i-1}^\vee \otimes 
         S^{\nu_{i+1}} V_{i+1}^\vee \otimes \ldots \otimes S^{\nu_d}V_d^\vee \to S^{\nu_i} V_i
     \]
    are jointly concise.
\end{example}

Now we are ready to proceed with the proofs. The crucial step is case of polynomials.
Here, we will need to extend coefficients, that is, consider $\kk[\![t^{1/N}]\!]$, rather than
$\kk[\![t]\!]$.

\begin{lemma}\label{l:algorithm_veronese}
    Let $(F_1)_t, \dots, (F_n)_t \in S^\nu V[\![t]\!]$ be degenerations of polynomials
    to $F_1, \dots, F_n \in S^\nu V$
    such that the general polynomials $(F_1)_{t \neq 0}, \dots, (F_n)_{t \neq 0}$ are jointly concise.
    Let $N = \nu!$ and extend the coefficients to $\kk[\![t^{1/N}]\!]$.
    One can algorithmically construct
    \begin{itemize}
        \item a degeneration of linear maps $\varphi_t \colon V[\![t^{1/N}]\!] \to V[\![t^{1/N}]\!]$ to a linear map $\varphi$ and
        \item degenerations of polynomials $(\Fppar{}_1)_t, \dots, (\Fppar{}_n)_t \in S^\nu V[\![t^{1/N}]\!]$ to polynomials $\Fppar{}_1, \dots, \Fppar{}_n$
    \end{itemize} 
    that satisfy the following conditions:
    \begin{enumerate}
        \item the polynomials $\Fppar{}_1, \dots, \Fppar{}_n$ are jointly concise,
        \item the map $\varphi$ yields restrictions $\varphi(\Fppar{}_*) = F_*$,
        \item the general map $\varphi_{t \neq 0}$ is a linear isomorphism
            and $\varphi_{t \neq 0}((\Fppar{}_*)_{t \neq 0}) = (F_*)_{t \neq 0}$.
    \end{enumerate}
\end{lemma}
\begin{proof}
    \newcommand{\FF}{\mathbf{F}}
    \newcommand{\FFpar}{\widetilde{\mathbf{F}}}
    \newcommand{\RR}[1]{\mathbf{R}^{(#1)}}
    \newcommand{\HH}{\mathbf{H}}
    Fix a basis $v_1, \dots, v_m$ of $V$ such that $F_1, \dots, F_n$ are jointly concise in 
    variables $v_1, \dots, v_r$, that is, $V' = \spann{v_1, \dots, v_r} \subset V$
    is the smallest subspace such that $F_1, \dots, F_n \in S^\nu V'$. 
    Below, we explain how to construct unrestrictions that are jointly concise at least in variables $v_1,\dots,v_r, v_{r+1}$.
    To construct unrestrictions that are jointly concise in all variables, we simply iterate this algorithm.

    Consider the tuple of polynomials $\FF_t = ((F_1)_t, \dots, (F_n)_t)$. Let $\FF := \FF_{t=0}$. We have
    $\partial_{r+1} \FF = 0$, so $\partial_{r+1} \FF_t = t \RR{1}_t$ for some tuple of polynomials $\RR{1}_t$.
    If $\RR{1}_{t=0}$ lies in the $\kk$-linear span $\spann{\partial_1 \FF, \dots, \partial_r \FF}$,
    then we can find coefficients $\lambda_i^1 \in \kk$ such that 
    $\RR{1}_t = \sum_{i=1}^r \lambda_i^1 \partial_i \FF_t + t \RR{2}_t$,
    so that
    \[
        \partial_{r+1} \FF_t = \sum_{i=1}^r (\lambda_i^1 t) \partial_i \FF_t + t^2 \RR{2}_t.
    \]
    If $\RR{2}_{t=0} \in \spann{\partial_1 \FF, \dots, \partial_r \FF}$, then we can find 
    coefficients $\lambda_i^2 \in \kk$ such that 
    $\partial_{r+1} \FF_t = \sum_{i=1}^r (\lambda_i^1 t + \lambda_i^2 t^2) \partial_i \FF_t + t^3 \RR{3}_t$,
    and so on.
    This process must terminate, because otherwise it would yield coefficients $(\lambda_i)_t \in \kk[\![t]\!]$
    such that $\partial_{r+1} \FF_t = \sum_{i=1}^r (\lambda_i)_t \partial_i \FF_t$, 
    contradicting the assumption that $\FF_t$ are jointly concise. Thus,
    we eventually find an integer $d$ and coefficients $(\lambda_i)_t \in (t\kk[t])_{\leq d-1} \subset \kk[\![t]\!]$
    such that 
    \[
        \partial_{r+1} \FF_t = \sum_{i=1}^r (\lambda_i)_t \partial_i \FF_t + t^d \RR{d}_t,
    \]
    where $\RR{d}_{t=0} \notin \spann{\partial_1 \FF, \dots, \partial_r \FF}$. 
    Consider the $\kk[\![t]\!]$-linear change of variables $\psi_t$ given by $v_i \mapsto v_i - (\lambda_i)_t v_{r+1}$ 
    for $i=1,\dots, r$ and $v_j \mapsto v_j$ for $j = r+1, \dots, m$. Applying it to $\FF_t$, we reduce to the case 
    \begin{equation}\label{eq:tmpRemainder}
        \partial_{r+1} \FF_t = t^d \RR{d}_t.
    \end{equation} 
    Since $\lambda_i$ are divisible by $t$, the map $\psi_t$ is the identity
    map modulo $t$, so $\partial_1 \FF, \dots, \partial_r \FF$
    and $\RR{d}_{t=0}$
    remain unchanged.  

    Now we proceed to rescale $v_{r+1}$ by a power of $t$, to obtain an unrestriction.
    Recall that all polynomials in $\FF_t$ have degree $\nu$.
    For every integer $1\leq j\leq \nu$, let $e_j\geq 1$ be the minimal number such that some polynomial in $\FF_t$ contains
    a monomial of the form $\mu_{a_1, \ldots ,a_m} v_1^{a_1} \ldots v_m^{a_m}$,
    where $a_{r+1} = j$ and $0\neq \mu_{a_1, \ldots ,a_m}\in \kk[\![t]\!]$ is divisible by
    $t^{e_j}$, but not by $t^{e_j+1}$. If such a monomial does not exist, we put $e_j := \infty$.
    Since some monomial containing $v_{r+1}$ exists, at least one $e_j$ is finite.

    Let $w = \min(e_1, e_2/2, \ldots , e_{\nu}/\nu)$. This is a finite positive rational number.
    Extend the coefficients to $\kk[\![t^{1/\nu!}]\!]$ and consider the tuple of polynomials 
    \[
        \FFpar_t = (\FF_t)|_{v_{r+1} := t^{-w}v_{r+1}}
    \]
    and $\FFpar := \FFpar_{t=0}$.
    By definition of $w$, the polynomials $\FFpar_t$ have coefficients in $\kk[\![t^{1/\nu!}]\!]$, there are no negative powers of $t$.
    The tuple $\FFpar_t$ restricts to $\FF_t$ via the map $\varphi_t \colon v_{r+1} \mapsto t^w v_{r+1}$.

    It remains to show that 
    $\partial_1 \FFpar, \dots, \partial_r \FFpar, \partial_{r+1} \FFpar$ are linearly independent.
    We consider two cases
    \begin{enumerate}
        \item $w < e_1$. In this case $\partial_{r+1}\FFpar$ is divisible by $v_{r+1}$.
            However, the partials
            \[
                \partial_{1}\FFpar|_{v_{r+1} = 0} = \partial_{1}\FF, \ldots , \partial_{r}\FFpar|_{v_{r+1} = 0} = \partial_{r}\FF
            \]
            are linearly independent,
            so no linear combination of $\partial_{1} \FFpar, \ldots ,\partial_{r}\FFpar$ is divisible by $v_{r+1}$. 
        \item $w = e_1$. By~\eqref{eq:tmpRemainder}, every monomial in $\FF_t$ divisible by
            $v_{r+1}$ has coefficients in $(t^d)$, so $e_j\geq d$ for all $j=1,\dots,\nu$.
            If $\RR{d}_{t=0}$ depends on the variable $v_{r+1}$, then $\FF_t$ contains a monomial divisible by $v_{r+1}^2$ and with
            coefficient in $(t^d) \setminus (t^{d+1})$, so $e_j = d$ for some $j \geq 2$.
            This gives $w \leq e_j/j = d/j < d \leq e_1$, a contradiction.
            We conclude that $\RR{d}_{t=0}$ does not contain $v_{r+1}$.
            Therefore, substituting $v_{r+1} := 0$ in $\partial_{1}\FFpar, \ldots , \partial_{r+1}\FFpar$, we obtain the tuple
            $\partial_{1}\FF, \ldots , \partial_{r}\FF, \RR{d}_{t=0}$.
            As discussed around~\eqref{eq:tmpRemainder}, its elements are $\kk$-linearly independent.
            % \item $w = e_1$. By~\eqref{eq:tmpRemainder}, every monomial divisible by $v_{r+1}$ has coefficients in $t^d\kk[\![t]\!]$,
        %     so $e_1 \geq d$.
        %     Since $\RR{d}_{t=0}$ is nonzero, some such coefficient does not lie in $t^{d+1}\kk[\![t]\!]$, so $e_1 = d$.

        %     If $\RR{d}_{t=0}$ contains $v_{r+1}$, then $\FFpar$ contains a monomial divisible by at least $(v_{r+1})^2$ and with
        %     coefficient in $(t^d) \setminus (t^{d+1})$, so $e_2 = d$ and $w \leq e_2 = d/2 < d = e_1$, a contradiction.
        %     We conclude that $\RR{d}_{t=0}$ does not contain $v_{r+1}$.
        %     Therefore, substituting $v_{r+1} := 0$ in $\partial_{1}\FFpar, \ldots , \partial_{r+1}\FFpar$, we obtain the tuple
        %     $\partial_{1}\FF, \ldots , \partial_{r}\FF, \RR{d}_{t=0}$.
        %     As discussed around~\eqref{eq:tmpRemainder}, its elements are $\kk$-linearly independent.
    \end{enumerate}
    In both cases, the elements of $\FFpar$ are 
    indeed jointly concise at least 
    in variables $v_1, \dots, v_r, v_{r+1}$. 
    % Let $I \subset \{1,\dots, \nu\}$ be the set of indices $j$ such that the vector of polynomials 
    % $\FF_t$ contains a monomial of $v_{r+1}$-degree equal to $j$. Write   
    % \[
    %     \FF_t = (\HH_0)_t + \sum_{j \in I} t^{e_j} v_{r+1}^j (\HH_j)_t,
    % \]
    % where $(\HH_0)_t, (\HH_j)_t$ do not contain $v_{r+1}$ and $e_j$ are maximal, that is $\HH_j \neq 0$
    % for all $j \in I$.
    % Let $w$ be the minimum of all ${e_j}/j$. 
    % Extend the coefficients to $\kk[\![t^{1/\nu!}]\!]$ and consider the vector of polynomials 
    % \[
    %     \FFpar_t = (\HH_0)_t + \sum_{j \in I} t^{e_j - jw} v_{r+1}^j (\HH_j)_t.
    % \]
    %
    % Note that $\FFpar_t$ restricts to $\FF_t$ via the map $\varphi_t \colon v_{r+1} \mapsto t^w v_{r+1}$.
    % Our aim is to show that coordinates $\Fppar{}_1, \dots, \Fppar{}_n$ of $\FFpar$ are jointly concise at least 
    % in variables $v_1, \dots, v_r, v_{r+1}$, that is, 
    % $\partial_1 \FFpar, \dots, \partial_r \FFpar, \partial_{r+1} \FFpar$ are linearly independent.
    % Let $J = \{j \in I \colon w = e_j/ j\} \subset I$. We have 
    % $
    %     \FFpar = \FF + \sum_{j \in J} v_{r+1}^j \HH_j,
    % $ 
    % so 
    % \[
    %     \partial_i \FFpar = \partial_i \FF + \sum_{j \in J} v_{r+1}^j \partial_i \HH_j 
    %     \quad\text{for $i=1,\dots,r$}\quad\text{and}\quad
    %     \partial_{r+1} \FFpar = \sum_{j \in J} j v_{r+1}^{j-1} \HH_j.
    % \]
    % Suppose that we have a linear relation $\sum_{i=1}^{r} c_i \partial_i \FFpar + c_{r+1} \partial_{r+1} \FFpar = 0$.
    % \begin{enumerate}
    %     \item First, consider the case $1 \notin J$, so that $\partial_{r+1} \FFpar$ is divisible by $v_{r+1}$.
    %     Evaluating at $v_{r+1} = 0$ yields $\sum_{i=1}^{r} c_i \partial_i \FF = 0$, which 
    %     implies that $c_1 = \dots = c_r = 0$ because $F_1, \dots, F_n$ are jointly concise in 
    %     $v_1,\dots,v_r$. The relation becomes $c_{r+1} \partial_{r+1} \FFpar = 0$,
    %     which forces $c_{r+1} = 0$, since $\FFpar$ depends on $v_{r+1}$ by construction.
    %     \item Now, assume that $1 \in J$. For any other $j \in I$, we get 
    %         $e_j \geq jw = je_1 \geq 2e_1 > e_1$. Recall that $\partial_{r+1} \FF_t = t^d \RR{d}_t$,
    %     so 
    %     \[
    %         t^d \RR{d}_t 
    %         = \sum_{j \in I} t^{e_j} j v_{r+1}^{j-1} (\HH_j)_t
    %         = t^d(t^{e_1-d} (\HH_1)_t + \sum_{j \in I \setminus \{1\}} t^{e_j-d} j v_{r+1}^{j-1} (\HH_j)_t).
    %     \]
    %     This implies that $e_1 = d$ and $e_j - d > 0$ for $j \in I \setminus \{1\}$, so 
    %     $\RR{d} = \HH_1$. Evaluation at $v_{r+1} = 0$ yields a relation
    %     $\sum_{i=1}^{r} c_i \partial_i \FF + c_{r+1} \partial_{r+1} \RR{d} = 0$.
    %     By construction, $\partial_i \FF$ and $\RR{d}$ are all linearly independent,
    %     so $c_1 = \dots = c_r = c_{r+1} = 0$.
    % \end{enumerate}
\end{proof}
% \begin{proof}
%     Fix a basis $v_1, \dots, v_m$ of $V$ such that $F_1, \dots, F_n$ are jointly concise in 
%     variables $v_1, \dots, v_r$. For each $i = 1, \dots, n$, write
%     \[
%         (F_i)_t = \sum t^{e_{i,a}} \lambda_{i,a} v_1^{a_1} v_2^{a_2} \dots v_m^{a_m}, \quad
%         \lambda_{i,a} \in \kk[\![t]\!], \quad\lambda_{i,a}(0) \neq 0.
%     \]
%     The general polynomials $(F_1)_{t \neq 0}, \dots, (F_n)_{t \neq 0}$ are jointly concise, so there 
%     is a monomial containing $v_{r+1}$ in some of the decompositions above. 
%     Let $e_{i',a'}/a'_{r+1}$ be the minimum of all $e_{i,a} / a_{r+1}$. 
%     Recall that we extend the coefficients to $\kk[\![t^{1/\nu!}]\!]$, so we can take roots $t^{1/l}$ for every $l = 1,\dots, \nu$.
%     Consider the map $\varphi_t'$ which sends $v_{r+1} \mapsto t^{e_{i',a'}/a'_{r+1}} v_{r+1}$
%     and does not change the other basis vectors of $V$. 
%     The change of variables via $(\varphi_{t \neq 0}')^{-1}$ replaces each monomial
%     $t^{e_{i,a}} \lambda_{i,a} v_1^{a_1} v_2^{a_2} \dots v_m^{a_m}$ containing $v_{r+1}$ by 
%     \[
%         t^{a_{r+1}(e_{i,a}/a_{r+1} - e_{i',a'}/a'_{r+1})} \lambda_{i,a} v_1^{a_1} v_2^{a_2} \dots v_m^{a_m},
%     \]
%     so the polynomials $(\varphi_{t \neq 0}')^{-1}(F_\bullet)_{t \neq 0} \in S^\nu V(\!(t^{1/\nu!})\!)$ 
%     have coefficients with non-negative valuations. This means that they
%     can be viewed as degenerations $(\Fppar{'}_\bullet)_t \in S^\nu V[\![t^{1/\nu!}]\!]$.
%     The limits $\Fppar{'}_\bullet := (\Fppar{'}_\bullet)_{t=0}$ are jointly concise with respect to the variables 
%     $v_1, \dots, v_{r+1}$ by construction. Moreover, the linear map $\varphi' := \varphi'_{t =0}$ gives restrictions $\Fppar{'}_\bullet \geq F_\bullet$.

%     We iteratively apply this construction until we produce degenerations $(\Fppar{}_\bullet)_t$ whose limits 
%     are jointly concise. The final degeneration of maps $\varphi_t$ is just the composition of 
%     degenerations of maps produced in the process.
% \end{proof}
\begin{corollary}\label{c:algorithm_veronese}
    Let $F \in S^\nu V$ be a polynomial. Suppose we have a degeneration of polynomials
    $F_t \in S^\nu V[\![t]\!]$ such that $F_{t = 0} = F$ and the general polynomial
    $F_{t \neq 0}$ is concise.
    \begin{enumerate}
        \item Using $F_t$, one can algorithmically construct a concise unrestriction 
        $\Fppar{} \in S^\nu V$ of $F$.
    \item If the general polynomial $F_{t \neq 0}$ has border rank $\leq m$,
        then $\Fppar{}$ has border rank $\leq m$ as well.
    \end{enumerate}
\end{corollary}
\begin{proof}
    Apply Lemma~\ref{l:algorithm_veronese} for $n=1$ and $(F_1)_t = F_t$. The first claim is immediate. 
    For the second claim, note that the general polynomial $\Fppar{}_{t \neq 0}$ is isomorphic to 
    the general polynomial $F_{t \neq 0}$ via $\varphi_{t \neq 0}$.
\end{proof}

\begin{example}\label{ex:smallCW}
    Consider the symmetric tensor $x_1x_2x_3$, which is the small Coppersmith-Winograd tensor~\cite[Chapter~15]{BurgisserBook}.
    It has border rank $4$, as witnessed, for example, by the limit
    \[
        F'_t = (x_1 + tx_2 + tx_3)^3 - (x_1+tx_2)^3 - (x_1+tx_3)^3 + x_1^3 = 6t^2\cdot x_1x_2x_3 + t^3(\ldots).
    \]
    The general tensor here, viewed in $\kk[x_1, \ldots ,x_4]$, is not concise, so we need to perturb it, for
    example by taking $N\gg 0$ and adding a ``quickly decaying'' term $t^Nx_4$ to the last factor:
    \[
    \begin{split}
        F_t =& (x_1 + tx_2 + tx_3)^3 - (x_1+tx_2)^3 - (x_1+tx_3)^3 + (x_1 + t^N x_4)^3 \\
        =& 6t^2\left(x_1 x_2 x_3 + \frac{1}{2} t x_2^2 x_3 + \frac{1}{2}t x_2 x_3^2 + 
        \frac{1}{2} t^{N-2} x_1^2 x_4 + \frac{1}{2} t^{2N-2} x_1 x_4^2 + \frac{1}{6}t^{3N-2} x_4^3\right).
    \end{split}
    \]
    Following the algorithm from Lemma~\ref{l:algorithm_veronese}, we look at monomials containing $x_4$,
    pick the minimal value among ratios between exponent of $t$ and exponent of $x_4$, which is 
    $
        N-2 = \min(\frac{N-2}{1}, \frac{2N-2}{2}, \frac{3N-2}{3}),
    $
    and apply the change of coordinates via $x_4 \mapsto t^{-(N-2)}x_4$. This way we obtain the degeneration 
    \[
        \Fppar{}_t = 6t^2\left(x_1 x_2 x_3 + \frac{1}{2} t x_2^2 x_3 + \frac{1}{2}t x_2 x_3^2 + 
        \frac{1}{2} x_1^2 x_4 + \frac{1}{2} t^{2} x_1 x_4^2 + \frac{1}{6}t^{4} x_4^3\right).
    \]
    The corresponding minimal border rank unrestriction is $\Fppar{} = x_1x_2x_3 + \frac{1}{2}x_4x_1^2$,
    which is isomorphic to the big Coppersmith-Winograd tensor.

    The tensor $x_1x_2x_3$ has several non-isomorphic unrestrictions from minimal border rank,
    for example:
    \begin{enumerate}
        \item  $x_1x_2x_3 + x_4x_1^2$, which is the big Coppersmith-Winograd tensor (obtained as above),
        \item  $x_1x_2x_3 + x_4(x_1^2 + x_2^2)$, which is isomorphic to the multiplication tensor in the finite 
        algebra $\kk[y_1]/(y_1^2) \times \kk[y_2]/(y_2^2)$,
        \item  $x_1x_2x_3 + x_4(x_1^2 + x_2^2 + x_3^2 + x_4^2)$, which is isomorphic to the unit tensor $\spann{4}$ of rank $4$.
    \end{enumerate}
\end{example}

Now we prove the general result for all partially symmetric formats.
\begin{proof}[Proof of Proposition~\ref{p:algorithm_full}]
    First, we construct an unrestriction $\Tppar{1} \in \pstspace$ that is concise on the first 
    coordinate $S^{\nu_1} V_1$. Consider the flattening of $T_t$ with respect to the coordinates 
    $S^{\nu_2} V_2 \otimes \dots \otimes S^{\nu_d} V_d$ and let $(F_1)_t, \dots, (F_n)_t \in (S^{\nu_1}V_1)[\![t]\!]$
    be a basis of its image. The general tensors $(F_\bullet)_{t \neq 0}$ are jointly concise by
    Example~\ref{e:jointly_concise}. The algorithm from Lemma~\ref{l:algorithm_veronese}
    produces a degeneration of maps $(\varphi_1)_t \in \End(V)[\![t^{1/N}]\!]$ 
    with $(\varphi_1)_{t \neq 0}$ invertible such that the degeneration of tensors 
    $((\varphi_1)_{t \neq 0})^{-1} T_{t \neq 0}$ extends to a degeneration of tensors $\Tppar{1}_t$ 
    whose limit $\Tppar{1}$ is a $V_1$-concise unrestriction of $T$.

    To obtain a concise unrestriction $\Tppar{} \geq T$, we just iterate the algorithm on the other coordinates. 
    This way we produce a sequence of unrestrictions 
    $\Tppar{}:= \Tppar{1,\dots,d} \geq \dots \geq \Tppar{1, 2} \geq \Tppar{1} \geq T$
    such that each tensor $\Tppar{1,\dots,i}$ is a priori $V_i$-concise. However, this forces $\Tppar{1,\dots,i}$ to be 
    $V_1, \dots, V_i$-concise, so the final unrestriction $\Tppar{}$ is indeed concise.

    The assertion about border rank follows from the fact the general tensor $\Tppar{}_{t \neq 0}$
    is isomorphic to the general tensor $T_{t \neq 0}$, as border rank can only drop in the limit.
\end{proof}

\begin{remark}
The algorithm from Proposition~\ref{p:algorithm_full} in general requires passing to an 
extension $\kk[\![t]\!] \subset \kk[\![t^{1/N}]\!]$, where $N = \prod_{i=1}^d \nu_i!$.
However, in the special case of tensors in $\tspace$, all $\nu_{\bullet}$ are equal to one, so
no extension is necessary.
\end{remark}

Below, we present an alternative algorithm for producing concise unrestrictions
for tensors of the Segre format $T \in \tspace$, where extensions do not appear and fewer choices are made. 
Moreover, this construction can be reinterpreted geometrically using the setup of 
unrestriction schemes introduced in this paper, see~\S\ref{sec:unrestrictions_geometric}. 

\begin{proposition}\label{p:algorithm_segre}
    Let $T \in \tspace$ be a tensor. Suppose we have a degeneration of tensors
    $T_t \in \tspace[\![t]\!]$ such that $T_{t = 0} = T$ and the general tensor
    $T_{t \neq 0}$ is concise.
    \begin{enumerate}
        \item Using $T_t$, one can algorithmically construct a concise unrestriction 
        $\Tppar{} \in \tspace$ of $T$.
        \item If the general tensor $T_{t \neq 0}$ has border rank $\leq m$, 
        then $\Tppar{}$ has border rank $\leq m$ as well.
    \end{enumerate}
\end{proposition}

Using the geometric perspective, we deduce that different choices of bases and minors in the 
algorithmic construction from the proof of Proposition~\ref{p:algorithm_segre} lead to isomorphic 
unrestrictions.
\begin{proposition}[Proposition~\ref{prop:uniqueness_of_unres}]
    Let $T \in \sigmahat_m \subset \tspace$ be a tensor of border rank $\leq m$.
    Let $T_t$ be a degeneration of tensors of border rank $\leq m$ to $T$ with 
    general tensor $T_{t \neq 0}$ concise. 
    Consider any two unrestrictions 
    \[(\Tppar{}, \varphi_1, \dots, \varphi_d)\quad\text{and}\quad (\Tppar{'}, \varphi_1', \dots, \varphi_d')\] 
    constructed from $T_t$ using the algorithmic from the proof 
    of Proposition~\ref{p:algorithm_segre} for different choices of bases and minors.
    Then there exists linear isomorphisms $\psi_i \colon V_i \to V_i$ such that 
    \[
        \Tppar{'} = \psi_{1,\dots,d}(\Tppar{}) \quad\text{and}\quad \varphi_i' = \varphi_i \circ \psi_i^{-1} \quad\text{for every} \quad i=1,\dots,d.
    \]
\end{proposition}

We reiterate that even though Proposition~\ref{p:algorithm_segre} is formally a special case of
Proposition~\ref{p:algorithm_full}, the proof given below is different and independent of 
the proof of Proposition~\ref{p:algorithm_full}.

The construction is iterative. The following lemma describes the general step.
\begin{lemma}\label{l:algorithm_step}
    Let $T_t \in \tspace[\![t]\!]$ be a degeneration of tensors to a tensor $T$ such that the general tensor
    $T_{t \neq 0}$ is $V_i$-concise. 
    One can algorithmically construct
    \begin{itemize}
        \item a degeneration of linear maps $(\varphi_i)_t \colon V_i[\![t]\!] \to V_i[\![t]\!]$ to a linear map $\varphi_i$ and
        \item a degeneration of tensors $\Tppar{i}_t \in \tspace[\![t]\!]$ to a tensor $\Tppar{i}$
    \end{itemize} 
    that satisfy the following conditions:
    \begin{enumerate}
        \item the tensor $\Tppar{i}$ is $V_i$-concise,
        \item the map $\varphi_i$ yields a restriction $\varphi_i(\Tppar{i}) = T$,
        \item the general map $(\varphi_i)_{t \neq 0}$ is a linear isomorphism
            and $(\varphi_i)_{t \neq 0}(\Tppar{i}_{t \neq 0}) = T_{t \neq 0}$.
    \end{enumerate}
\end{lemma}
\begin{proof}
    Fix coordinates on the vector space $\tspace$. Let $M_t$ be the $(m \times n)$-matrix representing the flattening
    $T_t \colon \Vhat^\vee[\![t]\!] \to V_i[\![t]\!]$. The general tensor 
    $T_{t \neq 0}$ is $V_i$-concise, so $m \leq n$ and  $M_t$ has a non-zero maximal minor. 
    Let $(X_i)_t$ be a $(m \times m)$-submatrix of $M_t$ which determinant has minimal valuation 
    among all non-zero minors of $M_t$. Cramer's rule from linear algebra says that entries 
    of the matrix $(X_i)_{t \neq 0}^{-1} \cdot M_{t \neq 0}$ are maximal minors of $M_{t \neq 0}$ 
    divided by $\det (X_i)_{t \neq 0}$, so they have positive valuation.
    Let us view $(X_i)_{t \neq 0}^{-1} \cdot M_{t \neq 0}$ as a matrix $(M_i)_t$ with coefficients in $\kk[\![t]\!]$.
    The submatrix of $(M_i)_t$ indexed by the same columns as the submatrix $(X_i)_t$ of $M_t$ is the identity matrix,
    so $(M_i)_{t = 0}$ has full rank. Moreover, we have $(X_i)_t \cdot (M_i)_t = M_t$,
    so in particular $(X_i)_{t = 0} \cdot (M_i)_{t = 0} = M_{t = 0}$.
    Finally, take $(\varphi_i)_t$ to be the degeneration of maps corresponding to $(X_i)_t$
    and $\Tp_t$ to be the degeneration of tensors corresponding $(M_i)_t$.
\end{proof}
\begin{proof}[Proof of Proposition~\ref{p:algorithm_segre}]
    First, take the degeneration $T_t$. The general tensor $T_{t \neq 0}$ is 
    concise, so we can apply the algorithm from Lemma~\ref{l:algorithm_step} on $V_1$ to construct 
    a degeneration of tensors $\Tppar{1}_t$ and a degeneration of maps $(\varphi_1)_t$.
    The tensor $\Tppar{1}$ is $V_1$-concise and the map $\varphi_1$ gives a restriction $\Tppar{1} \geq T$.
    Then, take the degeneration $\Tppar{1}_t$ and apply the construction from Lemma~\ref{l:algorithm_step}
    on $V_2$ to get degenerations $\Tppar{1,2}_t$ and $(\varphi_2)_t$ yielding a $V_2$-concise tensor $\Tppar{1,2}$ 
    restricting to $T_1$ via $\varphi_2$, and so on. 
    After $d$ steps, we get tensors $\Tppar{1}, \Tppar{1,2} \dots, \Tppar{1,\dots,d}\in \tspace$ and maps 
    $\varphi_1 \in \End(V_1), \dots, \varphi_d \in \End(V_d)$ such that each $\Tppar{1,\dots,i}$ is $V_i$-concise
    and $\varphi_i(\Tppar{1,\dots,i}) = \Tppar{1,\dots,i-1}$. 
    The flattening ranks can only drop under restriction, so the $i$-th tensor $\Tppar{1,\dots,i}$ is in fact 
    $V_1, \dots, V_i$-concise. In particular, the tensor $\Tppar{} := \Tppar{1,\dots,d}$ is concise
    and the maps $\varphi_1, \dots, \varphi_d$ give an unrestriction $T \leq \Tppar{}$.

    Now assume that the general tensor $T_{t \neq 0}$ has border rank $\leq m$.
    The general map $(\varphi_{1, \dots, d})_{t \neq 0}$ yields an isomorphism between 
    $\Tppar{}_{t \neq 0}$ and $T_{t \neq 0}$, so the general tensor $\Tppar{}_{t \neq 0}$
    and its limit $\Tppar{}$ have border rank $\leq m$ as well. 
\end{proof}



\begin{example}[Bini's tensor]
    Let $T$ be the tensor corresponding to multiplication of $2 \times 2$-matrices
    with the bottom-right entry of the first matrix being zero, see~\cite[Subsection 2.1.4]{JM_complexity}.
    This tensor has border rank equal to 5, which is witnessed by the following degeneration of unit tensors:
    \[
    \begin{aligned}
        T_t = &(t a_1 + a_3) \otimes b_2 \otimes (c_2 + t c_4)
        +(t a_1 + a_2) \otimes (b_1 + t b_3) \otimes c_1
        +(a_2 + a_3) \otimes (b_1 + t b_4) \otimes (c_2 + t c_3)\\
        +&(-a_3 + t^2 a_4) \otimes (b_1 + b_2 + t b_4 + t^2 b_5) \otimes c_2
        +(-a_2 + t^2 a_5) \otimes b_1 \otimes (c_1 + c_2 + t c_3 + t^2 c_5).
    \end{aligned}
    \]
    The algorithm applied to $T_t$ produces the degeneration of tensors
    \[
        \Tppar{}_t :=
        \begin{bmatrix}
        x_1 & x_2 & x_3 & 0 & x_5 \\
        0 & -tx_2 + x_3 & 0 & 0 & 0 \\
        0 & x_4 & 0 & -tx_2 + x_3 + tx_4 & 0 \\
        x_5 & 0 & 0 & 0 & tx_5 \\
        0 & -tx_1 + tx_2 + x_5 & -t^2x_1 + tx_3 + tx_5 & 0 & 0
        \end{bmatrix}
    \]
    whose general tensor $\Tppar{}_{t \neq 0}$ is isomorphic to $T_{t \neq 0}$ via the maps
    \[
        \begin{bmatrix}
        1 & 0 & 0 & 1 & t \\
        0 & 0 & 0 & 0 & 1 \\
        0 & 0 & 1 & 0 & 0 \\
        0 & t & 0 & t & 0 \\
        t & t & t^2 & 0 & 0
        \end{bmatrix},\quad
        \begin{bmatrix}
        1 & 0 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 0 & 1 \\
        0 & -t & 0 & 0 & 0
        \end{bmatrix},\quad
        \begin{bmatrix}
        1 & 0 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1 & 0 \\
        t^2 & 0 & 0 & 0 & -t
        \end{bmatrix}.
    \]
    To get the corresponding minimal border rank unrestriction $\Tppar{}$, we simply set $t = 0$.
    In a suitable basis, this unrestriction can be represented as
    \[
        T = \begin{bmatrix}
        x_1 & 0 & x_3 & 0 & 0 \\
        0 & x_1 & 0 & x_3 & 0 \\
        x_2 & 0 & 0 & 0 & 0 \\
        0 & x_2 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 & 0
        \end{bmatrix}
        \leq 
        \begin{bmatrix}
        x_1 & x_5 & x_3 & 0 & x_2 \\
        0 & x_1+x_4 & 0 & x_3 & 0 \\
        x_2 & 0 & 0 & 0 & 0 \\
        0 & x_2 & 0 & 0 & 0 \\
        0 & x_3 & 0 & 0 & 0
        \end{bmatrix}
        = \Tppar{}.
    \]
    The tensor $\Tppar{}$ is the $1$-degenerate tensor $T_{\mathcal{O}_{56}}$ from the classification from~\cite[Theorem 1.7]{JLP}.
\end{example}

In the algorithmic proof of Proposition~\ref{p:algorithm_full}, we had to choose an order of coordinates $V_1, \dots, V_d$. 
The following example shows that different choices can lead to non-isomorphic unrestrictions.
\begin{example}\label{ex:order_matters}
    Let $d = 3$ and $\dim_\kk V_\bullet = 2$. Consider the following degeneration of concise tensors, 
    represented in the matrix form as
  \[
    \begin{bmatrix}
    x_1 & t^2 x_2 \\
    t x_2 & t x_1 \\
  \end{bmatrix}.
  \]
  Applying the algorithm first to columns and then to variables yields the constant degeneration
  \[
  \begin{bmatrix}
    x_1 & t^2 x_2 \\
    t x_2 & t x_1 \\
  \end{bmatrix}
  \leadsto 
  \begin{bmatrix}
    x_1 & t x_2 \\
    t x_2 & x_1 \\
  \end{bmatrix}
  \leadsto 
  \begin{bmatrix}
    x_1 & x_2 \\
    x_2 & x_1 \\
  \end{bmatrix}
  \xrightarrow{t \to 0} \begin{bmatrix}
    x_1 & x_2 \\
    x_2 & x_1 \\
  \end{bmatrix}.
  \]
  Starting from rows, we obtain another degeneration
  \[
  \begin{bmatrix}
    x_1 & t^2 x_2 \\
    tx_2 & tx_1 \\
  \end{bmatrix}
  \leadsto
  \begin{bmatrix}
    x_1 & t^2 x_2 \\
    x_2 & x_1 \\
  \end{bmatrix}
  \xrightarrow{t \to 0} \begin{bmatrix}
    x_1 & 0 \\
    x_2 & x_1 \\
  \end{bmatrix}.
  \]
  The first minimal border rank unrestriction is the multiplication tensor in the algebra
  $\kk \times \kk$, written in the basis $(1,1), (1,-1)$. The second one
  comes from multiplication in $\kk[x]/(x^2)$. In particular, they are not isomorphic. 
%   This shows that at least for tensors lying in $\sigmahat_{m-1} \subset \sigmahat_m$, 
%   the unrestriction produced by the algorithm can depend on the choice of order.
\end{example}


\section{Unrestriction schemes}\label{sec:unrestrictionSchemes}

In this section we return to the Segre format and we build unrestriction schemes. The unrestrictions
from Section~\ref{sec:unrestrictions} are curves on these varieties.

We use the following conventions. On a $\kk$-vector space $V$ we put an affine space structure by
$V = \Spec\Sym V^{\vee}$. More generally, we identify a locally free sheaf
$\VV$ on a scheme $X$ with the associated vector bundle $\Spec_X \Sym
\VV^{\vee}$.

To cleanly state the result, we need a notion of a family of tensors parameterised by a variety $X$.
In the literature, such a family is sometimes defined to be a morphism $X\to V_1\otimes \ldots \otimes V_d$. However, this setup
is rather restrictive: in this way there is \emph{no} universal family over
$\mathbb{P}(V_1\otimes \ldots \otimes V_d)$, see
Example~\ref{ex:universalFamily} below. We take a different route by using
vector bundles.
We introduce the notions below.
The following dictionary may help to quickly grasp them:
\[
    \begin{array}{c c c}
        & \mathrm{tensor} & \mathrm{family\ of\ tensors}\\
        \toprule
        & T\in V_1\otimes \ldots \otimes V_d & T\colon \LL \to \VV_1 \otimes \ldots \otimes \VV_d\\
        \mathrm{concise} & V_1^{\vee}\to V_2\otimes \ldots \otimes V_d \mbox{ injective} & \VV_1^{\vee} \otimes \LL \into \VV_2\otimes \ldots \otimes \VV_d\mbox{ subbbundle}\\
        \mathrm{concise} & V_2^{\vee}\otimes \ldots \otimes V_d^{\vee}\to V_1 \mbox{ surjective} &  \VV_2^{\vee}\otimes \ldots \otimes \VV_d^{\vee}\otimes \LL \onto \VV_1 \mbox{ surjective}
        % \\
        % \mathrm{lying\ in\ the\ span} & T\in \spann{Z} & \Tppar{}\colon \LL \into \spann{\ZZ}
    \end{array}
\]

A map $\VV'\into \VV$ of vector bundles is a \emph{subbundle} if it is injective and $\VV/\VV'$ is also a vector bundle.
This also has a much more intuitive equivalent definition: it is not only injective, it stays injective after restriction to a point.
We make this explicit by the following lemma.
\begin{lemma}\label{ref:subbudle:lem}
    Let $\VV'\to \VV$ be a map of vector bundles (not a priori assumed injective) on a scheme $X$. The following are equivalent:
    \begin{enumerate}
        \item\label{it:subbundleAll} for every morphism $f\colon Y\to X$, the pullback $f^*\VV'\to f^*\VV$ is injective,
        \item\label{it:subbundlePoint} for every $x\in X$, the induced map $\VV'|_x\to \VV|_x$ is injective,
        \item\label{it:subbundle} $\VV'\to \VV$ is a subbundle (in particular, it is injective).
    \end{enumerate}
\end{lemma}
\begin{proof}
    \def\mm{\mathfrak{m}}%
    The implication $\ref{it:subbundleAll}\implies\ref{it:subbundlePoint}$ is formal.
    The implication $\ref{it:subbundle}\implies\ref{it:subbundleAll}$ follows from the fact that pullback of
    sequences of vector bundles stay exact.
    Assume $\ref{it:subbundlePoint}$ holds. The claim~\ref{it:subbundle} is local on $X$, so we may assume that $X = \Spec(A)$
    for a local ring $(A, \mm)$ and that $\VV$, $\VV'$ come from $A$-modules $V$, $V'$. By assumption, the map $V/\mm V\to V'/\mm V'$
    is injective. Pick elements $v_1, \ldots ,v_k$ of $V$ and $v_{k+1}, \ldots ,v_l$ of $V'$ such that the classes of $v_1, \ldots ,v_k$ form
    a basis of the vector space $V/\mm V$ and $v_1, \ldots , v_l$ form a basis of the vector space $V'/\mm V'$. This implies that $V\to V'$
    is injective. Consider the free submodule $V'' \subseteq V'$ generated by
    $v_{k+1}, \ldots ,v_l$. One verifies that the map $V' \to V'/V$ restricts
    to an isomorphism $V''\to V'/V$, hence $V'/V$ is a free $A$-module.
\end{proof}

Below, when working with vector bundles over $X$, we use $\otimes$ instead of $\otimes_{\OO_X}$. Similarly, when working with
vector spaces, we write $\otimes$ instead of $\otimes_{\kk}$. When $V$ is a vector space, we denote by $\OO_{X}\otimes V$ the trivial
vector bundle on $X$ with fibre $V$.
For vector spaces $V_1, \ldots ,V_d$, we write $\tspace := V_1 \otimes \ldots \otimes V_d$.
For vector bundles $\VV_1, \ldots , \VV_d$, we write $\tspacecurly := \VV_1 \otimes \ldots \otimes \VV_d$.
When $\tspacecurly$ is clear form the context, we write $\VVhat$ for $\VV_1\otimes  \ldots \otimes\VV_{i-1} \otimes \VV_{i+1}\otimes \ldots \otimes \VV_d$.

\begin{definition}\label{ref:tensor:def}
    Let $X$ be a scheme.
    A \emph{family of tensors over $X$} or a \emph{tensor on $X$} is a map
    $T\colon \LL\to \tspacecurly$, where $\LL$ is a line bundle. For a map
    $f\colon Y\to X$, we have an induced family over $Y$ given by $f^*T\colon
    f^*\LL \to f^*\tspacecurly$. When $Y = \{x\}$ is a point of $X$, we use the
    notation $T|_x$ instead of $f^*T$.
The map $T\colon \LL\to \tspacecurly$ is a subbundle $\LL\into \tspacecurly$ if and only if $T|_x\neq 0$ for every $x\in X$.
\end{definition}

\begin{example}\label{ex:universalFamily}
    Let $V_1, \ldots ,V_d$ be vector spaces.
    \begin{enumerate}
        \item
            There is a tensor over $\tspace$
            \[
                \Taf\colon \OO_{\tspace} \to \OO_{\tspace} \otimes \tspace
            \]
            such that for every $\kk$-point $x$ of $\tspace$ the tensor $\Taf|_x\in \tspace$ is the 
            tensor corresponding to $x\in \tspace$.
            In this case $\OO_{\tspace}$ is not a subbundle, since $\Taf|_0 = 0$.
        \item There is a tensor over $\mathbb{P}(\tspace)$ given by the subbundle
            \begin{equation}\label{eq:univTensorProj}
                \Tproj\colon \OO_{\mathbb{P}(\tspace)}(-1)\into \OO_{\mathbb{P}(\tspace)}\otimes \tspace.
            \end{equation}
            Over a  point a $\kk$-point $[T] \in \mathbb{P}(\tspace)$, the induced map on fibers is the inclusion map
            \[
                \Tproj|_{[T]}\colon \OO_{\mathbb{P}(\tspace)}(-1)|_{[T]} = \kk\cdot T \hookrightarrow \tspace = 
                (\OO_{\mathbb{P}(\tspace)} \otimes \tspace)|_{[T]}.
            \]
            Observe that in this case it is not possible to use only trivial vector bundles.
        \item Let $X \into \mathbb{P}(\tspace)$ be a closed subscheme. The restriction of~\eqref{eq:univTensorProj} to $X$
            yields a tensor $\OO_{X}(-1) \into \OO_{X}\otimes \tspace$. We will use this observation for $X$ being a
            secant or a cactus variety.
        \item Let $V$ be a vector spaces and let $\UU^\vee$ be the universal subbundle on $\Gr(m, V)$. 
            There is a tensor over $\Gr(m,V)$
            \[
                \TGr \colon \OO_{\Gr(m, V)} \to \UU \otimes V
            \]
            corresponding to the subbundle inclusion $\UU^\vee \into \OO_{\Gr(m, V)} \otimes V$.
            This tensor is $\UU$-concise in the sense of Definition~\ref{ref:concise:def}.
        % \item As a more exotic example, let $\mathcal{H} := \Hilb_d(\mathbb{A}^n)$ be the Hilbert scheme of points. It comes with
        %     a universal closed subscheme $\mathcal{Z} \into \mathcal{H}\times \mathbb{A}^n$. The morphism
        %     $p\colon \mathcal{Z}\to \mathcal{H}$ is finite and $\UU := p_*\OO_{\mathcal{Z}}$ is a rank $d$ vector bundle on $\mathcal{H}$.
        %     Since $\mathcal{Z}$ is a scheme, the bundle $\UU$ comes with a multiplication $\UU\otimes \UU\to \UU$, hence a universal
        %     tensor $\mu\colon \OO_{\mathcal{H}}\to \UU^{\vee}\otimes \UU^{\vee}\otimes \UU$. We will not use it much here,
        %     but it illustrates the versatility of the notion.
    \end{enumerate}
    % corresponding to the section
    % \[
    %     (\tspace^\vee \hookrightarrow \Sym \tspace^\vee)
    %     \in \Hom(\tspace^\vee, \Sym \tspace^\vee)
    %     = \Sym \tspace^\vee \otimes \tspace
    %     = H^0(X, \OO_X \otimes_\kk \tspace).
    % \]
    % Over a $\kk$-point $T \in X$, the induced map on fibers is given by
    % \[
    %     \OO_X|_T = \kk \ni 1 \mapsto T \in \tspace = (\OO_X \otimes \tspace)|_T.
    % \]
\end{example}

\begin{remark}
    A tensor of the form $T\colon \OO_X \to \tspacecurly$ is the same as an
    element $T\in H^0(\tspacecurly)$. In the latter form, families of tensors
    appear everywhere throughout the literature, for example in works related
    to secant varieties of any variety or in the toric setup~\cite{Galazka, Buczyska_Buczynski__border}.
\end{remark}

\begin{remark}\label{ref:localFamilies:rem}
    Let $T\colon \LL\to \tspacecurly$ be a family of tensors and $x\in X$ be a point.
    There is an open neighbourhood $x\in U \subseteq X$ such that $\LL|_U$, $(\VV_1)|_U$,
     \ldots, $(\VV_d)|_{U}$ are all trivial bundles. The tensor $T|_U$ is isomorphic to a tensor
     of the form $\OO_U \to \OO_U \otimes \tspace$, hence to a map $f\colon U\to \tspace$. In particular,
     $T|_U = f^*\Taf$, where $\Taf$ is the universal tensor on $\tspace$. Informally speaking,
     locally on $X$ the notion of a family agrees with the more common notion of $X\to \tspace$.
\end{remark}


\begin{definition}\label{ref:concise:def}
A family of tensors $T\colon \LL\to \tspacecurly$ is \emph{$\VV_i$-concise} if
the contraction
\[
    T_{\VV_i}\colon  \VV_i^{\vee}\otimes\LL \to \VVhat
\]
is a vector subbundle. In this case $\LL\to \tspacecurly$ is also a subbundle.
The family $T$ is \emph{concise} if it is concise with respect to every
coordinate.
\end{definition}

\begin{definition}\label{def:concise}
    A family of tensors $T \colon \LL \to \tspacecurly$ 
    is a \emph{restriction} of another family of tensors $\Tppar{} \colon \LL \to \WW_{1,\dots,d}$
    if there exist $\OO_X$-linear maps $\varphi_i \colon \WW_i \to \VV_i$ such 
    that $(\varphi_1 \otimes \dots \otimes \varphi_d)(\Tppar{}) = T$.
\end{definition}


\begin{remark}\label{ref:concise:rem}
    A family of tensor $T$ over $X$ is $\VV_i$-concise if and only if for every point $x\in X$, the induced
contraction ${T_{\VV_i}}|_x$ is injective. In particular, if $T$ restricts to a $\VV_i$-concise tensor
(in the sense of Definition~\ref{def:concise}), then
$T$ itself is $\VV_i$-concise. 
\end{remark}


% \begin{example}
%     Let $X = \PP(\tspace)$ be the projectivization of the space of tensors. Consider 
%     the family of tensors given by the universal line subbundle
%     \[
%         \OO_X(-1) \hookrightarrow \OO_X \otimes_\kk \tspace.
%     \]
%     Over a $\kk$-point $\langle T\rangle \in X$, the induced map on fibers is the inclusion map
%     \[
%         \OO_X(-1)|_{\langle T\rangle} = \langle T \rangle \hookrightarrow \tspace = 
%         (\OO_X \otimes \tspace)|_{\langle T \rangle}.
%     \]
% \end{example}

\subsection{Unrestriction schemes}

    In this section we define unrestriction schemes. Special cases of these
    serve as smooth ``ambient'' varieties in which concise secant and cactus
    varieties live.

    We need a piece of notation. For a map $\phi\colon \WW_1\to \WW_2$ of vector bundles on $X$, the \emph{zero locus
    of $\phi$} is the closed subscheme $\Z(\phi)$ of $X$ which is locally given by entries of $\phi$, that is,
    for any open $U\subseteq X$ with isomorphisms $(\WW_1)|_U \simeq \OO_U^{\rk
    \WW_1}$, $(\WW_{2})|_U\simeq \OO_U^{\rk \WW_2}$, the ideal of $\Z(\phi)$ is given by the entries of the matrix
    $\phi \in \OO_{U}^{\rk \WW_1 \cdot \rk \WW_2}$.

The following is our main object of interest. Again, we fix an integer $m$, which can be arbitrary, but in applications it will usually
be equal to the border rank.
\begin{definition}[Unrestriction scheme]\label{ref:unrestriction:def}
    Take a family of tensors $T\colon \LL\to \tspacecurly$. Fix an index $i$.
    Take the bundle of Grassmannians $p \colon \Gr_X(m, \VVhat) \to X$ and
    let $\UU_i^{\vee} \into p^*\VVhat$ denote the universal subbundle (the dual is introduced here to keep the notation consistent).
    The \emph{$i$-th unrestriction scheme} of $T$ is the closed subscheme 
    \[
        \begin{tikzcd}
            \unres \ar[rd]\ar[rr, hook, "\mathrm{cl}"] &&\Gr_X(m, \VVhat)\ar[ld, "p"]\\
            & X
        \end{tikzcd}
    \]
    defined as the zero locus of the following map of vector bundles
    \begin{equation}\label{eq:unrestrictionDef}
        p^*(\VV_i^\vee \otimes \LL) \xrightarrow{p^*T_{\VV_i}} p^*\VVhat \to \frac{p^*\VVhat}{\UU_i^{\vee}}.
    \end{equation}
\end{definition}
The unrestriction scheme comes with a $\UU_i$-concise family of tensors
\[
 \Tppar{i}\colon \OO_{\unres} \into p^*\VVhat \otimes \UU_i.
\]
By equation~\eqref{eq:unrestrictionDef}, the contraction
$p^*T_{\VV_i}\colon p^*(\VV_i^{\vee} \otimes \LL)\to p^*\VVhat$ factors through $\UU_i^{\vee}\into p^*\VVhat$,
so $p^*T_{\VV_i}$ induces a uniquely determined map $p^*(\VV_i^{\vee} \otimes \LL) \to \UU_i^{\vee}$. Its dual map
$\varphi_i\colon \UU_i\to p^*(\VV_i \otimes \LL^{\vee})$ shows that $p^*T$ is a restriction of $\Tppar{i}$. This explains
the name $\unres$.

It would be more precise to include $m$ in the notation $\OpUnres_i^m(T)$, yet in our setup $m$ is 
fixed, so we prefer the lighter notation.


\begin{lemma}\label{ref:baseChangeUnres:lem}
    Let $f\colon Y\to X$ be a morphism. Then the pullback $Y\times_X \unres$ is isomorphic to the unrestriction scheme $\unrespar{i}{f^*T}$.
\end{lemma}
\begin{proof}
    Both the bundle of Grassmannians and the condition~\eqref{eq:unrestrictionDef} pull back nicely.
\end{proof}

\begin{example}[Scheme of unrestrictions of a fixed tensor $T$]\label{ex:fibre}
    Let $T\colon \LL\into \tspacecurly$ be a family of tensors.
    Let $x\in X$ be a $\kk$-point and $T|_x\colon \LL|_{x}\into {\VV_1}|_x\otimes \ldots \otimes {\VV_d}|_x$ be the restriction.
    Then the fiber of $\unres \to X$ over $x$ is isomorphic to $\unrespar{i}{T|_x}$.
\end{example}

    Lemma~\ref{ref:baseChangeUnres:lem} yields also the functor of points of $\unres$.
    Namely, for a $\kk$-scheme $S$, a morphism $S\to \unres$ is the same as a morphism $f\colon S\to X$,
    together with a subbundle $\UU_i^{\vee}\into f^*\VVhat{}$ such that $f^*T_{\VV_i}\colon f^*(\LL \otimes \VV_i^{\vee})\to
    f^*\VVhat{}$ factors through $\UU_i^{\vee}$.

    In the following, we obtain another characterisation of the functor of points. In particular, applying $S = \kk$,
    we obtain a description of $\kk$-points.
    \begin{proposition}[Points of unrestriction scheme]\label{ref:functorOfUnrestrictions:prop}
        Let $T\colon \LL\into \tspacecurly$ be a family of tensors on $X$.
        For a $\kk$-scheme $S$, a morphism $S\to\unres$ is the same as a morphism $f\colon S\to X$,
        together with a pair $(U_i, \varphi_i)$, where
        \begin{enumerate}
            \item $U_i$ is a subbundle $U_i^{\vee} \into f^*\VVhat{}$, so it yields an $U_i$-concise tensor
                $\Tppar{i}\colon \OO_S \into U_i \otimes f^*\VVhat{}$,
            \item $\varphi_i$ is a map of vector bundles $\varphi_i\colon U_i \to f^*(\LL^{\vee} \otimes \VV_i)$,
        \end{enumerate}
        such that $\varphi_i(\Tppar{i})$ is equal to $f^*T$ as global sections of $f^*(\LL^{\vee} \otimes \tspacecurly)$.
        These data can be visualised as
        \[
            \begin{tikzcd}
                \Tppar{i} \arrow[r, phantom, "\colon"] \arrow[d, phantom, "\leq" rotate = 90] &[-1cm]
                \OO_S \arrow[d, equal] \arrow[r] &
                f^*\VVhat{}\ar[d, equal] \ar[r, phantom, "\otimes"] &[-0.7cm] U_i \arrow[d, "\varphi_i"] \\
                f^*T \arrow[r, phantom, "\colon"] &
                \OO_S \arrow[r] & f^*\VVhat{} \ar[r, phantom, "\otimes"] & f^*(\VV_i \otimes \LL^\vee).
            \end{tikzcd}
        \]
    \end{proposition}
    \begin{proof}
        From a map $S\to \unres$, we obtain the subbundle $U_i$ by pulling back $\UU_i$ and the map $\varphi_i$ by pulling back
        the map $\varphi_i$ from Definition~\ref{ref:unrestriction:def}. Conversely, having $U_i$, we obtain a morphism
        \[
            \begin{tikzcd}
                S \ar[rr, "\Tppar{i}"]\ar[rd, "f"] && \Gr_X(m, \VVhat{})\ar[ld, "p"]\\
                                      & X
            \end{tikzcd}
        \]
        and $\varphi_i$ shows that it factors through the zero locus defining $\unres{}$.
    \end{proof}
    
    



The construction of unrestrictions can be iterated: from a family of tensors $T$ on $X$,
we obtained a family $\Tppar{1}$ on $\unrespar{1}{T}\xrightarrow{\pi_1} X$ concise on the first coordinate.
We can iteratively consider the unrestriction scheme 
\[
    \unrespar{2}{\Tppar{1}} \xrightarrow{\pi_2} \unrespar{1}{T}
\]
together with the family of tensors $\Tppar{1,2}$. This family is concise on the second coordinate by definition,
but it is also concise on the first coordinate, because its restriction is $\Tppar{1}$, see Remark~\ref{ref:concise:rem}.
% After $i$ steps, we get the scheme 
% $\pi_i \colon \unrespar{i}{\Tppar{1, \dots, i-1}} \to \unrespar{i-1}{\Tppar{1, \dots, i-2}}$
% together with a family of tensor $\Tppar{1, \dots, i}$. 
\begin{definition}
    The $i$-th \emph{iterated unrestriction scheme} of $T$ is the scheme 
    \[
        \unrespar{1, \dots, i}{T} := \unrespar{i}{\Tppar{1, \dots, i-1}}.
    \]
    It comes with a family $\Tppar{1, \ldots , i}$ of tensors which is concise on coordinates $1, \ldots ,i$.
\end{definition}
The iterated unrestriction schemes fit into the following sequence
\[
    \unrespar{1, \dots, i}{T} \xrightarrow{\pi_i} \unrespar{1, \dots, i-1}{T} \xrightarrow{\pi_{i-1}}
    \dots \xrightarrow{\pi_3} \unrespar{1, 2}{T} \xrightarrow{\pi_2} \unrespar{1}{T}
    \xrightarrow{\pi_1} X.
\] 
In particular, we have the \emph{(full) unrestriction scheme} $\unresfullpar{T} := \unrespar{1, \ldots ,d}{T}$ with a concise tensor $\Tppar{}$.
The points of this scheme can be described by iterating Proposition~\ref{ref:functorOfUnrestrictions:prop}.

\subsection{Concise and secant varieties}\label{ssec:conciseSecants}

Having the notion of unrestrictions, we can finally define the objects of main interest: concise secant and cactus varieties.
Consider $m$-dimensional vector spaces $W_1, \ldots ,W_d$ and let $T\in \tconcspace$.
Recall from~\cite{JLP} that the tensor $T$ has \emph{minimal border rank} if $T$ is concise and $\brk T = m$.
\begin{definition}\label{ref:secantLocus:def}    
    Let $T\colon \LL\into \tconcspacecurly$ be a concise (Definition~\ref{ref:concise:def}) tensor on $X$, where every $\WW_i$ has rank $m$.
    \begin{enumerate}
        \item The \emph{minimal border rank locus} is the smallest closed
            subscheme $X^{\brk=m} \subseteq X$ such that for every $x\in
            X^{\brk=m}$, the tensor $T|_x$ has border rank $m$. Observe that $\brk = m$ is the
            minimal possible value given that $T$ is concise.
        \item The \emph{minimal border cactus rank locus} is the smallest closed
            subscheme $X^{\bcrk=m} \subseteq X$ such that for every $x\in
            X^{\bcrk=m}$, the tensor $T|_x$ has cactus border rank $m$. Buczy{\'nski}-Keneshlou~\cite{Buczynski_Keneshlou}
            give a canonical scheme structure on this locus.
    \item
    %     Now let $\WW_1, \ldots ,\WW_d$ be rank $m$ vector bundles and let 
    % $T \colon \LL \into \WW_{1,\dots,d}$ be a concise tensor. 
        Consider the following map of vector bundles
            \[
                \End(\WW_1)\times \ldots \times\End(\WW_d)\to \prod_{i=1}^{d-1} \WW_1\otimes \ldots \otimes \WW_d
            \]
            given by $(X_1, \ldots ,X_d)\mapsto (X_1\circ T - X_i\circ T)_{i=2,
            \ldots ,d}$. The \emph{centroid abundant locus} is the closed
            subscheme of $X$ given as the locus where this map has kernel of rank $\geq m$.
            % This is formally a Fitting ideal \jjeins{details}
        \end{enumerate}
    We say that $T$ \emph{has minimal border rank} / \emph{has minimal border cactus rank} / \emph{is centroid-abundant},
    if respective loci above are equal to the whole $X$.
\end{definition}

\begin{definition}[Concise secant and cactus varieties]\label{ref:conciseSecant:def}
    Let $V_1, \ldots ,V_d$ be vector spaces. Fix an integer $m\geq 1$. Recall that $\Tproj$ denotes the universal tensor 
    over $\mathbb{P}(\tspace)$ and $\Taf$ denotes the universal tensor over $\tspace$, see~Example~\ref{ex:universalFamily}.
    \begin{enumerate}
        \item
            \emph{The $m$-th concise secant variety} $\csigma_m$ is the minimal border rank locus
            for the universal tensor on the unrestriction scheme $\pi\colon \unrespar{}{\Tproj}\to \mathbb{P}(\tspace)$.
            We have $\pi(\csigma_m) = \sigma_m$, where $\sigma_m$ is the $m$-th secant 
            variety of $\Seg \into \PP(\tspace)$. The map $\rho\colon \csigma_m \onto \sigma_m$ is the restriction of $\pi$.
        \item
            \emph{The arithmetic $m$-th concise secant variety}
            $\csigmahat_m$ is the minimal border rank locus
            for the universal tensor on the unrestriction scheme $\pihat\colon \unrespar{}{\Taf}\to \tspace$.
            Again, the restriction of $\pihat$ yields a surjective map $\rhohat\colon \csigmahat_m \onto \sigmahat_m$,
            where $\sigmahat_m$ is the cone over $\sigma_m$.
        \item \emph{The $m$-th concise cactus variety} $\ckappa_m$ is the minimal cactus border rank locus
            for the universal tensor on the unrestriction scheme $\unrespar{}{\Tproj}\to \mathbb{P}(\tspace)$.
            The \emph{$m$-th arithmetic cactus variety} $\ckappahat_m$ is defined analogously.
    \end{enumerate}
    
\end{definition}

        \begin{proof}[Proof of Theorem~\ref{ref:cfit:thm}]
            By construction, the morphism $\rho$ is projective and $B$ acts on the projective scheme $\rho^{-1}([T])$.
            By the Borel Fixed Point Theorem, this action admits a fixed point, which is the required $\Tppar{}$.
        \end{proof}

\begin{example}[Baby case: matrices]
For $d=2$, that is, for matrices, the questions of tensor rank
are quite trivial. This makes it an ideal case for illustrating the new elements of $\csigma_m$.
Fix vector spaces $V_1, V_2$ and consider the determinantal variety
\[
    \sigma_m = \left\{ [M]\in \mathbb{P}(V_1 \otimes V_2)\ |\ \rk M\leq m \right\}.
\]
Take the Grassmannian $\Gr(m, V_2)$ of $m$-dimensional
subspaces of $V_2$ and its universal subbundle $\UU_1^\vee \subseteq \Gr(m,
V_2)\times V_2$. We can form a projective subbundle $\mathbb{P}(V_1\otimes\UU_1^\vee)$ inside
$\mathbb{P}(V_1\otimes V_2) \times \Gr(m, V_2)$, which comes with a map 
$\rho\colon \mathbb{P}(V_1 \otimes \UU_1^\vee)\to \mathbb{P}(V_1\otimes V_2)$.

It will turn out that $\csigma_m$ is $\mathbb{P}(V_1 \otimes \UU_1^\vee)$ in our case.
This is a smooth variety; a projective bundle over $\Gr(r, V_2)$.
To understand it better, we will describe its points (or, to be precise, $\kk$-points).
These are pairs. First, there is a point of the Grassmannian $\Gr(m,
V_2)$,
which we denote by $[U_1^{\vee}]\in \Gr(m, V_2)$. It corresponds to an
injection $U_1^{\vee} \into V_2$, so to a rank $m$ tensor $\Tppar{}\in
U_1\otimes V_2$. Second, there is an element of
$\mathbb{P}(V_1 \otimes \UU_1^\vee)|_{[U_1^{\vee}]}$, that is, a class $[\varphi_1]\in
\mathbb{P}(V_1 \otimes U_1^{\vee})$, where $\varphi_1\colon U_1\to V_1$ is a
nonzero linear map.

The map $\rho$ sends $(\Tppar{}, [\varphi_1])$ to the tensor $[\varphi_1(\Tppar{})]\in \mathbb{P}(V_1 \otimes V_2)$.
The image of $\rho$ is $\sigma_m$. If $V_1, V_2$ are at least $m$-dimensional,
then the map $\rho$ is birational and a resolution of singularities of $\sigma_m$. It is much employed 
in the geometry of syzygies, where it is attributed to Kempf~\cite{Kempf__Images_of_vector_bundles}, see~\cite[(6.1.9)]{Weyman__Cohohomology_of_vector_bundles}.
\end{example}


\subsection{Structure of unrestrictions and $\csigma_m$ over $\mathbb{P}(\tspace)$ and $\tspace$}

    In this section we discuss group actions and bundles which appear on unrestrictions starting from
    the ``universal'' tensors over $\mathbb{P}(\tspace)$ and $\tspace$. These structures appears essentially
    because $\tspace$ is a trivial vector bundle.


    Let $\Taf\colon \OO_{\tspace}\to \OO_{\tspace} \otimes \tspace$ be the universal tensor over $\tspace$ and let
    \[
        \unresfullpar{\Taf}\to \ldots \to \unrespar{1}{\Taf} \to \tspace.
    \]
    be its unrestriction schemes. Similarly, let $\Tproj\colon \OO_{\mathbb{P}(\tspace)}(-1) \into
    \OO_{\mathbb{P}(\tspace)}\otimes\tspace$ be the universal tensor of
    $\mathbb{P}(\tspace)$ and let 
    $
    \unresfullpar{\Tproj}\to \ldots \to \unrespar{1}{\Tproj} \to \mathbb{P}(\tspace)
    $ be its unrestriction schemes.

    \subsubsection{Group actions}\label{ssec:groupActions}

        Let $\GLV := \GL(V_1)\times \ldots \times \GL(V_d)$ be the general linear group.
        It acts naturally on $\tspace$ and on $\Vhatpar{1} = V_2 \otimes \dots \otimes V_d$, hence it acts on $\Gr(m, \Vhatpar{1}) \times \tspace$.
        The action restricts to $\unrespar{1}{\Taf}$ and makes $\unrespar{1}{\Taf}\to \tspace$
        into a $\GLV$-equivariant map. The action of $\GLV$ on $\Vhatpar{1}$ gives an action of $\GLV$ 
        on the (trivial) bundle $\OO_{\unrespar{1}{\Taf}}\otimes \Vhatpar{1}$. This action preserves the universal subbundle,
        hence induces a linearisation of the universal subbundle. Therefore we obtain an action on the Grassmannian bundle over
        $\unrespar{1}{\Taf}$ and on its subscheme $\unrespar{2}{\Taf}$. Continuing, we obtain $\GLV$-actions on 
        all unrestriction schemes $\unrespar{i}{\Taf}$ such that the restriction maps
        $\unresfullpar{\Taf}\to \ldots \to \unrespar{1}{\Taf}\to \tspace$ are equivariant.

        The argument can be repeated in the projective setting. There is one difference though. The action of scalar
        matrices $\Gmult^d \subseteq \GLV$ on $\mathbb{P}(\tspace)$ is trivial and so is their action on $\Gr(m, \Vhatpar{1})$. By induction,
        we conclude that $\Gmult^d$ acts trivially. In practice, it is hence reasonable to restrict to the action of $\SLV$ in the projective
        setting.

        One could ask, if there is a bigger connected group acting. The answer
        is expected to be negative in many cases. Indeed,
        if $\rho$ is birational, then a connected group action on $\csigma_m$
        descends to one on the normalisation of $\sigma_m = \rho(\csigma_m)$,
        see~\cite[Proposition~2.25]{Brion}. This is the case when $\dim
        V_{\bullet} = m$, but also in much larger number of cases discussed
        in~\S\ref{ssec:identifiability}.
        

    \subsubsection{Bundles}
    Recall that $\Vhatpar{1} = V_2 \otimes \ldots \otimes V_d$ and
    consider the Grassmannian $\Gr(m, \Vhatpar{1})$ with its universal tensor $\TGr$,
    see Example~\ref{ex:universalFamily}. Note that the tensor $\TGr$ is concise on the first coordinate.
    Let $\unresfullpar{\TGr} = \unrespar{2, \ldots ,d}{\TGr}\to \Gr(m, \Vhatpar{1})$ be its unrestriction scheme.
    % Let $\Taf\colon \OO\to \OO \otimes \tspace$ be the universal tensor over $\tspace$ and let
    % \[
    %     \unresfullpar{\Taf}\to  \ldots \to \unrespar{1}{\Taf} \to \tspace.
    % \]
    % be its unrestriction scheme.
    \newcommand{\ehat}{\widehat{e}}

    The scheme $\unrespar{1}{\Taf}$ is closed inside $\tspace \times \Gr(m, \Vhatpar{1})$, 
    so there is a natural
    \[\ehat\colon \unrespar{1}{\Taf} \to \Gr(m, \Vhatpar{1}).
    \] 
    By construction, we have that the universal tensor $\Tppar{1}$ on $\unrespar{1}{\Taf}$ 
    is the pullback $\ehat^* \TGr$, see Definition~\ref{ref:unrestriction:def}. 


    \begin{proposition}[Unrestriction scheme as a bundle]\label{ref:bundleAffine:prop}
        The morphism $\ehat$ makes $\unrespar{1}{\Taf}$ into a vector bundle of rank $m^2$ over $\Gr(m, \Vhatpar{1})$, more precisely
        it is the bundle $\UU_1^{\vee}\otimes V_1$, where $\UU_1^{\vee}$ it the universal subbundle.
        The diagram
        \begin{equation}\label{eq:unresBundle}
            \begin{tikzcd}
                \unresfullpar{\Taf} \ar[r]\ar[d] & \unresfullpar{\TGr}\ar[d]\\
                \unrespar{1}{\Taf} \ar[r, "\ehat"] & \Gr(m, \Vhatpar{1})
            \end{tikzcd}
        \end{equation}
        is cartesian, so $\unresfullpar{\Taf}\to \unresfullpar{\TGr}$ is also a vector bundle of rank $m^2$.
    \end{proposition}
    Observe that $\unresfullpar{\TGr}$ is a projective variety, while $\unresfullpar{\Taf}\to \unresfullpar{\TGr}$ is affine, so
    the above precisely measures the lack of projectivity of $\unresfullpar{\Taf}$.

    \begin{proof}
        The map $\varphi_1$ from Definition~\ref{ref:unrestriction:def} yields a map from $\unrespar{1}{\Taf}$ to
        the bundle $\UU_1^{\vee}\otimes V_1$. Conversely, from an element of $\UU_1^{\vee}\otimes V_1$, we obtain a map $\varphi_1\colon \UU_1\to V_1$
        and using the description in Proposition~\ref{ref:functorOfUnrestrictions:prop}, a map $\UU_1^{\vee}\otimes V_1\to \unrespar{1}{\Taf}$.
        This proves the first part.

        The tensor $\Tppar{1}$ on $\unrespar{1}{\Taf}$ is a pullback via $\ehat$ of the tensor $\TGr$ on $\Gr(m, \Vhatpar{1})$.
        By assuming that the diagram~\eqref{eq:unresBundle} is cartesian, we can apply the base change Lemma~\ref{ref:baseChangeUnres:lem} to conclude that the diagram~\eqref{eq:unresBundle} is indeed cartesian.
    \end{proof}
    % Similarly, let $\Tproj\colon \OO(-1) \into \OO_{\mathbb{P}(\tspace)}\otimes\tspace$ be the universal tensor of $\mathbb{P}(\tspace)$
    % and let $\unresfullpar{\Tproj}\to \unrespar{1}{\Tproj} \to \mathbb{P}(\tspace)$ be its unrestrictions.
    In the projective case, the variety $\unrespar{1}{\Tproj}$
    comes with a natural map
    \[e\colon \unrespar{1}{\Tproj}\to \Gr(m, \Vhatpar{1}).\]
    \begin{proposition}\label{ref:bundleProjective:prop}
        The morphism $e$ makes $\unrespar{1}{\Tproj}$ into a projectivisation of vector bundle of rank $m^2$ over $\Gr(m, \Vhatpar{1})$, more precisely
        it is the bundle $\mathbb{P}(\UU_1^{\vee}\otimes V_1)$, where $\UU_1^{\vee}$ it the universal subbundle.
        The diagram
        \[
            \begin{tikzcd}
                \unresfullpar{\Tproj} \ar[r]\ar[d] & \unresfullpar{\TGr}\ar[d]\\
                \unrespar{1}{\Tproj} \ar[r, "e"] & \Gr(m, \Vhatpar{1})
            \end{tikzcd}
        \]
        is cartesian, so $\unresfullpar{\Tproj}\to \unresfullpar{\TGr}$ is also a projectivised vector bundle of rank $m^2$.
    \end{proposition}
    \begin{proof}
        The argument mirrors Proposition~\ref{ref:bundleAffine:prop}, so we repeat the argument. The only difference is that we obtain a restriction map
        $\varphi_1\colon \UU_1 \to V_1\otimes \OO(1)$, hence a surjection $\UU_1\otimes V_1^{\vee}\to \OO(1)$, which implies that $\unresfullpar{\Tproj}$ is an affine bundle over $\unresfullpar{\TGr}$.
    \end{proof}

    
    
    
    




\subsection{Framed unrestrictions}\label{ssec:framedUnrestrictions}

Sometimes, it may be useful to work with ``usual'' tensors, that is, elements of a fixed vector space $W_1\otimes \ldots \otimes W_d$ rather than 
of a nontrivial vector bundle. This can be achieved naturally using framings. The result is the framed unrestriction scheme defined below.
The price paid is that the framed unrestriction scheme is no longer projective over the base scheme.

Recall that for a scheme $X$ and vector bundles $\VV'$, $\VV''$ of rank $m$ on $X$, there is a
principal $\GL_{m}$-bundle $\Iso(\VV', \VV'') \to X$ such that for any $\phi\colon S\to X$, the morphisms
$S\to \Iso(\VV', \VV'')$ over $X$ are in bijection with isomorphisms $\phi^*\VV'\to \phi^*\VV''$. It is called the \emph{bundle of isomorphisms}.
In the special case when $\VV' = \OO_X\otimes W$, the variety $\Iso(\VV', \VV'')\to X$ is a $\GL(W)$-bundle.
The bundles of isomorphisms can be applied very generally. To stay focused, we apply it only for the full unrestriction scheme.
Let $\GLW := \GL(W_1)\times \ldots \times\GL(W_d)$.

\begin{definition}
    Fix $m$-dimensional $\kk$-vector spaces $W_1$, \ldots ,$W_d$. 
    Let $T\colon \LL\to \VV_1 \otimes \ldots \otimes \VV_d$ be a
    tensor on $X$ and let $\Xppar{} :=\unresfullpar{T}$ be its full
    unrestriction scheme,
    with a tensor $\Tppar{}\colon \OO_{\Xppar{}} \into \UU_1\otimes \ldots \otimes \UU_d$.
    The \emph{framed unrestriction scheme} of $T$ is the principal $\GLW$-bundle
    \[
        \unresfrfull := \prod_{i=1}^d \Iso_{\Xppar{}}(\OO_{\Xppar{}}\otimes W_i, \UU_i) \xrightarrow{\upsilon} \Xppar{}.
    \]
\end{definition}
On the framed unrestriction scheme, we have in particular canonical isomorphisms
\[
    u_i\colon \OO_{\unresfrfull} \otimes W_i \to \upsilon^*\UU_i,
\]
so the family of tensors $\upsilon^*\Tppar{}$ yields a family of tensors
\[
    \Tpparfr{}\colon \OO_{\unresfrfull}\into \OO_{\unresfrfull}\otimes W_1\otimes \ldots \otimes W_d.
\]

Let us now describe the points of $\unresfrfull{}$.
\begin{proposition}\label{ref:framedUnrestrictionPoints:prop}
    Let $S$ be an $\kk$-scheme with a morphism $f\colon S\to X$. Morphisms
    $S\to \unresfrfull$ over $X$ are in bijection with tuples $(\Tpparfr{},
    \varphifr_{1}, \ldots , \varphifr_d)$, where $\Tpparfr{}\colon \OO_S\into \OO_S\otimes W_1\otimes
    \ldots \otimes W_d$ is a tensor, $\varphifr_1\colon \OO_S\otimes W_1 \to f^*(\VV_1\otimes \LL^\vee)$,
    $\varphifr_2\colon \OO_{S}\otimes W_2 \to f^*\VV_2$, \ldots , $\varphifr_{d}\colon \OO_S \otimes W_d\to f^*\VV_d$ are
    maps of bundles. These are required to satisfy the following condition:
    \begin{align}\label{eq:starCondition}
        \Tpparfr{} & \mbox{ is } W_1\text{-}, \ldots , W_{d-2}\text{-}, W_{d-1}\text{-}, W_d\text{-concise}\\\notag
        \varphifr_d(\Tpparfr{}) & \mbox{ is } W_1\text{-},
        \ldots , W_{d-2}\text{-}, W_{d-1}\text{-concise}\\\notag
        \varphifr_{d-1}\circ{}\varphifr_d(\Tpparfr{}) & \mbox{ is } W_1\text{-},
        \ldots , W_{d-2}\text{-concise}\\\notag
         \ldots \\\notag
         \varphifr_2\circ{} \ldots \varphifr_{d-1}\circ{} \varphifr_d(\Tpparfr{}) & \mbox{ is } W_1\text{-concise}\\\notag
         \varphifr_1\circ{} \varphifr_2\circ{} \ldots \varphifr_{d-1}\circ{}\varphifr_d(\Tpparfr{}) &= T.
    \end{align}
\end{proposition}
The conciseness conditions above are redundant: if a restriction of a tensor is, say, $W_1$-concise, then the tensor
itself is $W_1$-concise. Therefore, it is enough to require that $\Tpparfr{}$ is $W_d$-concise, $\varphifr_d(\Tpparfr{})$ is $W_{d-1}$-concise,
\ldots, $\varphifr_2\circ \ldots \circ \varphifr_{d-1}(\Tpparfr{})$ is $W_1$-concise.
\begin{proof}
    A morphism $\phi\colon S\to \unresfrfull$ yields a morphism $f\colon S\to X$ and a morphism $S\to \Xppar{} = \unrespar{1, \ldots ,d}{T}$ over $X$.
    By pulling back respective universal bundles, the latter yields
    \begin{enumerate}
        \item a subbundle $U_1^{\vee}\into f^*(\VV_2 \otimes \ldots \otimes \VV_d)$,
        \item a subbundle $U_2^{\vee}\into U_1\otimes f^*(\VV_3 \otimes \ldots \otimes \VV_d)$,
        \item and so on, all the way to
        \item a subbundle $U_d^{\vee}\into U_1\otimes  \ldots \otimes U_{d-1}$,
            this last one yielding a tensor denoted by $\Tppar{}|_S \colon \OO_S \into \OO_S \otimes U_1 \otimes \ldots \otimes U_d$,
    \end{enumerate}
    together with restriction maps $\varphi_1\colon U_1\to f^*(\VV_1 \otimes
    \LL^{\vee})$ and $\varphi_i\colon U_i\to f^*\VV_i$ for $i=2, \ldots , d$, such that
    $\varphi_1\circ \ldots \circ \varphi_d(\Tppar{}|_S) = T$.
    By the properties of the bundles of isomorphisms, the morphism $\phi\colon S\to \unresfrfull$ additionally yields isomorphisms
    $(u_i)|_S\colon \OO_S\otimes W_i\to U_i$.
    Now, the compositions $\varphi_i \circ (u_i)|_S$ give the maps $\varphifr_i$ from the statement, for $i=1, \ldots ,d$, while
    $((u_1)|_S)^{-1}\circ \ldots ((u_d)|_S)^{-1}\Tppar{}|_S$ yields $\Tpparfr{}$.
    The fact that respective $U_i^{\vee}$ are subbundles becomes equivalent to the required conciseness conditions.
    This gives one direction.

    The argument can be reversed, as follows. Suppose we are given $(\Tpparfr{}, \varphifr_1, \ldots ,\varphifr_d)$.
    Let
    \[
        \Tpparfr{}_{\leq i} := (\varphi_{i+1}\circ{} \ldots \circ{}
        \varphi_d)(\Tpparfr{})\colon \OO_S \into W_1\otimes
        \ldots \otimes W_i\otimes_{\kk} f^*\VV_{i+1}\otimes \ldots \otimes
        f^*\VV_d
    \]
    be the restriction. The tensor $\Tpparfr{}_{\leq 1}$ is $W_1$-concise, hence yields a subbundle
    $\OO_S \otimes W_1^{\vee}\into f^*\VV_{2}\otimes \ldots \otimes f^*\VV_d$. To be formal, denote by $U_1^{\vee}$ the image of this 
    and by $(u_1)|_S^{\vee}\colon \OO_S \otimes W_1^{\vee}\to U_1^{\vee}$ the isomorphism to the image, so that
    $(u_1)|_S\colon \OO_S \otimes W_1 \to U_1$ is also an isomorphism of vector bundles. Let
    \[
        \varphi_1 := (u_1)|_S^{-1} \circ \varphifr_1\colon U_1\to f^*(\VV_1 \otimes \LL^\vee).
    \]
    Having done this, the next steps follow by induction. Suppose we constructed $U_j^{\vee}$, $\varphi_j$, $(u_j)|_S$ for $j=1, \ldots , i-1$.
    To construct $U_i^{\vee}$, we assume $U_i = U_{i-1}$ and use $u_1, \ldots ,u_{i-1}$ to translate the tensor $\Tpparfr{}_{\leq i}$ to a tensor in
    \[
        U_1\otimes \ldots \otimes U_{i-1}\otimes (\OO_S \otimes W_i)\otimes f^*(\VV_{i+1}\otimes \ldots \otimes \VV_d).
    \]
    We obtain also a concise tensor $\Tppar{}\in U_1\otimes \ldots \otimes U_d$ from $\Tpparfr{}$ and $u_1, \ldots ,u_d$.
    By repetitive applications of Proposition~\ref{ref:functorOfUnrestrictions:prop}, the tuple $(\Tppar{}, \varphi_1, \ldots ,\varphi_d)$ yields
    a map $S\to \unresfullpar{T}$. The isomorphisms $(u_1)|_S$, \ldots, $(u_d)|_S$ then yield a map to $\unresfrfull$.
\end{proof}

\begin{definition}\label{def:framed_concise_secant}
    Let $V_1, \ldots ,V_d$ be vector spaces. Fix an integer $m\geq 1$. Recall that $\Tproj$ denotes the universal tensor 
    over $\mathbb{P}(\tspace)$ and $\Taf$ denotes the universal tensor over $\tspace$. 
    \begin{enumerate}
        \item
            \emph{The $m$-th framed concise secant variety} $\csigmafr_m$ is the minimal border rank locus
            on the framed unrestriction scheme 
            $\upsilon \colon \unresfrfullpar{\Tproj} \to \unresfullpar{\Tproj}$.
            Since the universal tensor on $\unresfrfullpar{\Tproj}$ is a pullback of the one on $\unresfullpar{\Tproj}$,
            we have $\csigmafr_m = \upsilon^{-1}(\csigma_m)$,
            and hence $\upsilon$ restricts to a smooth surjective map $\csigmafr_m\onto \csigma_m$.
            % Equivalently, it is the preimage of the minimal border rank locus 
            % $\upsilon^{-1}(\unresfullpar{\Tproj}^{\brk = m}) \subset  \unresfrfullpar{\Tproj}$.
        \item
            \emph{The $m$-th framed arithmetic concise secant variety} $\csigmahatfr_m$ is the minimal border rank locus
            on the framed unrestriction scheme 
            $\upsilon \colon \unresfrfullpar{\Taf} \to \unresfullpar{\Taf}$.
            Since the universal tensor on $\unresfrfullpar{\Taf}$ is a pullback of the one on $\unresfullpar{\Taf}$,
            we have $\csigmahatfr_m = \upsilon^{-1}(\csigmahat_m)$,
            and $\upsilon$ restricts to a smooth surjective map $\csigmahatfr_m\onto \csigmahat_m$.
    \end{enumerate}
\end{definition}

\subsection{Geometric interpretation of the algorithm from \S\ref{sec:unrestrictions}}\label{sec:unrestrictions_geometric}
In this section, we explain the geometry behind the algorithm from Proposition~\ref{p:algorithm_segre}
using concise secant varieties. 
\smallskip

Let $T \in \sigmahat_m$ be a tensor of border rank $\leq m$ and let $T_t \in \tspace[\![t]\!]$ 
be a degeneration of border rank $\leq m$ tensors to $T$ with general tensor $T_{t \neq 0}$ concise.
This is the data of a morphism
\[T_t \colon \Spec \kk[\![t]\!] \to \sigmahat_m \subset \tspace\]
such that $T_{t \neq 0} \colon \Spec \kk(\!(t)\!) \to \sigmahat_m$
factors through the embedding of the concise locus $\sigmahat_m^{\mathrm{conc}} \subset \sigmahat_m$ 
\[
\begin{tikzcd}
    \Spec \kk(\!(t)\!) \arrow[d, hook] \arrow[r, "T_{t \neq 0}"] & \sigmahat_m^\mathrm{conc} \arrow[d, hook] \\
    \Spec \kk[\![t]\!] \arrow[r, "T_t"] & \sigmahat_m 
\end{tikzcd}
\]
and $T_{t = 0} \colon \Spec \kk \to \sigmahat_m$ corresponds to $T$.
Consider the concise secant variety $\csigmahat_m$ together with the map $\rhohat \colon \csigmahat_m \to \sigmahat_m$,
see Definition~\ref{ref:conciseSecant:def}. 
The map $\sigmahat$ is an isomorphism over $\sigmahat_m^{\mathrm{conc}}\subset \sigmahat_m$, 
so we can view the general tensor
as a morphism $T_{t \neq 0} \colon \Spec \kk(\!(t)\!) \to \rhohat^{-1}(\sigmahat_m^{\mathrm{conc}}) \subset \csigmahat_m$,
so that we have the following commutative diagram:
\[
\begin{tikzcd}
    \Spec \kk(\!(t)\!) \arrow[d] \arrow[r, "T_{t \neq 0}"] & \csigmahat_m \arrow[d, "\rhohat"] \\
    \Spec \kk[\![t]\!] \arrow[r, "T_t"] & \sigmahat_m 
\end{tikzcd}
\]
The morphism $\rhohat$ is projective, so and hence proper, so by the valuative criterion for properness 
there exists a unique lift 
\begin{equation}\label{eq:lift_cisgma}
\begin{tikzcd}
    \Spec \kk(\!(t)\!) \arrow[d] \arrow[r, "T_{t \neq 0}"] & \csigmahat_m \arrow[d, "\rhohat"] \\
    \Spec \kk[\![t]\!] \arrow[r, "T_t"] \arrow[ru, "\exists!"] & \sigmahat_m 
\end{tikzcd}
\end{equation}
This morphism corresponds to a degeneration of unrestrictions 
\[
    (\Tppar{}_t, (\varphi_1)_t, \dots, (\varphi_d)_t) \colon 
    \Spec \kk[\![t]\!] \to \csigmahat_m.
\]
This is the unique degeneration of unrestrictions that extends the degeneration $T_t$.
For $t=0$, we obtain a minimal border rank unrestriction 
$(\Tppar{}, \varphi_1, \dots, \varphi_d)\in \csigmahat_m$ of the tensor $T$ 
that is uniquely determined by the choice of a degeneration $T_t$.

Let us compare it to the algorithmic proof of Proposition~\ref{p:algorithm_segre}.
Recall that the algorithm takes a degeneration
$T_t \colon \Spec\kk[\![t]\!] \to \sigmahat_m$ and produces a degeneration 
$\Tppar{}_t \colon \Spec\kk[\![t]\!] \to \sigmahat_m$ together with degenerations of restriction maps 
$(\varphi_1)_t, \ldots, (\varphi_d)_t$
by iteratively applying the construction described in the proof of Lemma~\ref{l:algorithm_step}.
Geometrically, the algorithm yields an explicit lift
\begin{equation}\label{eq:lift_csigmafr}
\begin{tikzcd}
     & \csigmahatfr_m \arrow[d, "\upsilon"] \\
     & \csigmahat_m \arrow[d, "\rhohat"] \\
    \Spec \kk[\![t]\!] \arrow[ruu]\arrow[r, "T_t"] & \sigmahat_m
\end{tikzcd}
\end{equation}
A choice of a degeneration $T_t$ does not uniquely determine an unrestriction because 
each step of the algorithm involves a choice of bases and a choice of a minor of the matrix 
describing the flattening of the degeneration obtained in the previous step. 
On the geometric side, this is reflected by the fact that the composite map $\rhohat \circ \upsilon$
is not proper, so there is no reason for a lift as in~\eqref{eq:lift_csigmafr} to be unique.
However, every such lift has the property that the composite map 
$\Spec \kk[\![t]\!] \to \csigmahat_m$ gives a lift as in~\eqref{eq:lift_cisgma},
which is unique. This shows that any degeneration of unrestrictions produced by the algorithm from 
Proposition~\ref{p:algorithm_segre} gives the same isomorphism class in $\csigmahat_m(\kk[\![t]\!])$.
The result below formalizes these observations.
\begin{proposition}\label{prop:uniqueness_of_unres}
    Let $T \in \sigmahat_m \subset \tspace$ be a tensor of border rank $\leq m$. 
    Fix a degeneration of border rank $\leq m$ tensors $T_t \colon \Spec\kk[\![t]\!] \to \sigmahat_m$ 
    to $T$ such that the general tensor is $T_{t \neq 0}$ concise. 
    Consider any two unrestrictions 
    \[
    (\Tppar{}, \varphi_1, \dots, \varphi_d)\quad\text{and}\quad (\Tppar{'}, \varphi_1', \dots, \varphi_d')
    \] 
    constructed from $T_t$ using the algorithm from Proposition~\ref{p:algorithm_segre},
    but for different choices of bases and minors.
    Then there exists linear isomorphisms $\psi_i \colon V_i \to V_i$ such that 
    \[
        \Tppar{'} = \psi_{1,\dots,d}(\Tppar{}) \quad\text{and}\quad \varphi_i' = \varphi_i \circ \psi_i^{-1} \quad\text{for every} \quad i=1,\dots,d.
    \]
\end{proposition}
\begin{proof}
    Recall that $W_1, \dots, W_d$ are the $m$-dimensional vector spaces from the definition of 
    framed concise secant variety, see Definition~\ref{def:framed_concise_secant}.
    Fix bases of $W_1, \dots, W_d$. At the first step, the algorithm fixes a basis of $V_1$ and 
    produces a $V_1$-concise degeneration of tensors 
    $\Tppar{1}_t \colon \Spec \kk[\![t]\!] \to \sigmahat_m \subset \tspace$ and a degeneration of maps 
    $(\varphi_1)_t \colon \Spec \kk[\![t]\!] \to \End(V_1)$ such that 
    $(\varphi_1)_t(\Tppar{1})_t = T_t$. We work in bases, so we can view $(\Tppar{1}_t, (\varphi_1)_t)$
    as a map $\Spec \kk[\![t]\!] \to W_1 \otimes V_{2,\dots,d} \times \Hom(W_1, V_1)$.
    By iterating this procedure, we obtain a map 
    \[
        (\Tppar{}_t, (\varphi_1)_t, \dots, (\varphi_d)_t) \colon \Spec \kk[\![t]\!] \to \csigmahatfr_m \subset W_{1,\dots,d}\times \prod_{i=1}^d \Hom(W_i, V_i).
    \]
    By construction, the composite map $\upsilon \circ (\Tppar{}_t, (\varphi_1)_t, \dots, (\varphi_d)_t)
    \colon \Spec \kk[\![t]\!] \to \csigmahat_m$ is a lift as in~\eqref{eq:lift_cisgma}.
    Since $\rhohat$ is not proper, such a lift is never unique, so $\upsilon \circ (\Tppar{}_t, (\varphi_1)_t, \dots, (\varphi_d)_t)$
    depends on all choices made in the algorithm. However, any two unrestrictions 
    $(\Tppar{}, \varphi_1, \dots, \varphi_d), (\Tppar{'}, \varphi_1', \dots, \varphi_d')$
    constructed from $T_t$ lie in the same fiber of $\upsilon$. The map $\upsilon$ is a principal
    $\GLW$-bundle, so any two unrestrictions in the same fiber differ by some $(\psi_1, \dots, \psi_d) \in \GLW$.
\end{proof}


\subsection{Smooth equivalences}\label{ssec:smoothEquivalences}
The most important consequence of
Proposition~\ref{ref:framedUnrestrictionPoints:prop} is that it allows us to reduce to the usual setup as follows.
Let $\Taf$ be the universal tensor on $\tspace$ and $\unresfrfullpar{\Taf}\to \tspace$ be the framed unrestriction scheme.
For a $\kk$-scheme $S$, to have a morphism $S\to
\tspace$ is the same as to have a tensor $T = \Taf|_S\colon \OO_S\to
\OO_S\otimes \tspace$. Therefore, the functor of points of $\unresfrfullpar{\Taf}$ simplifies:
we can forget the map $S\to X$ \emph{and} the last condition in~\eqref{eq:starCondition}. This means
that $\unresfrfullpar{\Taf}$ parameterises tuples $(\Tpparfr{}, \varphifr_1, \ldots ,\varphifr_d)$ where
$\Tpparfr{}$ is a concise tensor and $\varphifr_i\colon W_i\to V_i$ are
arbitrary restrictions (for $i=1, \ldots ,d$) that satisfy conciseness conditions
from~\eqref{eq:starCondition} without the last one. Therefore, the scheme
$\unresfrfullpar{\Taf}$ is an open subscheme of the affine space
\[
    \tconcspace \times \Hom(W_1, V_1)\times \ldots \times  \Hom(W_d, V_d).
\]
Let us denote the projection $\unresfrfullpar{\Taf}\to \tconcspace$ by $\alphahat$.
Let us denote by $\tconcspaceconc$ the open subvariety of $\tconcspace$ that parameterises
concise tensors.
We obtain the \emph{affine smooth equivalence} diagram
\begin{equation}\label{eq:smoothEquivalenceFramed}
    \begin{tikzcd}
        & \unresfrfullpar{\Taf} \ar[rd, "\alphahat", "\mathrm{sm}"']\ar[ld, two heads, "\upsilon"', "\mathrm{sm}"]\\
        \unresfullpar{\Taf} && \tconcspaceconc.
    \end{tikzcd}
\end{equation}
The map $\alphahat$ is smooth as a projection, while $\upsilon$ is smooth as a structure map of a principal $\GLW$-bundle.
The family of tensors $\Tpparfr{}$ on $\unresfrfullpar{\Taf}$ is defined as the
pullback $\upsilon^*\Tppar{}$.  Moreover, by the construction of the framed
concise secant variety, we obtain $\upsilon^*\Tppar{} \simeq \Tpparfr{} = \alphahat^*\Taf_W$.


An important consequence is of smooth equivalence is the smoothness of full unrestriction schemes for universal tensors on $\tspace$ and $\mathbb{P}(\tspace)$.
\begin{corollary}[Smoothness of universal unrestrictions]\label{ref:unrestrictionSmoothness:cor}
    Let $\Taf$, $\Tproj$ be the usual universal tensors on $\tspace$ and $\mathbb{P}(\tspace)$, respectively.
    The schemes $\unresfullpar{\Taf}$, $\unresfullpar{\Tproj}$ are smooth.
    Moreover, the fibre $\unresfullpar{\Taf} \to \tspace$ over $0\in \tspace$ is smooth.
\end{corollary}
\begin{proof}
    The smoothness of $\unresfullpar{\Taf}$ follows directly from~\eqref{eq:smoothEquivalenceFramed}.
    Propositions~\ref{ref:bundleAffine:prop}-\ref{ref:bundleProjective:prop} show that
    $\unresfullpar{\Tproj}$ is a projectivisation of a total space of vector bundle $\unresfullpar{\Taf}$, hence it is singular
    at the zero section. The fibre of $\unresfullpar{\Taf}\to \tspace$ over $0$ is the zero section of the aforementioned vector bundle, hence is singular
    as well.
\end{proof}

\begin{example}\label{ex:fibres}
    \def\bfP{\mathbf{P}}
    In general, it is not true that the unrestriction scheme of any tensor is smooth.
    To show this, by Example~\ref{ex:fibre}, it is enough to show that a fiber of 
    $\pihat\colon \unresfullpar{\Taf}\to \tspace$ over some tensor is not smooth. 
    
    Take $d =3$, $\dim V_\bullet = 2$ and let $T \in V_{1,2,3}$ be a rank one tensor.
    The fiber $\pihat_1^{-1}(T) \subset \Gr(2, V_2 \otimes V_3)$ is isomorphic 
    to the projective plane $\bfP = \PP((V_2 \otimes V_3) / \spann{T(V_1^\vee)})$. 
    There is one point $x_2 \in \pihat_1^{-1}(T)$ such that $\Tppar{1}|_{x_2}$ 
    is not $V_2$-concise and another point $[x_3]$ such that $\Tppar{1}|_{x_3}$ 
    is not $V_3$-concise. Similarly as above, the fibers of $\pihat_2 \circ \pihat_3$ over 
    $x_2$ and $x_3$ are projective planes $\bfP_2, \bfP_3$. Summing up, $\pihat^{-1}(T)$ 
    consists of three projective planes $\bfP, \bfP_2, \bfP_3$ glued by identifying points 
    $x_2' \in \bfP_2$, $x_3'\in \bfP_3$ with points $x_2, x_3 \in \bfP$. 
\end{example}

Another consequence, which is crucial to this article, is that the singularities of $\csigmahat_m$, $\csigma_m$
are smoothly equivalent to the singularities of the \emph{concise locus} of $\sigmahat_m$.
The concise locus is much better behaved than the whole variety $\sigmahat_m$.
Below we use the framed minimal border rank loci, see
Definition~\ref{def:framed_concise_secant}.


\begin{theorem}\label{ref:SmoothEquivalenceCsigmahat:thm}
    The diagram~\eqref{eq:smoothEquivalenceFramed} restricts to a smooth equivalence
    \begin{equation}\label{eq:smoothEquivalenceCsigmahat}
        \begin{tikzcd}
%         & \csigmahatfr_m \ar[rd, "\alphahat", "\mathrm{sm}"']\ar[ld, two heads, "\upsilon"', "\mathrm{sm}"]\\
        & \csigmahatfr_m \ar[rd, "\alphahat", "\mathrm{sm}"']\ar[ld, two heads, "\upsilon"', "\mathrm{sm}"]\\
            \csigmahat_m && \sigmahat_m^{\mathrm{conc}}
        \end{tikzcd}
    \end{equation}
    where $\csigmahatfr_m \subset \unresfrfullpar{\Taf}$ is the minimal border rank locus (Definition~\ref{def:framed_concise_secant}) and $\sigmahat_m^{\mathrm{conc}}\subseteq \tconcspaceconc$
    is the concise locus of the secant variety inside $\tconcspace$.
\end{theorem}
\begin{proof}
    By Definition~\ref{ref:secantLocus:def}, the variety $\sigmahat_m^{\mathrm{conc}}$ is equal to $(\tconcspaceconc)^{\brk = m}$ and the variety $\csigmahat_m$
    is equal to $\unresfullpar{\Taf}^{\brk =m}$.
    Since we assume that $\upsilon$ is a smooth map $\csigmahatfr_m\to \csigmahat_m$, we have that
    \[
        \csigmahatfr_m = (\unresfrfullpar{\Taf})^{\brk=m} = \upsilon^{-1}((\unresfullpar{\Taf})^{\brk = m}),
    \]
    which confirms that $\upsilon$ restricts to a smooth map $\csigmahatfr_m\to \csigmahat_m$. The tensor
    on $(\unresfrfullpar{\Taf})$ is also isomorphic to the pullback of the tensor on $\tconcspaceconc$, so the same argument yields that
    \[
        \csigmahatfr_m = \alphahat^{-1}((\tconcspaceconc)^{\brk = m}) = \alphahat^{-1}(\sigmahat_m^{\mathrm{conc}}).\qedhere
    \]
\end{proof}

We can repeat the procedure for the projective versions. Actually, there are two strategies to do this.
First, by Propositions~\ref{ref:bundleAffine:prop}-\ref{ref:bundleProjective:prop}, we know that $\unresfullpar{\Tproj}$
is a free quotient by $\Gmult$ of an open subset of $\unresfullpar{\Taf}$ and one can obtain the smooth equivalence
by quotienting out~\eqref{eq:smoothEquivalenceFramed}.
We take a different route, mostly to show that the result is obtained purely from the general theory.

Consider $\unresfrfullpar{\Tproj}$. Proposition~\ref{ref:framedUnrestrictionPoints:prop} yields its functor of points.
Once again, for a morphism $f\colon S\to \unresfrfullpar{\Tproj}$, we obtain in
particular a tensor $T\colon f^*\OO(-1)\to \tspace$, a $W_2$-concise tensor $T' := \varphifr_2\circ \ldots
\circ\varphifr_d(\Tpparfr{})$ and a restriction
map $\varphifr_1\colon \OO_S\otimes W_1\to f^*\OO(1)\otimes V_1$ such that $\varphifr_1(T') = T$. The contraction $(T')_1^{\vee}$ is a surjective map
$\Vhatpar{1}^{\vee}\onto W_1$. Together with $\varphifr_1$ it yields a surjection
\[
    \OO_S \otimes \tspace^{\vee} = \OO_S\otimes V_1^{\vee}\otimes \Vhatpar{1}^{\vee} \onto f^*\OO(1),
\]
hence a map $S\to \mathbb{P}\tspace$, which coincides with $T$. Therefore, once more, we can discard $T$ and the last
equality of~\eqref{eq:starCondition} from the data and obtain only open conditions on $\varphifr_1, \ldots ,\varphifr_d$.
We conclude that there is a \emph{projective smooth equivalence}
\begin{equation}\label{eq:smoothEquivalenceFramedProj}
    \begin{tikzcd}
        & \unresfrfullpar{\Tproj} \ar[rd, "\alpha", "\mathrm{sm}"']\ar[ld, two heads, "\upsilon"', "\mathrm{sm}"]\\
        \unresfullpar{\Tproj} && \tconcspace^{\mathrm{conc}}.
    \end{tikzcd}
\end{equation}
One might expect to see the projectivisation of $\tconcspace^{\mathrm{conc}}$ on the right hand side. However, observe that
on the concise locus this makes little difference: $\tconcspace^{\mathrm{conc}}$ is a $\Gmult$-bundle over its projectivisation.
Arguing exactly as in Theorem~\ref{ref:SmoothEquivalenceCsigmahat:thm} we obtain the following smooth equivalence
\begin{equation}\label{eq:smoothEquivalenceCsigma}
    \begin{tikzcd}
        & \csigmafr_m \ar[rd, "\alpha", "\mathrm{sm}"']\ar[ld, two heads, "\upsilon"', "\mathrm{sm}"]\\
        \csigma_m && \sigmahat_m^{\mathrm{conc}}
    \end{tikzcd}
\end{equation}
Moreover, we can use the framing on the intermediate secant varieties $c_{1, \ldots i}\sigma_m \subseteq \unrespar{1, \ldots ,i}{\Tproj}$.
For them, we obtain smooth equivalences
\begin{equation}\label{eq:smoothEquivalenceCsigmaPartial}
    \begin{tikzcd}
        & c_{1,\dots,i}\sigma^\mathrm{fr}_m \ar[rd, "\alpha_{1, \ldots ,i}", "\mathrm{sm}"']\ar[ld, two heads, "\upsilon_{1, \ldots ,i}"', "\mathrm{sm}"]\\
        c_{1, \ldots ,i}\sigma_m && \sigmahat_m^{W_1-, \ldots, W_i-\mathrm{conc}}
    \end{tikzcd}
\end{equation}
where $c_{1,\dots,i}\sigma^\mathrm{fr}_m \subset (\unresfrpar{1, \ldots ,i}{\Tproj})^{\brk = m}$ is the minimal border rank locus and $\sigmahat_m^{W_1-, \ldots, W_i-\mathrm{conc}}\subseteq W_1\otimes \ldots \otimes W_i\otimes V_{i+1}\otimes \ldots \otimes V_d$ is the
locus of $W_1$-, \ldots , $W_i$-concise tensors of border rank $m$.

\begin{corollary}[Dimension of concise secant]\label{ref:dimensionOfcsigma:cor}
    For every $V_1, \ldots , V_d$ such that $\csigma_m$ is nonempty, the dimension of $\csigma_m$ is $m\cdot (\sum_{i=1}^d \dim V_{i}) - m(d-1)-1$,
    and the dimension of $\csigmahat_m$ is $m\cdot (\sum_{i=1}^d \dim V_{i}) - m(d-1)$.
\end{corollary}
\begin{proof}
    The spaces $W_1, \ldots ,W_d$ are $m$-dimensional by definition, so
    the secant variety $\sigmahat_m^{\mathrm{conc}}\subseteq \tconcspace$ has expected dimension $dm^2 - m(d-1)$.
    The fibres of $\alphahat$ have dimension $m\cdot \left( \sum_{i=1}^d \dim
    V_i \right)$, the fibres of $\alpha$ one dimension less, and the fibres of
    $\upsilon$ have dimension $dm^2$, hence the dimension of $\csigmahat_m$ is $dm^2 + m(d-1)$.
\end{proof}

\begin{remark}
    Usually, the definition of smooth equivalence assumes surjectivity of both maps. In our setup, the maps $\alphahat$, $\alpha$ need
    not be surjective. However, they fail to be such only in somewhat pathological situations, so we chose to use the term anyway.
\end{remark}





\subsubsection{Smooth equivalences and singularities}\label{ssec:singularitiesMain}

    Above, we reduced the ``iterated setup'' to the usual one, that is, to the concise locus of $\sigmahat_m \subseteq W_{1,\dots, d}$.
    Part of this locus, which is ``1-generic enough'' is understood thanks to a
    long-investigated connection to the Hilbert
    scheme and Quot scheme~\cite{poonen_moduli_space, Blaser_Lysikov,
    Landsberg_Michalek__Abelian_Tensors, Wojtala_Irreversibility, JLP, GJLM}. This allows us to use the already
    existing knowledge of singularities of Hilbert and Quot schemes to obtain corresponding statements about the singularities of the
    concise secant variety.

    Consider a concise tensor $\Tppar{}\in \tconcspace$. Recall that $\Tppar{}$ is $1_{W_i}$-generic if there exist an element
    $\alpha_i\in W_i^{\vee}$ and an index $j$ such that $\Tppar{}(\alpha_i)\colon W_j^{\vee}\to W_1\otimes \ldots \otimes W_{\hat{i}}\otimes \ldots \otimes W_{\hat{j}}\otimes  \ldots \otimes W_d$ has maximal rank. This is an open condition. It will be discussed more thoroughly in
    Proposition~\ref{ref:genericity:prop}. 
    Currently, we need the following dictionary, which emerged in~\cite{JLP} using the ideas of~\cite{Landsberg_Michalek__Abelian_Tensors}.
    \begin{center}
    \begin{tabular}{c c}
        a tensor generic on coordinates & is isomorphic to\\
        \toprule
        $\geq d-2$ & multiplication tensor in a module\\
        $\geq d-1$ & multiplication tensor in an algebra\\
        $d$ & multiplication tensor in a Gorenstein algebra
    \end{tabular}
\end{center}

    The part of smooth equivalences which we need may be informally summarised as follows:
    \begin{enumerate}
        \item if $T$ is a tensor isomorphic to a multiplication tensor in an algebra $\cA$, then
            $T$ has minimal border rank if and only if $\cA$ is smoothable. Suppose that this condition holds,
            then the geometry of $T\in \sigmahat_m$ is the same as the geometry of any point $[\Spec(\cA)\subseteq \mathbb{A}^N]\in \Hilb_m^{\sm}(\mathbb{A}^N)$,
            up to adding free parameters,
        \item if $T$ is a tensor isomorphic to a multiplication tensor in a module $M$, then
            $T$ has minimal border rank if and only if $M$ is smoothable. Suppose that this condition holds,
            then the geometry of $T\in \sigmahat_m$ is the same as the geometry of any point $[\OO_{\mathbb{A}^N}^r\onto M]\in \Quot_m^{\sm}(\OO_{\mathbb{A}^N}^r)$,
            up to adding free parameters.
    \end{enumerate}
    For $m=2,3, 4$, we will only need the following part.
    \begin{proposition}[\cite{GJLM}, smoothness]\label{ref:Hilbsmoothness:prop}
        \begin{enumerate}
            \item Suppose that a tensor $T$ is isomorphic to a multiplication tensor in an algebra $\cA$.
                Then $T\in \sigmahat_m$ is a smooth point if and only if a point $[\Spec(\cA)\subseteq \mathbb{A}^N]\in \Hilb_m^\sm(\mathbb{A}^N)$
                is smooth.
            \item Suppose that a tensor $T$ is isomorphic to a multiplication tensor in a module $M$.
                Then $T\in \sigmahat_m$ is a smooth point if and only if a point $[\OO_{\mathbb{A}^N}^r\onto M]\in \Quot_m^\sm(\OO_{\mathbb{A}^N}^r)$
                is smooth.
        \end{enumerate}
    \end{proposition}
    This part, together with a smooth equivalence~\eqref{eq:smoothEquivalenceCsigmahat}, allows us to use the existing results 
    on $\Hilb^{\sm}$ and $\Quot^{\sm}$ to gain knowledge of $\csigma_m$. The
    amount of information obtained in this way is quite dramatic, if one
    compares it with what is known about $\sigma_m$.

    \begin{theorem}[Good geometry of $\csigma_m$]\label{ref:singularities:thm}
        The varieties $\csigma_2$ and $\csigma_3$ are smooth.
        The variety $\csigma_4$ is normal, Gorenstein (in particular, Cohen-Macaulay) and has canonical singularities, hence rational ones.
        Its singular locus has codimension $9$ and blowing it up resolves the singularities.
    \end{theorem}
    \begin{proof}
        For $m=2,3$, we employ Proposition~\ref{ref:Hilbsmoothness:prop}.

        For $m=2$, every minimal border rank tensor $T\in \tconcspace$ is a unit tensor. This case is an iterated multiplication tensor in the algebra $\kk\times \kk$. This algebra can be embedded into
        $\mathbb{A}^1$ and the Hilbert scheme $\Hilb_2(\mathbb{A}^1)\simeq
        \mathbb{A}^2$ is smooth.

        The case $m=3$ is similar. In this case, every minimal border rank tensor $T$ is generic on at least $d-1$ coordinates,
        hence corresponds to a multiplication tensor in an algebra $\cA$ with $\dim_{\kk} \cA = 3$.

        A scheme $\Spec(\cA)$ has degree $3$, so there exists a closed embedding $\Spec(\cA) \subseteq \mathbb{A}^2$. The Hilbert
        scheme of $3$ points on $\mathbb{A}^2$ is smooth, so we obtain that $T$ is smooth.

        The argument for $\csigma_4$ is quite similar, but the moduli space considerations become more involved. 
        Every minimal border rank tensor $T$ corresponds to a multiplication tensor in a module $M$.

        The possible modules are classified. Let
        $\cA_{2,6}
        = \kk[x_1,x_2,x_3]/(x_1,x_2,x_3)^2$ and let $M_{2,8}$ be the $\kk[x_1,
        x_2, x_3]$-module
        given by
        \[
            M_{2,8} = \frac{\kk[x_1, x_2, x_3]e_1 \oplus \kk[x_1, x_2, x_3]e_2}{(x_1e_1 - x_2e_2,\ x_2e_1,\ x_3^2e_1,\ x_1e_2,\ x_3e_2,\ x_2^2e_2)}.
        \]
        Let $U_{2,6}$ and $U_{2,8}$ be the corresponding tensors.
        Using the package \emph{Versal Deformations}, we verify that $\OO^{\oplus 2} \onto M_{2,8}$ is a smooth point of the principal
        component of the Quot scheme, so $U_{2,8}$ is a smooth point.
        In contrast, the point $\Spec(\cA_{2,6})\subseteq \mathbb{A}^3$ of the Hilbert scheme $\Hilb_4(\mathbb{A}^3)$
        is known to be singular, so also $U_{2,6}$ is singular.
        Hence, we conclude that the singular locus consists precisely of tensors isomorphic to $U_{2,6}$.
    \end{proof}

\begin{corollary}[Equations of concise secant]\label{ref:equationsSmallr:cor}
    Assume that $\kk$ has characteristic zero.
    For every $m\leq 5$, the concise secant $\csigma_m$, $\csigmahat_m$ are
    set-theoretically equal to the centroid abundant loci (see
    Definition~\ref{ref:secantLocus:def}).
    For every $m\leq 4$, these are equalities of schemes.
\end{corollary}

\begin{proof}[Proof-sketch]
    Using~\eqref{eq:smoothEquivalenceCsigma}-\eqref{eq:smoothEquivalenceCsigmahat}, we are reduced to showing that
    the concise part of $\csigmahat_m$ is given by the centroid abundant equations. This is proven by assuming Corollary~\ref{ref:equationsSmallr:cor} holds for $m \leq 4$, which implies that the appropriate Hilbert and Quot schemes are reduced, thus establishing the scheme-theoretic equality.
\end{proof}

    
    \begin{remark}\label{ref:singularitiesFive:rmk}
        The variety $\csigma_5$ also seems to have unexpectedly good singularities, in particular its singular locus
        is much smaller than naively expected: the points that correspond to $1$-degenerate tensors (found in~\cite{JLP}) are smooth.
        This implies that also for $m=5$ the equality of Corollary~\ref{ref:equationsSmallr:cor} is scheme-theoretic.
        This will be explained in a future work.
    \end{remark}
    The above results apply to small $m$. We need to stress, however, that even for larger $m$ there are many partial results
    describing the singularities of Hilbert and Quot schemes, see, for example~\cite{Hu__singular_Hilbert_schemes, AJR}. Hence,
    when enough coordinates are generic, it is most fruitful to use smooth equivalences to pass from $\csigma_m$ to analysing 
    $\Hilb_m^{\sm}$ or $\Quot_m^{\sm}$.

    The question of Cohen-Macaulayness of secant varieties has been addressed in many special cases in the literature,
    see, for example~\cite{landsberg_weyman_secants_ideal_sings_of_sv_of_Segree, Conca_deNegri_Stojanac}.
    Oeding put forward the following very bold, yet elegant, conjecture.
    \begin{conjecture}[{\cite[Conjecture~1.1]{Oeding__Cohen_Macaulay}}]\label{ref:Oeding:conj}
        All secant varieties of Segre product of projective spaces are arithmetically Cohen-Macaulay (that is, the affine cone $\sigmahat_r$ is Cohen-Macaulay).
    \end{conjecture}
    The conjecture is wide open.
    Via the smooth equivalences, it contains the conjectures of Artin-Hochster on the Cohen-Macaulayness of the Quot scheme of $\mathbb{A}^2$,
    and Haiman's conjecture~\cite[Conjecture~5.2.1]{Haiman_macdonald} on the Cohen-Macaulayness of $\Hilb^{\sm}_d(\mathbb{A}^n)$, for any $d,n$.
    Under the assumption of the conjecture, normality of $\sigma_r$ translates into $\sigma_r$
    being regular in codimension one, which is in practise easier to check. Hence, the conjecture suggests also the normality
    of all secant varieties.


\subsection{Unrestriction schemes as blowups}

When the coordinate bundles are large enough, the maps $\unresfullpar{\Taf}\to
\tspace$ and $\unresfullpar{\Tproj}\to \mathbb{P}(\tspace)$ are birational. From
the birational geometry perspective, it is interesting to realise them as a
blowup. This is the aim of the current section. 

\begin{proposition}\label{p:bl_in_unres}
    Let $T\colon \LL \to \tspacecurly$ be a family of tensors on a scheme $X$, let $T_{\VV_i}\colon \VV_i^{\vee}\otimes \LL \to \VVhat{}$ be the contraction and
    $\Lambda^m T_{\VV_i}\colon \Lambda^m (\VV_i^{\vee} \otimes \LL) \to \Lambda^m\VVhat{}$ its top exterior power.
    Assume that the vector bundle $\VV_i$ has rank $m$. Then:
    \begin{enumerate}
        \item The pullback of the closed subscheme $\Z(\Lambda^m T_{\VV_i}) \subset X$
            to $\unres$ is locally cut out by one equation $\det \varphi_i^\vee$, where $\varphi_i$
            is as in Definition~\ref{ref:unrestriction:def}.
        \item The blowup of $X$ along $\Z(\Lambda^m T_{\VV_i})$ is the scheme-theoretic closure of $X \setminus \Z(\Lambda^m T_{\VV_i})$
            in $\unres$. The blowup coincides with $\unres$ precisely if $\det \varphi_i^\vee$ is an effective Cartier divisor.
    %     \item The blowup of $\unres$ along $\Z(p^*\Lambda^m T)$
    % is the blowup of $X$ along $\Z(\Lambda^m T)$.
    \end{enumerate}
\end{proposition}
\begin{proof}
    By definition, the pullback of $T_{\VV_i}$ to $\unres$ factors through the universal subbundle inclusion
    \[
    \begin{tikzcd}
        p^*(\VV_i^\vee \otimes \LL) \arrow[rr, "p^*T_{\VV_i}"] \arrow[rd, "\varphi_i^\vee"] && p^*\VVhat \\
        & \UU_i^{\vee} \arrow[ru, hook] & 
    \end{tikzcd}.
    \]
    The universal subbundle has rank $m$, so its $m$-th exterior power is non-vanishing,
    hence 
    \[
        \Z(p^*\Lambda^m T_{\VV_i}) = \Z(\Lambda^m \varphi_i^\vee) = \Z(\det \varphi_i^\vee)
    \]
    which is locally cut out by one equation.

    The tensor $T$ is $\VV_{i}$-concise on the open locus $D(\Lambda^m T_{\VV_i}) := X \setminus \Z(\Lambda^m T_{\VV_i})$,
    so we obtain a lifting to the Grassmannian. The blowup of $X$ along $\Z(\Lambda^m T_{\VV_i})$ is the schematic closure of $f(D(\Lambda^m T_{\VV_i}))$. 
    Because $\det \varphi_i^\vee$ is locally cut out by one equation, it follows that $\det \varphi_i^\vee$ must be a zero divisor, and thus the closure is never the whole scheme $\unres$.
\end{proof}

\begin{corollary}\label{c:unres_blowup_first}
    Assume that $\dim_{\kk} V_{\bullet} = m$.
    Consider the affine space $\tspace$ with its universal family $\Taf$ as in Example~\ref{ex:universalFamily}. 
    Then $\unrespar{i}{\Taf}$ is the blowup $\Bl_{\Z(\Lambda^m \Taf_{\VV_i})} \tspace$.
\end{corollary}
\begin{proof}
    By Proposition~\ref{ref:bundleAffine:prop}, the scheme $\unres$ is smooth and integral (and $\det \varphi_i^\vee$ is not zero),
    so $\det \varphi_i^\vee$ is automatically a Cartier divisor and Proposition~\ref{p:bl_in_unres} applies.
\end{proof}



% \begin{corollary}\label{c:non-zero-divisor}
%     The blowup of $X$ along $\Z(\Lambda^m T)$ is a closed subscheme of $\unres$.
%     Moreover, it coincides with $\unres$ if and only if $\Z(p^*\Lambda^m T) \subset \unres$ is an 
%     effective Cartier divisor.
% \end{corollary}

To obtain equality of unrestriction and blowup, we would like to refer to Corollary~\ref{c:unres_blowup_first}
as the local model. However, the family from this corollary is canonically a local model only in the framed
setting. Hence, we make a small detour to justify that both unrestrictions and blowups behave well with respect
to smooth maps, or, actually, faithfully flat quasi-compact maps.

Let $f \colon X' \to X$ be a morphism of schemes. Any family of tensors $T$ on $X$ gives rise to 
a family of tensors $T' := f^* T$ on $X'$. By functoriality, the closed subscheme 
$\Z(\Lambda^m T_{\VV_i}) \subset X$ pulls back to the closed subscheme $\Z(\Lambda^m T'_{\VV_i}) \subset X'$
and the unrestriction scheme $\unres \to X$ pulls back to the unrestriction scheme 
$\unrespar{i}{T'} \to X'$. By Proposition~\ref{p:bl_in_unres} and the universal 
property of blowup, there exists a unique map $\Bl_{\Z(\Lambda^m T'_{\VV_i})}X' \to \Bl_{\Z(\Lambda^m T_{\VV_i})}X$
making the following diagram commute:
\[
\begin{tikzcd}[column sep=0.5]
    && \unrespar{i}{T'} \arrow[ddl] \arrow[rrrr] &&&& \unres \arrow[ddl] \\
    \Bl_{\Z(\Lambda^m T'_{\VV_i})}X' \arrow[rru, hook] \arrow[dr] \arrow[rrrr, crossing over] &&&&
    \Bl_{\Z(\Lambda^m T_{\VV_i})}X \arrow[rru, hook] \arrow[dr] && \\
    & X' \arrow[rrrr, "f"] &&&& X & \\
\end{tikzcd}
\]
We will employ the following descent result.
\begin{lemma}\label{l:pullback_flat}
    Let $f \colon X' \to X$ and $T', T$ be as above.
    \begin{enumerate}
        \item If $f$ is flat, then $\Bl_{\Z(\Lambda^m T_{\VV_i})}X = \unres$ implies that
            $\Bl_{\Z(\Lambda^m T'_{\VV_i})}X' =\OpUnres_{i}(T')$.
        \item If $f$ is fpqc, then $\Bl_{\Z(\Lambda^m T_{\VV_i})}X = \unres$
            if and only if $\Bl_{\Z(\Lambda^m T'_{\VV_i})}X' = \unrespar{i}{T'}$.
    \end{enumerate}
\end{lemma}
\begin{proof}
    The back square is a pullback, so the front square is a pullback if and only if the top square is 
    a pullback. The front square is a pullback when $f$ is
    flat~\cite[\href{https://stacks.math.columbia.edu/tag/0805}{Tag 0805}]{stacks-project}. In particular,
    this shows the first claim.

    If $f$ is fpqc, then $\unrespar{i}{T'} \to \unres$ is fpqc~\cite[\href{https://stacks.math.columbia.edu/tag/01U9}{Tag 01U9},
    \href{https://stacks.math.columbia.edu/tag/01S1}{Tag 01S1},
    \href{https://stacks.math.columbia.edu/tag/01K5}{Tag 01K5}]{stacks-project} as well. 
    Being an isomorphism is local in fpqc topology~\cite[\href{https://stacks.math.columbia.edu/tag/02L4}{Tag 02L4}]{stacks-project},
    which proves the second claim.
\end{proof}

% \section{Main examples of unrestriction schemes}
% Fix coordinates on $V_i$ and $\Vhat$ and identify
% $\tspace = V_i \otimes \Vhat = \Spec \kk[x_{1,1}, \dots, x_{m, M}]$.
% Consider the open subscheme $U = \Spec \kk[y_{1,m+1}, \dots, y_{m,M}] \subset \Gr(m, \Vhat)$
% given by 
% \[
%     U = \left\{\begin{bmatrix}
%         1 & 0 & \hdots & 0 & y_{1,m+1} & \hdots & y_{1,M} \\
%         0 & 1 & \hdots & 0 & y_{2,m+1} & \hdots & y_{2,M} \\
%         \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
%         0 & 0 & \hdots & 1 & y_{m,m+1} & \hdots & y_{m,M} \\
%     \end{bmatrix} \right\}.
% \]
% The affine piece $\unres \cap (\tspace \times U) \subset \tspace \times U$
% is cut out by the following equations:
% \[
%     \begin{bmatrix}
%     x_{1,1} & \cdots & x_{1,m} \\
%     x_{2,1} & \cdots & x_{2,m} \\
%     \vdots & \ddots & \vdots \\
%     x_{m,1} & \cdots & x_{m,m}
%     \end{bmatrix}
%     \cdot
%     \begin{bmatrix}
%     y_{1,m+1} & y_{1,m+2} & \cdots & y_{1,M} \\
%     y_{2,m+1} & y_{2,m+2} & \cdots & y_{2,M} \\
%     \vdots & \vdots & \ddots & \vdots \\
%     y_{m,m+1} & y_{m,m+2} & \cdots & y_{m,M}
%     \end{bmatrix}
%     =
%     \begin{bmatrix}
%     x_{1,m+1} & x_{1,m+2} & \cdots & x_{1,M} \\
%     x_{2,m+1} & x_{2,m+2} & \cdots & x_{2,M} \\
%     \vdots & \vdots & \ddots & \vdots \\
%     x_{m,m+1} & x_{m,m+2} & \cdots & x_{m,M}
%     \end{bmatrix},
% \]
% encoding the condition that each $(x_{i,1}, x_{i,2}, \dots, x_{i,M})$ lies in the linear span of 
% $(e_j, y_{j,m+1}, \dots, y_{j,M})$, where $e_j$ denotes the $j$-th vector 
% of the standard basis of $\kk^m$.
% Each of variables $x_{1,m+1}, \dots, x_{m,M}$ is expressed as a quadric in the 
% disjoint set of variables $x_{1,1}, \dots, x_{m,m}, y_{1,m+1}, \dots, y_{m,M}$, 
% so the affine piece of $\unres$ is the affine space of dimension 
% $(m \cdot M + m \cdot (M - m)) - m \cdot (M - m) = m \cdot M$.


% \begin{proposition}\label{p:unres_blowup_first}
%     Let $X =\tspace$ be the affine space of tensors and let 
%     $T \colon \OO_X \otimes_\kk V_i^\vee \to \OO_X \otimes_\kk \Vhat$ 
%     be the universal family over $X$. Then $\unres$
%     coincides with the blowup $\Bl_{\Z(\Lambda^m \tspace)} X$.
% \end{proposition}
% \begin{proof}
%     Consider the affine piece 
%     \[
%         \unres \cap (\tspace \times U) \cong \Spec \kk[x_{1,1}, \dots, x_{m,m}, y_{1,m+1}, \dots, y_{m, M}]
%     \] 
%     as above. The affine piece of the pullback of the closed subscheme $\Z(\Lambda^m T) \subset X$
%     \[\Z(\Lambda^m p^*T) \cap (\tspace \times U) \subset 
%     \unres \cap (\tspace \times U)\] is cut out by the polynomial
%     $\det [x_{i,j}]_{1 \leq i, j \leq m}$, which is a not a zero divisor.
%     Thus, the claim follows from Proposition~\ref{p:bl_in_unres}.
% \end{proof}

\begin{proposition}\label{ref:unrestrictionAsBlowp:prop}
    Assume that $\dim_{\kk} V_{\bullet} = m$.
    Let $\tspace$ be the affine space of tensors and let $\Taf$ 
    be the universal tensor over it. Then for every $i=1, \ldots ,d$ we have
    \[
        \unrespar{1, \dots, i}{\Taf} = \Bl_{\Z(\Lambda^m \Tppar{1, \dots, i-1}_{\VV_i})} \unrespar{1, \dots, i-1}{\Taf}.
    \]
    In particular, $\unresfullpar{\Taf}$ is obtained from $\tspace$ by repeated blowups with these centers.
    Same is true in the projective case.
\end{proposition}

\begin{proof}
    \def\tenmixed{T^{(i)}}
    We employ the framed unrestriction scheme. Recall that $W_1, \ldots ,W_d$ are fixed $m$-dimensional vector spaces.
    Let $\tenmixed$ be the universal family of tensors on the affine space $W_{1, \dots, i-1} \otimes V_{i, \dots, d}$.
    Consider the morphisms, defined similarly as in~\eqref{eq:smoothEquivalenceFramed}
    \[
    \begin{tikzcd}
        & \unresfrpar{1, \ldots, i-1}{\Taf} \arrow[dl, two heads, "\upsilon"', "\mathrm{sm.}"] 
        \arrow[dr, "\alphahat", "\sm."'] & \\
        \unrespar{1, \dots, i-1}{\Taf} && W_{1, \dots, i-1} \otimes V_{i, \dots, d}
    \end{tikzcd}
    \]
    On $\unresfrpar{1, \ldots , i-1}{\Taf}$, the family $\upsilon^* \Tppar{1, \dots, i-1}$ is isomorphic to $\alphahat^*\tenmixed$.
    Corollary~\ref{c:unres_blowup_first} says that $\unrespar{i}{T^{(i)}}$ and 
    $\Bl_{\Z(\Lambda^m \tenmixed_{\VV_i})} (W_{1, \dots, i-1} \otimes V_{i, \dots, d})$ coincide.
    The morphism $\alphahat$ is smooth, so by descent (the first part of Lemma~\ref{l:pullback_flat}) we have 
    \[\unrespar{i}{\alphahat^*\tenmixed} = \Bl_{\Z(\Lambda^m \alphahat^*\tenmixed_{\VV_i})}\unresfrpar{1, \dots, i-1}{\Taf}.\]
    The family $\alphahat^*\tenmixed$ is isomorphic to the family $\upsilon^* \Tppar{1, \dots, i-1}$,
    so we also have 
    \[\unrespar{i}{\upsilon^* \Tppar{1, \dots, i-1}} 
    = \Bl_{\Z(\Lambda^m \upsilon^* \Tppar{1, \dots, i-1}_{\VV_i})}\unresfrpar{1, \dots, i-1}{\Taf}.\]
    The morphism $\upsilon$ is smooth and surjective, so by descend again (the second part of Lemma~\ref{l:pullback_flat})
    we obtain
    \[
    \unrespar{1, \dots, i}{\Taf} = 
    \unrespar{i}{\Tppar{1, \dots, i-1}} 
    = \Bl_{\Z(\Lambda^m \Tppar{1, \dots, i-1}_{\VV_i})}\unrespar{1, \dots, i-1}{\Taf}.
    \]
    The projective case follows also by descent, since $\Taf$ restricted to $\tspace \setminus \{0\}$ is the
    pullback of $\Tproj$ from $\mathbb{P}(\tspace)$.
\end{proof}

As we have seen in~\S\ref{ssec:singularitiesMain}, the singularities of the concise secant variety are well understood.
Therefore, it is very interesting to understand when the map $\rho\colon \csigma_m\to \sigma_m$ is an
isomorphism near a given point $[T]\in \sigma_m$. As usually, it is most convenient to have a statement for
a single unrestriction.

Let $\Taf$, $\Tproj$ be universal tensors on $\tspace$, and $\mathbb{P}(\tspace)$, as usual, see Example~\ref{ex:universalFamily}.
Assume that $\dim V_{\bullet} = m$.
Let $c_{1, \ldots ,i}\sigmahat_m \into \unrespar{1, \ldots ,i}{\Taf}$ be the locus of minimal border rank, as in Definition~\ref{ref:secantLocus:def},
and similarly let $c_{1, \ldots ,i}\sigma_m \into \unrespar{1, \ldots ,i}{\Tproj}$ be the locus of minimal border rank.
\begin{proposition}\label{ref:secantAsBlowup:prop}
    Fix an index $1\leq i\leq d$ and assume that $\dim V_i = m$. Then the variety $c_{1, \ldots ,i}\sigmahat_m$ is the blowup of
    $c_{1, \ldots, i-1}\sigmahat_m$ along the closed subscheme described in Proposition~\ref{p:bl_in_unres}.
    Similarly, $c_{1, \ldots ,i}\sigma_m$ is the blowup of $c_{1, \ldots ,i-1}\sigma_m$.
\end{proposition}
\begin{proof}
    \def\Tu{T^u}%
    Let $\Tu$ be the universal tensor on $X := \unrespar{1, \ldots ,i}{\Taf}
    \xrightarrow{\pihat_i} \unrespar{1, \ldots ,i-1}{\Taf}$. This tensor is
    concise on coordinates $1, \ldots, i$ and $i\geq 1$, so for every point
    $x\in X$ the tensor $\Tu|_{[x]}$ has border rank at least $m$.
    Let $X^{\brk = m}\subseteq X$ be the closed locus (with reduced structure), where
    $\Tu$ has minimal border rank. Let $c_iX^{\brk = m}\subseteq X^{\brk = m}$ be the open sublocus
    consisting of points $x$ such that $\pi(x)$ is also concise on the $i$-th coordinate.
    By Proposition~\ref{p:bl_in_unres} and the Blowup Closure Lemma, the blowup
    of $c_{1, \ldots, i-1}\sigmahat_m$ is equal to the closure of $c_iX^{\brk = m}$ in $X^{\brk = m}$.
    By definition, the variety $c_{1, \ldots ,i}\sigmahat_m$ is equal to $X^{\brk = m}$.
    It remains to show that $c_iX^{\brk = m}$ is schematically dense in $X^{\brk = m}$.
    Since both are reduced, it is enough to show that $c_iX^{\brk = m}$ is
    dense in $X^{\brk = m}$.

    By passing to the framed version as in the proof of Proposition~\ref{ref:unrestrictionAsBlowp:prop},
    we are reduced to showing that the usual secant variety $\sigmahat_m \subseteq \tconcspace$ is
    the closure of its sublocus that consists of tensors concise on the $i$-th coordinate. This is true.
\end{proof}

It is very useful to understand the exceptional locus of $c_{1, \ldots ,i}\sigma_m\to c_{1, \ldots ,i-1}\sigma_m$.
We give a partial result in this direction.
Let us recall the notion of restriction on $i$-th coordinate.
Let $T', T''\in \tspace$. Assume that $\dim V_i = m$.
We say that
\emph{$T''$ restricts to $T'$ on the $i$-th coordinate} if there is a
restriction $T''\geq T'$ given by linear map $\varphi_i\colon V_i\to V_i$. We denote this relation by $T'' \geq_i T'$.
We say that $T'$ \emph{has a unique $i$-th minimal border rank unrestriction} if it admits an unrestriction $T''$
concise on the $i$-th coordinate such that $\brk(T'') = m$ and any two such unrestrictions are isomorphic tensors.

\begin{proposition}\label{ref:uniqueUnrestriction:prop}
    Assume $\dim V_i = m$.
    Let $T'\in \tspace$ be a tensor that has a unique $i$-th minimal border rank unrestriction $T''\in \tspace$ and assume that
    \begin{equation}\label{eq:orbitJump}
        \dim\left( \GLV\cdot T' \right) = \dim \left( \GLV \cdot T'' \right) - 1.
    \end{equation}
    Let $T\colon \LL\to \tspacecurly$ be any family of tensors on a scheme $X$ and
    consider $\rho\colon (\unrespar{i}{T})^{\brk = m}\to X$. Then for every $x\in X$ such that $T|_{[x]}\simeq T'$,
    the fibre $\rho^{-1}([x])$ is finite.
\end{proposition}
\begin{proof}
    The claim is local on $X$.
    Choose an open neighbourhood $x\in U \subseteq X$ which trivialises $\LL$ and $\VV_1, \ldots ,\VV_d$,
    as in Remark~\ref{ref:localFamilies:rem}. Replacing $X$ by $U$, we may assume that $\LL$, $\VV_1, \ldots ,\VV_d$
    are trivial and $T$ comes from a map $U\to \tspace$. Since the claim concerns the fibre, we may further replace
    $X$ by $\tspace$, so we are reduced to proving the claim for $(X, T)$ equal to $(\tspace, \Taf)$.

    Consider the unrestrictions $Y' := \unrespar{i}{\Taf}$, $Y := \unresfrpar{i}{\Taf}$, and their minimal border rank
    loci with natural maps $\rho\colon (Y')^{\brk =m}\to \tspace$, $p\colon Y^{\brk = m}\to (Y')^{\brk = m}\to \tspace$.
    Observe that $(Y')^{\brk = m}\to Y^{\brk = m}$ is a principal $\GL(W_i)$-bundle.
    Let $\mathrm{Res}(T'') \subset Y^{\brk = m}$ be the locally-closed locus of
    consisting of $(\Tpparfr{}, \varphifr_1)$, where $\Tpparfr{}$ is isomorphic
    to the unrestriction $T''$ from the statement. This locus is isomorphic to the product of $\Hom(W_i, V_i)$ and
    the $\GL(V_1) \times \ldots  \times\GL(V_{i-1})\times \GL(W_i) \times \GL(V_{i+1})\times\ldots \times \GL(V_d)$ orbit of $T''$.
    By assumption, the locus $\mathrm{Res}(T'')$ contains $p^{-1}(\GLV\cdot T')$, which is
    a principal $\GL(W_i)$-bundle over $\rho^{-1}(\GLV\cdot T')$.
    Putting this together, we obtain
    \[
        \dim \rho^{-1}(\GLV\cdot T') + \dim \GL(W_i) < \dim \mathrm{Res}(T'') = \dim (\GLV\cdot T'') + \dim \Hom(W_i, V_i).
    \]
    Taking into account~\eqref{eq:orbitJump} and $\dim V_i = m = \dim W_i$, the equality can only hold if
    $\dim \rho^{-1}(\GLV\cdot T') = \dim \GLV\cdot T'$. Using surjectivity, this
    implies that $\rho^{-1}(\GLV\cdot T')\to \GLV\cdot T'$ has finite fibres.
\end{proof}

\begin{theorem}\label{ref:uniqueUnrestrictionSecant:thm}
    Let $\dim V_i = m$. Assume that $x\in c_{1, \ldots ,i-1}\sigma_m$ is a normal point
    such that the corresponding tensor $T'$ has a unique $i$-th minimal border
    rank unrestriction $T''$ and assume that
    \[
        \dim\left( \GLV\cdot T' \right) = \dim \left( \GLV \cdot T'' \right) - 1.
    \]
    Then $\rho\colon c_{1, \ldots ,i}\sigma_m\to c_{1, \ldots ,i-1}\sigma_m$ is an isomorphism
    over a neighbourhood of $x$.
\end{theorem}

\begin{proof}
    From Proposition~\ref{ref:uniqueUnrestriction:prop}, we get that $\rho^{-1}(x)$ is finite.
    From Proposition~\ref{ref:secantAsBlowup:prop}, we get that $\rho$ is a birational map.
    Since $x$ is normal, Zariski's Main Theorem implies that $\rho$ is an isomorphism over a neighbourhood of $x$.
\end{proof}




\subsection{Geometry of $\csigma_2$}

In this section we apply the above results to the case of the (second) secant variety of the Segre embedding.

\newcommand{\TT}{\mathbb{T}}
\newcommand{\twx}{\widetilde{x}}
\newcommand{\twy}{\widetilde{y}}



Below, we consider varieties $c_{1,\dots,i}\sigma_2(\PP V_1 \times \dots \times \PP V_d)$, 
where all vector spaces $V_1, \dots, V_d$ have dimension $2$. We often fix bases 
$V_i = \langle x_i, y_i \rangle$. For a subset $I \subset \{1, \dots, d\}$, we write 
\[
x_I := \bigotimes_{i \in I} x_i \in \bigotimes_{i \in I} V_i \quad\text{and}\quad 
y_I := \bigotimes_{i \in I} y_i \in \bigotimes_{i \in I} V_i.
\]
It is well-known that there are only two isomorphism classes of concise tensors in $\sigma_2$.
This allows one to classify all isomorphism classes of tensors in $\sigma_2$, as observed in~\cite[Proposition 1.1]{Buczynski_Landbserg_sigma3}.
Namely, the tensors of border rank at most two have the following normal forms, 
    indexed by subsets $I \subset \{1, \dots, d\}$  (below $J$ denotes 
    the complement $\{1,\dots,d\} \setminus I$):
    \begin{itemize}
        \item $B_I = (x_I + y_I) \otimes x_J$, concise exactly on the coordinates $I$,
        \item $C_I = (\sum_{i \in I} x_{I \setminus \{i\}} \otimes y_i) \otimes x_J$,
            concise again on the coordinates indexed by $I$.
    \end{itemize}
    Observe that $C_I$ is the W-state tensored by $x_J$. In particular, $B_I$ degenerates to $C_I$.

\begin{proposition}\label{p:sigma2_iso_after_3_unres}
    The morphism $c\sigma_2 \to c_{1,\dots,i}\sigma_2$ is an isomorphism
    in the neighbourhood of all points $(\Tppar{1,\dots,i}, \varphi_\bullet) \in c_{1,\dots,i}\sigma_2$ 
    such that $\Tppar{1,\dots,i}$ is concise on at least three factors.
    In particular, the morphism $\csigma_2 \to c_{1,2,3}\sigma_2$
    is an isomorphism.
\end{proposition}
\begin{proof}
    The conciseness assumption means that we need to analyse $B_I$, $C_I$ with $|I|\geq 3$.
    The orbit of $B_{\{1, \dots, d\}}$ has dimension $2d+1$ since its closure is $\sigma_2$. 
    A direct calculation shows that the orbit of $C_I$ with $|I| = 3$ has dimension $d+3$. 
    Moreover, $C_I$ is a degeneration of $B_I$ for each $I$ and $B_{\{1,2,3\}} \leq B_{\{1,\dots, 4\}} 
    \leq \dots \leq B_{\{1,\dots, d\}}$. Thus, the orbit of $B_I$ has dimension $d + 1 + |I|$ 
    and the orbit of $C_I$ has dimension $d + |I|$. A non-zero restriction of a tensor with normal 
    form $B_I$ on $k$-th factor has normal form $B_I$ or $B_{I \setminus\{k\}}$, depending on the 
    rank of the restriction map and whether $k \in I$, and similarly for $C_I$.

    The variety $c_{1,\dots,i}\sigma_2$ is smoothly equivalent to an open subvariety 
    of $\sigma_2$ by~\eqref{eq:smoothEquivalenceCsigmaPartial}, so it is normal~\cite[Theorem 7.10]{michalek_oeding_zwiernik}.
    Let $(\Tppar{1,\dots,i}, \varphi_\bullet) \in c_{1,\dots,i}\sigma_2$ be a point with 
    $\Tppar{1,\dots,i}$ concise on at least three factors.
    If $\Tppar{1,\dots, i}$ is concise on the $(i+1)$-th factor, the fiber is one point because $\rho_{i+1}$ is an isomorphism over the 
    $V_{i+1}$-concise locus.   
    If $\Tppar{1,\dots, i}$ is not concise 
    on the $(i+1)$-th factor, then by the discussion above $\Tppar{1, \ldots ,i}$ satisfies the assumptions
    of Theorem~\ref{ref:uniqueUnrestrictionSecant:thm}.
    % the fiber $\rho_{i+1}^{-1}(\Tppar{1,\dots,i}, \varphi_\bullet)
    % \subset c_{1,\dots,i+1}\sigma_m$ is finite by discussion above and Proposition~\ref{ref:uniqueUnrestriction:prop}.
    % The variety $c_{1,\dots,i}\sigma_2$ is smoothly equivalent to an open subvariety 
    % of $\sigma_2$ \jjetoadd, so it is normal~\cite[Theorem 7.10]{michalek_oeding_zwiernik}, so 
    % Zariski's main theorem implies that $\rho_{i+1}$ is an isomorphism near the point 
    % $(\Tppar{1,\dots,i}, \varphi_\bullet)$.
\end{proof}

\begin{proposition}\label{ref:sigmaFixedPoints:prop}
    Let $\TT \subset \SLV$ be the diagonal torus. The $\TT$-action on $\csigma_2$ 
    has $2^d(2^{d-1} + 2d - 3)$ fixed points. In particular, $\csigma_2$ admits 
    a $\Gmult$-action with finitely many fixed points.
\end{proposition}

The description of fixed points is based on the following observations:
\begin{itemize}
    \item The morphisms 
        \[ 
            \csigma_m = c_{1,\dots,d}\sigma_m \xrightarrow{\rho_d} c_{1,\dots,d-1}\sigma_m 
            \xrightarrow{\rho_{d-1}} \dots \xrightarrow{\rho_2} c_1\sigma_m \xrightarrow{\rho_1} \sigma_m
        \]
        are equivariant, so the image of a fixed point of $\csigma_m$ in any 
        $c_{1,\dots,i}\sigma_m$ is a fixed point there. This means that fixed points 
        of $c_{1,\dots,i+1}\sigma_m$ lie over fixed points of $c_{1,\dots,i}\sigma_m$,
        so we can determine them iteratively.
    \item The morphisms $\rho_i$ are projective, by Borel's fixed point theorem the fiber of 
        $\rho_i$ over a fixed point of $c_{1,\dots,i}\sigma_m$ must contain a fixed point of 
        $c_{1,\dots,i+1}\sigma_m$.
\end{itemize}
These observations combined with Proposition~\ref{p:sigma2_iso_after_3_unres} imply that 
the structure of fixed points of $\csigma_2$ is fully determined by the structure 
of fixed points of $c_{1,2,3}\sigma_2$. \\


The fixed points are distributed evenly between fibers over the $2^d$ basis simple tensors,
as these are the fixed points of the $\TT$-action on $\PP(\tspace)$.
We focus on the fiber over $[T] = [x_{\{1,\dots,d\}}] \in \sigma_2$. 
The action on $\tspace$ has one-dimensional eigenspaces, spanned by basis simple tensors. 
Thus, a subspace $U_1^\vee \in \rho_1^{-1}(T) \subset c_1\sigma_2$
is fixed if and only if $U_1^\vee =\langle x_{\{2,\dots,d\}}, x_I \otimes y_J\rangle$ 
for a proper subset $I \subsetneq \{2, \dots, d\}$, where $J = \{2,\dots, d\} \setminus I$. 
Note that the tensors $\twx_1 \otimes x_{\{2,\dots,d\}} + \twy_1 \otimes x_I \otimes y_J$
indeed have (border) rank two.

If $|J| \geq 2$, then the tensor corresponding to $U_1^\vee$ is isomorphic to $B_{\{1\} \cup I}$, 
so it is concise on at least three factors. In this case Proposition~\ref{p:sigma2_iso_after_3_unres} 
implies that the fiber over $U_1^\vee$ contains exactly one fixed point. This way we obtain $\sum_{k=2}^{d-1} 
\binom{d-1}{k} = 2^{d-1} - d$ fixed points. We call these \emph{points of height one}.

The only remaining case is $|J| = 1$. Let us focus on $J = \{2\}$.
The subspace $U_1^\vee$ corresponds to the tensor 
$(\twx_1 \otimes x_2 + \twy_1 \otimes y_2) \otimes x_{\{3,\dots, d\}}$, which is already 
$V_2$-concise. Thus, the fiber $\rho_2^{-1}(U_1^\vee, T)$ is one point $U_2^\vee$,
corresponding to the tensor 
$(\twx_1 \otimes \twx_2 + \twy_1 \otimes \twy_2) \otimes x_{\{3,\dots, d\}}$.
The description of normal forms of border rank two tensors from Proposition~\ref{p:sigma2_iso_after_3_unres}
shows that the tensor from the fiber $\rho_3^{-1}(U_2^\vee, U_1^\vee, T)$ have normal 
forms $B_{\{1,2,3\}}$ or $C_{\{1,2,3\}}$. In particular, they are concise only on the first three 
factors, so the fixed points $U_3^\vee \in \rho_3^{-1}(U_2^\vee, U_1^\vee, T)$ must come from 
fixed points in the corresponding fiber in $\csigma_2(\PP V_1 \times \PP V_2 \times \PP V_3)$.
In this special case one checks directly that the eigenspaces of action on 
$U_1 \otimes U_2 = \langle \twx_1 \otimes \twx_2, \twx_1 \otimes \twy_2,
\twy_1 \otimes \twx_2, \twy_1 \otimes \twy_2 \rangle$ are one-dimensional, 
spanned by these basis vectors, which gives three fixed points in 
$\rho_3^{-1}(U_2^\vee, U_1^\vee, T) \subset \csigma_2(\PP V_1 \times \PP V_2 \times \PP V_3)$: 
\[
    \spann{\twx_1 \otimes \twx_2 + \twy_1 \otimes \twy_2, \twx_1\otimes \twx_2},\
    \spann{\twx_1 \otimes \twx_2 + \twy_1 \otimes \twy_2, \twx_1\otimes \twy_2},\
    \spann{\twx_1 \otimes \twx_2 + \twy_1 \otimes \twy_2, \twy_1\otimes \twx_2}.
\]
Thus, each case $|J| = 1$ contributes three points, which we call \emph{points of height two}.
The total number of points
is $(2^{d-1} - d) + 3(d-1) = 2^{d-1} + 2d - 3$.





\subsubsection{Weights on tangent spaces}

Recall that $\TT \subseteq \SLV$ is the full diagonal torus, which is $d$-dimensional.
We fix weights so that $\deg(x_i) = -e_i$, $\deg(y_i) = e_i$.
For a subset $I\subseteq \{1, \ldots ,d\}$, we denote $e_I := \sum_{i\in I} e_i$.

We will compute the weights on the tangent spaces at fixed points that lie over $[T := x_{\{1, \ldots ,d\}}]\in \mathbb{P}\tspace$.
This tensors corresponds to an embedding $\LL|_{[T]}\into \tspace$. The weight of the $1$-dimensional space $\LL|_{[T]}$
is $\deg(x_{\{1, \ldots ,d\}}) = -e_{\{1, \ldots ,d\}}$, so the weight on $\LL^{\vee}|_{[T]}$ is $e_{\{1, \ldots ,d\}}$.

Consider first a $\TT$-fixed point of concise height one. By the previous section, every such point $[T']$ is
obtained from a $2$-dimensional subspace of $\Vhatpar{1}$ obtain as follows: let $I\subseteq \{2, \ldots , d\}$
be a subset with at least $2$ elements. Let $J := \left\{ 2, \ldots , d \right\}\setminus I$. Then the subspace is
spanned $x_I\otimes x_J = x_{I\cup J}$ and $y_I\otimes x_J$.
The torus $\TT$ acts naturally on $\Vhatpar{1}$, hence also on the universal subbundle $\UU^{\vee}_1$ of $\Gr(2, \Vhatpar{1})$.
Calculating the tangent weights directly on the point corresponding to the subspace is cumbersome, so we pass to
the framed setting.

\newcommand{\frone}{c_{1}\sigma_2^{\mathrm{fr}}}

Take $W_1 = \spann{\twx_1, \twy_1}$ to be a $2$-dimensional $\kk$-vector space with a $\TT$-action such that $\deg(\twx_1) + \deg(x_{I\cup J}) = 0$,
and $\deg(\twy_1) + \deg(y_{I}\otimes x_{J}) = 0$. Consider the bundle $\frone := \Iso(\OO_{c_1\sigma_2}\otimes W_1, \UU_1)$ over $c_1\sigma_2$ and
its point that yields an isomorphism of $W_1$ with $\UU_1|_{[T']}$. The preimage of
$[T']$ under this isomorphism is a tensor
\begin{equation}\label{eq:fixedHeightOne}
    \twx_1 \otimes x_{I\cup J} + \twy_1 \otimes y_I \otimes x_J,
\end{equation}
which is fixed under the natural $\TT$-action on $W_1\otimes \Vhatpar{1}$.

Before we proceed with calculations, let us remark that isomorphisms from
Proposition~\ref{p:sigma2_iso_after_3_unres} are equivariant. This means that if 
$\csigma_2 \to c_{1,\dots,i}\sigma_2$ is an isomorphism near a fixed point, then the
weights on the tangent space to $\csigma_2$ are the same as the weights on the tangent space 
to $c_{1,\dots,i}\sigma_2$, so we can make computations on $c_{1,\dots,i}\sigma_2$.
\begin{lemma}\label{ref:weightsHeightOne:lem}
    The weights of $\TT$-action on the tangent space to $\frone$ at~\eqref{eq:fixedHeightOne} are given by
    \begin{align*}
        2e_i,\ -2e_i, & \quad\mbox{where}\quad i\in I,\\
        2e_j,\ 2e_j, & \quad\mbox{where}\quad j\in J,\\
        0, 0,\ \deg(\twx_1)-\deg(\twy_1),\ \deg(\twy_1) - \deg(\twx_1)&,\ 2e_1,\ 2e_I,\ 2e_1 + 2e_I.
    \end{align*}
    Consequently, the weights on the tangent space to $\csigma_2$ are given by
    \begin{align}\label{eq:weightsHeightOne}
        2e_i,\ -2e_i, & \quad\mbox{where}\quad i\in I,\\\notag
        2e_j,\ 2e_j, & \quad\mbox{where}\quad j\in J,\\\notag
                    2e_1,\ 2e_I,\ 2e_1 + 2e_I. &
    \end{align}
\end{lemma}
\begin{proof}
    The space $c_1\sigma_2$ is a quotient of $\frone$ by $\GL(W_1)$ and the weights on the tangent space to $\GL(W_1)$
    are $ 0, 0, \deg(\twx_1)-\deg(\twy_1), \deg(\twy_1) - \deg(\twx_1)$, so the latter statement follows from the former one.

    To compute the weights on $\frone$, we use the smooth map $\alpha_1$ from~\eqref{eq:smoothEquivalenceCsigmaPartial} to reduce to the absolute setting.
    In this setting, the variety $\frone$ is open inside the product
    of $\mathbb{P}\Hom(W_1, V_1\otimes \LL^{\vee}|_{[T]})$ and $\sigmahat_2 \into W_1 \otimes \Vhatpar{1}$.
    The first factor is a projectivisation of the affine space $\Hom(W_1, V_1\otimes \LL^{\vee}|_{[T]})$. The torus weight on $\LL^{\vee}|_{[T]}$
    is $e_1 + e_{I\cup J}$, so the torus weights on $V_1\otimes \LL^{\vee}|_{[T]}$ are $e_{I\cup J}$ and $2e_1 + e_{I\cup J}$. The torus weights on
    $W_1$ are $\deg(\twx_1) = e_{I\cup J}$ and $\deg(\twy_1) = -e_I + e_J$, so the torus weights on $\Hom(W_1, V_1\otimes \LL^{\vee}|_{[T]})$ are
    \[
        0,\ 2e_1,\ 2e_I,\ 2e_1 + 2e_I.
    \]
    We discard the zero weight, since we projectivise.
    
    Finally, we need to understand the tangent space to $\sigmahat_2$
    at~\eqref{eq:fixedHeightOne}. We already know that this is a smooth point
    (sse~\S\ref{ssec:singularitiesMain}),
    so it is easiest to avoid formal use of smooth equivalences from~\S\ref{ssec:smoothEquivalences}
    and just write down $\dim \sigmahat_2 = 2d+2$ linearly independent
    $\TT$-stable tangent directions. Two of them are induced by $\TT$-action and hence have weight $0$.
    The remaining $2d$ are given by adding
    \begin{itemize}
        \item $\varepsilon \twx_1\otimes x_{I\cup J \setminus \{i\}}\otimes y_i$, where $2\leq i\leq d$, this yields $d-1$ directions, the weights are $2e_i$,
        \item $\varepsilon \twy_1\otimes y_{I\cup\{i\}}\otimes x_{J \setminus \{i\}}$, where $i\in J$, this yields $|J|$ directions, the weights are $2e_i$,
        \item $\varepsilon \twy_1\otimes y_{I\setminus\{ i \}}\otimes x_{J\cup \{i\}}$, where $i\in I$, this yields $|I|$ directions, the weights are $-2e_i$,
        \item $\varepsilon \twy_1 \otimes x_{I\cup J}$, $\varepsilon \twx_1 \otimes y_I\otimes x_J$, this yields the remaining two directions, of
            weights $\deg(\twy_1) - \deg(\twx_1)$, $\deg(\twx_1) - \deg(\twy_1)$, respectively.
    \end{itemize}
    This concludes the computation.
\end{proof}

\newcommand{\frtwo}{c_{1,2}\sigma_2^{\mathrm{fr}}}

We pass to points of height two. Let $K := \left\{ 4, \ldots ,d \right\}$. As
explained in Proposition~\ref{ref:sigmaFixedPoints:prop}, there are, up to coordinate changes, three
possibilities.
All of them are obtained by starting from the already considered point $[T] = [x_1\otimes x_2\otimes x_3\otimes x_K]$ and afterwards considering
a subspace
\[
    \spann{x_2\otimes x_3,\ y_2\otimes x_3}\otimes x_K\subseteq \Vhatpar{1}.
\]
Let us take a vector space $W_1 = \spann{\twx_1, \twy_1}$
with weights $\deg(\twx_1) = -\deg(x_2\otimes x_3\otimes x_K)$, $\deg(\twy_1) = -\deg(y_2\otimes x_3\otimes x_K)$ and
frame the above subspace using $W_1$. We obtain a $\TT$-fixed tensor $(\twx_1\otimes x_2\otimes x_3 + \twy_1\otimes y_2 \otimes x_3)\otimes x_K$,
which is concise on the first two coordinates. For reference, we record the relevant weights
\[
        \begin{array}{c c}
            \deg(\twx_1),\ \deg(\twy_1) & e_2 + e_{\{3, \ldots ,d\}},\ -e_2 + e_{\{3, \ldots ,d\}}\\
            T\mathbb{P}\Hom(W_1, V_1\otimes \LL^{\vee}|_{[x_{1}\otimes x_2\otimes x_3\otimes x_K]}) & 2e_1,\ 2e_2, 2e_1 + 2e_2,\\
            T\GL(W_1) & 0,\ -2e_2,\ 2e_2,\ 0
        \end{array}
\]
We then frame the tensor on the second coordinate, using a vector space
$W_2 = \spann{\twx_2, \twy_2}$ with weights $\deg(\twx_2) = \deg(x_2)$, $\deg(\twy_2) = \deg(y_2)$, so that we consider
it as a point of $\frtwo$.
The three fixed points now correspond to the subspaces
\begin{align}
    \spann{\twx_1\otimes \twx_2 + \twy_1\otimes \twy_2,\ \twx_1\otimes \twx_2}\otimes x_K\subseteq W_{1,2} \otimes V_{4, \ldots ,d}.\label{eq:fixedHeightTwoTypeOne}\\
    \spann{\twx_1\otimes \twx_2 + \twy_1\otimes \twy_2,\ \twx_1\otimes \twy_2}\otimes x_K\subseteq W_{1,2} \otimes V_{4, \ldots ,d}.\label{eq:fixedHeightTwoTypeTwo}\\
    \spann{\twx_1\otimes \twx_2 + \twy_1\otimes \twy_2,\ \twy_1\otimes \twx_2}\otimes x_K\subseteq W_{1,2} \otimes V_{4, \ldots ,d}.\label{eq:fixedHeightTwoTypeThree}
\end{align}
Finally, we frame each of them using the vector space $W_3$, which will have different weights in each case.
The case~\eqref{eq:fixedHeightTwoTypeOne} is very similar to the previous one, as also here the full unrestriction is the unit tensor.
\begin{lemma}\label{ref:weightsHeightTwoTypeOne:lem}
    The weights of $\TT$-action on the tangent space to $\csigma_2$ at~\eqref{eq:fixedHeightTwoTypeOne} are given by
    \begin{equation}\label{eq:weightsHeightTwoTypeOne}
        2e_1,\ 2e_2,\ 2e_1 + 2e_2,\ 2e_3,\ 2e_3,\ 2e_2,\ -2e_2,\ 2e_k, 2e_k, \mbox{ for } k=4, \ldots d
    \end{equation}
\end{lemma}
\begin{proof}
    We follow the proof of Lemma~\ref{ref:weightsHeightOne:lem} and only highlight the changes.
    For framing, it is useful to choose a slightly different basis, so that we obtain a tensor
    \[
        (\twx_1 \otimes \twx_2 \otimes \twx_3 + \twy_1 \otimes \twy_2 \otimes \twy_3)\otimes x_K.
    \]
    The tangent space to $c_{1,2,3}\sigma_2^{\mathrm{fr}}$ at this point decomposes into the tangent
    spaces to $\mathbb{P}\Hom(W_1, V_1\otimes \LL^{\vee}|_{[x_{1}\otimes x_2\otimes x_3\otimes x_K]})$, $\Hom(W_2, V_2)$,
    $\Hom(W_3, V_3)$, and $\sigmahat_2$, and then we need to subtract the weights coming from the tangent 
    space to $\GL(W_1)$, $\GL(W_2)$, $\GL(W_3)$. Observe that the weights of $\GL(W_2)$ and $\Hom(W_2,V_2)$ are the same and
    we can discard them. The remaining weights are as follows
    \[
        \begin{array}{c c}
            \deg(\twx_3), \deg(\twy_3) & -e_3,\ -e_3\\
            T\Hom(W_3, V_3) & 0,\ 2e_3,\ 0, 2e_3\\
            T\sigmahat_2 & 0, 0, \pm 2e_2, \pm 2e_2, 0, 0, 2e_k, 2e_k\mbox{ for } k=4, \ldots ,d\\
            T\GL(W_3) & 0, 0, 0, 0
        \end{array}
    \]
    For the weights on $T\sigmahat_2$, we note that the first two zeros come from the torus action, the next $6$ entries
    are obtained by adding monomials
    \[
        \varepsilon \twy_1 \otimes \twx_2 \otimes \twx_3,\
        \varepsilon \twx_1 \otimes \twy_2 \otimes \twy_3,\
        \varepsilon \twx_1 \otimes \twy_2 \otimes \twx_3,\
        \varepsilon \twy_1 \otimes \twx_2 \otimes \twy_3,\
        \varepsilon \twx_1 \otimes \twx_2 \otimes \twy_3,\
        \varepsilon \twy_1 \otimes \twy_2 \otimes \twx_3,
    \]
    multiplied by $x_K$, while the
    remaining $2d-6$ entries are given by adding
    $\varepsilon\twx_{1,2,3} \otimes x_{\{K\setminus j\}}\otimes y_j$, $\varepsilon\twy_{1,2,3}\otimes x_{\{K\setminus j\}}\otimes y_j$,
    for $j\geq 4$.
\end{proof}
The cases~\eqref{eq:fixedHeightTwoTypeTwo}-\eqref{eq:fixedHeightTwoTypeThree}
are obtained from each other by coordinate change and we treat them together.
These cases are a bit different from the previous one, as the unrestriction is a W-state, hence in $\csigma_2$ there is also 
a tangent direction going outside the orbit. In both cases, these direction are supplied by the following
families of border rank two tensors, where $\lambda\in \kk$
\begin{align}\label{eq:normalDirection}
    (\twx_1\otimes \twx_2 \otimes \twx_3 + \twy_1 \otimes \twy_2 \otimes \twx_3 + \twx_1 \otimes \twy_2 \otimes \twy_3 + \lambda \twy_1 \otimes \twx_2\otimes \twy_3)\otimes x_K,\\\notag
    (\twx_1\otimes \twx_2 \otimes \twx_3 + \twy_1 \otimes \twy_2 \otimes \twx_3 + \twy_1 \otimes \twx_2 \otimes \twy_3 + \lambda \twx_1 \otimes \twy_2\otimes \twy_3)\otimes x_K.
\end{align}

\begin{lemma}\label{ref:weightsHeightTwoTypeTwo:lem}
    The weights of $\TT$-action on the tangent space to $\csigma_2$ at~\eqref{eq:fixedHeightTwoTypeTwo} are given by
    \begin{equation}\label{eq:weightsHeightTwoTypeTwo}
        2e_1,\ 2e_2,\ 2e_1 + 2e_2,\ 2e_3,\ 2e_2 + 2e_3,\ -2e_2,\ -4e_2, \mbox{ and }
        2e_k, 2e_k+2e_2,\mbox{ where }\quad k=4, \ldots d.
    \end{equation}
\end{lemma}
\begin{proof}
    The strategy is once more the same as in
    Lemma~\ref{ref:weightsHeightTwoTypeOne:lem}, with the one change being
    that we need to include the weight coming from~\eqref{eq:normalDirection}
    among the tangent weights in the $\sigmahat_2$ part and calculate the orbit weights. We record the weights as follows
    \[
        \begin{array}{c c}
            \deg(\twx_3), \deg(\twy_3) & -e_3,\ -e_3 - 2e_2\\
            T\Hom(W_3, V_3) & 0,\ 2e_3,\ 2e_2, 2e_2 + 2e_3\\
            T\sigmahat_2 & 0, 0, 0, -2e_2, -2e_2, \pm2e_2, \mathbf{-4e_2}, 2e_k, 2e_k+2e_2\mbox{ for } k=4, \ldots ,d\\
            T\GL(W_3) & 0,\ -2e_2,\ 2e_2,\ 0
        \end{array}
    \]
    In the orbit we have $3$ directions coming from adding an element of
    \[
        \spann{\twx_1\otimes \twx_2 \otimes \twx_3, \twy_1 \otimes \twy_2 \otimes \twx_3, \twx_1 \otimes \twy_2 \otimes \twy_3}\otimes x_K.
    \]
    They have weight $0$. Next, there are three directions coming from
    coordinate changes $\twx_1 \mapsto \varepsilon \twy_1$, $\twy_2 \mapsto
    \varepsilon \twx_2$, $\twx_3 \mapsto \varepsilon \twy_3$. They all have weight
    $-2e_2$. There is a direction coming from adding $\varepsilon \twx_1\otimes \twy_2 \otimes \twx_3 \otimes x_K$. It has weight $2e_2$.
Additionally, we have $d-4$ directions coming from adding $\varepsilon \twx_{1}\otimes \twy_{2}\otimes \twx_{3}\otimes y_k \otimes x_{K\setminus\{k\}}$.
    These yield weights $2e_k+2e_2$, $4\leq k\leq d$. We also have $d-4$ directions coming from the coordinate changes $x_i\mapsto \varepsilon y_i$.
    Also these yield weights $2e_k$, $4\leq k\leq d$.

    The last tangent direction comes from~\eqref{eq:normalDirection}, it is bolded above. It has weight $-4e_2$.
\end{proof}

\begin{lemma}\label{ref:weightsHeightTwoTypeThree:lem}
    The weights of $\TT$-action on the tangent space to $\csigma_2$ at~\eqref{eq:fixedHeightTwoTypeThree} are given by
    \begin{equation}\label{eq:weightsHeightTwoTypeThree}
        2e_1,\ 2e_2,\ 2e_2,\ 2e_1 + 2e_2,\ 2e_3,\ -2e_2 + 2e_3,\ 4e_2 \mbox { and }
        2e_k, 2e_k-2e_2,\mbox{ where }\quad k=4, \ldots d.
    \end{equation}
\end{lemma}
\begin{proof}
    This case is resolved exactly as the previous one. The weights are
    \[
        \begin{array}{c c}
            \deg(\twx_3), \deg(\twy_3) & -e_3,\ -e_3 + 2e_2\\
            T\Hom(W_3, V_3) & 0,\ 2e_3,\ -2e_2, -2e_2 + 2e_3\\
            T\sigmahat_2 & 0, 0, 0, 2e_2, 2e_2, 2e_2, -2e_2, \mathbf{4e_2}, 2e_k, 2e_k-2e_2\mbox{ for } k=4, \ldots ,d\\
            T\GL(W_3) & 0,\ -2e_2,\ 2e_2,\ 0
        \end{array}
    \]
    The three directions coming from
    coordinate changes are $\twy_1 \mapsto \varepsilon \twx_1$, $\twx_2 \mapsto
    \varepsilon \twy_2$, $\twx_3 \mapsto \varepsilon \twy_3$, with weights $2e_2$, $2e_2$, $2e_2$.
    There is a direction coming from adding $\varepsilon \twy_1\otimes \twx_2 \otimes \twx_3 \otimes x_K$. It has weight $-2e_2$.
    The bold entry comes from~\eqref{eq:normalDirection}. In this case, we have
    $d-4$ directions coming from adding $\varepsilon \twy_{1}\otimes
    \twx_{2,3}\otimes y_k \otimes x_{K\setminus\{k\}}$. These
    yield weights $2e_k-2e_2$, $4\leq k\leq d$.
\end{proof}

\newcommand{\Knot}{K_{0}(\operatorname{Var}_{\kk})}

The following proposition gives the classes of $\csigma_2$ and $\sigma_2$ in the ring $\Knot$, denoted by
$[\csigma_2]$, $[\sigma_2]$, respectively; these are so-called motives. Computing the motive of a smooth projective variety, such as $\csigma_2$, allows to
compute the Betti numbers and the Hodge diamond, in particular. Computing the motive of a singular variety (not necessarily
projective), such as $\sigma_2$, allows one to compute the number of $\mathbb{F}_p$-points of this variety.
We use the notation $\Lmot{} := [\mathbb{A}^1_{\kk}]$.
\begin{proposition}[Betti numbers of $\csigma_2$ and $\sigma_2$]\label{ref:motivecsigma2:prop}
    Let $\csigma_2$ be the second concise secant and let $\sigma_2\subseteq \mathbb{P}(\tspace)$ be the ordinary secant. Their motives are
    given by the formula
    \begin{align*}
        [\csigma_2] =  (1+\Lmot)&\cdot (1+\Lmot^2)\cdot \left( \frac{1}{2}\left( (1+\Lmot)^{2(d-1)} + (1+\Lmot^2)^{d-1} \right) + \Lmot{}\cdot (1+\Lmot{})^{d-1}\cdot \left( 1+\Lmot{}+\Lmot{}^2+ \ldots +\Lmot{}^{d-3} \right) \right)\\
        [\sigma_2] = [\csigma_2] &- \binom{d}{2}\left( \Lmot{}^3-\Lmot{} \right)\cdot (\Lmot{}+\Lmot{}^2)\cdot (1+\Lmot{})^{d-2}-\\
                                 &- \left( (\Lmot{}+1)^{d-1}+(\Lmot{}+\Lmot{}^2+ \ldots +\Lmot{}^{d-2}) + (d-1)\Lmot{}^2 - 1 \right)\cdot (1+\Lmot{})^{d}.
    \end{align*}
    In particular, both varieties admit a polynomial point count. The Picard rank of $\csigma_2$ is $d$.
\end{proposition}
\begin{proof}
    \def\diag{\operatorname{diag}}%
    We begin with computing $[\csigma_2]$. The overall idea is to use the \BBname{} decomposition~\cite{Ellingsrud_Stromme__On_the_homology}.
    Consider the torus $\TT\subseteq \SLV$ and fix a one-parameter subgroup $\Gmult \into \TT$ given by
    diagonal matrices $\diag(t^{-e_1}, t^{e_1})$, $\diag(t^{-e_2}, t^{e_2})$, \ldots, $\diag(t^{-e_d}, t^{e_d})$,
    where $0 < e_1 \ll e_2 \ll \ldots \ll e_d$.
    The fixed points of $\Gmult$ coincide with the fixed points for $\TT$ and, in particular, are isolated.
    By general theory of \BBname{}~\cite{BialynickiBirula__decomposition} decompositions, see \jjetoadd, we obtain that
    \[
        [\csigma_2] = \bigoplus_{x\in \csigma_2^{\Gmult}} \Lmot{}^{n_x},
    \]
    where $n_x$ is the number of positive weights in the tangent space at the fixed point $x$.
    These weights were computed in Lemmas~\ref{ref:weightsHeightOne:lem}, \ref{ref:weightsHeightTwoTypeOne:lem}, \ref{ref:weightsHeightTwoTypeTwo:lem},
    \ref{ref:weightsHeightTwoTypeThree:lem} above. Computing the weights, we arrive at the formula; we omit the
    combinatorics part here.

    Recall the map $\rho\colon \csigma_2\to \sigma_2$.
    We use the \BBname{} decomposition also to compute the motive of the fibre $\rho^{-1}([T_0])$, where $[T_0]\in \Seg$ is
    a tensor of rank one. Up to coordinate change, we may assume that $T_0 = x_1\otimes \ldots \otimes x_d$.
    In the \BBname{} decomposition of $\mathbb{P}(\tspace)$, the point $[T_0]$ is isolated: no other point converges to it.
    The morphism $\rho$ is equivariant, hence the fibre $\rho^{-1}([T_0])$ is a union of \BBname{} cells for the variety $\csigma_2$.
    Counting the positive weights (but only for fixed points in the fibre!), we learn that the motive of the fibre is
    \begin{equation}\label{eq:fibreMotive}
        (\Lmot{}+1)^{d-1}+(\Lmot{}+\Lmot{}^2+ \ldots +\Lmot{}^{d-2}) + (d-1)\Lmot{}^2.
    \end{equation}
    To compute the class of $\sigma_2$ we use the fact that for every locally-closed subvariety $V$ of a variety $X$,
    we have $[X] = [V] + [X\setminus V]$ in $\Knot$. Informally speaking, cutting and pasting is allowed.
    To compute $[\sigma_2]$, we subdivide points of $\sigma_2$ into three groups:
    \begin{itemize}
        \item tensors not concise on any coordinate, which form the Segre subvariety $\Seg \subseteq \sigma_2$,
        \item tensors concise on exactly two coordinates, which form a locally-closed subvariety $\sigma_2'\subseteq \sigma_2$,
        \item tensors concise on at least three coordinates, which form an open subvariety $\sigma_2^{\op}\subseteq \sigma_2$.
    \end{itemize}
    The fibre over a tensor in $\sigma_2^{\op}$ is a point, as explained in Proposition~\ref{p:sigma2_iso_after_3_unres}.
    The fibre over a tensor in $\sigma_2'$ is a $\mathbb{P}^2$, as explained in the proof of Proposition~\ref{ref:sigmaFixedPoints:prop}.
    The fibre over a tensor in $\Seg$ is given in~\eqref{eq:fibreMotive}.

    It remains to compute how many tensors in $\Seg$ and $\sigma_2'$ are there. The Segre variety has motive $[\mathbb{P}^1]^d = (\Lmot{}+1)^d$.
    The locus $\sigma_2'$ consists of $\binom{d}{2}$ copies of 
    $(\mathbb{P}^3 \setminus \mathbb{P}^1\times\mathbb{P}^1) \times (\PP^1)^{d-2}$, which has motive
    $((\Lmot{}^3 + \Lmot{}^2 + \Lmot{} + 1) - (\Lmot{}+1)^2) (\Lmot{} + 1)^{d-2} = 
    (\Lmot{}^3 - \Lmot{})(\Lmot{} + 1)^{d-2}$. Since in $\csigma_2$ it comes multiplied by $[\mathbb{P}^2] =
    \Lmot{}^2 + \Lmot{} + 1$,
    while in $\sigma_2$ just by $1$, we remove $\Lmot{}^2 + \Lmot{}$.
\end{proof}




\section{Smoothable and cactus ranks}

    % This section is logically independent from the previous ones. It is included, because it will be crucial for
    % the embedding of the abstract secant variety into $\csigma_m$, see Section~\ref{sec:abstractSecant}.
    In this section, we produce an open embedding $\AsigmaHilb_m$ into $\csigma_m$.

    To do this, we propose a new way of thinking about several familiar objects. Since this may be confusing,
    let us explain in broad strokes the content.
    We will be working with the following objects: a finite algebra $\cA$, modules $W_1^{\vee}$, \ldots , $W_d^{\vee}$ over $\cA$
    which are isomorphic to $\cA^{\oplus 1}$ itself, linear maps $\varphi_i\colon W_i\to V_i$ and a tensor $\Tppar{}\in \tconcspace$.
    These objects will appear in three configurations.
    \begin{enumerate}
        \item Evaluations tensors associated to an algebra. In this setting $W_1^{\vee} =  \ldots = W_d^{\vee} = \cA^{\oplus 1}$,
            $\Tppar{}$ is an evaluation tensor and the maps
            $\varphi_{\bullet}$ yield a restriction of $\Tppar{}$ to a tensor in $\tspace$.
        \item Line bundles and algebraic characterisation of spans. In this setting, we additionally have a
            finite scheme $Z$ with a map $Z\to \mathbb{P}V_1\times \ldots
            \times \mathbb{P}V_d$. Here $\cA = H^0(\OO_{Z})$,
            the morphisms $Z\to \mathbb{P}V_i$ induce surjections $\cA \otimes_{\kk} V_i^{\vee}\onto
            W_i^{\vee}$ onto 
            line bundles $W_i^{\vee}$, and the surjections yield restriction maps
            $W_i\to V_i$.
        \item Algebras from centroids. In this setting, $\Tppar{}$ is a $1$-generic tensor and the maps $\varphi_i\colon W_i\to V_i$ yield its restriction
            to a tensor in $\tspace$. Here, $\cA = \Cen{\Tppar{}}$, the $\cA$-module structure
            on $W_i^{\vee}$ comes from the centroid action, and the isomorphisms $W_i^{\vee}\simeq \cA^{\oplus 1}$ are consequences of
            $1$-genericity.
    \end{enumerate}
    
    \subsection{Evaluation tensors}\label{ssec:evaluation}
    Let $\cA$ be a finite $\kk$-algebra. By its \emph{(iterated) multiplication tensor} we mean 
    the tensor in $\cA^{\vee}\otimes \ldots \otimes \cA^{\vee}\otimes \cA$ associated to be the multiplication map
    \[
        \underbrace{\cA\times \ldots \times\cA}_{d-1}\to \cA.
    \]
    Let $\epsilon \colon \cA\to \kk$ be a
    functional. The \emph{(order $d$) evaluation tensor} associated to $(\cA, \epsilon)$ is
    an element of $\cA^{\vee}\otimes \ldots \otimes \cA^{\vee}$ given by the composed multilinear map
    \begin{equation}\label{eq:evaluationTensor}
        \begin{tikzcd}
            \eval\colon \underbrace{\cA\times  \ldots \times \cA}_d \ar[r, "\mathrm{mult.}"] & \cA \ar[r, "\epsilon"]
            & \kk.
        \end{tikzcd}
    \end{equation}
    Recall that a finite algebra $\cA$ is \emph{Gorenstein} if there exists a functional $\epsilon \in \cA^{\vee}$
    such that $\cA^{\vee} = \cA\cdot \epsilon$. Every such functional is called a \emph{dual generator} of $\cA$.

    \begin{proposition}\label{ref:evaluationTensors:prop}
        Let $\cA$ be a finite $\kk$-algebra. Let $d\geq 2$ be an integer. The following conditions are
        equivalent for a tensor $T$:
        \begin{enumerate}
            \item\label{it:evalOne} the tensor $T$ is isomorphic to an evaluation tensor
                associated to some $\epsilon\colon \cA\to \kk$,
            \item\label{it:evalTwo} the tensor $T$ is isomorphic to a
                multiplication tensor of a
                Gorenstein quotient algebra $\cA' = \cA/I$.
        \end{enumerate}
        In particular, if there exists a concise evaluation tensor $T\in \cA^{\vee}\otimes \ldots \otimes \cA^{\vee}$, then
        $\cA$ is Gorenstein.
    \end{proposition}
    \begin{proof}
            $\ref{it:evalOne}\implies \ref{it:evalTwo}$. Let $I = \left\{ a\in \cA\
            |\ \epsilon(\cA\cdot a) = 0 \right\}$. This is an ideal of $\cA$. Let
            $\cA' := \cA/I$.

            The functional $\epsilon$ vanishes on $I$, so it
            yields a functional $\epsilon'\colon \cA'\to \kk$ given by
            $\epsilon'(a + I) := \epsilon(a)$.
            Consider the map $\varphi\colon \cA'\to (\cA')^{\vee}$
            given by $\varphi(a')= a'\cdot \epsilon'$. If $\varphi(a') = 0$
            for some $a' = a + I\in \cA'$, then $\epsilon(\cA a) = 0$, so $a\in I$ and
            $a' = 0$. This
            shows that $\varphi$ is injective. The dimensions of $\cA'$,
            $(\cA')^{\vee}$ are the same, so $\varphi$ is bijective, hence $\cA'$
            is Gorenstein with dual generator $\epsilon'$.

            The evaluation tensor can be rewritten as a multilinear map
            \[
                T\colon \underbrace{\cA\times  \ldots \times \cA}_{d-1} \to \cA^{\vee}
            \]
            given by $T(a_1, \ldots ,a_{d-1}) := (a_1 \ldots a_{d-1})\cdot
            \epsilon$. Whenever at least one $a_j$ lies in $I$, then $T(a_1, \ldots
            ,a_{d-1}) = 0$, so $T$ is isomorphic to a multilinear map
            \[
                T'\colon \underbrace{\cA'\times  \ldots \times \cA'}_{d-1} \to (\cA')^{\vee}
            \]
            given by $T'(a_1', \ldots ,a_{d-1}') := (a_1' \ldots a_{d-1}')\cdot
            \epsilon'$. Composing with the isomorphism $\varphi^{-1}\colon
            (\cA')^{\vee} \to \cA'$, we obtain that $T'$ is isomorphic to the
            multiplication tensor in $\cA'$.

            $\ref{it:evalTwo}\implies \ref{it:evalOne}$. The algebra $\cA'$ is
            Gorenstein and finite, hence there exists a functional
            $\epsilon'\colon \cA' \to \kk$ such that $(\cA')^{\vee} = \cA'\cdot
            \epsilon'$. Let $\varphi\colon \cA'\to (\cA')^{\vee}$ be given by
            $\varphi(a') = a'\cdot \epsilon'$ and let $\epsilon\colon \cA\to
            \kk$ be the composition of $\cA\onto \cA'$ and $\epsilon'$. The proof
            above reverses and shows that the multiplication tensor in $\cA'$ is
            isomorphic to the evaluation tensor associated to $(\cA, \epsilon)$.

            To prove the final statement, observe that $T$ is isomorphic to a multiplication
            tensor in a Gorenstein quotient algebra $\cA' = \cA/I$ but by conciseness, we have
            $I = 0$.
    \end{proof}

    \begin{corollary}\label{ref:dualSocle:cor}
        Let $\cA$ be a finite Gorenstein algebra and $\epsilon \colon \cA\to \kk$ be a
        dual generator. The evaluation tensor associated to $(\cA, \epsilon)$ is
        isomorphic to the multiplication tensor of $\cA$. In particular, the
        tensors associated to different $\epsilon$ are all isomorphic.
    \end{corollary}
    \begin{proof}
        Follows from Proposition~\ref{ref:evaluationTensors:prop}.
    \end{proof}
    Corollary~\ref{ref:dualSocle:cor} was also obtained independently in~\cite{Chang_Gesmundo_Zuiddam}.

    \begin{remark}\label{ref:evaluationTensorsLineBundles:rem}
        One can slightly generalise the notion of evaluation tensor. Namely, let $\cA$ be a finite algebra
        and $W_1^{\vee}$, \ldots , $W_d^{\vee}$ be $\cA$-modules isomorphic to $\cA^{\oplus 1}$.
        For a functional $\epsilon \colon W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee}\to \kk$,
        we can form a generalised evaluation tensor
        \[
            \begin{tikzcd}
                W_1^{\vee}\otimes_{\kk} \ldots \otimes_{\kk} W_d^{\vee} \ar[r, two heads] & W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee}
                \ar[r, "\epsilon"] & \kk.
            \end{tikzcd}
        \]
        It corresponds to an element
        \[
            \epsilon \in (W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee})^{\vee}\subset \left( W_1^{\vee}\otimes_{\kk} \ldots \otimes_{\kk} W_d^{\vee} \right)^{\vee} = \tconcspace.
        \]
    \end{remark}
    

    \subsection{Line bundles and algebraic characterisation of spans}\label{ssec:lineBundlesAndSpans}


    Let $Z$ be a zero-dimensional scheme. We will use the words \emph{finite scheme} and \emph{zero-dimensional} scheme
    interchangeably, preferring the word finite. If $Z = \Spec(\cA)$, then the \emph{degree} of $Z$ is defined as $\dim_{\kk} \cA$.
    We will usually consider schemes of degree $\leq m$.

    Let $Z = \Spec(\cA)$ be a finite scheme with a morphism $Z\to \mathbb{P}V_1
    \times \ldots \times \mathbb{P}V_d$. To give such a morphism is the same as to give
    surjections $\cA \otimes_{\kk} V_i^{\vee} \onto W_i^{\vee}$ for $i=1, \ldots ,d$, where $W_i^{\vee}$ are
    line bundles on $Z$. We identify the line bundles with their global sections, so that $W_i^{\vee}$ becomes
    a vector space which is a $\cA$-module that is isomorphic to $\cA^{\oplus 1}$. In this way $W_i$ is also a $\cA$-module, which
    is, however, not necessarily isomorphic to $\cA^{\oplus 1}$. It may seem odd that $W_i^{\vee}$ plays a bigger role than $W_i$,
    but this convention is necessary to be compatible with unrestrictions, see~\S\ref{sec:abstractSecant}.

    The \emph{linear span} of $Z$,
    denoted $\spann{Z}$ is the smallest linear subspace $\spann{Z}\subseteq
    \tspace$ such that the image of $Z$ lies in $\mathbb{P}\spann{Z}\subseteq
    \mathbb{P}\tspace$. The linear span is usually defined only for closed embeddings.

    \begin{proposition}[Linear span from a tensor product]\label{ref:linearSpanAbstract:prop}
        Let $Z=\Spec(\cA)$ be a finite scheme with a morphism $Z\to \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$ and let
        $\cA\otimes_{\kk} V_i^{\vee}\onto W_i^{\vee}$ be the associated line bundles. Let $\varphi_i\colon W_i\to V_i$ be dual to
        $V_i^{\vee}\into \cA \otimes_{\kk} V_i^{\vee}\onto W_i^{\vee}$.
        The linear span of $Z$ is equal to the image of
        \[
            (W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA}
            W_d^{\vee})^{\vee} \into W_1 \otimes_{\kk} \ldots \otimes_{\kk} W_d
            \to V_1\otimes_{\kk} \ldots \otimes_{\kk} V_d.
        \]
    \end{proposition}
    \begin{proof}
        The ideal of $\spann{Z}$ is given by the kernel of the restriction map
        \[
            V_1^{\vee} \otimes_{\kk} \ldots
            \otimes_{\kk} V_d^{\vee} = H^0\left(
            \OO_{\mathbb{P}V_1\times \ldots \times\mathbb{P}V_d}(1,1, \ldots ,1)
            \right) \to H^0(\OO_{Z}(1,1, \ldots ,1)).
        \]
        To compute it, we complete this diagram to
        \begin{equation}\label{eq:linearSpanDiagram}
            \begin{tikzcd}
                V_1^{\vee}\ar[d, "\varphi_1^{\vee}"]\ar[rr, phantom, "\otimes_{\kk} \ldots
                \otimes_{\kk}"] && V_d^{\vee} \ar[d, "\varphi_d^{\vee}"]\ar[r] & H^0(\OO_{Z}(1,1, \ldots ,1))\\
                W_1^{\vee} \ar[rr, phantom, "\otimes_{\kk}  \ldots \otimes_{\kk}"] && W_d^{\vee} \ar[r, two heads] &
                W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee} \ar[u, "\simeq"]
            \end{tikzcd}
        \end{equation}
        Therefore, the ideal is the kernel of the composition
        \[
            V_1^{\vee} \otimes_{\kk} \ldots \otimes_{\kk} V_d^{\vee} \to
            W_1^{\vee}\otimes_{\kk} \ldots \otimes_{\kk} W_d^{\vee} \onto
            W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee},
        \]
        so the span is the image of the dual map, as claimed.
    \end{proof}

    \begin{example}[``Universal'' span]\label{ex:universalLinearSpan}
        For any finite scheme $Z = \Spec(\cA)$ we can take line bundles $W_i^\vee := \cA$ 
        and vector spaces $V_i := \cA^\vee$.
        Multiplication maps $\cA \otimes_\kk V_i^\vee \onto W_i^\vee$ yield an embedding 
        $Z \into \PP V_1\times \ldots \times \PP V_d = \PP\cA^{\vee}\times \ldots \times \PP\cA^{\vee}$.
        The associated restrictions $\varphi_i \colon W_i \to V_i$
        are just the identity maps and the map 
        \[
            \cA \otimes_\kk \ldots \otimes_\kk \cA =
            W_1^{\vee}\otimes_{\kk} \ldots \otimes_{\kk} W_d^{\vee} \onto
            W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee} =
            \cA \otimes_\cA \ldots \otimes_\cA \cA =
            \cA
        \]
        is just the iterated multiplication in $\cA$. 
        By Proposition~\ref{ref:linearSpanAbstract:prop}, the linear span $\spann{Z}$ is the image of
        the dual map of $\cA \otimes_\kk \ldots \otimes_\kk \cA \xrightarrow{\mathrm{mult.}} \cA$, that is,
        the image of
        \[
            \cA^\vee \to \cA^\vee \otimes_\kk \ldots \otimes_\kk \cA^\vee,\quad
            (\epsilon \colon \cA \to \kk) \mapsto 
            (\eval \colon \cA \otimes_\kk \ldots \otimes_\kk \cA \xrightarrow{\mathrm{mult.}} \cA \xrightarrow{\epsilon} \kk).
        \]
        In words, tensors in $\spann{Z} \subset \cA^\vee \otimes \ldots \otimes \cA^\vee$ are exactly the 
        evaluation tensors associated to functionals $\epsilon \colon \cA \to \kk$.
    \end{example}
    
    To proceed, we introduce two nondegeneracy conditions on restrictions: regularity and begin jointly
    spanning. The latter will not be needed until much later, so the reader is free to ignore it for the time being.
    
    \begin{definition}\label{ref:regularMap:def}
        Let $Z = \Spec(\cA)$ be a finite scheme, $W^{\vee}$ be a line bundle on $\cA$, and $V$ be a vector space with
        a linear map $\varphi\colon W \to V$. We say that $\varphi$ is
        \emph{regular} if the linear map $\cA \otimes_\kk V^{\vee} \to W^{\vee}$ given by $(a,
        v^{*})\mapsto a\varphi^{\vee}(v^*)$ is surjective, so that it gives a morphism 
        $Z \to \PP V$.
    \end{definition}

    \begin{definition}\label{ref:regularAndJointlySpanning:def}
        Let $Z = \Spec(\cA)$ be a finite scheme, $W_1^{\vee}$,  \ldots , $W_{d}^{\vee}$ be line bundles on $\cA$
        and $V_1, \ldots ,V_d$ be vector spaces with linear maps $\varphi_i\colon W_i\to V_i$ for $i=1, \ldots ,d$.
        \begin{enumerate}
            \item We say that $\varphi_1, \ldots ,\varphi_d$ is a \emph{regular restriction} if every $\varphi_1, \ldots ,\varphi_d$
                is regular,
            \item We say that $\varphi_1, \ldots ,\varphi_d$ are \emph{jointly spanning} if the composition
                \[
                    (W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA}
                    W_d^{\vee})^{\vee} \into W_1 \otimes_{\kk} \ldots \otimes_{\kk} W_d
                    \to V_1\otimes_{\kk} \ldots \otimes_{\kk} V_d
                \]
                is injective.
        \end{enumerate}
        
    \end{definition}
    It will be useful to rephrase the notion of jointly spanning in dual terms. We have the following diagram
    \begin{equation}\label{eq:jointSpanConcrete}
            \begin{tikzcd}
                V_1^{\vee}\ar[rr, phantom, "\otimes_{\kk} \ldots \otimes_{\kk}"]\ar[d, equal] &&[-0.5cm] V_d^{\vee}\ar[d, equal]\ar[r, "\varphi_{\bullet}^{\vee}"] & W_1^{\vee}\ar[d, "\simeq"] \ar[rr, phantom, "\otimes_{\kk}  \ldots \otimes_{\kk}"] &&[-0.5cm] W_d^{\vee}\ar[d, "\simeq"] \ar[r, two heads, "\mathrm{mult.}"] & W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee}\ar[d, "\simeq"]\\
                V_1^{\vee}\ar[rr, phantom, "\otimes_{\kk} \ldots \otimes_{\kk}"] &&[-0.5cm] V_d^{\vee}\ar[r] & \cA \ar[rr, phantom, "\otimes_{\kk}  \ldots \otimes_{\kk}"] &&[-0.5cm] \cA \ar[r, two heads, "\mathrm{mult.}"] & \cA
            \end{tikzcd}
        \end{equation}
        and the restrictions $\varphi_{\bullet}$ are jointly spanning if the resulting linear map $\tspace^{\vee} \to \cA$ is surjective.

    \begin{lemma}\label{ref:regularity:lem}
        If $\varphi_1, \ldots ,\varphi_d$ are jointly spanning, then every $\varphi_1$, \ldots , $\varphi_d$ is regular.
        If $(\varphi_i)_{i\in I}$ are jointly spanning for some $I\subseteq \{1, \ldots ,d\}$ and $\varphi_j$ is regular,
        for some $j\in \left\{ 1, \ldots ,d \right\}$, then $(\varphi_i)_{i\in I\cup \{j\}}$ are also jointly spanning.
        % (regularity was defined in Definition~\ref{ref:regularMap:def}).
    \end{lemma}
    \begin{proof}
        Suppose that $\varphi_i$ is not regular for some $i$. This is
        equivalent to saying that the ideal of $\cA$ generated by the image
        of $\varphi_i^{\vee}$ is not the whole $\cA$. In other words, $\im
        \varphi_i^{\vee}$ lies in an ideal $I\subsetneq \cA$. Then also the
        image of the first map of~\eqref{eq:jointSpanConcrete} is contained in $I$,
        hence the map is not surjective.

        Suppose now that $(\varphi_i)_{i\in I}$ are jointly spanning. In the
        formalism of~\eqref{eq:jointSpanConcrete}, this means that $\prod_{i\in
        I}\varphi_i^{\vee}(V_i^{\vee}) = \cA$. Since $\varphi_j$ is regular, we have
        $\cA\cdot \varphi_j^{\vee}(V_{j}^{\vee}) = \cA$. Putting this together, we have
        \[
            \prod_{i\in I\cup \{j\}} \varphi_i^{\vee}(V_i^{\vee}) = \left(\prod_{i\in I} \varphi_i^{\vee}(V_i^{\vee})\right)\cdot \varphi_j^{\vee}(V_j^{\vee}) = 
            \cA\cdot \varphi_j^{\vee}(V_j^{\vee}) = \cA,
        \]
        so the claim follows by~\eqref{eq:jointSpanConcrete} again.
    \end{proof}

    \begin{example}[Not jointly spanning regular maps]\label{ex:jointSurjectivity}
        Let $\cA = \kk[x]/(x^{5})$.
        Let $W_1^{\vee} = W_2^{\vee} = W_3^{\vee} = \cA$. Let $V_1^{\vee} = V_2^{\vee} = V_3^{\vee} = \spann{1, x}$ and let $V_i^{\vee} \to W_i^{\vee}$
        be the inclusion maps. They correspond to regular restrictions $W_i \to V_i$. The sequence~\eqref{eq:jointSpanConcrete} is
        \[
            \begin{tikzcd}
                \spann{1, x} \otimes_\kk \spann{1, x}\otimes_\kk  \spann{1, x} \ar[r, hook] & \cA \otimes_\kk \cA \otimes_\kk \cA \ar[r, two heads, "\mathrm{mult.}"] & \cA
            \end{tikzcd}
        \]
        which is not surjective, so the restrictions $(W_i\to V_i)_{i=1,2,3}$ are not jointly spanning.
    \end{example}
    
    Having dealt with the conditions on restrictions, we proceed to our main statements.

    \begin{theorem}[Cactus Apolarity Lemma]\label{ref:spanChar:thm}
        Let $T$ in $\tspace$ be a tensor and $\cA$ be a finite $\kk$-algebra. Let $Z = \Spec(\cA)$. The following are equivalent:
        \begin{enumerate}
            \item\label{it:spansGeo} there exists a morphism $Z \to \mathbb{P}V_1\times \ldots
                \times \mathbb{P}V_d$ such that $T$ lies in the linear span
                $\spann{Z}$,
            \item\label{it:spansAlg} there exist regular linear maps $\varphi_i\colon \cA^{\vee} \to V_i$ 
                and a functional $\epsilon \colon \cA \to \kk$ such that the tensor $T$ is associated to the
                multilinear map
                \[
                    \begin{tikzcd}
                        V_1^{\vee} \ar[d, "\varphi_1^{\vee}"]\ar[r, phantom, "\times
                        \ldots \times"] & V_{d}^{\vee}\ar[d,
                        "\varphi_d^{\vee}"] \ar[rr] && \kk\ar[d, equal]\\
                        \cA \ar[r, phantom, "\times \ldots \times"] & \cA \ar[r,
                        "\mathrm{mult.}"]& \cA \ar[r, "\epsilon"] &
                        \kk
                    \end{tikzcd}
                \]
        \end{enumerate}
    \end{theorem}

    \begin{proof}
        Assume~\ref{it:spansGeo} and apply Proposition~\ref{ref:linearSpanAbstract:prop}. Since $T\in \spann{Z}$, we have
        an element $\epsilon\in(W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee})^{\vee}$ yielding $T$.
        In terms of Diagram~\eqref{eq:linearSpanDiagram}, the tensor $T$ corresponds to a linear map
        \[
            V_1^{\vee}\otimes_\kk \ldots \otimes_\kk V_d^{\vee}\to
            W_1^{\vee}\otimes_{\kk} \ldots \otimes_{\kk}W_d^{\vee} \onto
            W_1^{\vee}\otimes_{\cA}  \ldots \otimes_{\cA} W_d^{\vee} \xrightarrow{\epsilon} \kk.
        \]
        Fix isomorphisms $W_i^{\vee}\to \cA$ for each $i=1, \ldots ,d$. Then the above linear map becomes
        \[
            V_1^{\vee}\otimes_\kk \ldots \otimes_\kk V_d^{\vee}\to
            \cA\otimes_{\kk} \ldots \otimes_{\kk}\cA \xrightarrow{\mathrm{mult.}}
            \cA \xrightarrow{\epsilon} \kk,
        \]
        as claimed. This yields~\ref{it:spansAlg}. The argument can be reversed.
    \end{proof}

    \begin{corollary}[Algebraic characterisation of
        spans]\label{ref:spanCharPopular:cor}
        Let $T$ in $\tspace$ be a tensor and $\cA$ be a finite $\kk$-algebra.
        Let $Z = \Spec(\cA)$. The following conditions are equivalent:
        \begin{enumerate}
            \item there exists a morphism $Z\to \mathbb{P}V_1\times \ldots
                \times \mathbb{P}V_d$ such that $T\in \spann{Z}$,
            \item there exists a functional $\epsilon\colon \cA\to \kk$ such that $T$ is a
                regular restriction (Definition~\ref{ref:regularAndJointlySpanning:def}) of the evaluation tensor of $(\cA, \epsilon)$,
            \item the tensor $T$ is a regular restriction of the multiplication tensor
                in a quotient algebra $\cA' = \cA/I$ which is Gorenstein.
        \end{enumerate}
    \end{corollary}
    \begin{proof}
        The equivalence of first two conditions is given in
        Theorem~\ref{ref:spanChar:thm}, while the equivalence of the latter
        two is given in Proposition~\ref{ref:evaluationTensors:prop}.
    \end{proof}

    \begin{proof}[Proof of Theorem~\ref{ref:restriction:introthm}]
        The equivalence $\ref{it:cactusrankAlg}\Leftrightarrow\ref{it:cactusrankSpan}$ follows from
        Corollary~\ref{ref:spanCharPopular:cor}.
        The implication $\ref{it:cactusrankOne}\implies\ref{it:cactusrankSpan}$ is purely formal.
        To obtain $\ref{it:cactusrankSpan}\implies\ref{it:cactusrankOne}$, take a map $Z\to \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$
        and consider its scheme-theoretic image $Z'\into \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$. By definitions,
        the spans of $Z$ and $Z'$ coincide. The argument can be given also in purely algebraic terms. In the setting of
        Theorem~\ref{ref:spanChar:thm}, let $\mathcal{B}\subseteq \cA$ be the subalgebra generated by the images of $\varphi_1^{\vee}$,
        \ldots, $\varphi_d^{\vee}$. One obtains that $T$ is a restriction
        of the evaluation tensor associated to $(\mathcal{B},
        \epsilon|_{\mathcal{B}})$ and that $\Spec(\mathcal{B})\to
        \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$ is a closed embedding.
    \end{proof}

    \begin{remark}\label{ref:smoothableApolarityLemma:rem}
        There is an analogue of Theorem~\ref{ref:restriction:introthm} for smoothable rank.
        It is not immediate, since the smoothability of $Z$ and $Z'$ given in the proof needs
        to be taken into account. The result
        is obtained by Buczy{\'n}ski (unpublished) and we do not mention it here further.
    \end{remark}
    
    \subsection{Algebras from centroids}\label{ssec:genericityConditions}

        Above, we started from a finite scheme $Z = \Spec(\cA)$ and obtained tensors $T\in\spann{Z}\subseteq \tspace$. In
        this section we reverse this procedure. The reversal is possible thanks to the theory of centroids, as developed in~\cite{JLP}.
        Namely, for a $1$-generic (defined below) centroid-abundant tensor $\Tppar{}\in \tconcspace$,
        we will obtain $\cA$ as $\Cen{\Tppar{}}$.


    The following theorem in the case of three factors was proved in~\cite[Proposition~5.3]{JLP}.
    The proof generalises immediately as soon as one takes the correct notion of ``full rank''.
    \begin{proposition}[genericity conditions]\label{ref:genericity:prop}
        Let $d\geq 3$ and $\dim_{\kk} W_{\bullet} = m$.
        Let $\Tppar{}\in W_1 \otimes  \ldots \otimes W_d$ be a concise tensor with $\dim_{\kk} \Cen{\Tppar{}} \geq
        m$. Fix an index $1\leq i\leq d$ and let $\alpha\in W_i^{\vee}$ be a
        functional. The following are equivalent:
        \begin{enumerate}
            \item\label{it:generityRank} for \emph{some} index $j\neq i$, the contraction
                \[
                    \Tppar{}(\alpha)\colon W_{j}^{\vee} \to W_1\otimes  \ldots \otimes
                    W_{\hat{i}}\otimes  \ldots \otimes W_{\hat{j}} \otimes
                    \ldots \otimes W_d
                \]
                is injective,
            \item\label{it:generityRankEvery} for \emph{every} index $j\neq i$, the contraction
                \[
                    \Tppar{}(\alpha)\colon W_{j}^{\vee} \to W_1\otimes  \ldots \otimes
                    W_{\hat{i}}\otimes  \ldots \otimes W_{\hat{j}} \otimes
                    \ldots \otimes W_d
                \]
                is injective.
            \item\label{it:generityGenerator} the $\Cen{\Tppar{}}$-module $W_i^\vee$ is generated by the element
                $\alpha$.
        \end{enumerate}
        If these hold, then $\dim_{\kk} \Cen{\Tppar{}} = m$ and the
        $\Cen{\Tppar{}}$-module $W_i^{\vee}$ is isomorphic to $\Cen{\Tppar{}}$. In this case,
        we say that $\Tppar{}$ is \emph{$1_{W_i}$-generic via $\alpha$} or that $\Tppar{}$
        is \emph{generic at the $i$-th coordinate via $\alpha$}.
    \end{proposition}
    \begin{proof}
        \def\What{W_{\widehat{ij}}}
        Fix an index $j\neq i$ and let $\What := W_1\otimes  \ldots \otimes
        W_{\hat{i}}\otimes \ldots \otimes W_{\hat{j}} \otimes \ldots \otimes
        W_d$. For any $\alpha'\in W_i^{\vee}$, we view $\Tppar{}(\alpha')$ as the
        linear map $\Tppar{}(\alpha')\colon W_j^{\vee}\to \What$.

        By $\Cen{\Tppar{}}$-linearity, for every $a\in \Cen{\Tppar{}}$
        we have
        \begin{equation}\label{eq:compatibility}
            \begin{tikzcd}
                W_j^{\vee} \ar[rr, "a\cdot(-)"]\ar[rd, "\Tppar{}(a\cdot \alpha)"'] &&
                W_j^{\vee}\ar[ld, "\Tppar{}(\alpha)"]\\
                & \What
            \end{tikzcd}
        \end{equation}
        The tensor $\Tppar{}$ is concise on the $i$-th coordinate, so for $\alpha'\in W_i^{\vee}$ we have that $\alpha' = 0$ if and
        only if $\Tppar{}(\alpha') = 0$. In particular, for every
        $a\in\Cen{\Tppar{}}$ we have $a\cdot \alpha = 0$ if and only if $\Tppar{}(a\cdot
        \alpha) = 0$.

        Now, assume that the condition~\ref{it:generityRank} from the
        statement holds and assume $a\cdot \alpha = 0$.
        Diagram~\eqref{eq:compatibility} implies that $a\cdot (-)\colon
        W_j^{\vee}\to W_j^{\vee}$ is zero, so $a = 0$ by conciseness. It follows that the
        $\Cen{\Tppar{}}$-module homomorphism
        \[
            \Cen{\Tppar{}}\ni a\mapsto a\cdot\alpha\in W_i^{\vee}
        \]
        is
        injective. By assumption, $\dim_{\kk} \Cen{\Tppar{}}\geq m = \dim_{\kk}
        W_i^{\vee}$, hence this homomorphism is an isomorphism, which means
        precisely that $\alpha$ generates
        the $\Cen{\Tppar{}}$-module $W_i^{\vee}$. Therefore, also~\ref{it:generityGenerator}
        holds, $\dim_{\kk} \Cen{\Tppar{}} = m$ and $W_i^{\vee}$ is isomorphic to
        $\Cen{\Tppar{}}$.

        Assume conversely, that~\ref{it:generityGenerator} holds. Suppose that
        $\beta\in W_j^{\vee}$ lies in the kernel of $\Tppar{}(\alpha)$.
        By~\eqref{eq:compatibility} it lies in the kernel of every
        $\Tppar{}(a\cdot\alpha)$. But $\Cen{\Tppar{}}\cdot\alpha = W_i^{\vee}$, so $\beta$ lies in the
        joint kernel of all elements of $\Tppar{}(W_i^{\vee})$, which is zero by conciseness of $\Tppar{}$.
        We proved that~\ref{it:generityRank} holds.

        We proved that~\ref{it:generityRank} and~\ref{it:generityGenerator}
        are equivalent. Since the latter does not depend on the choice of
        index $j$, it is also equivalent to~\ref{it:generityRankEvery}.
    \end{proof}

    We say that a tensor $\Tppar{}$ as in Proposition~\ref{ref:genericity:prop} is \emph{$1$-generic} if it
    is generic at every of its $d$ coordinates. Being $1$-generic is an open
    condition among concise tensors with $\dim_{\kk} \Cen{\Tppar{}} \geq m$.
    Being $1$-generic is tightly connected to the algebraic characterisation of spans from~\S\ref{ssec:lineBundlesAndSpans},
    as we now show.

    \begin{corollary}\label{ref:1generic:cor}
        Let $d\geq 3$ and $\dim_{\kk} W_{\bullet} = m$. Let $\Tppar{}\in W_1 \otimes  \ldots
        \otimes W_d$ be a concise tensor with $\dim_{\kk} \Cen{\Tppar{}} \geq m$.
        The following are equivalent:
        \begin{enumerate}
            \item $\Tppar{}$ is $1$-generic,
            \item $\Tppar{}$ is isomorphic to an evaluation tensor associated to some $(\cA, \epsilon)$.
        \end{enumerate}
        If the above condition hold, then $\cA$ is Gorenstein, isomorphic to $\Cen{\Tppar{}}$, the functional $\epsilon$ is its dual generator, the line bundles $W_1^{\vee}, \ldots ,W_{d}^{\vee}$ yield
        an embedding of $\Spec(\Cen{\Tppar{}})$ into $\mathbb{P}W_1\times \ldots \times \mathbb{P}W_d$, and $\Tppar{}$ lies in $\spann{\Spec(\Cen{\Tppar{}})} = \Cen{\Tppar{}}\cdot \Tppar{}$.
    \end{corollary}
    \begin{proof}
        Assume that $\Tppar{}$ is $1$-generic.
        Let $\cA = \Cen{\Tppar{}}$. We use Proposition~\ref{ref:genericity:prop}.
        For every $i=1, \ldots ,d$, choose a generator $\alpha_i\in W_i^{\vee}$ of the $\cA$-module $W_i^\vee$.
        The map $\sigma_i\colon \cA\to W_i^{\vee}$ given by $\sigma_i(a) = a\alpha_i$ is an isomorphism.
        View $\Tppar{}$ as the contraction $\Tppar{}\colon W_1^{\vee}\otimes  \ldots \otimes W_d^{\vee}\to \kk$.
        By definition of the centroid, this map factors as
        \[
            \begin{tikzcd}
                W_1^{\vee}\otimes_{\kk} \ldots \otimes_{\kk} W_d^{\vee} \ar[r, two heads] & W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee}
                \ar[r, "\epsilon"] & \kk
            \end{tikzcd}
        \]
        where $\epsilon$ is some functional. Applying the isomorphisms $\sigma_1, \ldots ,\sigma_d$, we get
        an isomorphism $W_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} W_d^{\vee}\simeq \cA$ and so $\Tppar{}$
        comes from an evaluation tensor associated to $\epsilon$, see also Remark~\ref{ref:evaluationTensorsLineBundles:rem}.
        % Jointly, the maps $\sigma_1, \ldots ,\sigma_d$ yield an isomorphism of
        % $\Tppar{}$ with a multilinear map $e\colon \cA\times \cA\times \ldots \times
        % \cA\to \kk$ which is $\cA$-linear.
        % Such a multilinear map is an evaluation tensor associated to a functional $\epsilon = e(1,1, \ldots ,1,-)\colon \cA\to \kk$.
        Conversely, a concise evaluation tensor $\Tppar{}$ is by definition $1$-generic.

        To prove the final statements, observe that by
        Proposition~\ref{ref:evaluationTensors:prop} the algebra $\cA$ is Gorenstein
        and $\epsilon$ is a dual generator of $\cA$.
        The line bundles $W_1^{\vee}$, \ldots , $W_d^{\vee}$ on $\Spec(\cA)$ yield an embedding
        $\Spec(\cA)\to \mathbb{P}W_1\times \ldots \times\mathbb{P}W_d$.
        As in Example~\ref{ex:universalLinearSpan}, the linear span of this
        embedding coincides with $\cA^{\vee} = \cA\cdot \epsilon$. In particular, $1\cdot \epsilon$ is
        the element corresponding to $\Tppar{}$.
    \end{proof}
    For a tensor $\Tppar{}$ as above, we can consider the very same nondegeneracy conditions on restrictions as in Definition~\ref{ref:regularAndJointlySpanning:def},
    by applying these definitions to $\cA = \Cen{\Tppar{}}$ and line bundles $W_1^\vee, \dots, W_d^\vee$.

    \begin{lemma}\label{ref:consiseness1generic:lem}
        Let $\dim W_{\bullet} = m$ and let $\Tppar{}\in \tconcspace$ be a $1$-generic tensor (so that in particular $\dim_{\kk} \Cen{\Tppar{}}\geq m$)
        and let $\varphi_1, \ldots ,\varphi_d$ be regular restrictions.
        Fix a subset $I\subseteq \{1, \ldots ,d\}$ and let $J$ be its complement. Assume that $(\varphi_i)_{i\in I}$ are jointly spanning and let
        \[
            T = \varphi_I(\Tppar{})\in \bigotimes_{i\in I}V_{i} \otimes \bigotimes_{j\in J} W_j
        \]
        be the restriction. Then $T$ is $W_j$-concise for every $j\in J$.
    \end{lemma}
    \begin{proof}
        Pick an index $j \in J$. Up to permuting coordinates, we can and do assume that $j=1$.
        Let $\cA = \Cen{\Tppar{}}$. By Corollary~\ref{ref:1generic:cor}, we may identify $W_j^{\vee}$ with $\cA$ for every $j\in J$
        and $\Tppar{}$ with the evaluation tensor associated to a dual generator $\epsilon\in \cA^{\vee}$.
        By Lemma~\ref{ref:regularity:lem}, the restrictions $\varphi_2, \ldots ,\varphi_d$ are jointly spanning.
        % By~\eqref{eq:jointSpanConcrete},
        % it is enough to prove that
        % \[
        %     \varphi_2^{\vee}(V_2^{\vee})\cdot  \ldots \cdot \varphi_d^{\vee}(V_d^{\vee}) \subseteq \cA
        % \]
        % is the whole $\cA$. Since $(\varphi_i)_{i\in I}$ are jointly spanning, we know that $\prod_{i\in I}\varphi_i(V_i^{\vee}) = \cA$.
        % Since $\varphi_2, \ldots ,\varphi_d$ are regular, we have $\cA\cdot \varphi_i(V_i^{\vee}) = \cA$ for every $i$.
        % Therefore
        % \begin{equation}\label{eq:tmpJoint}
        %  \varphi_2^{\vee}(V_2^{\vee})\cdot  \ldots \cdot \varphi_d^{\vee}(V_d^{\vee}) = \prod_{i\in I}\varphi_i(V_i^{\vee})\cdot \prod_{j\in \left\{ 2, \ldots ,d \right\}\setminus I} \varphi_j(V_j^{\vee}) = \cA \cdot \prod_{j\in \left\{ 2, \ldots ,d \right\}\setminus I} \varphi_j(V_j^{\vee}) = \cA.
        % \end{equation}
        Since we are analysing $j=1$, we can restrict further to $W_1\otimes V_{2, \ldots ,d}$, that is, assume that $I = \left\{ 2, \ldots ,d \right\}$.
        
        If $T$ is not $W_1$-concise, then there exists an element $r\in \cA = W_1^\vee$ such that $T(r) = 0$.
        This implies that $T(r, v_2^*, \ldots , v_d^*) = 0$ for every $v_i^*\in V_i^{\vee}$, $i=2, \ldots ,d$. Since $T$ is an evaluation
        tensor, this translates to
        \[
            0 = \epsilon\left( r\cdot \varphi_2^{\vee}(V_2^{\vee})\cdot  \ldots \cdot \varphi_d^{\vee}(V_d^{\vee}) \right) = \epsilon(r\cdot \cA).
        \]
        In the last equality, we used~\eqref{eq:jointSpanConcrete}. The equality $\epsilon(r\cdot \cA)=0$ means that $r\epsilon = 0$. 
        But $\epsilon$ is a dual generator, so $r = 0$, which concludes the proof.
    \end{proof}
    

    \subsection{Abstract secant varieties}\label{sec:abstractSecant}

    The aim of this section is to show that the abstract secant variety
    (defined without closure) is an open subvariety of the concise secant
    variety. This requires a shift of perspective: traditionally, the points of
    an abstract secant (or cactus) variety are viewed as pairs $Z = \Spec(\cA)$, $T$ such that
    \[
        T\in \spann{Z}.
    \]
    This perspective is very useful under positivity assumptions, when all concise tensors become $1$-generic (see~\cite{Buczyska_Buczynski__cactus}).
    Without these assumptions, it becomes very hard to interpret the above away from the $1$-generic locus. We argue that one should rewrite the above as
    \[
        T \leq \eval,
    \]
    where $\eval$ is an evaluation tensor on $\cA$. For almost all applications, we can assume
    that $\cA$ is Gorenstein and replace $\eval$ by the (iterated) multiplication tensor on $\cA$.

    \bigskip

    We now discuss the spaces of interest.
        Let $\csigma_m$ be the concise secant variety
        with its family of tensors $\Tppar{}$. We define the \emph{tame locus} $\csigmaOneGen_m$
        of $\csigma_m$ as the locus given by the conditions:
        \begin{enumerate}
            \item\label{it:1generic} the restriction of the universal tensor $\Tppar{}$ to $\csigmaOneGen_m$ is $1$-generic, see Definition~\ref{ref:1genericityInFamilies:def},
            \item\label{it:jointSpan} the restriction map $\varphi_1$ is regular and the maps $\varphi_{\mathbf{2}}, \ldots ,\varphi_d$ are jointly spanning for $\cA = \Cen{\Tppar{}}$, see Definition~\ref{ref:regularAndJointlySpanning:def}; note that the indexing starts from $2$.
            % \item the map $\varphi_1$ is regular.
        \end{enumerate}

        Classically~\cite[p.439]{Chiantini_Ciliberto__On_the_concept}, the open part of the abstract secant variety
        consists of pairs $\{x_1, \ldots ,x_m\}$, $[T]$, where
        $x_1, \ldots ,x_m$ are general points of $\mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$ and $T\in \spann{x_1, \ldots ,x_m}$
        is general. Here, we work with a slightly different locus, defined as follows.
        Consider the reduced subscheme $\AsigmaHilb_m$ of $\Hilb_m^{\sm}(\mathbb{P}V_1\times \ldots \times \mathbb{P}V_d) \times \mathbb{P}(\tspace)$,
        whose $\kk$-points are pairs $(Z, [T])$ where
        \begin{enumerate}
            \item $[Z] = [\Spec(\cA)]\in \Hilb_m^{\sm}(\mathbb{P}V_1\times \ldots
                \times \mathbb{P}V_d)$ is a smoothable Gorenstein degree $m$ subscheme whose 
                linear span in $\mathbb{P}(V_{\mathbf{2}, \ldots ,d})$ is isomorphic to $\mathbb{P}^{m-1}$; note that the
                indexing starts from $2$.
            \item $T\in \spann{Z} \subset \PP(\tspace)$ is a tensor, which is a restriction of the evaluation tensor on a dual generator
                $\epsilon\colon \cA\to \kk$.
        \end{enumerate}
        % Since
        %
        %
        %  and $T\in \spann{Z}$, moreover we require that . Observe that, on the one hand, since the indices range between $2$ and $d$, this is a slightly stronger condition than found in,
        % for example, \cite[p.439]{Chiantini_Ciliberto__On_the_concept}. On the other hand, since
        %
        % we allow nonreduced schemes, it is a larger locus than considered
        % classically for example,
        % . Sometimes, the above
        % it called the open part of the abstract secant variety, while the
        % variety itself is defined as the closure inside the product.

        The main result of this section, Theorem~\ref{ref:abstractInsideConcise:thm} below, gives an isomorphism of $\csigmaOneGen_m$ with $\AsigmaHilb_m$.
        Before we go to the formal proof, we discuss what happens on $\kk$-points.

        \subsubsection{Comparison of $\kk$-points}\label{ssec:kpointsAbstractSecant}

        Take a $\kk$-point of $\csigmaOneGen_m$. By Lemma~\ref{ref:regularity:lem}, the maps $\varphi_1, \ldots ,\varphi_d$
        are jointly spanning, in particular regular. Let $\cA = \Cen{\Tppar{}}$ and $Z = \Spec(\cA)$.
        Since $\varphi_2, \ldots ,\varphi_d$ are jointly spanning,
        by~\eqref{eq:jointSpanConcrete}, they yield a closed embedding $Z\into
        \mathbb{P}V_2\times \ldots \times \mathbb{P}V_d$ with $\spann{Z}$ isomorphic to $\mathbb{P}^{m-1}$.
        Since $\varphi_1, \ldots ,\varphi_d$, are jointly spanning, they yield a closed embedding $Z\into
        \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$, so a point $[Z]\in \Hilb_d(\mathbb{P}V_1\times \ldots \times\mathbb{P}V_d)$.
        The tensor $\Tppar{}$ has minimal border rank, so $\cA$ is smoothable, hence $[Z]$ lies in $\Hilb_d^{\sm}$.
        Let $[T] = \varphi_{1, \ldots ,d}(\Tppar{})\in \mathbb{P}\tspace$ be the restriction.
        Since $\Tppar{}$ is $1$-generic, by Proposition~\ref{ref:1generic:cor}, it is an evaluation tensor associated to
        a dual generator $\epsilon \in \cA^{\vee}$, hence $T$ is a restriction of such a tensor. We obtain a point of $\AsigmaHilb_m$.

        Now, take a $\kk$-point $(Z, [T])$ in $\AsigmaHilb_m$. The linear span of $Z$ in $\mathbb{P}V_{2, \ldots ,d}$ has maximal dimension,
        so also the linear span of $Z$ in $\mathbb{P}\tspace$ has maximal dimension. Let $\cA$ be an algebra such that $Z = \Spec(\cA)$.
        Let $W_1^{\vee}$, \ldots , $W_d^{\vee}$ be the line bundles coming from the embedding $Z\into \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$ and
        $\varphi_i\colon W_i\to V_i$ be the restriction maps for $i=1, \ldots ,d$.
        Twist $\varphi_1$ by $\OO_{[T]}(-1)$.
        Comparing Proposition~\ref{ref:linearSpanAbstract:prop} and Definition~\ref{ref:regularAndJointlySpanning:def}, we see that
        $\varphi_1, \ldots ,\varphi_d$ are jointly spanning, so there is a \emph{unique} evaluation tensor $\Tppar{}\in W_1\otimes \ldots \otimes W_d$
        such that $\varphi_{1, \ldots ,d}(\Tppar{}) = [T]$.

        Analogously, the maps $\varphi_2, \ldots ,\varphi_d$ are jointly spanning.
        By Lemma~\ref{ref:consiseness1generic:lem}, for every $1\leq i\leq d$, the restriction
        \[
            \varphi_{i+1, \ldots ,d}(\Tppar{}) \in W_{1, \ldots ,i}\otimes V_{i+1,  \ldots , d}
        \]
        is $W_1$-, \ldots , $W_i$-concise. These, essentially speaking, yield a point of $\csigmaOneGen_m$.
        To be more precise, the contraction of the $W_1$-concise tensor $\varphi_{2, \ldots ,d}(\Tppar{})$ yields
        a subspace of $V_{2, \ldots ,d}$, which we call $U_1^{\vee}$ and an isomorphism $W_1^{\vee}\to U_1^{\vee}$. This isomorphism
        allows us to interpret $\varphi_{3, \ldots ,d}(\Tppar{})$ as a tensor $\Tppar{1}$ in $U_1\otimes W_2\otimes V_{3, \ldots ,d}$.
        Its contraction with respect to the second coordinate yields a subspace $U_2^{\vee}\subseteq U_1\otimes V_{3, \ldots ,d}$
        and an isomorphism $W_2^{\vee}\to U_2^{\vee}$. The subspace yields a tensor $\Tppar{1,2}$. Continuing, we obtain tensors all the way up to
        $\Tppar{1, \ldots ,d}$ which is isomorphic to $\Tppar{}$, in particular it is $1$-generic.
        Arguing as above, we see that $\varphi_2, \ldots ,\varphi_d$ are jointly spanning, so we obtain a $\kk$-point of $\csigmaOneGen_m$.

        \begin{example}
            Above, it is not enough to assume that $\varphi_1, \ldots ,\varphi_d$ are jointly surjective, the condition on $\varphi_2, \ldots ,\varphi_d$
            is necessary. Indeed, consider the situation from Example~\ref{ex:jointSurjectivity}. Namely, take $d = 4$, $\cA = \kk[x]/(x^5)$,
            $W_1^{\vee} =  \ldots = W_4^{\vee} = \cA$ and $V_i^{\vee}\to
            W_i^{\vee}$ is the inclusion of $\spann{1, x}$ and $\varphi_1 =
            \ldots = \varphi_4\colon W_i\to V_i$ be the associated
            restriction maps.
            Let $\epsilon = (x^4)^*$ be the functional in the monomial basis of
            $\cA$, and $\Tppar{}\in W_{1, \ldots ,4}$ be the associated tensor.
            Then the restriction $\varphi_{2, \ldots ,4}(\Tppar{})\in W_1\otimes V_{2, \ldots ,4}$ is not $W_1$-concise.
            Indeed, the associated contraction $W_1^{\vee} \to V_{2, \ldots , 4}$ sends $x^4$ to zero.
        \end{example}
        

        \subsubsection{$S$-points and comparison of functors}

    % Indeed, the current section is mostly ``just'' a relative version of~\S\ref{sec:spans}.
        To prove Theorem~\ref{ref:abstractInsideConcise:thm}, we repeat the argument given above on $\kk$-points,
        but using $S$-points, where $S$ is a $\kk$-scheme.
        To even formulate Theorem~\ref{ref:abstractInsideConcise:thm}, we need to have openness of $\csigmaOneGen_m$ inside $\csigma_m$.

    We begin by generalising the notions from~\S\ref{ssec:lineBundlesAndSpans} to the setting of families of tensors.
        \begin{definition}\label{ref:1genericityInFamilies:def}
            Let $\WW_1, \ldots, \WW_d$ be rank $m$ vector bundles on a scheme $X$ and let
            \[
                T\colon \LL \into \WW_1\otimes \ldots \otimes \WW_d,
            \]
            be a concise
            (Definition~\ref{ref:concise:def}) family of tensors.
            For a fixed $1\leq i\leq d$, we say that $T$ is a family of \emph{$1_{\WW_i}$-generic tensors} if for every point $x\in
            X$, the tensor $T|_x$ is $1_{\WW_i}$-generic in the sense of
            Proposition~\ref{ref:genericity:prop}. We say that $T$ is a family of $1$-generic tensors if
            every $T|_x$ is $1$-generic.
        \end{definition}

        \begin{proposition}\label{ref:centroidsInFamilies:prop}
            Let $T$ be a family of $1$-generic tensors on a scheme $X$. Assume
            that $T$ is centroid-abundant
            (Definition~\ref{ref:secantLocus:def}). Then there is a subbundle
            \[
                \Cen{T}\into \End(\WW_1)\times \ldots \times\End(\WW_d)
            \]
            of commutative subalgebras such that $(\Cen{T})|_x \simeq \Cen{T|_x}$ for every $x\in X$. We call
            it the \emph{centroid} of $T$ or \emph{the family of centroids}.
            The vector bundles $\WW_1^{\vee}$, \ldots ,$\WW_d^{\vee}$ on $X$ are $\Spec(\Cen{T})$-line bundles.
            There is also a subbundle $\Cen{T}\cdot T\into \WW_1\otimes \ldots
            \otimes \WW_d$, which satisfies $(\Cen{T}\cdot T)|_x \simeq
            (\Cen{T|_x})\cdot T|_{x}$ for every $x\in X$.

        \end{proposition}
        \begin{proof}
            Define $\Cen{T}$ as the kernel of the map of vector bundles
            \[
                \End(\WW_1)\times \ldots \times\End(\WW_d)\to \prod_{i=2}^{d} \WW_1\otimes \ldots \otimes \WW_d
            \]
            given by $(X_1, \ldots ,X_d)\mapsto (X_1\circ T - X_i\circ T)_{i=2, \ldots ,d}$.
            We claim that this map has constant rank. 
            By assumption, the kernel at every point is at least $m$-dimensional.
            By Proposition~\ref{ref:genericity:prop}, at every point the centroid is exactly $m$-dimensional,
            hence the map has constant rank, equal to $d\cdot m^2 - m$.
            By the constancy of rank, the kernel of this map is
            a vector subbundle which commutes with base change. In particular,
            $\Cen{T}$ satisfies $(\Cen{T})|_x \simeq \Cen{T|_x}$ for every
            $x\in X$. Similarly, we take
            the map $\Cen{T} \to \WW_1\otimes \ldots \otimes \WW_d$ given by $\Cen{T}\ni r\mapsto r\cdot T$. It is a map of vector bundles and it is
            injective on each fiber, hence it is a subbundle and we obtain $\Cen{T}\cdot T$.

            Finally, each vector bundle $\WW_i$ comes with a $\Cen{T}$-action, hence $\WW_i$ and $\WW_i^{\vee}$ are $\Cen{T}$-modules. For every point $x\in X$,
            by Proposition~\ref{ref:genericity:prop}, after perhaps shrinking $X$ to a neighbourhood of $x$, we have an element $\alpha\in \WW_i^{\vee}$
            such that the map $\Cen{T}\to \WW_i^{\vee}$ given by $r\mapsto r\cdot \alpha$ is surjective. Both $\Cen{T}$ and $\WW_i^{\vee}$ are rank $m$ vector
            bundles on $X$, so this map is an isomorphism. This means that $\WW_i^{\vee}$ is a line bundle on $\Spec_X(\Cen{T})\to X$.
        \end{proof}

        \begin{proposition}[relative spans in the ``good case'']\label{ref:linearSpanAbstractRelative:prop}
            Let $\ZZ\to S$ be a finite flat family with a map $\ZZ\to S \times \mathbb{P}V_1 \times \ldots \times \mathbb{P}V_d$.
            Let $\varphi_i\colon \WW_i\to \OO_S\otimes V_i$ be the associated maps of vector bundles on $\OO_S$ and assume that $\varphi_1, \ldots ,\varphi_d$ are jointly spanning
            at every point of $S$. Then the composition
            \begin{equation}\label{eq:relativeSpanEq}
                (\WW_1^{\vee}\otimes_{\OO_{\ZZ}} \ldots \otimes_{\OO_{\ZZ}}
                \WW_d^{\vee})^{\vee} \into \WW_1 \otimes_{\OO_S} \ldots \otimes_{\OO_S} \WW_d
                \to \VV_1\otimes_{\OO_S} \ldots \otimes_{\OO_S} \VV_d
            \end{equation}
            is a vector subbundle and for every $s\in S$ and its restriction yields the linear span $\spann{\ZZ|_s}$.
            This subbundle is called the \emph{relative linear span} of $\ZZ$.
        \end{proposition}
        \begin{proof}
            Since $\varphi_1, \ldots ,\varphi_d$ are jointly spanning, the restriction of~\eqref{eq:relativeSpanEq}
            to every point is injective. Hence~\eqref{eq:relativeSpanEq} is a vector subbundle. Its connection with
            linear spans is proved in Proposition~\ref{ref:linearSpanAbstract:prop}, see also~\eqref{eq:jointSpanConcrete}.
        \end{proof}

        \begin{corollary}[Openness of $1$-generic locus]\label{ref:opennessOf1generic:cor}
            The locus $\csigmaOneGen_m$ is open inside $\csigma_m$.    
        \end{corollary}
        \begin{proof}
            Being $1$-generic is open thanks to Proposition~\ref{ref:genericity:prop}.
            On the $1$-generic locus, there is a flat family of centroids
            (Proposition~\ref{ref:centroidsInFamilies:prop}). Using this family, we obtain a family of linear maps as in
            Definition~\ref{ref:regularAndJointlySpanning:def}. Being injective
            is open in such a family.
        \end{proof}
        We are now in position to embed the abstract secant variety $\AsigmaHilb_m$ into $\csigma_m$.
        %
        % To obtain the embedding, we will use Corollary~\ref{ref:spanCharPopular:cor}.

       %  \begin{lemma}\label{ref:tameLocusTechnical:lem}
       %      The maps $\varphi_1, \ldots ,\varphi_d$ are also jointly spanning on the tame locus.
       %  \end{lemma}
       %  \begin{proof}
       %      We use~\eqref{eq:jointSpanConcrete}. We already know that $\varphi_2, \ldots ,\varphi_d$ are jointly spanning.
       %      Since $\varphi_1$ is regular, the image of $V_1^{\vee}$ in $\Cen{\Tppar{}}$ is not contained in any ideal,
       %      so this image contains an invertible element. The image of $V_2^{\vee}\otimes \ldots \otimes V_d^{\vee}$ is the whole
       %      centroid by assumption, so the image of $V_1^{\vee}\otimes \ldots \otimes V_d^{\vee}$ is also the whole centroid. 
       % \end{proof}
        
        

    \begin{theorem}[Concise secant compactifies the abstract one]\label{ref:abstractInsideConcise:thm}
        Let $\csigma_m$ be the concise secant variety (Definition~\ref{ref:conciseSecant:def}).
        Its tame locus $\csigmaOneGen_m$ is isomorphic to the abstract secant variety $\AsigmaHilb_m$. 
        % Consider its \emph{tame sublocus} $\Tame$ given by
        % the conditions
        % This locus is open inside the concise secant variety.
        % It is isomorphic to the open part $\Asigma_m^{\op}$ of the abstract secant variety.
        % In particular, the points of $\Tame \simeq \Asigma_m^{\op}$ are identified with
        % the pairs $(T, Z)$, where $Z$ is a finite smoothable scheme of
        % degree $m$ with a closed embedding $Z \into \mathbb{P}V_1
        % \times \ldots \times \mathbb{P}V_d$ such that $\dim (\spann{Z} \into V_{\mathbf{2}}\otimes \ldots \otimes V_d) = m$, and
        % $T\in \spann{Z}\subseteq \tspace{}$.
    \end{theorem}

    \begin{proof}
        % First, we prove openness. Being $1$-generic is open thanks to Proposition~\ref{ref:genericity:prop}.
        % We can thus restrict to the $1$-generic locus. Locally, we can even pick functionals $\alpha_1\in W_1^{\vee}, \ldots ,\alpha_d^{\vee}$
        % which prove genericness of $\Tppar{}$ on coordinates $W_1$, \ldots ,
        % $W_d$, respectively. Using these functionals, we obtain a family of
        % linear maps as in~\eqref{eq:jointSpan}. Being jointly spanning is open
        % in this family. This proves openness of the tame locus $\Tame$.

        To prove that $\csigmaOneGen_m$ and $\AsigmaHilb_m$ are isomorphic, we produce maps in both directions 
        on $S$-points for an any $\kk$-scheme $S$. This generalises the comparison for $S = \Spec(\kk)$ from~\S\ref{ssec:kpointsAbstractSecant}.

        Let $\Tppar{}$ be the universal tensor on $\csigmaOneGen_m$.
        Take an $S$-point of $\csigmaOneGen_m$, that is, a map $f\colon S\to \csigmaOneGen_m$.
        Let $\cA := \Cen{f^*\Tppar{}}$ be the centroid of $f^*\Tppar{}$ as in
        Proposition~\ref{ref:centroidsInFamilies:prop}.
        Let $g\colon \ZZ = \Spec_S(\cA) \to S$. This is a finite flat family of degree $m$ over $S$ and it is Gorenstein,
        that is, has Gorenstein fibres.

        Let $\varphi_1, \ldots ,\varphi_d$ be the restriction maps obtained from Proposition~\ref{ref:functorOfUnrestrictions:prop},
        so that $\varphi_1\colon U_1\to f^*\OO(1) \otimes V_1$ and $\varphi_i\colon U_i\to \OO_S\otimes V_i$ for $i=2, \ldots ,d$.
        The bundles $U_1^{\vee}, \ldots , U_d^{\vee}$ are $\cA$-modules. In fact, they are line bundles by assumption on $1$-genericity.
        To check that the associated maps
        \[
            g^*f^*\OO(-1) \otimes V_1^{\vee} \to
            U_1^{\vee},\quad \OO_{\ZZ}\otimes V_i^{\vee}
            \to U_i^{\vee}\quad\mbox{for}\quad i=2, \ldots ,d
        \]
        are surjective, we can argue point by point, so it follows from~\S\ref{ssec:kpointsAbstractSecant}.
        % Surjectivity can be checked pointwise. Since
        % $\varphi_1, \ldots ,\varphi_d$ are jointly spanning, every of them is
        % regular by Lemma~\ref{ref:regularity:lem}. This yields the required surjectivity.
        Each of the maps yields a globally generated line bundle on $\ZZ$, hence jointly they produce a morphism
        \begin{equation}\label{eq:Zmorphism}
            \ZZ\to S\times \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d.
        \end{equation}
        % Take an $S$-point $(\Tppar{}, \varphi_1, \ldots ,\varphi_d)$, where $\varphi_i\colon \WW_i\to \VV_i$, where $\VV_i := \OO_S\otimes_{\kk} V_i$.
        % Let $\ZZ = \Spec_S(\cA) \to S$. This is a finite flat family of degree $m$ over $T$.
        % The spaces $\WW_1, \ldots ,\WW_d$ come from line bundles on $\ZZ$ by Proposition~\ref{ref:centroidsInFamilies:prop}.
        % For every $i=1, \ldots ,d$, the restriction $\varphi_i\colon \WW_i\to \VV_i$ is regular at every point by Lemma~\ref{ref:regularity:lem},
        % so the associated map $\cA\otimes \VV_i^{\vee}\to \WW_i^{\vee}$ are surjective after restriction to every point, so it is surjective.
        % Using these maps, we obtain a morphism $\ZZ\to S\times \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$.
        %
        % By Lemma~\ref{ref:tameLocusTechnical:lem}, the maps $\varphi_1, \ldots ,\varphi_d$ are jointly spanning, so
        The restrictions $\varphi_2, \ldots
        ,\varphi_d$ are jointly spanning at any point, so
        by~\eqref{eq:jointSpanConcrete} we get that the map
        \begin{equation}\label{eq:surj}
            \OO_S\otimes V_2^{\vee}\otimes \ldots \otimes V_d^{\vee}\to  U_2^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} U_d^{\vee}
        \end{equation}
        is surjective pointwise, so it is surjective. This means that the linear span $\spann{\ZZ}\subseteq \OO_S\otimes V_{2, \ldots ,d}$ defined in Proposition~\ref{ref:linearSpanAbstractRelative:prop} is a
        rank $m$ vector subbundle. Taking into account also $\varphi_1$, this implies in particular that the map~\eqref{eq:Zmorphism} is a closed embedding,
        so it yields a morphism $S \to \Hilb_m(\mathbb{P}V_1\times \ldots \times \mathbb{P}V_d)$. Since members of $f^*\Tppar{}$ have
        minimal border rank, the map actually factors through $\Hilb_m^{\sm}(\mathbb{P}V_1\times \ldots \times \mathbb{P}V_d)$.
        Projecting the tensor $f^*\Tppar{}$ using $\varphi_1, \ldots ,\varphi_d$, we obtain a tensor $T\colon f^*\OO(-1) \to \OO_S\otimes \tspace$,
        which lies in the family of spans of $\ZZ$ by Proposition~\ref{ref:linearSpanAbstractRelative:prop}.
        Since $\Tppar{}$ is $1$-generic pointwise, the tensor $T$ is pointwise a restriction of the evaluation tensor obtained
        from a dual generator, as claimed.
        The tensor $T$ yields a map $S \to \AsigmaHilb_m$.

        Conversely, take a morphism $S\to \AsigmaHilb_m$. It gives a morphism $S\to \Hilb_m^{\sm}(\mathbb{P}V_1\times \ldots \times \mathbb{P}V_d)$,
        which corresponds to a family $f\colon \ZZ\to S$ and its closed embedding $\ZZ\into S\times \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$.
        Let $\cA := f_*\OO_{\ZZ}$ be the corresponding algebra.
        The induced maps $\ZZ\to \mathbb{P}V_i$ yield maps $\cA\otimes_{\kk} V_i^{\vee}\onto \WW_i^{\vee}$ for some line bundles $\WW_i^{\vee}$ on $\ZZ$.
        Let $\varphi_i\colon \WW_i \to \OO_S \otimes_{\kk} V_i$ be the associated restriction maps; they are regular by their very construction.
        These maps produce a composition
        \begin{equation}\label{eq:tmpRelativeSpan}
            (\WW_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} \WW_d^{\vee})^{\vee}\to \WW_1\otimes_{\OO_S} \ldots \otimes_{\OO_S} \WW_{d} \to \OO_S\otimes_{\kk} \tspace.
        \end{equation}
        By assumption and by Proposition~\ref{ref:linearSpanAbstractRelative:prop} this composition is injective pointwise, so (by Lemma~\ref{ref:subbudle:lem})
        it is a subbundle.
        % By assumption, the linear span of $\ZZ\to S\times \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$ has maximal dimension fiberwise.
        % hence also the linear span of $\ZZ\to S\times \mathbb{P}V_1\times \ldots \times \mathbb{P}V_d$ has maximal dimension.
        The morphism $S\to \AsigmaHilb_m$ yields also a family of tensors $T\colon \LL\into \spann{\ZZ} \into \OO_S\otimes \tspace$
        which factors from the image of~\eqref{eq:tmpRelativeSpan}. Since~\eqref{eq:tmpRelativeSpan} is a subbundle,
        this family gives a family of tensors
        \[
            \Tppar{}\colon \LL\into
            (\WW_1^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} \WW_d^{\vee})^{\vee}\into \WW_1\otimes_{\OO_S} \ldots \otimes_{\OO_S} \WW_d.
        \]
        By assumption, at every point, the family $\Tppar{}$ is an evaluation on a dual socle generator,
        see Corollary~\ref{ref:dualSocle:cor}, in the smoothable algebra, so every of these tensors has minimal border rank.
        For clarity, we replace $\WW_1$ by $\WW_1\otimes \LL^{\vee}$, so that
        $\Tppar{}$ becomes a map from $\OO_S$ and $\varphi_1\colon \WW_1 \to
        \LL^{\vee}\otimes_{\kk} V_1$.

        Using the restriction maps, we obtain tensors $\varphi_{2, \ldots
        ,d}(\Tppar{})\colon \OO_S\to \WW_1 \otimes_{\kk} V_{2, \ldots ,d}$,
        $\varphi_{3, \ldots ,d}(\Tppar{})\colon \OO_S \into \WW_1\otimes \WW_2\otimes_{\kk} V_{3, \ldots ,d}$, etc.
        The tensor $\varphi_{2, \ldots ,d}(\Tppar{})$ yields a contraction $\WW_1^{\vee}\to \OO_S^{\vee}\otimes_{\kk} V_{2, \ldots ,d}$.
        By~\S\ref{ssec:kpointsAbstractSecant}, this contraction is injective pointwise, so it is a subbundle. We obtain a
        subbundle $U_1^{\vee}\subseteq \OO_S\otimes_{\kk} V_{2, \ldots ,d}$ and an isomorphism $\WW_1^{\vee}\simeq U_1^{\vee}$.
        Similarly, we produce $U_2^{\vee}$, \ldots , $U_d^{\vee}$ and a tensor $\OO_S\into U_{1, \ldots ,d}$ isomorphic to $\Tppar{}$.
        The tensor $\Tppar{}$ is $1$-generic pointwise, hence so is $\OO_S\into U_{1, \ldots ,d}$.

        By assumption and by Proposition~\ref{ref:linearSpanAbstractRelative:prop} also the composition
        \[
            (\WW_2^{\vee}\otimes_{\cA} \ldots \otimes_{\cA} \WW_d^{\vee})^{\vee}\to \WW_2\otimes_{\OO_S} \ldots \otimes_{\OO_S} \WW_{d} \to \OO_S\otimes_{\kk} V_{2, \ldots ,d}.
        \]
        is injective pointwise, so (by Lemma~\ref{ref:subbudle:lem})
        it is a subbundle, hence $\varphi_2, \ldots ,\varphi_d$ are jointly spanning pointwise.
    \end{proof}

    \begin{example}
        The variety $\AsigmaHilb_r$ admits a map to $\Sym^m(\mathbb{P}V_1\times \ldots \times\mathbb{P}V_d)$ and one could ask whether
        it extends to a morphism on the whole $\csigma_r$. However, it turns out that the support of a minimal border rank tensor is not well-defined in general.
        Indeed, consider the Perazzo cubic $F = x_0^2x_3 + x_0x_1x_4 + x_1^2x_5$.
        As in~\cite{bucz_bucz_smoothable_rank_example}, one can produce a limit $F = \lim_{t\to 0} F_t$, where $F_t = \sum_{i=1}^5 \lambda_i(t)$ are of rank $5$ and where
        the five points $[\lambda_i(t)]$ converge to arbitrary $5$ pairwise different points on the line $\spann{x_0, x_1}$.
        The support of $F_t$ is $\left\{ [\lambda_1(t)], \ldots , [\lambda_5(t)] \right\}$, so this shows that the support of $F$ cannot
        be defined such that support of each of these families is a continuous map.
        This shows that the rational map $\csigma_r\dashrightarrow \Asigma_r$ is not defined everywhere.
    \end{example}

    \subsection{Relation with identifiability}\label{ssec:identifiability}

        Theorem~\ref{ref:abstractInsideConcise:thm} gives us plenty of information about the birational behaviour of
        the map $\rho$. The \emph{(nonembedded) expected dimension} of $\sigma_m\subseteq \mathbb{P}\tspace$ is the number 
        $m\cdot (\dim \Seg + 1) - 1 = m\cdot (\sum\dim V_{\bullet} - (d-1)) - 1$. We add the word ``nonembedded'', since
        it is more common to define the \emph{expected dimension} by
        \[
            \expdim \sigma_m = \min\left( m\cdot (\dim \Seg + 1)-1,\ \dim \mathbb{P}\tspace \right).
        \]
        The critical value of $m$ in the above formula is
        \begin{equation}\label{eq:scrit}
            s(\Seg) := \left\lfloor \frac{\prod_{i=1}^{d}\dim V_i}{\sum_{i=1}^d (\dim V_i - 1)+1} \right\rfloor.
        \end{equation}
        Below, we usually assume $m < s(\Seg)$, so that the nonembedded and usual expected dimensions agree.
        In contrast with $\sigma_m$, the dimension of $\csigma_m$ is always the expected one, as follows from Corollary~\ref{ref:dimensionOfcsigma:cor}.

        The Segre variety $\Seg \subseteq \mathbb{P}\tspace$ is \emph{$m$-nondefective} if
        $\dim \sigma_m = \expdim \sigma_m$, or equivalently, the map $\AsigmaHilb_m \to \sigma_m$
        is generically finite. Otherwise, it is \emph{$m$-defective}.
        This variety is \emph{$m$-identifiable} if the map $\AsigmaHilb_m\to \sigma_m$ is birational. 
        This can happen only if $\dim \sigma_m$ is equal to the nonembedded expected dimension.

        \begin{lemma}[Concise secants and defectivity]\label{ref:identifiability:lem}
            Take $V_{1}, \ldots ,V_d$ and $m < s(\Seg)$.
            Then the following hold:
            \begin{enumerate}
                \item $\Seg\subseteq \mathbb{P}\tspace$ is $m$-nondefective if and only if $\rho\colon \csigma_m\to \sigma_m$ is generically finite,
                \item $\Seg \subseteq \mathbb{P}\tspace$ is $m$-identifiable if and only if $\rho\colon \csigma_m\to \sigma_m$ is birational.
            \end{enumerate}
        \end{lemma}
        \begin{proof}
            Directly from definitions and Theorem~\ref{ref:abstractInsideConcise:thm}.
        \end{proof}

        The above is a birational result. Using $\csigma_m$, we can transform it into a result about varieties
        of sums of powers.
        \begin{corollary}\label{ref:infiniteFibers:cor}
            Assume that $\Seg$ is $m$-identifiable and let $[T]\in \sigma_m$ be a normal point.
            Then the concise variety of sums of powers $\cVSP([T])$ is either a point or
            it is positive-dimensional.
        \end{corollary}
        \begin{proof}
            By definition, the scheme $\cVSP([T])$ is equal to $\rho^{-1}([T])$.
            By Zariski Main Theorem, this fibre of $\rho$ is connected.
        \end{proof}
        
        By Oeding's Conjecture~\ref{ref:Oeding:conj}, in ``good'' situations normality should hold.

        The questions of defectivity and identifiability of Segre (and Segre-Veronese) varieties have gathered much attention
        classically and since the Alexander and Hirschowitz theorem~\cite{AlexHirsch},
        the field exploded with new beautiful results. A very much non-exhaustive list, mostly geared towards the Segre case, is \cite{Chiantini_Ciliberto__Weakly_defective, Chiantini_Ciliberto__On_the_concept, Chiantini_Ciliberto__On_the_dimension, Abo_Brambilla, Abo_Ottaviani_Peterson_segre, Araujo_Massarenti_Rischter, Laface_Postinghel, Ballico__Partially_symmetric, Massarenti_Mella, Vannieuwenhoven_Vandebril_Meerbergen, Chiantini_Ottaviani_Vannieuwenhoven, Chiantini_Ottaviani_Vannieuwenhoven__On_generic_identifiability, Laface_Massarenti_Rischter, Ballico_Bernardi_Santarsiero, Dolevalek_Ken}. 
        To begin, for example, see the discussion in \cite{Abo_Brambilla_Galuppi_Oneto} or in~\cite{Casarotti_Mella}. For Segre, the picture, at least conjecturally, is quite complete.
        \begin{enumerate}
            \item For $m\leq 6$, the $m$-defective cases are listed in~\cite{Abo_Ottaviani_Peterson_segre}.
                The authors also formulate Question~6.6 which conjecturally lists \emph{all} defective cases in the Segre case.
            \item Casarotti-Mella~\cite[Theorem~18, Corollary~22]{Casarotti_Mella} (see also~\cite{Massarenti_Mella}) provide
                powerful tools to transform results about nondefectivity to ones about identifiability. We list two special cases below.
            \item If $\dim V_{\bullet} = 2$ then $\rho$ is birational for every $d$ and $m < s(\Seg)$ except for
                $(m, d) = (2, 1), (3,2), (4,2), (5,4), (6, 9)$, see~\cite[Theorem~26]{Casarotti_Mella}.
            \item If $d = 3$, $\dim V_1 = \dim V_2 = \dim V_3$, then $\rho$ is
                birational for every $m < s(\Seg)$,
                see~\cite[Theorem~28]{Casarotti_Mella}.
        \end{enumerate}
        



% \bibliographystyle{alpha} 
% \bibliography{refs}  
{\small
\newcommand{\etalchar}[1]{$^{#1}$}
\begin{thebibliography}{ABGO24}

\bibitem[AB09]{Abo_Brambilla}
Hirotachi Abo and Maria~Chiara Brambilla.
\newblock Secant varieties of {S}egre-{V}eronese varieties {$\mathbb{P}^m\times \mathbb{P}^n$} embedded by {$\mathcal{O}(1,2)$}.
\newblock {\em Experiment. Math.}, 18(3):369--384, 2009.

\bibitem[ABGO24]{Abo_Brambilla_Galuppi_Oneto}
Hirotachi Abo, Maria~Chiara Brambilla, Francesco Galuppi, and Alessandro Oneto.
\newblock Non-defectivity of {S}egre-{V}eronese varieties.
\newblock {\em Proc. Amer. Math. Soc. Ser. B}, 11:589--602, 2024.

\bibitem[AF24]{Fulton_Anderson}
David Anderson and William Fulton.
\newblock {\em Equivariant cohomology in algebraic geometry}, volume 210 of {\em Cambridge Studies in Advanced Mathematics}.
\newblock Cambridge University Press, Cambridge, 2024.

\bibitem[AFP{\etalchar{+}}19]{Green__Weyman}
Marian Aprodu, Gavril Farkas, {\c{S}}tefan Papadima, Claudiu Raicu, and Jerzy Weyman.
\newblock Koszul modules and {G}reen's conjecture.
\newblock {\em Invent. Math.}, 218(3):657--720, 2019.

\bibitem[AH95]{AlexHirsch}
James Alexander and Andr{\'e} Hirschowitz.
\newblock Polynomial interpolation in several variables.
\newblock {\em J. Algebraic Geom.}, 4(2):201--222, 1995.

\bibitem[AMR19]{Araujo_Massarenti_Rischter}
Carolina Araujo, Alex Massarenti, and Rick Rischter.
\newblock On non-secant defectivity of {S}egre-{V}eronese varieties.
\newblock {\em Trans. Amer. Math. Soc.}, 371(4):2255--2278, 2019.

\bibitem[AOP09]{Abo_Ottaviani_Peterson_segre}
Hirotachi Abo, Giorgio Ottaviani, and Chris Peterson.
\newblock Induction for secant varieties of {S}egre varieties.
\newblock {\em Trans. Amer. Math. Soc.}, 361(2):767--792, 2009.

\bibitem[AP25]{Agostini_Park}
Daniele Agostini and Jinhyung Park.
\newblock Determinantal ideals of secant varieties, 2025.
\newblock \url{https://arxiv.org/abs/2510.01895}.

\bibitem[AR08]{Allman_Rhodes}
Elizabeth~S. Allman and John~A. Rhodes.
\newblock Phylogenetic ideals and varieties for the general {M}arkov model.
\newblock {\em Adv. in Appl. Math.}, 40(2):127--148, 2008.

\bibitem[Bal25]{Ballico__Partially_symmetric}
Edoardo Ballico.
\newblock Partially symmetric tensors and the non-defectivity of secant varieties of products with a projective line as a factor.
\newblock {\em Vietnam J. Math.}, 53(2):341--350, 2025.

\bibitem[BB73]{BialynickiBirula__decomposition}
A.~Bia{\l{}}ynicki-Birula.
\newblock Some theorems on actions of algebraic groups.
\newblock {\em Ann. of Math. (2)}, 98:480--497, 1973.

\bibitem[BB14]{Buczyska_Buczynski__cactus}
Weronika Buczy{\'n}ska and Jaros{\l}aw Buczy{\'n}ski.
\newblock Secant varieties to high degree {V}eronese reembeddings, catalecticant matrices and smoothable {G}orenstein schemes.
\newblock {\em J. Algebraic Geom.}, 23:63--90, 2014.

\bibitem[BB15]{bucz_bucz_smoothable_rank_example}
Weronika Buczy\'{n}ska and Jaros{\l}aw Buczy{\'n}ski.
\newblock On differences between the border rank and the smoothable rank of a polynomial.
\newblock {\em Glasg. Math. J.}, 57(2):401--413, 2015.

\bibitem[BB21]{Buczyska_Buczynski__border}
Weronika Buczy{\'{n}}ska and Jaros{\l}aw Buczy{\'{n}}ski.
\newblock Apolarity, border rank, and multigraded {H}ilbert scheme.
\newblock {\em Duke Mathematical Journal}, 170(16), November 2021.

\bibitem[BBS21]{Ballico_Bernardi_Santarsiero}
Edoardo Ballico, Alessandra Bernardi, and Pierpaola Santarsiero.
\newblock Identifiability of rank-3 tensors.
\newblock {\em Mediterr. J. Math.}, 18(4):Paper No. 174, 26, 2021.

\bibitem[BCS13]{BurgisserBook}
Peter B{\"u}rgisser, Michael Clausen, and Mohammad~A Shokrollahi.
\newblock {\em Algebraic complexity theory}, volume 315 of Grundlehren der mathematischen Wissenschaften.
\newblock Springer Science \& Business Media, 2013.

\bibitem[BGJ{\etalchar{+}}26]{BGJLM}
Jaros{\l}aw Buczy{\'n}ski, Fulvio Gesmundo, Joachim Jelisiejew, Joseph Landsberg, and Tomasz Ma{\'n}dziuk.
\newblock Symmetries of structure tensors of algebras and modules.
\newblock Preprint, 2026.

\bibitem[BK24]{Buczynski_Keneshlou}
Jaros{\l}aw Buczy{\'n}ski and Hanieh Keneshlou.
\newblock Cactus scheme, catalecticant minors, and scheme theoretic equations.
\newblock \url{https://arxiv.org/abs/2410.21908}, 2024.

\bibitem[BL14]{Buczynski_Landbserg_sigma3}
Jaros{\l}aw Buczy{\'n}ski and J.~M. Landsberg.
\newblock On the third secant variety.
\newblock {\em J. Algebraic Combin.}, 40(2):475--502, 2014.

\bibitem[BL16]{Blaser_Lysikov}
Markus Bl\"aser and Vladimir Lysikov.
\newblock On degeneration of tensors and algebras.
\newblock In {\em 41st {I}nternational {S}ymposium on {M}athematical {F}oundations of {C}omputer {S}cience}, volume~58 of {\em LIPIcs. Leibniz Int. Proc. Inform.}, pages Art. No. 19, 11 pages. Schloss Dagstuhl. Leibniz-Zent. Inform., Wadern, 2016.

\bibitem[BO11]{Bates_Oeding}
Daniel~J. Bates and Luke Oeding.
\newblock Toward a salmon conjecture.
\newblock {\em Exp. Math.}, 20(3):358--370, 2011.

\bibitem[BOT24]{Bernardi_Oneto_Taufer__On_GADs}
Alessandra Bernardi, Alessandro Oneto, and Daniele Taufer.
\newblock On schemes evinced by generalized additive decompositions and their regularity.
\newblock {\em Journal de Mathématiques Pures et Appliquées}, 2024.

\bibitem[Bri25]{Brion}
Michel Brion.
\newblock Notes on automorphism groups of projective varieties.
\newblock \url{https://www-fourier.univ-grenoble-alpes.fr/~mbrion/autos_final.pdf}, 2025.

\bibitem[Buc22]{Bucz_Communication}
Jaros{\l}aw Buczy{\'n}ski.
\newblock Personal communication to {J}oachim {J}elisiejew and {J}oseph {L}andsberg.
\newblock During the {T}oulouse workshop, 2022.

\bibitem[CC02]{Chiantini_Ciliberto__Weakly_defective}
L.~Chiantini and C.~Ciliberto.
\newblock Weakly defective varieties.
\newblock {\em Trans. Amer. Math. Soc.}, 354(1):151--178, 2002.

\bibitem[CC06]{Chiantini_Ciliberto__On_the_concept}
Luca Chiantini and Ciro Ciliberto.
\newblock On the concept of {$k$}-secant order of a variety.
\newblock {\em J. London Math. Soc. (2)}, 73(2):436--454, 2006.

\bibitem[CC10]{Chiantini_Ciliberto__On_the_dimension}
Luca Chiantini and Ciro Ciliberto.
\newblock On the dimension of secant varieties.
\newblock {\em J. Eur. Math. Soc. (JEMS)}, 12(5):1267--1291, 2010.

\bibitem[CDNS20]{Conca_deNegri_Stojanac}
Aldo Conca, Emanuela De~Negri, and {\v{Z}}eljka Stojanac.
\newblock A characteristic free approach to secant varieties of triple {S}egre products.
\newblock {\em Algebr. Comb.}, 3(5):1011--1021, 2020.

\bibitem[CFJ]{CFJ}
Stefano Canino, Cosimo Flavi, and Joachim Jelisiejew.
\newblock Detecting {D}irect {S}ums of {T}ensors and {T}heir {L}imits.
\newblock https://arxiv.org/abs/2512.05215.

\bibitem[CGZ23]{Christandl_Gesmundo_Zuiddam__A_gap_in_the_subrank}
Matthias Christandl, Fulvio Gesmundo, and Jeroen Zuiddam.
\newblock A gap in the subrank of tensors.
\newblock {\em SIAM J. Appl. Algebra Geom.}, 7(4):742--767, 2023.

\bibitem[CGZ26]{Chang_Gesmundo_Zuiddam}
Chia-Yu Chang, Fulvio Gesmundo, and Jeroen Zuiddam.
\newblock Border subrank of higher order tensors.
\newblock \url{https://arxiv.org/abs/2604.19872}, 2026.

\bibitem[CHL23a]{Conner_Harper_Landsberg}
Austin Conner, Alicia Harper, and J.~M. Landsberg.
\newblock New lower bounds for matrix multiplication and {$\rm det_3$}.
\newblock {\em Forum Math. Pi}, 11:Paper No. e17, 30, 2023.

\bibitem[CHL23b]{Conner_Huang_Landsberg}
Austin Conner, Hang Huang, and J.~M. Landsberg.
\newblock Bad and good news for {S}trassen's laser method: border rank of {${\rm perm}_3$} and strict submultiplicativity.
\newblock {\em Found. Comput. Math.}, 23(6):2049--2087, 2023.

\bibitem[CLPS25]{Park}
Doyoung Choi, Justin Lacini, Jinhyung Park, and John Sheridan.
\newblock Singularities and syzygies of secant varieties of smooth projective varieties.
\newblock \url{https://arxiv.org/abs/2502.19703}, 2025.

\bibitem[CM23]{Casarotti_Mella}
Alex Casarotti and Massimiliano Mella.
\newblock From non-defectivity to identifiability.
\newblock {\em J. Eur. Math. Soc. (JEMS)}, 25(3):913--931, 2023.

\bibitem[COV14]{Chiantini_Ottaviani_Vannieuwenhoven}
Luca Chiantini, Giorgio Ottaviani, and Nick Vannieuwenhoven.
\newblock An algorithm for generic and low-rank specific identifiability of complex tensors.
\newblock {\em SIAM J. Matrix Anal. Appl.}, 35(4):1265--1287, 2014.

\bibitem[COV17]{Chiantini_Ottaviani_Vannieuwenhoven__On_generic_identifiability}
Luca Chiantini, Giorgio Ottaviani, and Nick Vannieuwenhoven.
\newblock On generic identifiability of symmetric tensors of subgeneric rank.
\newblock {\em Trans. Amer. Math. Soc.}, 369(6):4021--4042, 2017.

\bibitem[DK26]{Dolevalek_Ken}
Mat{\v{e}}j Dole{\v{z}}{\'a}lek and Nikhil Ken.
\newblock Secant varieties of {S}egre-{V}eronese varieties {$\mathbb{P}^{m}\times \mathbb{P}^{n}$} embedded by {$\mathcal{O}(1,2)$} are non-defective for {$n \gg m^{3}$}, {$m \geq 3$}.
\newblock {\em J. Symbolic Comput.}, 135:Paper No. 102546, 36, 2026.

\bibitem[DM19]{Derksen_Makam}
Harm Derksen and Visu Makam.
\newblock Explicit tensors of border rank at least {$2d-2$} in {$K^d\otimes K^d\otimes K^d$} in arbitrary characteristic.
\newblock {\em Linear Multilinear Algebra}, 67(10):2104--2116, 2019.

\bibitem[DM26]{Dolevalek_Michalek}
Mat{\v{e}}j Dole{\v{z}}{\'a}lek and Mateusz Micha{\l}ek.
\newblock Nonlinear methods for tensors: determinantal equations for secant varieties beyond cactus.
\newblock \url{https://arxiv.org/abs/2602.12762}, 2026.

\bibitem[ENP20]{Ein_Niu_Park}
Lawrence Ein, Wenbo Niu, and Jinhyung Park.
\newblock Singularities and syzygies of secant varieties of nonsingular projective curves.
\newblock {\em Invent. Math.}, 222(2):615--665, 2020.

\bibitem[ES87]{Ellingsrud_Stromme__On_the_homology}
Geir Ellingsrud and Stein~Arild Str{\o}mme.
\newblock On the homology of the {H}ilbert scheme of points in the plane.
\newblock {\em Invent. Math.}, 87(2):343--352, 1987.

\bibitem[FG12]{Friedland_Gross}
Shmuel Friedland and Elizabeth Gross.
\newblock A proof of the set-theoretic version of the salmon conjecture.
\newblock {\em J. Algebra}, 356:374--379, 2012.

\bibitem[FH25]{Furukawa_Han}
Katsuhisa Furukawa and Kangjin Han.
\newblock On the singular loci of higher secant varieties of {V}eronese embeddings.
\newblock {\em J. Reine Angew. Math.}, 824:203--251, 2025.

\bibitem[Fog68]{fogarty}
John Fogarty.
\newblock Algebraic families on an algebraic surface.
\newblock {\em Amer. J. Math}, 90:511--521, 1968.

\bibitem[Fri13]{Friedland}
Shmuel Friedland.
\newblock On tensors of border rank {$l$} in {$\mathbb{C}^{m\times n\times l}$}.
\newblock {\em Linear Algebra Appl.}, 438(2):713--737, 2013.

\bibitem[FSO]{FOS}
Cosimo Flavi, Tim Seynnaeve, and Weronika Obcowska.
\newblock Classification of symmetric tensors of small border ranks.
\newblock In preparation.

\bibitem[Ga{\l}23]{Galazka}
Maciej Ga{\l}{\k{a}}zka.
\newblock Multigraded apolarity.
\newblock {\em Math. Nachr.}, 296(1):286--313, 2023.

\bibitem[GJLM25]{GJLM}
Fulvio Gesmundo, Joachim Jelisiejew, Joseph Landsberg, and Tomasz Ma{\'n}dziuk.
\newblock Boundary components of minimal border rank tensors.
\newblock Preprint, 2025.

\bibitem[GO22]{Galuppi_Oneto}
Francesco Galuppi and Alessandro Oneto.
\newblock Secant non-defectivity via collisions of fat points.
\newblock {\em Adv. Math.}, 409:Paper No. 108657, 58, 2022.

\bibitem[Hai01]{Haiman_macdonald}
Mark Haiman.
\newblock Hilbert schemes, polygraphs and the {M}acdonald positivity conjecture.
\newblock {\em J. Amer. Math. Soc.}, 14(4):941--1006 (electronic), 2001.

\bibitem[Han18]{Han__singularities}
Kangjin Han.
\newblock On singularities of third secant varieties of {V}eronese embeddings.
\newblock {\em Linear Algebra Appl.}, 544:391--406, 2018.

\bibitem[HMV20]{Huang_Michalek_Ventura}
Hang Huang, Mateusz Micha{\l}ek, and Emanuele Ventura.
\newblock Vanishing {H}essian, wild forms and their border {VSP}.
\newblock {\em Math. Ann.}, 378(3-4):1505--1532, 2020.

\bibitem[HS04]{Haiman_Sturmfels__multigraded}
Mark Haiman and Bernd Sturmfels.
\newblock Multigraded {H}ilbert schemes.
\newblock {\em J. Algebraic Geom.}, 13(4):725--769, 2004.

\bibitem[Hu21]{Hu__singular_Hilbert_schemes}
Xiaowen Hu.
\newblock On singular {H}ilbert schemes of points: local structures and tautological sheaves.
\newblock \url{https://arxiv.org/abs/2101.05236}, 2021.

\bibitem[Ilt12]{Ilten}
Nathan~Owen Ilten.
\newblock Versal deformations and local {H}ilbert schemes.
\newblock {\em J. Softw. Algebra Geom.}, 4:12--16, 2012.

\bibitem[IR01]{Ranestad_Iliev__VSPcubic}
Atanas Iliev and Kristian Ranestad.
\newblock {$K3$} surfaces of genus 8 and varieties of sums of powers of cubic fourfolds.
\newblock {\em Trans. Amer. Math. Soc.}, 353(4):1455--1468, 2001.

\bibitem[IT16]{Ilten_Teitler}
Nathan Ilten and Zach Teitler.
\newblock Product ranks of the {$3\times3$} determinant and permanent.
\newblock {\em Canad. Math. Bull.}, 59(2):311--319, 2016.

\bibitem[JJ26]{Jagiella_Jelisiejew}
Jakub Jagie{\l}{\l}a and Joachim Jelisiejew.
\newblock Classification and degenerations of small minimal border rank tensors via modules.
\newblock {\em To appear in Transactions AMS}, 2026.

\bibitem[JLP24]{JLP}
Joachim Jelisiejew, J.~M. Landsberg, and Arpan Pal.
\newblock Concise tensors of minimal border rank.
\newblock {\em Math. Ann.}, 388(3):2473--2517, 2024.

\bibitem[JM25]{Jelisiejew_Mandziuk}
Joachim Jelisiejew and Tomasz Ma{\'n}dziuk.
\newblock Limits of saturated ideals.
\newblock {\em J. Lond. Math. Soc. (2)}, 111(6):Paper No. e70188, 41, 2025.

\bibitem[JRS25]{Jelisiejew_Ranestad_Schreyer__polar_simplices}
Joachim Jelisiejew, Kristian Ranestad, and Frank-Olaf Schreyer.
\newblock The variety of polar simplices {II}.
\newblock {\em Exp. Math.}, 34(2):237--253, 2025.

\bibitem[JRS26]{AJR}
Joachim Jelisiejew, Ritvik Ramkumar, and Alessio Sammartano.
\newblock The {H}ilbert scheme of points on a threefold, {I}.
\newblock {\em J. Reine Angew. Math.}, 2026.

\bibitem[Kat94]{Katz__4points}
Sheldon Katz.
\newblock The desingularization of {${\rm Hilb}^4{\bf P}^3$} and its {B}etti numbers.
\newblock In {\em Zero-dimensional schemes ({R}avello, 1992)}, pages 231--242. de Gruyter, Berlin, 1994.

\bibitem[Kem75]{Kempf__Images_of_vector_bundles}
George~R. Kempf.
\newblock Images of homogeneous vector bundles and varieties of complexes.
\newblock {\em Bull. Amer. Math. Soc.}, 81(5):900--901, 1975.

\bibitem[Kol13]{Kollar__Sings}
J{\'a}nos Koll{\'a}r.
\newblock {\em Singularities of the minimal model program}, volume 200 of {\em Cambridge Tracts in Mathematics}.
\newblock Cambridge University Press, Cambridge, 2013.
\newblock With a collaboration of S{\'a}ndor Kov{\'a}cs.

\bibitem[Lan17]{JM_complexity}
J.~M. Landsberg.
\newblock {\em Geometry and complexity theory}, volume 169 of {\em Cambridge Studies in Advanced Mathematics}.
\newblock Cambridge University Press, Cambridge, 2017.

\bibitem[LM04]{Landsberg_Manivel}
J.~M. Landsberg and L.~Manivel.
\newblock On the ideals of secant varieties of {S}egre varieties.
\newblock {\em Found. Comput. Math.}, 4(4):397--422, 2004.

\bibitem[LM17]{Landsberg_Michalek__Abelian_Tensors}
J.~M. Landsberg and Mateusz Micha{\l}ek.
\newblock Abelian tensors.
\newblock {\em J. Math. Pures Appl. (9)}, 108(3):333--371, 2017.

\bibitem[LMR22]{Laface_Massarenti_Rischter}
Antonio Laface, Alex Massarenti, and Rick Rischter.
\newblock On secant defectiveness and identifiability of {S}egre-{V}eronese varieties.
\newblock {\em Rev. Mat. Iberoam.}, 38(5):1605--1635, 2022.

\bibitem[LP13]{Laface_Postinghel}
Antonio Laface and Elisa Postinghel.
\newblock Secant varieties of {S}egre-{V}eronese embeddings of {$(\mathbb{P}^1)^r$}.
\newblock {\em Math. Ann.}, 356(4):1455--1470, 2013.

\bibitem[LT10]{landsberg_teitler}
Joseph~M. Landsberg and Zach Teitler.
\newblock On the ranks and border ranks of symmetric tensors.
\newblock {\em Found. Comput. Math.}, 10(3):339--366, 2010.

\bibitem[LW07]{landsberg_weyman_secants_ideal_sings_of_sv_of_Segree}
Joseph~M. Landsberg and Jerzy Weyman.
\newblock On the ideals and singularities of secant varieties of {S}egre varieties.
\newblock {\em Bull. Lond. Math. Soc.}, 39(4):685--697, 2007.

\bibitem[MM24]{Massarenti_Mella}
Alex Massarenti and Massimiliano Mella.
\newblock Bronowski's conjecture and the identifiability of projective varieties.
\newblock {\em Duke Math. J.}, 173(17):3293--3316, 2024.

\bibitem[MOZ14]{michalek_oeding_zwiernik}
Mateusz Micha{\l{}}ek, Luke Oeding, and Piotr Zwiernik.
\newblock Secant cumulants and toric geometry.
\newblock {\em International Mathematics Research Notices}, 2015(12):4019--4063, 04 2014.

\bibitem[MV24]{Mandziuk_Ventura}
Tomasz Ma{\'n}dziuk and Emanuele Ventura.
\newblock Border apolarity and varieties of sums of powers.
\newblock \url{https://arxiv.org/abs/2310.19625}, 2024.

\bibitem[Oed16]{Oeding__Cohen_Macaulay}
Luke Oeding.
\newblock Are all secant varieties of segre products arithmetically cohen-macaulay?
\newblock \url{https://arxiv.org/abs/1603.08980}, 2016.

\bibitem[OO13]{Oeding_Ottaviani}
Luke Oeding and Giorgio Ottaviani.
\newblock Eigenvectors of tensors and algorithms for {W}aring decomposition.
\newblock {\em J. Symbolic Comput.}, 54:9--35, 2013.

\bibitem[Poo08]{poonen_moduli_space}
Bjorn Poonen.
\newblock The moduli space of commutative algebras of finite rank.
\newblock {\em J. Eur. Math. Soc. (JEMS)}, 10(3):817--836, 2008.

\bibitem[RS00]{ranestad_schreyer_VSP}
Kristian Ranestad and Frank-Olaf Schreyer.
\newblock Varieties of sums of powers.
\newblock {\em J. Reine Angew. Math.}, 525:147--181, 2000.

\bibitem[RS13]{Ranestad_Schreyer__polar_simplices}
Kristian Ranestad and Frank-Olaf Schreyer.
\newblock The variety of polar simplices.
\newblock {\em Doc. Math.}, 18:469--505, 2013.

\bibitem[RV17]{Ranestad_Voisin__VSP}
Kristian Ranestad and Claire Voisin.
\newblock Variety of power sums and divisors in the moduli space of cubic fourfolds.
\newblock {\em Doc. Math.}, 22:455--504, 2017.

\bibitem[{Sta}25]{stacks-project}
The {Stacks project authors}.
\newblock The stacks project.
\newblock \url{https://stacks.math.columbia.edu}, 2025.

\bibitem[Ste03]{stevens_deformations_of_singularities}
Jan Stevens.
\newblock {\em Deformations of singularities}, volume 1811 of {\em Lecture Notes in Mathematics}.
\newblock Springer-Verlag, Berlin, 2003.

\bibitem[Ull16]{Ullery}
Brooke Ullery.
\newblock On the normality of secant varieties.
\newblock {\em Adv. Math.}, 288:631--647, 2016.

\bibitem[Voi05]{Green__Voisin}
Claire Voisin.
\newblock Green's canonical syzygy conjecture for generic curves of odd genus.
\newblock {\em Compos. Math.}, 141(5):1163--1190, 2005.

\bibitem[VVM15]{Vannieuwenhoven_Vandebril_Meerbergen}
Nick Vannieuwenhoven, Raf Vandebril, and Karl Meerbergen.
\newblock A randomized algorithm for testing nonsingularity of structured matrices with an application to asserting nondefectivity of {S}egre varieties.
\newblock {\em IMA J. Numer. Anal.}, 35(1):289--324, 2015.

\bibitem[Wey03]{Weyman__Cohohomology_of_vector_bundles}
Jerzy Weyman.
\newblock {\em Cohomology of vector bundles and syzygies}, volume 149 of {\em Cambridge Tracts in Mathematics}.
\newblock Cambridge University Press, Cambridge, 2003.

\bibitem[Woj23]{Wojtala_Irreversibility}
Maciej Wojtala.
\newblock Irreversibility of structure tensors of modules.
\newblock {\em Collect. Math.}, 74(2):487--499, 2023.

\end{thebibliography}

}

\end{document}

