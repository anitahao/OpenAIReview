\documentclass[11pt,reqno]{amsart}

\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{indentfirst}
\usepackage[left=3cm, right=3cm, top=2.5cm, bottom=2.5cm]{geometry}
\geometry{margin=1in}
\usepackage[foot]{amsaddr}

\usepackage{setspace}
\onehalfspacing

% \usepackage{fancyhdr}
\usepackage{tikz}
\usetikzlibrary{graphs,patterns,decorations.markings,arrows,matrix}
\usetikzlibrary{calc,decorations.pathmorphing,decorations.pathreplacing,shapes}
\usetikzlibrary{trees,cd}
\usepackage[centertableaux]{ytableau}

% Math packages
\usepackage{amsmath, amssymb, amsthm, mathrsfs}
\usepackage{mathtools}
\mathtoolsset{showonlyrefs}
\usepackage{bbm}
\usepackage{enumitem}

% Probability / operators
\newcommand{\sectionbreak}{\bigskip}
\newcommand{\Pbb}{\mathbb{P}}
\newcommand{\Pp}{\mathbb{P}}
\newcommand{\Pb}{\mathbb{P}}
\newcommand{\Ebb}{\mathbb{E}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\tym}{\mathfrak{T}}
\newcommand{\PD}{\mathrm{PD}}
\newcommand{\GEM}{\mathrm{GEM}}
\newcommand{\Aut}{\mathrm{Aut}}
\newcommand{\Beta}{\mathrm{Beta}}
\newcommand{\Poi}{\mathrm{Poisson}}
\newcommand{\NB}{\mathrm{NegBin}}
\newcommand{\eps}{\varepsilon}
\newcommand{\as}{\stackrel{\mathrm{as}}{=}}
\newcommand{\dto}{\xrightarrow{d}}
\newcommand{\pto}{\xrightarrow{\Pp}}
\newcommand{\asto}{\xrightarrow{\mathrm{a.s.}}}
\newcommand{\ind}{\mathbbm{1}}
%
% % Theorem environments
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{assumption}[theorem]{Assumption}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
%
% Cross-references
\usepackage{hyperref}
\usepackage[nameinlink,capitalize]{cleveref}


\title{Asymptotic height of Plancherel random trees}
\author[Shengjun Zhang]{Shengjun Zhang}
\email{zhang.shengjun@universite-paris-saclay.fr}

\begin{document}



\begin{abstract}
We study a natural analogue of Ulam's problem for random rooted trees distributed according to a Plancherel-type measure.  
This probability measure is closely related to the classical Plancherel measure
on integer partitions. For a Plancherel random tree $T_n$ with $n$ vertices, we
investigate the asymptotic behavior of its height $H_n$, defined as the maximal
distance from the root to a leaf. We prove that this height grows
logarithmically. More precisely, there is a one-parameter family of random
trees $(T_n(\theta))_{n \in \N}$
indexed by $\theta<0$ such that
\[
    \frac{H_n}{\log n} \xrightarrow{\mathbb{P}} c_\star(\theta),
\]
where $\frac{H_n}{n} \xrightarrow{\mathbb{P}} c_\star(\theta)$ is an explicit constant depending on the parameter
$\theta$. The case of Plancherel trees corresponds to the parameter $\theta=1$.
\medskip
 

The proof is based on the fact that the Plancherel random trees can be viewed as Ewens fragmentation trees, for which the height exhibits a sharp threshold phenomenon.  An upper bound is obtained via $s$-mass functionals and contraction estimates, while the lower bound is derived by embedding the model into a branching random walk with logarithmic displacements governed by a Poisson--Dirichlet distribution.
The constant $c_\star(\theta)$ is characterized through a variational principle associated with this branching random walk.
\end{abstract}

\maketitle

\tableofcontents
\clearpage 

\section{Introduction}

In this section, we introduce the Plancherel random tree, a model of random rooted trees governed by a Plancherel-type measure. 
We then describe the connection between this measure and the classical
Plancherel measure on integer partitions, and we establish several basic properties that will be used repeatedly in the sequel.


\subsection{Plancherel random trees}

A \emph{rooted tree} $t$ is defined by the data of a distinguished vertex, called the \emph{root}, together with a multiset (that is, a set with multiplicities) of other rooted trees $\{(t_1)^{m_1}, (t_2)^{m_2}, \dots, (t_s)^{m_s}\}$. This multiset of subtrees may be empty. The tree $t$ can be represented as a graph by connecting the root to the roots of the subtrees $t_1$, which appear with multiplicity $m_1$, $t_2$ with multiplicity $m_2$, and so on.
The order of the subtrees is irrelevant, so different planar representations may correspond to the same rooted tree.
Throughout, rooted trees are considered up to rooted graph isomorphism.
The \emph{size} of a rooted tree is defined as its number of vertices, and we denote by $\tym(n)$ the set of rooted trees of size $n$.

The uniform probability measure on $\tym(n)$ is not necessarily the most natural choice, especially when one thinks of building a tree through a recursive leaf-grafting procedure. In \cite{fulman2009sharp}, Fulman introduced an analogue of the Plancherel measure on integer partitions for rooted trees.

Let $t \in \tym(n)$. A \emph{standard labelling} of $t$ is a numbering of the
vertices of the tree by the integers $0, 1,2,\dots,n-1$ such that labels are
strictly increasing along every path from the root to a leaf. For example,
\begin{center}
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw, inner sep=2pt] (root) at (0,0) {0};
        \node[circle,draw, inner sep=2pt] (n4) at (0,0.8) {2};
        \node[circle,draw, inner sep=2pt] (n1) at (-1,0.8) {3};
        \node[circle,draw, inner sep=2pt] (n3) at (1,0.8) {1};
        \node[circle,draw, inner sep=2pt] (n6) at (1,1.6) {4};
        \node[circle,draw, inner sep=2pt] (n5) at (0,2.4) {5};
        \node[circle,draw, inner sep=2pt] (n2) at (1,2.4) {7};
        \node[circle,draw, inner sep=2pt] (n7) at (2,2.4) {6};

        % Edges with labels
        \draw (root) -- (n4) ;
        \draw (root) -- (n1) ;
        \draw (root) -- (n3) ;
        \draw (n3) -- (n6) ;
        \draw (n6) -- (n5) ;
        \draw (n6) -- (n2) ;
        \draw (n6) -- (n7) ;

    \end{tikzpicture}
\end{center}
is a standard labelling. 
This definition provides the tree analogue of standard Young tableaux. However, since rooted trees are considered up to symmetry, there are in fact two natural notions of standard labellings.
\medskip
 
Viewing $t = (V_t, E_t)$ as a graph, a standard labelling is a bijection
\[
L : V_t \longrightarrow \{0,1,\dots,n - 1\}
\]
that is increasing along every root-to-leaf path.
Alternatively, one may consider \emph{standard labellings up to symmetry}, that is, equivalence classes of such bijections under the relation
\[
L_1 \sim L_2
\quad \Leftrightarrow \quad
\text{there exists a rooted graph isomorphism }
\psi : V_t \to V_t
\text{ such that }
L_2 \circ \psi = L_1.
\]
Consequently, the previous standard labelling is equivalent to
\begin{center}
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw, inner sep=2pt] (root) at (0,0) {0};
        \node[circle,draw, inner sep=2pt] (n4) at (0,0.8) {3};
        \node[circle,draw, inner sep=2pt] (n1) at (-1,0.8) {2};
        \node[circle,draw, inner sep=2pt] (n3) at (1,0.8) {1};
        \node[circle,draw, inner sep=2pt] (n6) at (1,1.6) {4};
        \node[circle,draw, inner sep=2pt] (n5) at (0,2.4) {6};
        \node[circle,draw, inner sep=2pt] (n2) at (1,2.4) {5};
        \node[circle,draw, inner sep=2pt] (n7) at (2,2.4) {7};

        % Edges with labels
        \draw (root) -- (n4) ;
        \draw (root) -- (n1) ;
        \draw (root) -- (n3) ;
        \draw (n3) -- (n6) ;
        \draw (n6) -- (n5) ;
        \draw (n6) -- (n2) ;
        \draw (n6) -- (n7) ;

    \end{tikzpicture}
\end{center}

We denote by $\mathrm{SL}(t)$ the set of standard labellings of the rooted tree $t$, by $d(t) = |\mathrm{SL}(t)|$ its cardinality, and by $u(t)$ the number of standard labellings of $t$ up to symmetry. These quantities are related by $d(t) = |\mathrm{Aut}(t)|\, u(t)$, where $\mathrm{Aut}(t)$ denotes the automorphism group of the rooted tree $t$.
There is a hook-length-type formula for $d(t)$, which seems to have appeared
first in an exercise of \cite{Knu73}. For a vertex $v \in V_t$, let $t_v$ denote the rooted subtree of $t$ located below the vertex $v$, with $v$ included (that is, the subtree consisting of $v$ and all edges and vertices that are descendants of $v$).
Then one has
\begin{equation*}
d(t)
=
\frac{|t|!}{\prod_{v \in V_t} |t_v|}.
\end{equation*}
For example, in the example displayed above, the sizes of the subtrees $t_v$ are
\begin{center}
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw, inner sep=2pt] (root) at (0,0) {8};
        \node[circle,draw, inner sep=2pt] (n4) at (0,0.8) {1};
        \node[circle,draw, inner sep=2pt] (n1) at (-1,0.8) {1};
        \node[circle,draw, inner sep=2pt] (n3) at (1,0.8) {5};
        \node[circle,draw, inner sep=2pt] (n6) at (1,1.6) {4};
        \node[circle,draw, inner sep=2pt] (n5) at (0,2.4) {1};
        \node[circle,draw, inner sep=2pt] (n2) at (1,2.4) {1};
        \node[circle,draw, inner sep=2pt] (n7) at (2,2.4) {1};

        % Edges with labels
        \draw (root) -- (n4) ;
        \draw (root) -- (n1) ;
        \draw (root) -- (n3) ;
        \draw (n3) -- (n6) ;
        \draw (n6) -- (n5) ;
        \draw (n6) -- (n2) ;
        \draw (n6) -- (n7) ;

    \end{tikzpicture}
\end{center}
and therefore $d(t)=252$ and $u(t)=252/12=21$.
We will give a proof of this formula inspired by \cite{greene1982probabilistic}
in Subsection \ref{sub:basic_properties}; it is related to an algorithm that samples a standard labelling uniformly at random from $\mathrm{SL}(t)$.
Given a rooted tree $t$, the product $d(t)\,u(t)$ corresponds to pairs of standard labellings of $t$ modulo symmetries. One then has the following fundamental identity:
\begin{equation}\label{eq:fund-identity}
\prod_{i=1}^{n} \binom{i+1}{2}
=
\sum_{t \in \tym(n)} d(t)\,u(t).
\end{equation}

There are several proofs of the fundamental identity for trees; one of them
relies on an RSK-type algorithm described in
Subsection \ref{sub:basic_properties}. With this identity, we can define an
interesting probability measure on $\tym(n)$.

\begin{definition}[Plancherel measure on $\tym(n)$]
The Plancherel measure on rooted trees of size $n$ is
\begin{equation}\label{eq:plancherel-measure}
\mathbb{P}_{n,\mathrm{trees}}[t]
=
\frac{d(t)\,u(t)}{\prod_{k=2}^{n} \binom{k}{2}}.
\end{equation}
\end{definition}


\subsection{Similarities with Plancherel random partitions}

In this subsection, we emphasize the close analogy between Plancherel random trees and Plancherel random partitions, a class of objects that has been extensively studied.
A partition of size $n$ is a weakly decreasing sequence of integers
\[
\lambda = (\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_\ell)
\]
such that
\[
n = |\lambda| = \sum_{i=1}^{\ell} \lambda_i .
\]
Such a sequence is most often represented by its \emph{Young diagram}, which is the array of boxes with $\lambda_1$ boxes in the first row, $\lambda_2$ boxes in the second row, and so on.
\[
 (5, 3, 2) = \ydiagram{2, 3, 5}
\]
\medskip

We denote by $\mathfrak{Y}(n)$ the set of partitions of size $n$. Let $\lambda \in \mathfrak{Y}(n)$, a \emph{standard Young tableau} of shape $\lambda$ is a filling of the boxes of the Young diagram of $\lambda$ with the integers $1,2,\dots,n$ in such a way that the entries are strictly increasing along each row and each column. For example,
\[
\ytableausetup{centertableaux}
    \begin{ytableau}
        6 & 9 \\
        3 & 5 & 8 \\
        1 & 2 & 4 & 7 & 10 
    \end{ytableau}
\]
is a standard Young tableau of shape $\lambda = (5,3,2)$. We denote by $\mathrm{ST}(\lambda)$ the set of standard Young tableaux of shape $\lambda$.
It can be shown (see, for instance, \cite{greene1982probabilistic}) that
\[
|\mathrm{ST}(\lambda)|
=
\frac{|\lambda|!}{\prod_{\square \in \lambda} h(\square,\lambda)},
\]
where the denominator is the product over all boxes $\square$ of the Young diagram of $\lambda$ of the corresponding \emph{hook lengths} $h(\square,\lambda)$.
The hook length of a box $\square$ is defined as the number of boxes in the largest L-shaped hook that can be drawn inside the diagram with $\square$ as its corner.
For example, the partition $\lambda = (5,3,2)$ has the following hook lengths:
\[
\ytableausetup{centertableaux}
    \begin{ytableau}
        2 & 1 \\
        4 & 3 & 1 \\
        7 & 6 & 4 & 2 & 1 
    \end{ytableau}
\]
which implies that $|\mathrm{ST}(\lambda)| = 450$.
\medskip

For every $n \in \mathbb{N}$, one has the following fundamental identity:
\[
n! = \sum_{\lambda \in \mathfrak{Y}(n)} |\mathrm{ST}(\lambda)|^2 .
\]
This fundamental identity allows one to define the \emph{Plancherel measure} on the set
$\mathfrak{Y}(n)$ of partitions of size $n$.
It is given by
\begin{equation}
\mathbb{P}_{n,\mathrm{partitions}}[\lambda]
=
\frac{|\mathrm{ST}(\lambda)|^2}{n!},
\qquad \lambda \in \mathfrak{Y}(n).
    \label{eq:plancherel-partitions}
\end{equation}
The similarity between the two identities \eqref{eq:plancherel-measure} and
\eqref{eq:plancherel-partitions} explains why we use the word Plancherel for our
model of random rooted trees. 
The asymptotic properties of random partitions distributed according to the
Plancherel measure have been studied extensively since the 1970s, in close
connection with Ulam's problem. If $\lambda \sim
\mathbb{P}_{n,\mathrm{partitions}}$, the size of the first part $\lambda_1$
has the same distribution as the length $\ell_n$ of the longest increasing
subsequence of a uniformly random permutation $\sigma_n \in \mathfrak{S}(n)$.
In particular, Logan--Shepp and Kerov--Vershik~\cite{LS77,KV77} proved that the
Young diagram of a Plancherel-distributed partition admits a deterministic limit
shape as $n \to \infty$. This implies:
\[
\frac{\lambda_1}{2\sqrt{n}} \xrightarrow[n\to\infty]{\Pbb} 1~.
\]
The goal of our paper is to obtain an analogue of this
 law of large numbers for Plancherel random rooted
trees. Notice that a second-order result exists in the setting of Plancherel
random partitions.
Indeed, the reinterpretation of the Plancherel measure as a point process made it possible to analyze the asymptotic behavior of the largest parts of the partition. The works~\cite{BOO00,Oko00,Joh01} established, by complementary methods, the Baik--Deift--Johansson correspondence:
\[
n^{1/3}
\left(
\frac{\lambda_1}{2\sqrt{n}} - 1,
\frac{\lambda_2}{2\sqrt{n}} - 1,
\dots
\right)
\sim_{\substack{\mathrm{law} \\ n\to \infty}}
n^{2/3}
\left(
\frac{x_1}{2\sqrt{n}} - 1,
\frac{x_2}{2\sqrt{n}} - 1,
\dots
\right),
\]
where $(x_1,x_2,\dots)$ denotes the sequence of largest eigenvalues of a Gaussian Unitary Ensemble (GUE) random Hermitian matrix. The common limiting object is the Airy determinantal point process.
In particular,
\[
n^{1/3}
\left(
\frac{\lambda_1}{2\sqrt{n}} - 1
\right)
\xrightarrow[n\to\infty]{\mathrm{law}}
\mathrm{TW},
\]
where $\mathrm{TW}$ denotes the Tracy--Widom distribution~\cite{tracy1994level}.
The analogue of this limiting result for Plancherel rooted trees is beyond the
scope of our paper, but might be accessible by using more advanced techniques
from the theory of branching processes.

\subsection{Properties of labelled and bilabelled trees}
\label{sub:basic_properties}

We first present an RSK-type algorithm that establishes the fundamental identity~\eqref{eq:fund-identity}
\[
\prod_{i=1}^{n-1} \binom{i + 1}{2}
=
\sum_{t \in \tym(n)} d(t)\,u(t)
\]
for rooted trees.
In the numerator of the Plancherel measure on rooted trees of size $n$, each factor $\binom{i + 1}{2}$
counts the number of sets of the form $\{u,v\}$ with $0 \le u < v \le i$. As a consequence, there must exist a bijection between rooted trees of size $n$ equipped with a pair of standard labellings, and sequences $(\{u_1,v_1\},\dots,\{u_{n-1},v_{n-1}\})$ with $0 \le u_i < v_i \le i$  for all $1 \le i \le n - 1$.
Such a RSK-type bijection has been proven in \cite{kuba2012bilabelled}. One constructs recursively a doubly labelled rooted tree of size $n$ by reading the sequence $\{u_1,v_1\},\dots,\{u_{n-1},v_{n-1}\}$. After reading $\{u_i,v_i\}$, the tree has size $i + 1$.
\begin{itemize}
    \item  At the first step, one grafts above the root labelled $(0,0)$ a vertex labelled $(1,1)$.
    \item At step $i \ge 2$, there are two vertices labelled $(u_i,p)$ and $(v_i,q)$. One shifts all left labels $r \ge v_i$ to $r+1$, and grafts above the vertex labelled $(u_i,p)$ a new vertex labelled $(v_i,i)$.
 \end{itemize}
For example, for the sequence $\{0,1\},\{0,1\},\{2,3\},\{1,2\},\{2,3\},\{1,6\},\{1,4\}$, one obtains successively the doubly labelled trees:
\begin{center}
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw, inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw, inner sep=1pt] (n1) at (0,0.8) {1,1};

        % Edges with labels
        \draw (root) -- (n1) ;
    \end{tikzpicture}\qquad\quad
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw, inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw, inner sep=1pt] (n1) at (-1,0.8) {2,1};
        \node[circle,draw, inner sep=1pt] (n2) at (1,0.8) {1,2};

        % Edges with labels
        \draw (root) -- (n1) ;
        \draw (root) -- (n2);
    \end{tikzpicture}\qquad\quad
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw , inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw , inner sep=1pt] (n1) at (-1,0.8) {2,1};
        \node[circle,draw , inner sep=1pt] (n2) at (1,0.8) {1,2};
        \node[circle,draw , inner sep=1pt] (n3) at (-1,1.6) {3,3};

        % Edges with labels
        \draw (root) -- (n1) ;
        \draw (root) -- (n2) ;
        \draw (n1) -- (n3) ;
    \end{tikzpicture}
    \qquad\quad
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw , inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw , inner sep=1pt] (n1) at (-1,0.8) {3,1};
        \node[circle,draw , inner sep=1pt] (n2) at (1,0.8) {1,2};
        \node[circle,draw , inner sep=1pt] (n3) at (-1,1.6) {4,3};
        \node[circle,draw , inner sep=1pt] (n4) at (1,1.6) {2,4};

        % Edges with labels
        \draw (root) -- (n1) ;
        \draw (root) -- (n2) ;
        \draw (n1) -- (n3) ;
        \draw (n2) -- (n4) ;
    \end{tikzpicture}
    \vspace*{5mm}

    \begin{tikzpicture}
        % Nodes
        \node[circle,draw , inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw , inner sep=1pt] (n1) at (-1,0.8) {4,1};
        \node[circle,draw , inner sep=1pt] (n2) at (1,0.8) {1,2};
        \node[circle,draw , inner sep=1pt] (n3) at (-1,1.6) {5,3};
        \node[circle,draw , inner sep=1pt] (n4) at (1,1.6) {2,4};
        \node[circle,draw , inner sep=1pt] (n5) at (1,2.4) {3,5};

        % Edges with labels
        \draw (root) -- (n1) ;
        \draw (root) -- (n2) ;
        \draw (n1) -- (n3) ;
        \draw (n2) -- (n4) ;
        \draw (n4) -- (n5) ;
    \end{tikzpicture}\qquad\quad
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw , inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw , inner sep=1pt] (n1) at (-1,0.8) {4,1};
        \node[circle,draw , inner sep=1pt] (n2) at (1,0.8) {1,2};
        \node[circle,draw , inner sep=1pt] (n3) at (-1,1.6) {5,3};
        \node[circle,draw , inner sep=1pt] (n4) at (0,1.6) {2,4};
        \node[circle,draw , inner sep=1pt] (n5) at (0,2.4) {6,6};
        \node[circle,draw , inner sep=1pt] (n6) at (2,1.6) {3,5};

        % Edges with labels
        \draw (root) -- (n1) ;
        \draw (root) -- (n2) ;
        \draw (n1) -- (n3) ;
        \draw (n2) -- (n4) ;
        \draw (n4) -- (n5)  ;
        \draw (n2) -- (n6)  ;
    \end{tikzpicture}\qquad\quad
    \begin{tikzpicture}
        % Nodes
        \node[circle,draw , inner sep=1pt] (root) at (0,0) {0,0};
        \node[circle,draw , inner sep=1pt] (n1) at (-1,0.8) {5,1};
        \node[circle,draw , inner sep=1pt] (n2) at (1,0.8) {1,2};
        \node[circle,draw , inner sep=1pt] (n3) at (-1,1.6) {6,3};
        \node[circle,draw , inner sep=1pt] (n4) at (0,1.6) {2,4};
        \node[circle,draw , inner sep=1pt] (n5) at (0,2.4) {3,5};
        \node[circle,draw , inner sep=1pt] (n6) at (2,1.6) {7,6};
        \node[circle,draw , inner sep=1pt] (n7) at (3,1.6) {4,7};

        % Edges with labels
        \draw (root) -- (n1) ;
        \draw (root) -- (n2) ;
        \draw (n1) -- (n3) ;
        \draw (n2) -- (n4) ;
        \draw (n4) -- (n5) ;
        \draw (n2) -- (n6) ;
        \draw (n2) -- (2.5,0.8);
        \draw (2.5,0.8) -- (n7) ;
    \end{tikzpicture}
\end{center}

\begin{proposition}[Bijection of the vertex-labelled construction]
Fix $n\ge 1$. Let $\mathrm S_n$ be the set of sequences
\[
\left(\{u_1,v_1\},\ldots,\{u_{n-1},v_{n-1}\}\right)
\quad\text{with}\quad
0\le u_i< v_i\le i,\ \ 1\le i\le n-1.
\]
Let $\mathrm T_n$ be the set of bilabelled rooted trees with $n$ vertices: an
element of $\mathrm{T}_n$ is a rooted tree $T$ whose vertices are labelled by pairs
\[
(\ell(v),r(v))\in\mathbb Z_{\ge0}\times \mathbb Z_{\ge0},
\]
such that $\ell$ and $r$ are both standard labellings of $T$.
Then, the map $F:\mathrm S_n\to\mathrm T_n$ defined by the recursive algorithm
described above is a bijection.
\end{proposition}

\begin{proof}
We build an explicit inverse map $G:\mathrm T_n\to\mathrm S_n$ and verify that $G\circ F=\mathrm{Id}$ and $F\circ G=\mathrm{Id}$.
At step $i$ the algorithm creates exactly one new vertex, and its right-label
equals $i$.
Subsequent steps only modify left-labels via shifts and never change any right-label.
Hence, in any $T\in\mathrm T_n$, for each $1\le i\le n-1$ there exists a unique vertex $w_i(T)$ such that
\[
r\left(w_i(T)\right)=i.
\]

\medskip
\noindent\textbf{Definition of the inverse map $G$.}
Fix $T\in\mathrm T_n$. We will recover the pairs $(u_i,v_i)$ for $i=n-1,n-2,\ldots,1$ and simultaneously reduce $T$ step by step.

Set $T^{(n-1)}:=T$. Suppose inductively that $T^{(i)}$ is a tree of size $i+1$ obtained after undoing the steps $n-1,\dots,i+1$.
Let $w_i:=w_i(T^{(i)})$ be the unique vertex with right-label $i$, and write
\[
(\ell(w_i),r(w_i))=(a_i,i).
\]
We define
$v_i := a_i.$ 
Let $p_i$ be the parent of $w_i$ (the unique neighbour of $w_i$ on the path to the root).
We then define
$u_i := \ell(p_i).$ 
This is well-defined because $w_i$ is not the root: it was created by grafting
above an existing vertex. Now we undo step $i$ to obtain $T^{(i-1)}$ as follows:
\begin{enumerate}
\item \emph{Delete the vertex $w_i$:} remove $w_i$.
\item \emph{Undo the left-label shift:} for every remaining vertex $v$, set
\[
\ell(v)\longmapsto
\begin{cases}
\ell(v)-1, & \text{if }\ell(v)>v_i,\\
\ell(v), & \text{if }\ell(v)<v_i.
\end{cases}
\]
\end{enumerate}
There is no remaining vertex with left-label exactly \(v_i\): indeed, in the forward construction,
at step \(i\) all existing labels \(\ell\ge v_i\) are first shifted to \(\ell+1\), and then the unique
new vertex is inserted with left-label \(v_i\). After deleting this vertex \(w_i\), the value \(v_i\)
therefore disappears from the set of remaining left-labels. 
Denote the resulting vertex-labelled rooted tree by $T^{(i-1)}$. 
Iterating for $i=n-1,n-2,\ldots,1$ yields a sequence
$(\{u_i,v_i\})_{i=1}^{n-1}\in\mathrm S_n$.
We set $G(T)$ to be this sequence.

\medskip
\noindent\textbf{Verification that $G\circ F=\mathrm{Id}$.}
Start from a sequence in $\mathrm S_n$ and construct $T^{(i)}$ forward by $F$.
At the end of step $i$, the newly created vertex has label $(v_i,i)$, hence it is exactly the unique vertex with right-label $i$.
Therefore the inverse procedure identifies the correct vertex $w_i$, reads $v_i=\ell(w_i)$, and reads $u_i$ as the left-label of its parent.
Finally, deleting \(w_i\) and reversing the shift of all left-labels strictly larger than \(v_i\)
restores exactly the tree from the previous step.
Thus every pair $(u_i,v_i)$ is recovered correctly, and $G(F(\cdot))=\mathrm{Id}$.

\medskip
\noindent\textbf{Verification that $F\circ G=\mathrm{Id}$.}
Conversely, start from $T\in\mathrm T_n$.
By construction, the tree $T^{(i-1)}$ is obtained from $T^{(i)}$ by removing the unique vertex with right-label $i$ and applying the inverse left-label shift.
Applying $F$ to the recovered pair $(u_i,v_i)$ performs exactly the opposite operations:
it shifts all left-labels $\ell\ge v_i$ by $+1$ and grafts a new vertex labelled $(v_i,i)$ above the vertex with left-label $u_i$.
Hence $F$ reconstructs $T^{(i)}$ from $T^{(i-1)}$ for each $i$, and in particular $F(G(T))=T$.

\medskip
Therefore $F$ is bijective.
\end{proof}


We next present a proof of the hook-length formula for the number of standard
labellings of a rooted tree. The argument is very similar in spirit to the
probabilistic proof of
the hook-length formula for partitions (see
\cite{greene1982probabilistic}), and it is based on a random walk on the rooted tree.

\begin{proposition}[Hook-length formula]\label{prop:hook-length}
For a rooted tree $t \in \tym(n)$, the number of standard labellings is given by
\begin{equation}\label{eq:hook-length}
|\mathrm{SL}(t)|
=
\frac{n!}{\prod_{v \in V_t} |t_v|}.
\end{equation}
\end{proposition}

Since rooted trees are considered up to rooted graph isomorphism, whenever we
perform an operation depending on individual vertices, we fix an arbitrary rooted
graph representative $\bar t$ of the isomorphism class $t$. The quantities
below do not depend on the choice of this representative. 

Let $t\in\mathfrak T(n+1)$, and fix a representative $\bar t$. Given $t' \in \tym(n)$, we denote $t' \nearrow t$
if $t'$ is obtained by removing a leaf (a vertex of degree 1) from $\bar t$ and taking the isomorphism class.
Given a rooted tree $t$ of size $n+1$, one selects a random rooted tree $t'$ of size $n$
among those satisfying $t' \nearrow t$ according to the following procedure:
\begin{itemize}
\item First, choose uniformly at random a vertex $v_1$ of $t$.
Each vertex has probability $1/(n+1)$ of being selected.
\item If $v_1$ is a leaf, remove it and obtain a tree $t'$ such that $t' \nearrow t$.
\item Otherwise, the size of the subtree $t_{v_1}$ is greater than $2$.
Choose uniformly at random a new vertex $v_2$ in the subtree $t_{v_1}$, distinct from $v_1$.
Each vertex in this subtree has probability $1/(|t_{v_1}|-1)$ of being selected.
\item If $v_2$ is a leaf, remove it and obtain $t' \in \tym(n)$ with
$t' \nearrow t$. Otherwise, repeat the procedure by choosing a vertex $v_3$ in $t_{v_2}$, then a vertex $v_4$
in $t_{v_3}$, and so on, until a leaf is selected.
\end{itemize}
At each step, the size of the subtree $t_{v_i}$ strictly decreases, so the procedure
terminates almost surely.
For $t'\in\mathfrak T(n)$, define
\[
m_t(t')
:=
\#\{\ell\in\mathrm{Leaves}(\bar t):[\bar t-\ell]=t'\}.
\]
Thus $t' \nearrow t$ if $m_t(t')>0$.

\begin{lemma}\label{lem:leaf-rem}
Let $p(t \to t')$ denote the probability of obtaining $t'$ from $t$ by the above random
leaf-removal procedure, and let
\[
g(t) = \frac{|t|!}{\prod_{v \in V_t} |t_v|}
\]
denote the right-hand side of the hook-length formula.
Then
\[
p(t \to t') = \frac{m_t(t')g(t')}{g(t)}.
\]
\end{lemma}

\begin{proof}
Let $v^\ast$ be one of the leaves removed from $t$ to obtain $t'$.
We have
\[
\frac{g(t')}{g(t)}
=
\frac{1}{n+1}
\frac{\prod_{v \in V_t} |t_v|}{\prod_{v \in V_{t'}} |t'_v|}.
\]
The vertices for which the subtree sizes differ in $t$ and $t'$ are precisely those lying
on the path connecting $v^\ast$ to the root.
Let
$C_{v^\ast} = \{v_1,v_2,\dots,v_{r-1},v_r=v^\ast\}$ 
denote this path.
Then
\[
\frac{g(t')}{g(t)}
=
\frac{1}{n+1}
\prod_{i=1}^{r-1}
\frac{|t_{v_i}|}{|t_{v_i}|-1}
=
\frac{1}{n+1}
\prod_{i=1}^{r-1}
\left(1+\frac{1}{|t_{v_i}|-1}\right)
=
\frac{1}{n+1}
\sum_{I \subset \{1,\dots,r-1\}}
\frac{1}{\prod_{i \in I} (|t_{v_i}|-1)}.
\]
One may also derive the same expression by analyzing the random edge-removal procedure
directly.
Let $I \subset \{1,\dots,r-1\}$ and let $C_I = \{v_i : i \in I\} \cup \{v_r\}$ denote a
possible path followed by the algorithm.
Denote by $p(t \to t',I)$ the probability of obtaining $t'$ when the procedure follows
the path $C_I$.
Then
\[
p(t \to t',I)
=
\frac{1}{n+1}
\frac{1}{\prod_{i \in I} (|t_{v_i}|-1)}.
\]
Summing over all subsets $I$ and all the corresponding leaves yields the desired identity.
\end{proof}


Since $p(t \to \cdot)$ defines a probability distribution on the set of trees $t'$ such
that $t' \nearrow t$, we obtain
\[
1 = \sum_{t' :\, t' \nearrow t} \frac{m_t(t')g(t')}{g(t)}.
\]
Equivalently, the function $g(\cdot)$ satisfies the recurrence
\[
g(t) = \sum_{t' :\, t' \nearrow t}m_t(t') g(t').
\]
On the other hand, the number \(|\mathrm{SL}(t)|\) of standard labellings satisfies the same recurrence.
Indeed, in any standard labelling of a tree \(t\) with \(|t|=n+1\), the maximal label must be
carried by a leaf. Removing that leaf produces a tree \(t'\) such that \(t' \nearrow t\), and
conversely every standard labelling of such a tree \(t'\) extends uniquely to a standard labelling
of \(t\) by assigning this label to the added leaf. Therefore
\[
|\mathrm{SL}(t)|=\sum_{t':\, t'\nearrow t}m_t(t') |\mathrm{SL}(t')|.
\]
Since \(g(\bullet)=1\) for the one-vertex tree and \(g\) satisfies the same recurrence by Lemma~\ref{lem:leaf-rem},
we conclude by induction that \(|\mathrm{SL}(t)|=g(t)\) for every rooted tree \(t\) (Proposition \ref{prop:hook-length}).


\subsection{Height of Plancherel random trees}

The main objective of this article is to study a natural analogue of Ulam's problem for random rooted trees distributed according to a Plancherel-type measure. More precisely, for a Plancherel random tree with $n$ vertices, we investigate the asymptotic behavior of its height $H_n$.
\medskip
 
Let $T_n \sim \mathbb{P}_n = \mathbb{P}_{n,\mathrm{trees}}$ be a random rooted
tree of size $n$ distributed according to the Plancherel
measure~\eqref{eq:plancherel-measure} on $\tym(n)$. For a vertex $u \in
V_{T_n}$, denote by $|u|$ the graph distance (i.e.\ the number of edges) from $u$ to the root.
We define the height of $T_n$ by
\[
    H_n := \max (\{ |u| : u \in V_{T_n} \}).
\]
The main goal of this article is to describe the asymptotic behavior of $H_n$
as $n \to \infty$. Here is a figure of a Plancherel tree of size $3000$, which
has height $H_{3000}=12$.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{PT3000.pdf}
\caption{Plancherel tree of size $3000$.}
\end{figure}

\begin{theorem}[Convergence of the scaled height]\label{thm:height}
There exists a constant $c>0$ such that
\[
\frac{H_n}{\log n}
\xrightarrow[n\to\infty]{\mathbb{P}} c~.
\]
The value of the constant $c$ is
$$\inf_{t>1}\left(\frac{t}{-\log\beta_t(2)}\right) \approx
1.6738,\qquad  \text{with }\beta_t(2) = \frac{\Gamma(t)\,\Gamma(3)}{\Gamma(2+t)} =
\frac{1}{t(t+1)}.$$
\end{theorem}
\bigskip
 
The proof relies on the observation that the Plancherel random tree can be viewed
as a particular case of an Ewens fragmentation tree with parameter $\theta = 2$.
Therefore, we shall study the height $H_n$ of Ewens fragmentation trees for general
$\theta > 0$.
More precisely, we shall show that for any $\varepsilon > 0$,
\[
 (c_\star(\theta)-\varepsilon)\log n
\le H_n \le (c_\star(\theta)+\varepsilon)\log n,
\]
with high probability, where $c_\star(\theta) = \inf_{t>1}(\frac{t}{-\log\beta_t(\theta)})$ is a constant
depending only on $\theta$, and $\beta_t(\theta) = \frac{\Gamma(t)\,\Gamma(\theta + 1)}{\Gamma(\theta+t)}$.
\bigskip

\noindent \textbf{Outline of the article.} Some notations used throughout the
paper will be fixed in the next subsection. In the next Section \ref{sec:2},
we explain why the Plancherel random tree fits naturally into the 
framework of Ewens fragmentation trees, and we identify it with the case $\theta=2$ 
in that family. We then establish a general threshold result for the height
$H_n$ (Theorem \ref{thm:threshold}) by means of generating functions and
Poissonization. This reduces the asymptotic
study of the height to finding a suitable rate $h(n)$. 
\begin{itemize}
    \item In Section~\ref{sec:3}, we
prove that $h(n)\leq C \log n$, by proving an a priori upper bound 
for $\frac{H_n}{\log n}$ via $s$-mass estimates and a contraction argument
for weighted generation sizes. 
\item Section~\ref{sec:4} is devoted to some preparation for the identification
    of the correct constant $C=c_{\star}(\theta)$ such that $h(n) \simeq
    c_{\star}(\theta)\,\log n$:  we establish the existence of many macroscopic 
    subtrees, and we prove an amplification argument which will be used to prove
    the lower bound with very high probability. 
\item 
 Finally, in Section~\ref{sec:5}, we prove the matching upper and
lower bounds by using a branching random walk argument, and by identifying the relevant
variational constant and showing the existence of sufficiently deep vertices
with high probability. The most technical arguments and
computations are relegated to the appendix (Section \ref{sec:appendix}).

\end{itemize}
The last section, Section~\ref{sec:6}, is devoted to the
Plancherel case itself: we make the constant explicit when $\theta=2$, 
and we conclude with some remarks and perspectives. \medskip

Although the random fragmentation trees that we shall consider are locally close to 
branching processes, they cannot directly be rewritten as
such, and one cannot directly apply the classical Biggins theory from
\cite{Big77, Big92, Big95}. Thus, a large part of the article is devoted to rigorous proofs of comparison
techniques and arguments; this explains why the paper is quite long.



\subsection{Probability spaces, filtrations and measures}\label{subsec:spaces}

In this subsection, we collect almost all probability spaces and probability measures that we will use in this paper.
\medskip

\noindent\textbf{The basic tree-valued space.}
We refer to \cite{Ott49, Har63, Nev86} for the classical formalism of random
branching trees, which we will here adapt to the case where nodes carry a mass.
Let $\mathcal U=\bigcup_{h\ge0}(\mathbb Z_{>0})^h$ be the Ulam--Harris tree, with root
$\varnothing$. We denote by $\Omega$ the set of pairs
$(\mathcal T,K),$ 
where:
\begin{itemize}
    \item $\mathcal T\subset \mathcal U$ is a \emph{rooted tree subset}, i.e.
    \begin{itemize}
        \item $\varnothing\in \mathcal T$;
        \item if $u=vj\in \mathcal T$, then its parent $v$ belongs to $\mathcal T$;
        \item for every $u\in \mathcal T$, there exists $\delta(u)\in \mathbb N$ such that
        $uj\in \mathcal T$ if and only if $1\le j\le \delta(u)$;
    \end{itemize}
\item $K: \mathcal T\to \mathbb N$ is a \emph{mass function}: 
    \begin{equation}
        K(u)+1 = \sum_{j=1}^{\delta(u)} K(uj).\label{eq:mass_function}
    \end{equation}
        In particular, $K(u)=1$ if and only if $\delta(u)=0$ and $u$ has no
        child. 
\end{itemize}
The conditions above imply that $K(\varnothing) = |\mathcal T|$. For $u\notin
\mathcal T$ we extend the degree and mass function by setting
$\delta(u) = K(u)=0$.
We equip $\Omega$ with the canonical $\sigma$-field
\[
\mathcal{F} := \sigma\left(\{\delta(u),\ u \in \mathcal{U}\}\sqcup \{K(u),\ u \in \mathcal{U}\}\right).
\]
For each $n\ge1$ and $\theta>0$, Definition~\ref{def:model} will define a probability measure on
$(\Omega,\mathcal F)$, namely the \emph{Ewens fragmentation law}
$\Pp^{(n,\theta)}$. 
The natural generation filtration on $(\Omega, \mathcal{F})$ is
\begin{equation}
\mathcal F_h:=\sigma\left(\{\delta(u),\ |u|\le h-1\}\sqcup\{K(u),\ |u|\le h\}\right),
\qquad h\ge0.\label{eq:filtration}
\end{equation}
\medskip

\noindent\textbf{The labelled space.}
Denote by $\mathfrak{P}_{<\infty}(\N)$  the set of finite subsets of $\N$.
Let $\Omega^\bullet$ be the set of pairs
$(\mathcal T,K^\bullet),$ 
where $\mathcal T\subset\mathcal U$ is as above and
$K^\bullet:\mathcal T\to \mathfrak P_{<\infty}(\mathbb N)$ 
assigns to each vertex a finite set of labels, with the condition:
$$K^\bullet(u) = \{\min K^\bullet(u)\} \sqcup \bigsqcup_{j=1}^{\delta(u)}
K^{\bullet}(uj)$$
for all $u \in \mathcal T$. The equation above is the labelled analogue of Equation
\eqref{eq:mass_function}. Besides, each pair $(\mathcal T, K^\bullet)$ in
$\Omega^\bullet$ is endowed with a standard labelling of the tree $\mathcal T$:
$$L(u) = \min K^\bullet(u) \quad \forall u \in \mathcal{T}.$$
We denote by $\mathcal F^\bullet$ the canonical
$\sigma$-field generated by the tree structure and by the labelled masses $K^\bullet(u)$,
$u\in\mathcal U$. The labelled Ewens fragmentation procedure described before
the proof of Theorem~\ref{thm:plancherel_to_fragmentation} will define a probability measure
$\Pp^{\bullet,(n,\theta)}$
on
$(\Omega^\bullet,\mathcal F^\bullet).$ 
There is a forgetful map
\begin{align*}
    \pi_{\mathrm{unlab}}:\Omega^\bullet&\to\Omega,\\
    (\mathcal T,K^\bullet)&\mapsto (\mathcal T,|K^\bullet|),
\end{align*}
and by construction
$\Pp^{(n,\theta)} = \Pp^{\bullet,(n,\theta)}\circ \pi_{\mathrm{unlab}}^{-1}.$ 
\medskip

\noindent\textbf{Plancherel measures at $\theta=2$.}
When $\theta=2$, we will prove that the Ewens fragmentation law coincides with the Plancherel tree law after
forgetting the masses and keeping only the underlying rooted tree isomorphism class.
More precisely, if
\begin{align*}
\imath:\Omega&\to \mathfrak T,\\ 
(\mathcal T,K)& \mapsto \text{isomorphism class of }\mathcal T,
\end{align*}
where $\mathfrak T = \bigsqcup_{n \geq 1} \mathfrak T(n)$ is the set of finite
rooted trees, then Theorem~\ref{thm:plancherel_to_fragmentation} states that the
image of $\Pp^{(n,2)}$ under $\imath$ is exactly the Plancherel
measure on rooted trees of size $n$:
\[
\Pp_n=\Pp^{(n,2)}\circ \imath^{-1}.
\]
Likewise, if
\begin{align*}
\imath^\bullet:\Omega^\bullet&\to \mathfrak T^\bullet,\\
(\mathcal T,K^\bullet)&\mapsto \text{isomorphism class of the labelled tree
}(\mathcal T, L),
\end{align*}
where $\mathfrak T^\bullet$ is the set of rooted trees endowed with a standard
labelling, then the labelled Plancherel measure defined by $\Pp_n^\bullet[(t,L)]
= \frac{d(t)}{\prod_{k=2}^n \binom{k}{2}}$ satisfies
\[
\Pp_n^\bullet:=\Pp^{\bullet,(n,2)}\circ (\imath^\bullet)^{-1}.
\]
Thus, $\Pp_n^\bullet$ is the labelled version of the Plancherel measure, and $\Pp_n$ is its image under the forgetful map
$\pi_{\mathrm{unlab}}: (t,L)\mapsto t$.
In particular, the hierarchy of measures at $\theta=2$ is:
\begin{center}
\begin{tikzcd}
    \Pp^{\bullet,(n,2)}
    \arrow[r, "\pi_{\mathrm{unlab}}"] \arrow[d, "\imath^{\bullet}"'] &
    \Pp^{(n,2)}
\arrow[d, "\imath"]\\
\Pp_n^\bullet \arrow[r, "\pi_{\mathrm{unlab}}"'] & \Pp_n   
\end{tikzcd}
\end{center}
\medskip

\noindent\textbf{The cemetery-extended tree space.}
In Section~\ref{sec:5}, Definition~\ref{def:cemetery}, we pass from the original
fragmentation tree to the \emph{cemetery-extended tree}
by attaching to each mass-one vertex an infinite deterministic ray of descendants of mass $1$
and displacement $0$. Since the resulting object $(\widetilde{\mathcal T},
K) =
\mathrm{Ext}(\mathcal T,K)$  is in general infinite, it is cleaner to introduce
a new state space.
Let $\widetilde\Omega$ be the set of pairs
\[
(\widetilde{\mathcal T}, K),
\]
where $\widetilde{\mathcal T}\subset \mathcal U$ is a rooted tree subset and
$K:\widetilde{\mathcal T}\to\mathbb N$ satisfies:
\begin{itemize}
    \item if $K(u)=k\ge2$, then $u$ has children $u1,\dots,u\delta(u)$ with
    \[
    k-1 = K(u1)+\cdots+K(u\delta(u)),
    \qquad
    K(uj)\ge1\ \text{ for all }1\le j\le \delta(u);
    \]
    \item if $K(u)=1$, then $\delta(u)=1$ and
    \[
    K(u1)=1.
    \]
\end{itemize}
We let $\widetilde{\mathcal F}$ be the canonical $\sigma$-field generated by the tree structure and the masses, and we define
\[
\widetilde{\mathcal F}_h
:=
\sigma\left(\{\delta(u):|u|\le h-1\}\sqcup\{K(u):|u|\le h\}\right).
\]
The cemetery-extension map
$\mathrm{Ext}:\Omega\to\widetilde\Omega$ 
is deterministic, hence the Ewens fragmentation law $\Pp^{(n,\theta)}$ will induce a probability measure
\[
\widetilde{\Pp}^{(n,\theta)}
:=
\Pp^{(n,\theta)}\circ \mathrm{Ext}^{-1}
\qquad\text{on }(\widetilde\Omega,\widetilde{\mathcal F}).
\]
\medskip

\noindent\textbf{The pruning map.}
Define the subset of \emph{genuine vertices} of a cemetery-extended tree by
\[
\mathcal T^{\mathrm{gen}}(\widetilde{\mathcal T},K)
:=
\{u\in \widetilde T:\ K(v)\ge2 \text{ for every strict ancestor } v\prec u\}.
\]
Equivalently, on each mass-one ray we keep only the first mass-one vertex and delete all its
strict descendants. This defines the pruning map
\[
\mathrm{Pr}:\widetilde \Omega\to\Omega,\qquad
\mathrm{Pr}(\widetilde{\mathcal T},K):=\left (\mathcal
T^{\mathrm{gen}}(\widetilde{\mathcal T},K),\,K|_{\mathcal
T^{\mathrm{gen}}(\widetilde{\mathcal T},K)}\right).
\]
By construction,
$\mathrm{Pr}\circ \mathrm{Ext}=\mathrm{Id}_{\Omega}.$ 
\medskip

\noindent\textbf{The spinal space.} In Subsection \ref{subsub:spinal_change}, we shall
use a positive mean one martingale $(\widetilde{Z}_h(t))_{h \ge 0 }$ defined on the probability
space $(\widetilde{\Omega},\widetilde{\mathcal F},\widetilde{\Pp}^{(n,\theta)})$
in order to perform a \emph{spinal change of measure}.
To define this change of measure rigorously, one has to keep track not only of the
cemetery-extended tree, but also of a distinguished infinite line. Therefore we introduce
\[
\Omega^{\mathrm{sp}}
:=
\left\{(\widetilde{\mathcal T} ,K,(U_h)_{h\ge0})\in \widetilde\Omega\times \mathcal U^{\mathbb N}:
U_0=\varnothing,\ U_{h+1}\text{ is a child of }U_h,\ \forall h\ge0\right\}.
\]
Its canonical $\sigma$-field is denoted by $\mathcal F^{\mathrm{sp}}$, and the corresponding
 filtration is
\[
\mathcal F_h^{\mathrm{sp}}
:=
\widetilde{\mathcal F}_h\vee \sigma(U_0,\dots,U_h),
\qquad h\ge0.
\]
This will be the state space for the spinal measure $\Q_t$, where $t > 1$ is a real
parameter. If $t=1$ and 
\[
\pi_{\mathrm{tree}}:\Omega^{\mathrm{sp}}\to \widetilde\Omega,
\qquad
(\widetilde{\mathcal T},K,(U_h)_{h\ge0})\mapsto (\widetilde{\mathcal
T},K).
\]
forgets the distinguished path, 
then $\Q_1 \circ (\pi_{\mathrm{tree}})^{-1} = \widetilde{\Pp}^{(n,\theta)}$.
\medskip

\noindent\textbf{Summary of the hierarchy of spaces and measures.}
The objects introduced above fit into the diagram:
\begin{center}
    \begin{tikzcd}[sep=small]
        (\Omega^{\mathrm{sp}},\mathcal{F}^{\mathrm{sp}},\Q_t) 
        \arrow[r, "t=1", "\pi_{\mathrm{tree}}"'] & (\widetilde{\Omega},
        \widetilde{\mathcal F},\widetilde{\Pp}^{(n,\theta)}) 
        \arrow[r, "\mathrm{Pr}"'] & 
        (\Omega,\mathcal{F}, \Pp^{(n,\theta)}) 
        \arrow[r, "\theta=2", "\imath"'] &
        (\mathfrak{T},\mathfrak{P}(\mathfrak{T}),\Pp_n) \\ 
        { \text{spinal tree}} \arrow[rd] & {} &   {\text{fragmentation tree}}
        \arrow[rd] &{} &  \\ 
                                         & {\text{cemetery-extended tree}}
        \arrow[ru] & &{ \text{Plancherel tree}}
    \end{tikzcd}
 \end{center}
\bigskip
 


\section{From Plancherel random trees to Ewens fragmentation trees}\label{sec:2}

In this section, we  introduce Ewens fragmentation trees and we explain how
Plancherel random trees arise as a particular case of this model (Theorem
\ref{thm:plancherel_to_fragmentation}).
We then use generating functions to establish a threshold phenomenon for the
height of Ewens fragmentation trees (Theorem \ref{thm:threshold}).
For most of the results on Ewens distributions, for example the relations
between the Ewens distribution and the Chinese restaurant process, we refer to \cite{arratia2003logarithmic} and \cite{pitman2006combinatorial}.


\subsection{Relations with Ewens fragmentation trees}

First, we recall the definition of the Ewens distribution.
For $x>0$ and integer $m\ge 0$, we define the rising factorial
\[
x^{(0)}:=1,\qquad x^{(m)}:=x(x+1)\cdots(x+m-1)\quad (m\ge 1),
\]
and the falling factorial
\[
(x)_0:=1,\qquad (x)_m:=x(x-1)\cdots(x-m+1)\quad (m\ge 1).
\]
Fix $\theta>0$. For an integer $m\ge 1$, an integer partition of $m$ can be encoded by its \emph{count vector}
\[
(c_1,\dots,c_m)\in\Z_{\ge 0}^m,\qquad \sum_{j=1}^m j c_j = m~,
\]
where $c_j$ is the number of blocks (parts) of size $j$~.

\begin{definition}[$\mathrm{Ewens}(m,\theta)$ distribution]\label{def:ewens}
    The $\mathrm{Ewens}(m,\theta)$ distribution on integer partitions of $m$ is the probability
measure on feasible count vectors
$(C_1,\dots,C_m)$ given by
\begin{equation}\label{eq:ewens}
\Pp\left((C_j)_{1\le j\le m}=(c_j)_{1\le j\le m}\right)
=\frac{m!}{\theta^{(m)}}\prod_{j=1}^m \frac{\theta^{c_j}}{j^{c_j}c_j!}~,
\end{equation}
for all $(c_j)_{1\le j\le m}$ such that $\sum_{j=1}^m j c_j=m$~.
\end{definition}

We now define a class of random rooted trees which will generalize the
Plancherel rooted trees from the introduction. The nodes of the \emph{random
fragmentation trees} $\mathcal{T}_n$ will
belong to the infinite Ulam--Harris tree $\mathcal{U} = \bigcup_{h \geq 0}
(\Z_{>0})^h$, and each node $u \in \mathcal{T}_n$ will carry a mass $K(u)$ equal
to the total number of its descendants.


\begin{definition}[Ewens fragmentation process $\Pp^{(n,\theta)}$]\label{def:model}
Fix $\theta>0$ and an integer $n\ge 1$.
We construct a random finite rooted tree $(\mathcal T_n , K)\in \Omega$ as follows.
Each vertex $u$ carries an integer mass $K(u)\in\{1,2,\dots\}$.
The root is denoted by $\varnothing$ and has mass
\[
K(\varnothing)=n.
\]

\smallskip
\noindent\textbf{Splitting rule.}
Let $u$ be a vertex.
\begin{itemize}
\item If $K(u)=1$, then $u$ is declared a leaf and produces no children.
\item If $K(u)=k\ge 2$, set $m:=k-1$ and sample an $\mathrm{Ewens}(m,\theta)$ partition with count vector
$(C^{(u)}_1,\dots,C^{(u)}_m)$ as in Definition~\ref{def:ewens}.
Let $(A^{(u)}_1 \ge A^{(u)}_2 \ge \cdots \ge A^{(u)}_{\delta(u)})$ be the corresponding partition of block sizes, i.e.
\[
\sum_{i=1}^{\delta(u)} A^{(u)}_i = m,\qquad
\#\{i: A^{(u)}_i=j\}=C^{(u)}_j.
\]
Then $u$ produces $\delta(u)$ children, denoted $(ui)_{1\le i\le \delta(u)}$, with masses
\[
K(ui):=A^{(u)}_i,\qquad i=1,\dots,\delta(u).
\]
\end{itemize}
All splitting variables at different vertices are sampled independently. We
denote $\Pp^{(n,\theta)}$ the probability measure on $(\Omega,\mathcal{F})$
corresponding to this procedure.
\end{definition}

The Ewens fragmentation trees satisfy a Markov branching property:
\begin{proposition}[Markov branching property]\label{prop:markov}
Fix $n\ge 1$.
Conditionally on the multiset of children masses $(A_i)_{1\le i\le \delta}$ produced
at the root of $\mathcal T_n$, the subtrees rooted at distinct children are independent and satisfy
\[
\mathcal T_n^{(i)} \ \stackrel{d}{=}\ \mathcal T_{A_i},
\]
where $\mathcal T_n^{(i)}$ denotes the subtree rooted at the $i$-th child and $\mathcal T_k$ denotes an independent copy
of the entire model started from mass $k$.
The same statement holds for every node $u$ in place of the root, conditionally on the children masses of $u$.
\end{proposition}

\begin{proof}
This is immediate from Definition~\ref{def:model}: once the
children masses $(A_i)_{1\leq i \leq \delta(u)}$ at a node $u$
are sampled, the evolution below each child depends only on that child mass and uses independent fresh Ewens partitions,
independent across different children and independent of the past. Therefore the child subtrees are conditionally independent,
and each has the same law as the original model started from the corresponding mass.
\end{proof}

We now show that for $\theta = 2$, the Ewens fragmentation tree law
$\Pp^{(n, 2)}$ corresponds to the Plancherel measure on $\tym(n)$ given by Equation \eqref{eq:plancherel-measure}.

\begin{theorem}[From Plancherel random trees to Ewens fragmentation
    trees]\label{thm:plancherel_to_fragmentation}
    Fix $\theta = 2$ and an integer $n \ge 1$. Let $T_n=\imath(\mathcal{T}_n)$ be the
isomorphism class in $\tym(n)$ of a random
rooted tree constructed as an Ewens fragmentation tree $(\mathcal{T}_n,K)$ with law
$\Pp^{(n,2)}$. Then,
\begin{equation*}
\Pp(T_n = t) = \mathbb{P}_n[t]
= \frac{d(t)\,u(t)}{\prod_{k=2}^{n} \binom{k}{2}},
\qquad t \in \tym(n).
\end{equation*}
\end{theorem}

% PL

To prove this result, it is convenient to rewrite the Plancherel measure, the
Ewens distribution and the Ewens fragmentation process as probability measures on \emph{labelled}
objects:
\begin{itemize}
    \item Denote by $(t,L)$ a rooted tree with size $n$ endowed with a standard labelling, and
        $\tym^{\bullet}(n)$ the set of such pairs (up to isomorphism). The Plancherel measure
        $\Pp_n$ on rooted trees is the image under the map 
        \begin{align}\label{eq:forget_labels}
            \pi_{\mathrm{unlab}}:\tym^{\bullet}(n) &\to \tym(n) \\
(t,L)  &\mapsto t\nonumber
\end{align}
of the probability measure $\Pp_n^{\bullet}[(t,L)] = \frac{d(t)}{\prod_{k=2}^n
\binom{k}{2}}$ on labelled rooted trees.

\item For any set $S$ with cardinality $m$, the $\mathrm{Ewens}(m,\theta)$ distribution on integer partitions of $m$
    is the image under the map 
    \begin{align}\label{eq:forget_2}
            \text{set partitions of }S &\to \mathfrak{Y}(m) \\ 
            (\pi_1,\pi_2,\ldots,\pi_\ell) &\mapsto \text{non-increasing
            reordering of }(|\pi_1|,|\pi_2|,\ldots,|\pi_{\ell}|) \nonumber
        \end{align}
        of the probability measure
        on set partitions of $S$
        \begin{equation}
        \mathrm{Ewens}^{\bullet}(S,\theta)[\pi] = \frac{1}{\theta^{(m)}} \prod_{i=1}^{\ell}
        (\theta\,(|\pi_i| -1)!).
            \label{eq:ewens_labelled}
        \end{equation}
        Indeed, if $\pi$ is a set partition with sizes of parts given by
        a count vector $(c_1,\ldots,c_m)$, then multiplying the formula above by the
        number $\frac{m!}{\prod_{j=1}^m (j!)^{c_j} c_j!}$ of set partitions with
        the same sizes of parts yields Equation
        \eqref{eq:ewens}.

\item The Ewens fragmentation process $\Pp^{(n,\theta)}$ can also be lifted to
    get a labelled rooted tree $(\mathcal{T}_n,K^\bullet)$. To this purpose,
    we replace each integer
mass $K(u)$ by a \emph{labelled mass} $K^\bullet(u)$ which is a finite subset of
    $\N$. We set $K^{\bullet}(\varnothing) = \{0,1,2,\ldots,n-1\}$.
    Given a vertex $u$, if $K^{\bullet}(u) = \{l\}$ is a singleton, then $u$ produces no
    children, and we set $\mathcal{L}_n(u) = l$.
    Otherwise, we give to $u$ the label $L(u) = \min K^{\bullet}(u)$, and we sample
an $\mathrm{Ewens}^{\bullet}(S,\theta)$ set partition $\{\pi_i\}_{i=1}^{\delta(u)}$ of $S = K^{\bullet}(u)
\setminus \{L(u)\}$. The parts $\pi_i$ are ordered by decreasing size, and
then by their minimal element. The vertex $u$ produces $\delta(u)$ children with labelled
masses $$K^{\bullet}(ui) = \pi_i, \qquad i=1,\ldots,\delta(u).$$
As in the unlabelled case, all splitting variables at different vertices are
sampled independently.
The procedure described above defines a probability
measure $\Pp^{\bullet,(n,\theta)}$ on the labelled analogue
$\Omega^\bullet$ of $\Omega$ (see Subsection \ref{subsec:spaces}).
Note that by construction:
\begin{itemize}
    \item 
If $(\mathcal{T}_n, K^{\bullet}) \sim
\Pp^{\bullet,(n,\theta)}$, then the map
$L:V_{\mathcal{T}_n} \to \{0,1,\ldots,n-1\}$ is a standard labelling of the random tree $\mathcal{T}_n$.
\item
The image of the measure
$\Pp^{\bullet,(n,\theta)}$ of the labelled Ewens fragmentation process
by the forgetful map $\pi_{\mathrm{unlab}}: (\mathcal{T}_n,K^\bullet) \mapsto
(\mathcal{T}_n,|K^\bullet|)$ is the measure
$\Pp^{(n,\theta)}$ on $\Omega$, 
because forgetting labels at each node leads to the construction from Definition
\ref{def:model}.
\end{itemize}
\end{itemize}
Denote $\Omega_n$ the subset of $\Omega$ which consists of trees $\mathcal{T}_n$
with $K(\varnothing)=n$, and $\Omega_n^\bullet$ the subset of
$\Omega^{\bullet}$ which consists of pairs $(\mathcal{T}_n, K^\bullet)$
with $K^\bullet(\varnothing) = \{0,1,\ldots,n-1\}$. 
The measures
$\Pp^{(n,\theta)}$ and $\Pp^{\bullet,(n,\theta)}$ are respectively
supported by $\Omega_n$ and by $\Omega_n^{\bullet}$, and we have two natural maps: 
\begin{align*}
    \imath : \Omega_n &\to \mathfrak{T}(n) \\ 
    (\mathcal{T}_n,K) &\mapsto \text{isomorphism class of
    }\mathcal{T}_n;\\
    \imath^{\bullet} : \Omega_n^{\bullet} &\to \mathfrak{T}^\bullet(n) \\
    (\mathcal{T}_n,K^\bullet) &\mapsto \text{isomorphism class  of
    }(\mathcal{T}_n,L).
\end{align*}
Now, it suffices to prove that
$\Pp_{n}^{\bullet}$ comes from the labelled Ewens fragmentation measure:
$$\Pp_n^\bullet = \Pp^{\bullet,(n,2)} \circ (\imath^{\bullet})^{-1}.$$
The identity $\Pp_n = \Pp^{(n,2)} \circ \imath^{-1}$ will then
follow by projecting through the maps \eqref{eq:forget_labels} and
\eqref{eq:forget_2}.

\begin{remark}
In the literature, a rooted tree with a standard labelling is also called a
\emph{recursive tree}. These objects have been introduced by Meir and Moon in
\cite{MM78}, and their behavior under the \emph{uniform} measure on
$\tym^{\bullet}(n)$ : 
$$\Pp[(t,L)]
= \frac{1}{|\tym^{\bullet}(n)|}=\frac{1}{n!}$$ has been extensively studied in many papers; see \cite{MS95}
for a survey of the known results on this uniform model. In particular, the
 height of a uniform recursive tree with size $n$ has been proven by Pittel in
\cite{Pit94} to be equivalent to $\mathrm{e} \log n$. Our main Theorem \ref{thm:height}
is the analogue result for a non-uniform, Plancherel-distributed recursive tree.
\end{remark}

\begin{remark}
If $(\mathcal{T}_n,K^{\bullet}) \in \Omega_n^{\bullet}$, then the labelled mass
function $K^\bullet$ and the
standard labelling $L$ can be deduced from one another:
$L(u) = \min K^\bullet(u)$, and $K^\bullet(u) = \{L(v),\
v \text{ descendant of }u\}$. We shall use this correspondence implicitly in the
sequel.
\end{remark}
 
\begin{proof}[Proof of Theorem \ref{thm:plancherel_to_fragmentation}]
We prove the result by induction on $n$. For $n=1$, the claim is trivial.
Assume that for all $k \le n-1$, if $(\mathcal{T}_k,\mathcal L_k)$ is a labelled  Ewens
fragmentation tree with law $\Pp^{\bullet,(k,2)}$, then
\[
    \Pp(\imath^\bullet(\mathcal{T}_k, \mathcal{L}_k) = (t,L))
=
\frac{d(t)}{\prod_{r=2}^{k} \binom{r}{2}},
\qquad t \in \mathfrak{T}(k).
\]
Notice that by the hook-length formula \eqref{eq:hook-length}, the right-hand
side rewrites as: 
$$ \frac{k!}{\prod_{v \in V_t} |t_v| }\,\frac{2^{k-1}}{k!\,(k-1)!} =
\frac{2^{k-1}}{(k-1)!\,\prod_{v \in V_t} |t_v|}.$$
Let $(\mathcal{T}_n,\mathcal{L}_n)$ be a labelled Ewens fragmentation tree with
distribution
$\Pp^{\bullet,(n,2)}$, and $(t,L)$ be a fixed recursive tree with size
$n$. For each child $v_i$ of the root of $t$, the set of labels of the vertices in
the subtree $t_{v_i}$ forms a subset $\pi_i$ of $\{1,\ldots,n-1\}$. The collection
$\pi = \{\pi_i\}_{i=1}^{\delta}$ of these subsets forms a set partition of
$\{1,\ldots,n-1\}$ by definition of a standard labelling. 
Then,
$$\Pp(\imath^{\bullet}(\mathcal{T}_n, \mathcal{L}_n) = (t,L)) =
\mathrm{Ewens}^{\bullet}(\{1,\ldots,n-1\},2)[\pi] \,\,\,\prod_{i=1}^{\delta} 
\left(\frac{d(t_{v_i})}{\prod_{r=2}^{|\pi_i|} \binom{r}{2}}\right) $$
using the induction hypothesis, and the analogue of the Markov property
\ref{prop:markov} for labelled fragmentation trees. Combining Equation
\eqref{eq:ewens_labelled} and the hook-length formula \eqref{eq:hook-length}, we
obtain:
\begin{align*}
    \Pp(\imath^{\bullet}(\mathcal{T}_n, \mathcal{L}_n) = (t,L)) = \frac{2^\delta}{2^{(n-1)}}
    \prod_{i=1}^\delta \left(\frac{2^{|\pi_i|-1}}{\prod_{v \in V_{t_{v_i}}}
    |t_v|}\right) =  \frac{2^{n-1}}{n!}
    \left(\prod_{v \neq \varnothing} \frac{1}{|t_v|}\right) =
    \frac{2^{n-1}}{(n-1)!\,\prod_{v \in V_t} |t_v|},
\end{align*}
whence the result in size $n$. 
% \[
% \sum_{i=1}^{d} A_i = n-1,
% \qquad
% \#\{i : A_i = j\} = C_j
% \]
% be the masses of the children of the root, distributed according to the $\mathrm{Ewens}(n-1,2)$ law.
%
% Fix a rooted tree $t \in \tym(n)$, and let
% \[
% \sum_{i=1}^{d} a_i = n-1,
% \qquad
% \#\{i : a_i = j\} = c_j
% \]
% be the sizes of the root-subtrees of $t$, denoted by $t^{(1)},\dots,t^{(d)}$.
%
% Let $\Sigma(t)$ be the set of isomorphism types among the rooted trees $\{t^{(i)}\}_{1\le i\le d}$.
% For each $\sigma \in \Sigma(t)$, define
% \[
% m_\sigma := \#\{1\le i\le d : t^{(i)} \simeq \sigma\}.
% \]
% Then the automorphism group of $t$ decomposes as
% \begin{equation}\label{eq:Aut-decomposition}
% |\Aut(t)|
% =
% \left(\prod_{\sigma \in \Sigma(t)} m_\sigma!\right)
% \prod_{i=1}^d |\Aut(t^{(i)})|.
% \end{equation}
%
% Conditionally on the count vector $(C_j)_{j\ge1}$, the Ewens splitting produces an unordered multiset of child masses. 
% For convenience, we realize this multiset as a uniformly random ordering $(A_1,\dots,A_d)$ of its elements, where $d=\sum_j C_j$. 
% The number of distinct orderings compatible with the multiplicities $(c_j)$ is
% \[
% \frac{d!}{\prod_{j\ge1} c_j!}.
% \]
%
% However, different ordered collections of subtrees may correspond to the same unordered rooted tree. 
% More precisely, exactly
% \[
% \frac{d!}{\prod_{\sigma\in\Sigma(t)} m_\sigma!}
% \]
% ordered realizations collapse to the same unordered rooted tree $t$.
%
% Consequently, when passing from the ordered representation to the unordered rooted tree $t$, a net combinatorial correction factor
% \[
% \frac{\prod_{j\ge1} c_j!}{\prod_{\sigma\in\Sigma(t)} m_\sigma!}
% \]
% appears.
%
%
% By the Markov branching property and conditional independence of the subtrees,
% \begin{align*}
% \Pp(\mathcal{T}_n = t)
% &=
% \Pp((C_j)=(c_j))
% \cdot
% \frac{\prod_j c_j!}{\prod_{\sigma\in\Sigma(t)} m_\sigma!}
% \cdot
% \prod_{i=1}^d \Pp(\mathcal{T}_{a_i} = t^{(i)}).
% \end{align*}
%
% By the $\mathrm{Ewens}(n-1,2)$ distribution,
% \[
% \Pp((C_j)=(c_j))
% =
% \frac{(n-1)!}{2^{(n-1)}}
% \prod_{j\ge1} \frac{2^{c_j}}{j^{c_j} c_j!}.
% \]
% By the induction hypothesis,
% \[
% \Pp(\mathcal{T}_{a_i} = t^{(i)})
% =
% \frac{d(t^{(i)})\,u(t^{(i)})}{\prod_{r=2}^{a_i} \binom{r}{2}}
% =
% \frac{d(t^{(i)})^2}{|\Aut(t^{(i)})|\,\prod_{r=2}^{a_i} \binom{r}{2}}.
% \]
%
% Combining these expressions and using \eqref{eq:Aut-decomposition}, we obtain
% \begin{align*}
% \Pp(\mathcal{T}_n = t)
% &=
% \frac{(n-1)!}{2^{n-1}}
% \prod_{j\ge1} \frac{2^{c_j}}{j^{c_j}}
% \cdot
% \frac{1}{|\Aut(t)|}
% \cdot
% \prod_{i=1}^d
% \frac{d(t^{(i)})^2}{\prod_{r=2}^{a_i} \binom{r}{2}}.
% \end{align*}
%
% Note that
% \[
% \prod_{j\ge1} j^{c_j} = \prod_{i=1}^d a_i,
% \qquad
% \prod_{j\ge1} 2^{c_j} = 2^d,
% \qquad
% \sum_{i=1}^d (a_i - 1) = n-1-d.
% \]
% Moreover,
% \[
% \prod_{r=2}^{a} \binom{r}{2}
% =
% \frac{a!(a-1)!}{2^{a-1}}.
% \]
% Hence,
% \[
% \prod_{i=1}^d \prod_{r=2}^{a_i} \binom{r}{2}
% =
% \frac{\prod_{i=1}^d a_i!(a_i-1)!}{2^{n-1-d}}.
% \]
%
% Substituting and simplifying,
% \[
% \Pp(\mathcal{T}_n = t)
% =
% \frac{2^{n-1}}{n}
% \cdot
% \frac{1}{|\Aut(t)|}
% \cdot
% \frac{\prod_{i=1}^d d(t^{(i)})^2}{(\prod_{i=1}^d a_i!)^2}.
% \]
%
% By the hook-length formula \eqref{eq:hook}, since
% \[
% \prod_{i = 1}^d \prod_{v \in V_{t^{(i)}}} |t_v| = \frac{1}{n}\prod_{v \in V_{t}} |t_v|,
% \]
% we have,
% \[
% d(t)
% =
% \frac{n!}{n \prod_{i=1}^d a_i!}
% \prod_{i=1}^d d(t^{(i)}).
% \]
% Therefore,
% \[
% \Pp(\mathcal{T}_n = t)
% =
% \frac{d(t)^2}{|\Aut(t)|}
% \cdot
% \frac{2^{n-1} n}{(n!)^2}.
% \]
%
% Finally, since
% \[
% \prod_{k=2}^n \binom{k}{2}
% =
% \frac{n!(n-1)!}{2^{n-1}},
% \]
% we conclude that
% \[
% \Pp(\mathcal{T}_n = t)
% =
% \frac{d(t)\,u(t)}{\prod_{k=2}^n \binom{k}{2}},
% \]
% as claimed.
\end{proof}


In the sequel, we will frequently use the following basic formula
satisfied by the Ewens distributions:

\begin{lemma}[Mixed factorial moments]\label{lem:Mixed}
Let $(C_1,\dots,C_m)\sim \mathrm{Ewens}(m,\theta)$.
Fix distinct indices $j_1,\dots,j_r\in\{1,\dots,m\}$ and integers $a_1,\dots,a_r\ge 1$ such that
$
L=\sum_{\ell=1}^r a_\ell j_\ell \le m.
$
Then,
\begin{equation*}
\E\left[\prod_{\ell=1}^r (C_{j_\ell})_{a_\ell}\right]
=
\left(\prod_{\ell=1}^r \left(\tfrac{\theta}{j_\ell}\right)^{a_\ell}\right)\,
\frac{m!}{(m-L)!}\, \frac{\theta^{(m-L)}}{\theta^{(m)}}.
\end{equation*}
In particular, for each $1\le j\le m$,
\begin{align}
    \E[C_j]&=\frac{\theta}{j}\, \frac{m!}{(m-j)!}\,
\frac{\theta^{(m-j)}}{\theta^{(m)}}; \label{eq:ECj-exact}\\ 
    \E[(C_j)_2]&=\left(\frac{\theta}{j}\right)^2\, \frac{m!}{(m-2j)!}\,
    \frac{\theta^{(m-2j)}}{\theta^{(m)}},\nonumber
\end{align}
with the convention that the second expression is $0$ if $2j>m$.
\end{lemma}
\begin{proof}
See for instance \cite{watterson1974sampling} and \cite[Equation (5.6)]{arratia2003logarithmic}.
\end{proof}


\subsection{Generating functions and Poissonization}

From now on, we concentrate on the study of the height $H_n$ of an Ewens fragmentation
tree $\mathcal{T}_n$ with parameter $\theta > 0$.

\begin{proposition}[Tail functions]\label{prop:mono}
For integers $n\ge 1$ and $h\ge 0$, we define
\[
q_n(h):=\Pp(H_n\le h),\qquad p_n(h):=1-q_n(h)=\Pp(H_n>h).
\]
Then:
\begin{itemize}
    \item $h\mapsto q_n(h)$ is non-decreasing and $h\mapsto p_n(h)$ is non-increasing.
    \item $n\mapsto q_n(h)$ is non-increasing and $n \mapsto p_n(h)$ is
        non-decreasing.
\end{itemize}
\end{proposition} 
\begin{proof}
   The only non-trivial part is the monotonicity with respect to $n$. One can
   adapt the consistency coupling of Ewens partitions given by the Chinese
   restaurant process to the Ewens fragmentation trees. We construct 
    a sequence $(\mathcal{T}_n,\mathcal{L}_n)_{n \geq
   0}$ of random recursive trees with:
   \begin{itemize}
    \item 
   $(\mathcal{T}_n, \mathcal{L}_n) \sim
   \Pp^{\bullet,(n,\theta)}$ for any $n \geq 0$, 
\item 
 if $n' \ge n$, then
$(\mathcal{T}_n,\mathcal{L}_n)$ is the subtree of
$(\mathcal{T}_{n'},\mathcal{L}_{n'})$ obtained by keeping the nodes with
$\mathcal{L}_{n'}$-labels
in $\{0,1,\ldots,n-1\}$.  
   \end{itemize}
Suppose that $(\mathcal{T}_n, \mathcal{L}_n)$ is already constructed. To add the
$(n+1)$-th vertex labelled by $n$ (thereby obtaining
$(\mathcal{T}_{n+1},\mathcal{L}_{n+1})$), we start at the root $\varnothing$ and go up
the tree. At each node $v$ with mass $K(v) = |(\mathcal{T}_n)_v|$:
\begin{enumerate}
    \item We add the $(n+1)$-th vertex as a leaf of $v$ with probability
        $\frac{\theta}{\theta + |(\mathcal{T}_n)_v| - 1}$;
    \item Otherwise, we choose $v'$ among the children of $v$; each child
        $v'$ has probability $\frac{|(\mathcal{T}_n)_{v'}|}{\theta + |(\mathcal{T}_n)_v| -
        1}$. We then pursue the construction with $v'$ instead of $v$.
\end{enumerate}
The algorithm ends almost surely, because if one reaches a leaf $v$ of
$\mathcal{T}_n$, then the probability of the first option is $1$, and 
$(n+1)$-th vertex is necessarily added as the leaf $v1$ of
$v$. By construction, at any step $n$ and for any node $v$ of $\mathcal{T}_n$,
the set partition formed by the labels appearing in the subtrees attached to $v$
has been obtained by the Chinese restaurant process with parameter $\theta$.
Therefore, it
has distribution $\mathrm{Ewens}^{\bullet}(S,\theta)$, where $S = \{k
\text{ label appearing in }(\mathcal{T}_n)_v \setminus \{v\} \}$. So,
$(\mathcal{T}_n,\mathcal{L}_n) \sim \Pp^{\bullet,(n,\theta)}$, and the
consistency of the recursive trees is immediate.
Because of this consistency, $H_n$ is stochastically non-decreasing in $n$, hence for fixed
$h$, $q_n(h)$ is non-increasing in $n$.
We will use this monotonicity repeatedly.
\end{proof}


Let the root of $\mathcal T_n$ have children masses $(A_i)_{1\le i\le \delta}$ (with $\sum_i A_i=n-1$ if $n\ge 2$). Then, for $n=1$, $H_1=0$. For $n\ge 2$,
\begin{equation}\label{eq:height-rec}
H_n = 2 + \max_{1\le i\le \delta} H_{A_i},
\end{equation}
where $(H_{A_i})$ are the heights of the child subtrees.
This relation leads to a recursion for $q_n(h)$.
\begin{proposition}[Recursion for $q_n(h)$]
For $n\ge 2$ and $h\ge 0$,
\begin{equation}\label{eq:q-product}
q_n(h)=\E\left[\prod_{i=1}^{\delta} q_{A_i}(h-1)\right],
\end{equation}
with the convention $q_k(-1)=0$ for all $k\ge 1$.
Equivalently, if $(C_1,\dots,C_{n-1})$ is the $\mathrm{Ewens}(n-1,\theta)$ count vector at the root, then
\begin{equation}
    \label{eq:q-count}
q_n(h)=\E\left[\prod_{j=1}^{n-1} q_j(h)^{C_j}\right].
\end{equation}
\end{proposition}

\begin{proof}
By relation~\eqref{eq:height-rec}, the event $\{H_n\le h\}$ equals the event that every child subtree has height at most $h-1$:
\[
    \{H_n\le h\}=\bigcap_{i=1}^{\delta} \{H_{A_i}\le h-1\}.
\]
By the Markov branching property (Proposition~\ref{prop:markov}), conditioned on the multiset $(A_i)$, the child subtrees are independent and
$\Pp(H_{A_i}\le h-1)=q_{A_i}(h-1)$. Therefore
\[
    \Pp(H_n\le h\mid (A_i))=\prod_{i=1}^{\delta} q_{A_i}(h-1).
\]
Taking expectation over $(A_i)$ gives \eqref{eq:q-product}, and Equation
\eqref{eq:q-count} follows by gathering the terms of the product according to
sizes. 
\end{proof}

We now define for each $h\ge 0$ and $z \in [0,1)$ the generating functions:
\begin{align*}
    F_h(z)&:=\sum_{m\ge 0}\frac{\theta^{(m)}}{m!}\,q_{m+1}(h)\,z^m;\\
\Phi_h(z)&:=\sum_{j\ge 1}\frac{p_j(h)}{j}\,z^j.
\end{align*}

\begin{proposition}[Poissonized recursion]
For each $h\ge 1$ and $z\in[0,1)$,
\begin{equation}\label{eq:F-rec}
F_h(z)=\exp\left(\theta\sum_{j\ge 1}\frac{q_j(h-1)}{j}z^j\right).
\end{equation}
Equivalently,
\begin{equation}\label{eq:key-identity}
(1-z)^\theta F_h(z)=\exp\left(\theta\,\Phi_{h-1}(z)\right).
\end{equation}
\end{proposition}

\begin{proof}
Fix $h\ge 1$. For $m\ge 0$, consider $q_{m+1}(h)$.
By the recursion \eqref{eq:q-count}, with $n=m+1$:
\[
q_{m+1}(h)=\E\left[\prod_{j=1}^{m} (q_j(h-1))^{C_j}\right],
\]
where $(C_1,\dots,C_m)\sim \mathrm{Ewens}(m,\theta)$.
Thus we have:
\begin{align*}
F_h(z)
&=
\sum_{m\ge 0}\frac{\theta^{(m)}}{m!}z^m\,
\E\left[\prod_{j=1}^m (q_j(h-1))^{C_j}\right]\\
&=
\sum_{\substack{m\ge 0 \\ c_1+2c_2+\cdots+mc_m=m}}z^m
\left(\frac{m!}{\theta^{(m)}}\prod_{j=1}^m\frac{\theta^{c_j}}{j^{c_j}c_j!}
\right)
\left(\frac{\theta^{(m)}}{m!}
\prod_{j=1}^m q_j(h-1)^{c_j}\right) \\
&=
\sum_{\substack{m\ge 0 \\ c_1+2c_2+\cdots+mc_m=m}}z^m
\prod_{j=1}^m \frac{\left(\theta\, q_j(h-1)\right)^{c_j}}{j^{c_j}c_j!}.
\end{align*}
Now sum over all $(c_j)_{j\ge 1}$ without the constraint by factorization; since $0 \le q_j(h-1) \le 1$ and $z \in [0,1)$, all the series involved are absolutely convergent. Hence we may exchange the order of summation and rewrite the constrained sum as an infinite product:
\[
\sum_{\substack{m\ge 0 \\ c_1+2c_2+\cdots+mc_m=m}}z^m
\prod_{j=1}^m \frac{\left(\theta\, q_j(h-1)\right)^{c_j}}{j^{c_j}c_j!}
=
\prod_{j\ge 1}\sum_{c\ge 0}\frac{1}{c!}\left(\frac{\theta\, q_j(h-1)}{j}z^j\right)^c
=
\prod_{j\ge 1}\exp\left(\frac{\theta\, q_j(h-1)}{j}z^j\right),
\]
which equals the exponential form \eqref{eq:F-rec}.
Finally, since
\[
\sum_{j\ge 1}\frac{z^j}{j}=-\log(1-z),
\qquad
\Phi_{h-1}(z)=\sum_{j\ge 1}\frac{1-q_j(h-1)}{j}z^j,
\]
we have
\[
\theta\sum_{j\ge 1}\frac{q_j(h-1)}{j}z^j
=
\theta\sum_{j\ge 1}\frac{z^j}{j}-\theta\,\Phi_{h-1}(z)
=
-\theta\log(1-z)-\theta\,\Phi_{h-1}(z),
\]
and substituting into \eqref{eq:F-rec} yields \eqref{eq:key-identity}. From this
identity we obtain, 
for all $h\ge 1$ and $z\in[0,1)$,
$
0< (1-z)^\theta F_h(z) = \exp(-\theta\,\Phi_{h-1}(z)) \le 1~.
$
\end{proof}



\subsection{De-Poissonization and threshold phenomenon for the height}

For $r\in(0,1)$ define a random variable $M_r$ by
\begin{equation}\label{eq:NB}
\Pp(M_r=m)=(1-r)^\theta\,\frac{\theta^{(m)}}{m!}\,r^m,\qquad m\ge 0.
\end{equation}
This is the negative binomial distribution with parameters $(\theta,r)$; its
generating function is
\[
    \E[s^{M_r}]=\left(\frac{1-r}{1-rs}\right)^\theta,\qquad |s|< \frac{1}{r},
\]
and in particular,
\begin{equation}\label{eq:meanvar}
\E[M_r]=\frac{\theta r}{1-r},\qquad \Var(M_r)=\frac{\theta r}{(1-r)^2}.
\end{equation}

\begin{lemma}[De-Poissonization identity]
For any $h\ge 0$ and any $r\in(0,1)$,
\begin{equation}\label{eq:depois}
(1-r)^\theta F_h(r)=\E\left[q_{M_r+1}(h)\right].
\end{equation}
\end{lemma}

\begin{proof}
By the definition of $F_h$,
\[
(1-r)^\theta F_h(r)
=
(1-r)^\theta\sum_{m\ge 0}\frac{\theta^{(m)}}{m!}q_{m+1}(h)r^m
=
\sum_{m\ge 0}\Pp(M_r=m)\,q_{m+1}(h)
=
\E[q_{M_r+1}(h)].
\qedhere \]
\end{proof}

Combining \eqref{eq:key-identity} and \eqref{eq:depois} yields the key bridge:
\begin{equation}\label{eq:bridge}
\E[q_{M_r+1}(h)]=\exp\left(-\theta \,\Phi_{h-1}(r)\right).
\end{equation}
We choose $r=r_n$ so that the mixing distribution $M_{r_n}$ is centered at $n-1$:
\begin{equation}\label{eq:rn}
r_n:=\frac{n-1}{n+\theta}\in(0,1).
\end{equation}
Then by \eqref{eq:meanvar},
$
\E[M_{r_n}]=n-1$ and $\Var(M_{r_n})=\frac{(n-1)(n-1+\theta)}{\theta}.$


\begin{lemma}[Scaling limit]
\label{lem:scaling-limit}
Let $r_n$ be as in \eqref{eq:rn} and $M_{r_n}$ as in \eqref{eq:NB}.
Let $\Gamma_\theta$ be a $\mathrm{Gamma}(\theta, 1)$ random variable. Then we have the convergence in distribution:
\begin{equation*}
\frac{M_{r_n}}{n-1}\ \xrightarrow[n\to\infty]{\text{law}}\ \frac{\Gamma_\theta}{\theta}.
\end{equation*}
\end{lemma}

\begin{proof}
    The Laplace transform of the random variable $\frac{\Gamma_\theta}{\theta}$ is:
    $$\E\left[\mathrm{e}^{z\frac{\Gamma_\theta}{\theta}}\right] =
    \int_{0}^\infty x^{\theta-1}\,
    \mathrm{e}^{-x+z\frac{x}{\theta}}\,\frac{dx}{\Gamma(\theta)} =
    \left(\frac{1}{1+\frac{z}{\theta}}\right)^{\theta}.$$
    It is convergent for any complex number $z$ with $|z|<\theta$. In
    particular, the law of $\frac{\Gamma_\theta}{\theta}$ is determined by its
    moments, and it suffices to prove that the Laplace transforms of
    $Y_n:=\frac{M_{r_n}}{n-1}$ converge towards the same function.
    Notice that 
    $$\left|\mathrm{e}^{\frac{z}{n-1}}\right|<\frac{1}{r_n}\quad\text{ if
    }\quad\mathrm{Re} \,z
    \leq (n-1)\,\log \!\left(1+\frac{\theta}{n-1}\right).$$
    Therefore, if $|z|<\theta$,
    then for $n$ large enough one can use the formula for the generating
    function of $M_{r_n}$, with $s=\mathrm e^{\frac{z}{n-1}}$. 
\begin{align*}
    \E\left[\mathrm{e}^{zY_n}\right] &= \left(
    \frac{1-r_n}{1-r_n\,\mathrm{e}^{\frac{z}{n-1}}}\right)^\theta =
    \left( \frac{\theta}{\theta +
    (n-1)(1-\mathrm{e}^{\frac{z}{n-1}})}\right)^\theta \to_{n \to \infty}
    \left(\frac{\theta}{\theta-z}\right)^{\theta}.\qedhere
 \end{align*}
%     Using the standard binomial series identity
% \[
% (1-x)^{-\theta}=\sum_{m=0}^\infty \frac{\theta^{(m)}}{m!}x^m,\qquad |x|<1,
% \]
% we compute for $|s|\le 1$:
% \begin{align*}
% G_r(s):=\mathbb E[s^{M_r}]
% &=\sum_{m=0}^\infty s^m (1-r)^\theta \frac{\theta^{(m)}}{m!}r^m \\
% &=(1-r)^\theta \sum_{m=0}^\infty \frac{\theta^{(m)}}{m!}(rs)^m \\
% &=(1-r)^\theta (1-rs)^{-\theta}
% =\left(\frac{1-r}{1-rs}\right)^\theta .
% \end{align*}
%
% For any $t\in\mathbb R$,
% \[
% \varphi_{Y_n}(t)
% =\mathbb E\!\left[\mathrm{e}^{itY_n}\right]
% =\mathbb E\!\left[\left(\mathrm{e}^{it/(n-1)}\right)^{M_{r_n}}\right]
% =G_{r_n}\!\left(\mathrm{e}^{it/(n-1)}\right)
% =\left(\frac{1-r_n}{1-r_n \mathrm{e}^{it/(n-1)}}\right)^\theta .
% \]
% Using $1-r_n=\frac{\theta}{n-1+\theta}$ and $r_n=\frac{n-1}{n-1+\theta}$, we rewrite
% \begin{align*}
% \frac{1-r_n}{1-r_n \mathrm{e}^{it/(n-1)}}
% &=\frac{\theta/(n-1+\theta)}{1-\frac{n-1}{n-1+\theta}\mathrm{e}^{it/(n-1)}} \\
% &=\frac{\theta}{(n-1+\theta)-(n-1)\mathrm{e}^{it/(n-1)}} \\
% &=\frac{\theta}{\theta+(n-1)\left(1-\mathrm{e}^{it/(n-1)}\right)} .
% \end{align*}
%
% Set $x_n:=t/(n-1)$. Then $x_n\to 0$ and we use the exact identity
% \[
% 1-\mathrm{e}^{ix}=-ix\int_0^1 \mathrm{e}^{iux}\,du,\qquad x\in\mathbb R,
% \]
% which implies
% \[
% (n-1)\left(1-\mathrm{e}^{it/(n-1)}\right)
% =-it\int_0^1 \mathrm{e}^{iu x_n}\,du.
% \]
% Since the integrand $\mathrm{e}^{iu x_n}\to 1$ pointwise and is uniformly bounded by $1$,
% the dominated convergence theorem yields
% \[
% \int_0^1 \mathrm{e}^{iu x_n}\,du \longrightarrow \int_0^1 1\,du = 1,
% \]
% hence
% \[
% (n-1)\left(1-\mathrm{e}^{it/(n-1)}\right)\longrightarrow -it.
% \]
% Therefore,
% \[
% \theta+(n-1)\left(1-\mathrm{e}^{it/(n-1)}\right)\longrightarrow \theta-it,
% \]
% and because $\theta-it\neq 0$ for all $t\in\mathbb R$, for all sufficiently large $n$ the denominator is nonzero and
% \[
% \frac{1-r_n}{1-r_n \mathrm{e}^{it/(n-1)}}
% =\frac{\theta}{\theta+(n-1)(1-\mathrm{e}^{it/(n-1)})}
% \longrightarrow \frac{\theta}{\theta-it}.
% \]
% By continuity of $z\mapsto z^\theta$ on $\mathbb C\setminus\{0\}$ along this sequence (and the fact the limit is nonzero),
% we obtain
% \[
% \varphi_{Y_n}(t)=\left(\frac{1-r_n}{1-r_n \mathrm{e}^{it/(n-1)}}\right)^\theta
% \longrightarrow \left(\frac{\theta}{\theta-it}\right)^\theta.
% \]
%
% Let $\Gamma_\theta\sim \mathrm{Gamma}(\theta,1)$, i.e. with density
% $f(x)=\frac{1}{\Gamma(\theta)}x^{\theta-1}\mathrm{e}^{-x}\ind_{x>0}$.
% Its moment generating function is $\mathbb E[\mathrm{e}^{u\Gamma_\theta}]=(1-u)^{-\theta}$ for $u<1$,
% hence for $t\in\mathbb R$,
% \[
% \mathbb E\!\left[\mathrm{e}^{it\,\Gamma_\theta/\theta}\right]
% =\mathbb E\!\left[\mathrm{e}^{(it/\theta)\Gamma_\theta}\right]
% =\left(1-\frac{it}{\theta}\right)^{-\theta}
% =\left(\frac{\theta}{\theta-it}\right)^\theta.
% \]
% Thus the pointwise limit of $\varphi_{Y_n}(t)$ is the characteristic function of $\Gamma_\theta/\theta$.
%
% Since $\varphi_{Y_n}(t)\to \left(\frac{\theta}{\theta-it}\right)^\theta$ for all $t\in\mathbb R$ and the limit is continuous at $t=0$,
% L\'evy's continuity theorem implies
% \[
% Y_n=\frac{M_{r_n}}{n-1}\ \Rightarrow\ \frac{\Gamma_\theta}{\theta}.
% \]
\end{proof}
\medskip
 
Since $\Gamma_\theta$ has full support on $(0,+\infty)$,
Lemma~\ref{lem:scaling-limit} immediately implies:
\begin{lemma}\label{lem:two-sided}
Let $r_n$ be as in Equation \eqref{eq:rn} and $M_{r_n}$ as in Equation \eqref{eq:NB}. Then there exist constants $p_-, p_+ > 0$ and an integer $n_0$ such that for all $n \ge n_0$,
\[
\mathbb{P}(M_{r_n} \le n-1) \ge p_-, 
\qquad 
\mathbb{P}(M_{r_n} \ge n-1) \ge p_+ .
\]
\end{lemma}

% \begin{proof}
%     By Lemma~\ref{lem:scaling-limit}, we have the convergence in distribution
% \[
% \frac{M_{r_n}}{n-1} \ \xrightarrow[n\to\infty]{\text{law}}\  \frac{\Gamma_\theta}{\theta},
% \]
% where $\Gamma_\theta \sim \mathrm{Gamma}(\theta,1)$. The limiting distribution is continuous and non-degenerate on $(0,\infty)$.
%
% In particular, since the Gamma distribution has full support on $(0,\infty)$, we have
% \[
% 0 < \mathbb{P}\left(\frac{\Gamma_\theta}{\theta} < 1\right) < 1.
% \]
% By the Portmanteau theorem, it follows that
% \[
% \liminf_{n \to \infty} \mathbb{P}\!\left(\frac{M_{r_n}}{n-1} < 1\right)
% \ge
% \mathbb{P}\left(\frac{\Gamma_\theta}{\theta} < 1\right)
% > 0.
% \]
% Hence there exists $p_- > 0$ and $n_0$ such that for all $n \ge n_0$,
% \[
% \mathbb{P}(M_{r_n} \le n-1) \ge p_-.
% \]
%
% Similarly,
% \[
% \liminf_{n \to \infty} \mathbb{P}\!\left(\frac{M_{r_n}}{n-1} > 1\right)
% \ge
% \mathbb{P}\left(\frac{\Gamma_\theta}{\theta} > 1\right)
% > 0,
% \]
% so there exists $p_+ > 0$ such that for all sufficiently large $n$,
% \[
% \mathbb{P}(M_{r_n} \ge n-1) \ge p_+.
% \]
%
% This concludes the proof.
% \end{proof}

We now show how $\mathbb E[q_{M_{r_n}+1}(h)]$ controls $q_n(h)$.
The key input is monotonicity: for each fixed $h$, the function $m \mapsto q_m(h)$ is nonincreasing
in $m$ (Proposition \ref{prop:mono}).

\begin{lemma}
\label{lem:mix-to-fixedn}
Fix $n\ge 2$ and $h\ge 0$, and let $M:=M_{r_n}$ with $r_n$ as in \eqref{eq:rn}.
Then, we have
\begin{align}
q_n(h)&\le \frac{\mathbb E[q_{M+1}(h)]}{\mathbb P(M\le n-1)};\label{eq:mix-upper}\\
q_n(h)&\ge \frac{\mathbb E[q_{M+1}(h)]-\mathbb P(M\le n-2)}{\mathbb P(M\ge n-1)}.\label{eq:mix-lower}
\end{align}
Consequently, for any sequence of integers $(h(n))_{n \geq 0}$, 
\begin{align}
\label{eq:mix-to-fixed-consequence}
\left(\mathbb E[q_{M_{r_n}+1}(h(n))]\to_{n \to \infty} 0\right) \ 
&\Longrightarrow\
\left(q_n(h(n))\to_{n \to \infty} 0\right),
\\
\left(\mathbb E[q_{M_{r_n}+1}(h(n))]\to_{n \to \infty} 1\right) \
&\Longrightarrow\ \left( q_n(h(n))\to_{n \to \infty}  1\right).\nonumber
\end{align}
\end{lemma}

\begin{proof}
\noindent\textbf{Upper bound.}
On the event $\{M\le n-1\}$ we have $M+1\le n$, hence by monotonicity
$q_{M+1}(h)\ge q_n(h)$. Therefore
\[
\mathbb E[q_{M+1}(h)]
\ge \mathbb E[q_{M+1}(h)\,\ind_{\{M\le n-1\}}]
\ge q_n(h)\,\mathbb P(M\le n-1),
\]
which gives \eqref{eq:mix-upper}.

\smallskip
\noindent\textbf{Lower bound.}
On the event $\{M\ge n-1\}$ we have $M+1\ge n$, hence $q_{M+1}(h)\le q_n(h)$.
Decompose the expectation:
\begin{align*}
\mathbb E[q_{M+1}(h)]
&=\mathbb E[q_{M+1}(h)\, \ind_{\{M\ge n-1\}}]+\mathbb E[q_{M+1}(h)\, \ind_{\{M\le n-2\}}] \\
&\le q_n(h)\,\mathbb P(M\ge n-1)+\mathbb P(M\le n-2),
\end{align*}
since $0\le q_{M+1}(h)\le 1$. Rearranging yields \eqref{eq:mix-lower}.

\smallskip
\noindent\textbf{$\mathbf{0/1}$ transfer.} Set $h=h(n)$.
If $\mathbb E[q_{M+1}(h)]\to 0$, then \eqref{eq:mix-upper} and Lemma~\ref{lem:two-sided}
give $$q_n(h)\le \frac{\mathbb E[q_{M+1}(h)]}{p_-}\to 0.$$
If $\mathbb E[q_{M+1}(h)]\to 1$, then since $\mathbb P(M\le n-2) = 1 - \mathbb P(M\ge n-1)$,
\eqref{eq:mix-lower} and Lemma~\ref{lem:two-sided} yield
\begin{align*}
q_n(h)&\ge \frac{\mathbb E[q_{M+1}(h)]-\mathbb P(M\le n-2)}{\mathbb P(M\ge n-1)} \\
&\ge \frac{\mathbb E[q_{M+1}(h)]-1+\mathbb P(M\ge n-1)}{\mathbb P(M\ge n-1)}
=1-\frac{1-\mathbb E[q_{M+1}(h)]}{\mathbb P(M\ge n-1)}\to 1.
\end{align*}
This proves \eqref{eq:mix-to-fixed-consequence}.
\end{proof}


We can now show that the asymptotic behavior of
\[
\Phi_{h-1}(r_n)=\sum_{j\ge1}\frac{p_j(h-1)}{j}\,(r_n)^j
\]
fully determines the $0/1$ law for $q_n(h)=\mathbb P(H_n\le h)$.

\begin{theorem}[Threshold phenomenon]
\label{thm:threshold}
Let $h=h(n)\ge0$ and $r_n=(n-1)/(n-1+\theta)$.
\begin{enumerate}
\item If $\Phi_{h(n)-1}(r_n)\to0$, then $q_n(h(n))\to1$.
\item If $\Phi_{h(n)-1}(r_n)\to\infty$, then $q_n(h(n))\to0$.
\end{enumerate}
\end{theorem}

\begin{proof}
This follows immediately from the last part of Lemma \ref{lem:mix-to-fixedn} and
from Equation \eqref{eq:bridge}.
% , which gives
% \begin{equation*}
% \mathbb E[q_{M_{r_n}+1}(h(n))]
% =\exp \left(-\theta \,\Phi_{h(n)-1}(r_n)\right).\qedhere
% \end{equation*}
\end{proof}








\section{Upper bound via \texorpdfstring{$s$}{s}-masses}\label{sec:3}

In this section we prove that the change of behaviour given by Theorem
\ref{thm:threshold} occurs around $h(n) \asymp \log n$. More precisely, we prove
that
\[
\limsup_{n\to\infty}\frac{H_n}{\log n}\le c_+(\theta)
\qquad\text{in probability},
\]
where the infimum in $c_+(\theta):=\inf_{s\ge2}(\frac{s}{-\log
\beta_s(\theta)})$
is taken only over integers $s$ (instead of real numbers larger than $1$).
% However, this result indicates the asymptotic
% behavior of $H_n$, which facilitates our further study.
We will prove a sharper upper bound by a different method in Section~\ref{sec:5}.


\subsection{The \texorpdfstring{$s$}{s}-mass functional}

We first recall a standard and very useful identity: for a random
$\mathrm{Ewens}(m,\theta)$ partition, the probability that $s$ uniformly 
sampled labels fall in the same block is explicit.

\begin{lemma}[Same-block probability under Ewens]\label{lem:same-block}
Let $\Pi_m$ be an $\mathrm{Ewens}(m,\theta)$ random partition of $\{1,\dots,m\}$. Pick $s\ge 2$ distinct labels $U_1,\dots,U_s$ uniformly without replacement from $\{1,\dots,m\}$, then
\begin{equation}\label{eq:same-block-prob}
\Pp\left(U_1,\dots,U_s \text{ are in the same block of }\Pi_m\right)
=
\frac{(s-1)!}{(\theta+1)^{(s-1)}}
=
\frac{\Gamma(s)\,\Gamma(\theta+1)}{\Gamma(\theta+s)}=: \beta_s(\theta),
\end{equation}
for all $m\ge s$.
\end{lemma}

\begin{proof}
We use the Chinese restaurant process (CRP) representation of Ewens partitions:
customers $1,2,\dots,m$ sit sequentially, and customer $t$ either starts a new
table with probability $\theta/(\theta+t-1)$, or joins an existing table proportional to its current size.
\smallskip

Fix the set of customers $\{U_1,\dots,U_s\}$: by exchangeability, we may assume without loss of generality that these are customers $1,2,\dots,s$. We compute the probability that they all sit at the same table in the CRP.
Customer $1$ starts a new table. For $t=2,\dots,s$, customer $t$ must join the table containing customer $1$. At time $t$, that table has size $t-1$, and the total mass is $\theta+t-1$. Hence
\[
\Pp(\text{customer }t \text{ joins table of }1 \mid \text{previous successes})
=\frac{t-1}{\theta+t-1}.
\]
Multiplying over $t=2,\dots,s$ yields
\[
\prod_{t=2}^s \frac{t-1}{\theta+t-1}
=
\frac{(s-1)!}{(\theta+1)(\theta+2)\cdots(\theta+s-1)}
=
\frac{(s-1)!}{(\theta+1)^{(s-1)}}~.
\]
This probability is independent of $m$ once $m\ge s$, proving \eqref{eq:same-block-prob}.
\end{proof}

\begin{lemma}[Expected falling-factorial $s$-sum of block sizes]\label{lem:EsumAs}
Let $(A_i)_{i=1}^d$ be the block sizes of an $\mathrm{Ewens}(m,\theta)$ partition (so $\sum_i A_i=m$). Then for any integer $s\ge 2$,
\begin{equation}\label{eq:EsumAs}
\E\left[\sum_{i=1}^d (A_i)_s\right]=(m)_s\,\beta_s(\theta).
\end{equation}
\end{lemma}

\begin{proof}
For each block $B$ of size $|B|$, the number of ordered $s$-tuples of distinct labels inside $B$ equals $(|B|)_s$. Summing over blocks gives $\sum_i (A_i)_s$ equals the number of ordered $s$-tuples of distinct labels that fall in the same block.
On the other hand, the total number of ordered distinct $s$-tuples in $\{1,\dots,m\}$ is $(m)_s$. By exchangeability,
\[
\E\left[\sum_i (A_i)_s\right]
=
(m)_s \cdot \Pp(U_1,\dots,U_s \text{ in same block}).
\]
Apply Lemma~\ref{lem:same-block} to obtain \eqref{eq:EsumAs}.


\end{proof}

Given $s \ge 2$ and $\ell \ge 0$, we define the level-$\ell$
$s$-mass of the Ewens fragmentation tree $\mathcal T_n$:
\[
V_\ell^{(s)} := \sum_{|u|=\ell} (K(u)-1)_s,
\]
where $K(u)$ is the mass at node $u$. This quantity is measurable with respect to
$\mathcal{F}_\ell$, $(\mathcal{F}_h)_{h \ge 0}$ being 
 the natural filtration
of the probability space $(\Omega, \mathcal{F}, \Pp)$ (see Equation
\eqref{eq:filtration}).
% According to Definition
% \ref{def:model}, $\Omega$ can be taken to be the set of all pairs
% $(\mathcal{T},K)$ with $\mathcal{T}
% \subset \mathcal{U}$ tree subset, and $\Pp = \Pp^{(n,\theta)}$.
% Then, $\mathcal F_\ell$ is the $\sigma$--algebra generated by the entire
% subtree of $\mathcal{T}$ consisting of the vertices up to generation $\ell$,
% plus the mass variables $K(u)$ with $|u|=\ell$; and $\mathcal F =
% \sigma(\bigcup_{\ell \geq 1} \mathcal F_\ell)$.
% The $\sigma$-algebra $\mathcal F_\ell$  contains all the information on the structure
% and masses of the tree up to generation $\ell$, but it does not contain any
% information on the random splittings producing generation $\ell+1$ from
% generation $\ell$.

\begin{lemma}[One-step factorial contraction]
For every $\ell\ge0$,
\begin{equation}\label{eq:V-cont}
\mathbb E\!\left[V_{\ell+1}^{(s)}\mid \mathcal F_\ell\right]
\le
\beta_s(\theta)\,V_\ell^{(s)}~.
\end{equation}
\end{lemma}

\begin{proof}
Fix $\ell\ge0$ and condition on $\mathcal F_\ell$. Let $u$ be a vertex at generation $\ell$ with $K(u)=k$.
If $k\le1$, then $u$ has no children and contributes zero to $V_{\ell+1}^{(s)}$.
Assume henceforth that $k\ge2$.
Conditionally on $\mathcal F_\ell$, the children of $u$ have masses
$(K(v_i))_{i\ge1}=(A_i)_{i\ge1}$, where $(A_i)$ is distributed as an
$\mathrm{Ewens}(k-1,\theta)$ partition.
Consequently,
\[
\sum_{v:\,\mathrm{parent}(v)=u}(K(v)-1)_s
=
\sum_i (A_i-1)_s
\le
\sum_i (A_i)_s~,
\]
since $(a-1)_s\le (a)_s$ for all integers $a\ge0$ (notice that $(a)_s=0$ for $a<s$).
Taking conditional expectations and using Lemma \ref{lem:EsumAs}, we obtain
\[
\mathbb E\!\left[
\sum_{v:\,\mathrm{parent}(v)=u}(K(v)-1)_s
\;\middle|\; \mathcal F_\ell
\right]
\le
\mathbb E\!\left[\sum_i (A_i)_s \,\middle|\; \mathcal F_\ell\right]
=
(k-1)_s\,\beta_s(\theta)~.
\]
Summing over all vertices $u$ at generation $\ell$ and using linearity of
conditional expectation yields
\[
\mathbb E\!\left[V_{\ell+1}^{(s)}\mid \mathcal F_\ell\right]
\le
\beta_s(\theta)\sum_{|u|=\ell}(K(u)-1)_s
=
\beta_s(\theta)\,V_\ell^{(s)}~,
\]
which completes the proof.
\end{proof}


% We now give a first-moment bound for the level-$\ell$ $s$-mass.

\begin{lemma} [First-moment bound]
For every $\ell\ge0$,
\begin{equation}\label{eq:first-moment-V}
\mathbb E[V_\ell^{(s)}]\le (n-1)_s\,(\beta_s(\theta))^\ell.
\end{equation}
\end{lemma}
\begin{proof}
Taking expectations in \eqref{eq:V-cont} and using the tower property
of conditional expectation, we obtain
$
\mathbb E[V_{\ell+1}^{(s)}]
 \le
\beta_s(\theta)\,\mathbb E[V_\ell^{(s)}]
$, and we conclude by using the initial condition $V_0^{(s)} = (n-1)_s$, 
since the root has mass $n$.
\end{proof}

\subsection{A first upper bound on the height}

A key observation is that along any ancestral line, the mass decreases by at
least one unit at each generation: if $v$ is a child of $u$, then
$K(v)\le K(u)-1$.
As a consequence, small--mass vertices cannot support long descendant chains.

\begin{lemma}[Deep vertices imply large mass earlier]\label{lem:deep-implies-large}
Fix an integer $s\ge2$. For every $h\ge s-1$,
\begin{equation}
\{H_n>h\}
\subseteq
\left\{\exists\,u:\ |u|=h-(s-1)\ \text{and}\ K(u)\ge s+1\right\}.
\end{equation}
\end{lemma}

\begin{proof}
Assume $H_n>h$, so there exists a vertex $v$ at generation $h + 1$.
Let $u$ be its ancestor at generation $h-(s-1)$.
Along the ancestor chain from $u$ to $v$, which has length $s$, the mass
decreases by at least one at each step. Hence
\[
K(v)\le K(u)-s.
\]
Since $K(v)\ge1$, it follows that $K(u)\ge s + 1$.
\end{proof}

For integers $k\ge s+1$, we have $(k-1)_s\ge s!$, hence
$\ind_{\{k\ge s+1\}}\le \frac{(k-1)_s}{s!}$.
Therefore, for any generation $\ell$,
\[
\ind_{\{\exists |u|=\ell:K(u)\ge s+1\}}
\le
\sum_{|u|=\ell}\ind_{\{K(u)\ge s+1\}}
\le
\frac{1}{s!}\sum_{|u|=\ell}(K(u)-1)_s
=
\frac{1}{s!}\, V^{(s)}_\ell.
\]
Taking expectations and using \eqref{eq:first-moment-V} yields
\[
\Pp\left(\exists |u|=\ell:K(u)\ge s+1\right)
\le
\frac{1}{s!}\,\E[V^{(s)}_\ell] \le \frac{(n-1)_s}{s!}\,(\beta_s(\theta))^\ell~.
\]
Combining Lemma~\ref{lem:deep-implies-large} with the previous estimates, we
obtain for all $h\ge s-1$,
\[
\Pp(H_n>h)
\le
\Pp\left(\exists |u|=h-(s-1):K(u)\ge s+1\right)
\le
\frac{(n-1)_s}{s!}\,(\beta_s(\theta))^{\,h-(s-1)}~.
\]
Absorbing the factor $(\beta_s(\theta))^{-(s-1)}$ into the constant and using
$(n-1)_s\le n^s$, we conclude that there exists $C_s<\infty$ such that
\[
\Pp(H_n>h)\le C_s\,n^s\,(\beta_s(\theta))^h,
\qquad h\ge s-1~.
\]
If $h=\lfloor (c+\varepsilon)\log n\rfloor$ and $ 
c>\frac{s}{-\log \beta_s(\theta)}$, 
then $n^s(\beta_s(\theta))^h\to 0$, and hence
$\Pp\!\left(H_n>(c+\varepsilon)\log n\right)\to 0$.
Optimizing over $s\ge2$ yields
\[
\limsup_{n\to\infty}\frac{H_n}{\log n}\le
c_+(\theta):=\inf_{\substack{s\ge2 \\ s \in \mathbb{N}}} \left(\frac{s}{-\log \beta_s(\theta)}\right)
\qquad\text{in probability}.
\]

\section{Macroscopic subtrees and amplification}\label{sec:4}

In this section, we prove that the root of the Ewens fragmentation tree produces
many macroscopic subtrees, and that a positive-probability depth event for a
single subtree can be amplified to a high-probability event using independence.
We will use these results in order to prove the lower bound in the next section.

\subsection{Many macroscopic subtrees}

Fix $\delta\in(0,1)$ and denote
\[
N_0 := \sum_{j=\lceil (n-1)^{1-\delta}\rceil}^{n-1} C_j,
\]
the number of children whose masses are at least $(n-1)^{1-\delta}$.

\begin{lemma}[Many macroscopic children]\label{lem:N0-diverges}
Let $\theta>0$ and $m:=n-1$. Fix any $\delta\in(0,1)$ and set
\[
J:=\left\{\left\lceil m^{1-\delta}\right\rceil,\dots,\left\lfloor
    m^{1-\delta/2}\right\rfloor\right\},
\qquad
\widetilde N_0:=\sum_{j\in J} C_j,
\]
where $C_j$ is the number of parts of size $j$ in an $\mathrm{Ewens}(m,\theta)$ partition.
Then $\widetilde N_0\to\infty$ in probability as $m\to\infty$. In particular,
$N_0\to\infty$ in probability.
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:Mixed}, for each $1\le j\le m$,
\[
\mathbb E[C_j]
= \frac{\theta}{j}\,R_{m,j}(\theta),
\qquad
R_{m,j}(\theta)
:=\frac{\Gamma(m+1)\,\Gamma(m-j+\theta)}{\Gamma(m-j+1)\,\Gamma(m+\theta)}.
\]

We shall prove that there exists a constant $c_0=c_0(\theta)>0$ and $m_0\in\mathbb N$ such that for all $m\ge m_0$ and all $j\in J$,
\begin{equation*}
R_{m,j}(\theta)\ge c_0~.
\end{equation*}
To this end, we use the following \emph{Wendel-type inequality}: there exist constants
$0<a_\theta\le b_\theta<\infty$, depending only on $\theta$, such that for all $x\ge 1$,
\begin{equation*}
a_\theta\, x^{1-\theta}
\le \frac{\Gamma(x+1)}{\Gamma(x+\theta)}
\le b_\theta\, x^{1-\theta}.
\end{equation*}
Applying with $x=m$ and $x=m-j$ yields
\[
\frac{\Gamma(m+1)}{\Gamma(m+\theta)}
\ge a_\theta\, m^{1-\theta},
\qquad
\frac{\Gamma(m-j+\theta)}{\Gamma(m-j+1)}
\ge \frac{1}{b_\theta}\,(m-j)^{\theta-1}.
\]
Therefore,
\begin{equation*}
R_{m,j}(\theta)
\ge \frac{a_\theta}{b_\theta}\left(\frac{m}{m-j}\right)^{1-\theta}.
\end{equation*}
As $j \in J$ is uniformly negligible compared to $m$,  
 we conclude that there exists $m_0$ such that for all $m\ge m_0$ and all $j\in J$,
\[
R_{m,j}(\theta)\ge \frac{a_\theta}{2b_\theta}=:c_0>0.
\]
Therefore, for all $m\ge m_0$ and all $j\in J$, $
\mathbb E[C_j]\ge \frac{c_0\,\theta}{j}$.  Summing over $j\in J$ yields
\begin{equation}\label{eq:EN0-tilde-lower}
\mathbb E[\widetilde N_0]
=\sum_{j\in J}\mathbb E[C_j]
\ge c_0\,\theta \sum_{j=\lceil m^{1-\delta}\rceil}^{\lfloor m^{1-\delta/2}\rfloor}\frac{1}{j}
= c_0\,\theta\left(\frac{\delta}{2}\log m+O(1)\right)
\xrightarrow[m\to\infty]{}\infty.
\end{equation}
We now control the variance. We write
\[
\mathrm{Var}(\widetilde N_0)
=\sum_{j\in J}\mathrm{Var}(C_j)
+ \sum_{\substack{j,k\in J\\ j\neq k}}\mathrm{Cov}(C_j,C_k).
\]
From Lemma~\ref{lem:Mixed}, 
\begin{align*}
\mathbb E[(C_j)_2]
&= \left(\frac{\theta}{j}\right)^2 R_{m,2j}(\theta) \quad\text{for }2j \le m;\\ 
\mathbb E[C_jC_k]
&= \frac{\theta^2}{jk}\, R_{m,j+k}(\theta)\quad\text{for }j\neq k,\,\,j+k \leq m.
\end{align*}
In particular,
\begin{equation}\label{eq:cov-formula}
\mathrm{Cov}(C_j,C_k)
= \frac{\theta^2}{jk}\left(R_{m,j+k}(\theta)-R_{m,j}(\theta)R_{m,k}(\theta)\right).
\end{equation}
Since $j\in J$ implies $j=o(m)$, the same Wendel-type bound as above shows that
$R_{m,j}(\theta)$ and $R_{m,2j}(\theta)$ are uniformly bounded over $j\in J$.
Therefore, for $j\in J$,
\begin{align*}
\mathrm{Var}(C_j)
&\le \mathbb E[C_j]+\mathbb E[(C_j)_2]
\end{align*}
and hence
\begin{equation}\label{eq:var-sum}
\sum_{j\in J}\mathrm{Var}(C_j)
=O\left(\sum_{j\in J}\frac1j\right)
=O(\log m).
\end{equation}
\medskip

It remains to bound the sum of covariances.
Define
\[
f(\ell):=\log R_{m,\ell}(\theta)
= \log\Gamma(m-\ell+\theta)-\log\Gamma(m-\ell+1)
+ \text{(constant in $\ell$)}.
\]
Differentiating twice yields
$
f''(\ell)=\psi'(m-\ell+\theta)-\psi'(m-\ell+1),
$ 
where $\psi'(x)$ denotes the trigamma function.
Using the classical bounds
\begin{equation*}
\frac{1}{x}\le \psi'(x)\le \frac{1}{x}+\frac{1}{x^2},\qquad x>0,
\end{equation*}
we obtain, for $x:=m-\ell\ge m/2$,
\[
\left|\psi'(x+\theta)-\psi'(x+1)\right|
\le \left|\frac{1}{x+\theta}-\frac{1}{x+1}\right| + O\!\left(\frac{1}{x^2}\right)
\le \frac{C_\theta}{x^2}.
\]
Since $j,k\in J$ implies $j+k=o(m)$, we have $m-\ell\ge m/2$ for all
$0\le \ell\le j+k$ and $m$ large enough, and thus
\begin{equation*}
\sup_{0\le \ell\le j+k}|f''(\ell)| \le \frac{C_\theta}{m^2}.
\end{equation*}
By a twofold integral form of Taylor's theorem,
\begin{align*}
f(j)+f(k)-f(j+k)
&= -\int_0^j\int_0^k f''(u+v)\,dv\,du;\\ 
    |f(j)+f(k)-f(j+k)|&\le \frac{C_\theta}{m^2}\,jk.
\end{align*}
Set $\varepsilon_{j,k}:=f(j)+f(k)-f(j+k)$; we have
$ R_{m,j}(\theta)R_{m,k}(\theta)
= R_{m,j+k}(\theta)\exp(\varepsilon_{j,k}). $
Since $j+k=o(m)$, the Wendel bound implies that $\sup_{j,k\in J}R_{m,j+k}(\theta)\le C_\theta$.
Moreover, for $m$ large we have $|\varepsilon_{j,k}|\le1$, and hence
\[
    |\mathrm{e}^{\varepsilon_{j,k}}-1|
    \le \mathrm{e}^{|\varepsilon_{j,k}|}\,|\varepsilon_{j,k}|
\le C\,\frac{jk}{m^2}.
\]
Therefore,
\[
\left|R_{m,j+k}(\theta)-R_{m,j}(\theta)R_{m,k}(\theta)\right|
\le C_\theta\,\frac{jk}{m^2}.
\]
Plugging this into \eqref{eq:cov-formula}, we obtain
\[
|\mathrm{Cov}(C_j,C_k)|
\le \frac{C_\theta}{m^2},
\qquad j\neq k,\ j,k\in J.
\]
Since $|J|=O(m^{1-\delta/2})$, it follows that
\begin{equation}\label{eq:cov-sum}
\sum_{\substack{j,k\in J\\ j\neq k}}
|\mathrm{Cov}(C_j,C_k)|
\le \frac{C_\theta}{m^2}\,|J|^2
=O(m^{-\delta})
=o(\log m).
\end{equation}
Combining \eqref{eq:var-sum} and \eqref{eq:cov-sum}, we obtain
$
\mathrm{Var}(\widetilde N_0)=O(\log m).
$
Together with \eqref{eq:EN0-tilde-lower}, this yields
\[
\frac{\mathrm{Var}(\widetilde N_0)}{\mathbb E[\widetilde N_0]^2}
=O\left(\frac{1}{\log m}\right)\xrightarrow[m\to\infty]{}0.
\]
By Chebyshev's inequality, for every $\varepsilon>0$,
$
\mathbb P(
|\widetilde N_0-\mathbb E[\widetilde N_0]|
\ge \varepsilon\, \mathbb E[\widetilde N_0]
)
\to 0.
$
Since $\mathbb E[\widetilde N_0]\to\infty$, we conclude that
$
\widetilde N_0 \xrightarrow{\mathbb P} \infty
$, and 
 as $N_0\ge \widetilde N_0$, this implies $
N_0 \xrightarrow{\mathbb P} \infty
$.
\end{proof}

\subsection{Amplification}

\begin{lemma}[Amplification via many macroscopic subtrees]\label{lem:amplification}
Fix $\theta>0$ and let $H_n$ denote the height of the Ewens tree $\mathcal T_n$.
Assume that there exist constants $p_0\in(0,1)$ and $m_0\ge 1$ such that
\begin{equation}\label{eq:uniform}
\inf_{m\ge m_0}\Pp\left(H_m\ge h(m)\right)\ \ge\ p_0,
\end{equation}
for some function $h:\mathbb N\to\mathbb N$.
Fix any $\delta\in(0,1)$ and set $m:=n-1$ and the macroscopic threshold
\[
t_n := \lceil m^{1-\delta}\rceil,
\qquad
h_{\min}(n):=\min(\{h(j):\ t_n\le j\le m\}).
\]
Then, for all $n$ large enough so that $t_n\ge m_0$,
\begin{equation}\label{eq:ampli-main}
\Pp\left(H_n \ge 1+h_{\min}(n)\right)
\ \ge\
1-\E\left[(1-p_0)^{N_0}\right].
\end{equation}
Moreover,
\begin{equation}\label{eq:goes-to-1}
\E[(1-p_0)^{N_0}]\xrightarrow[n\to\infty]{}0
\qquad\text{and therefore}\qquad
\Pp\left(H_n \ge 1+h_{\min}(n)\right)\xrightarrow[n\to\infty]{}1.
\end{equation}
\end{lemma}
\begin{proof}
Let $(A_i)_{1\le i\le d}$ be the vector of subtree sizes of the root, so that
$\sum_{i=1}^d A_i = m = n-1$. We define the index set of macroscopic children
\[
I:=\{\,i:\ A_i\ge t_n\,\};
\]
by definition, $|I|=N_0$.
Conditioned on $(A_i)$, the tree height satisfies the recursion
$H_n = 1+\max_{1\le i\le d} H_{A_i}$.
So, if there exists $i\in I$ such that $H_{A_i}\ge h(A_i)$, then we have
\[
H_n \ge 1 + H_{A_i} \ge 1 + h(A_i) \ge 1 + h_{\min}(n),
\]
since $A_i\in[t_n,m]$ for $i\in I$.
Therefore, conditioned on $(A_i)$,
\[
\{H_n < 1+h_{\min}(n)\}
\subseteq
\bigcap_{i\in I}\{\,H_{A_i} < h(A_i)\,\}.
\]
Taking conditional probabilities given $(A_i)$ and using conditional independence,
\begin{align*}
\Pp\left(H_n < 1+h_{\min}(n)\mid (A_i)\right)
\le
\prod_{i\in I}\Pp\left(H_{A_i}<h(A_i)\right).
\end{align*}
For $n$ large enough we have $t_n\ge m_0$, hence for every $i\in I$,
$A_i\ge t_n\ge m_0$, and by \eqref{eq:uniform}, all the terms of the right-hand
side of the equation above are smaller than $1-p_0$. Thus,
\[
\Pp\left(H_n < 1+h_{\min}(n)\mid (A_i)\right)\le (1-p_0)^{N_0}.
\]
Taking complements and averaging over $(A_i)$ yields \eqref{eq:ampli-main}:
\[
\Pp\left(H_n \ge 1+h_{\min}(n)\right)
=
1-\E\left[\Pp\left(H_n < 1+h_{\min}(n)\mid (A_i)\right)\right]
\ge
1-\E[(1-p_0)^{N_0}].
\]
Finally, the convergences in Equation \eqref{eq:goes-to-1} follow from the
convergence in probability of $N_0$ to infinity (Lemma
\ref{lem:N0-diverges}). 
\end{proof}


\section{Branching random walk structure and height asymptotics}\label{sec:5}

In this section, we prove the sharp logarithmic asymptotics for the height by
recasting the Ewens fragmentation
process as a \emph{branching random walk} (BRW) with logarithmic mass decrements.

\begin{theorem}[Convergence of the scaled height]\label{thm:height-Ewens}
Let $H_n$ be the height of an Ewens fragmentation
tree $\mathcal{T}_n$ with parameter $\theta > 0$ in Definition \ref{def:model}, then there exists a constant $c_\star(\theta)>0$ such that
\[
\frac{H_n}{\log n}
\xrightarrow[n\to\infty]{\mathbb{P}} c_\star(\theta)~,
\]
where $c_\star(\theta) = \inf_{t>1}(\frac{t}{-\log\beta_t(\theta)})$ is a constant
depending only on $\theta$, and $\beta_t(\theta) = \frac{\Gamma(t)\,\Gamma(\theta + 1)}{\Gamma(\theta+t)}$.
\end{theorem}

\subsection{Logarithmic displacements}

Consider the Ewens fragmentation tree $ \mathcal T_n$ in Definition \ref{def:model}. Let $u_0=\varnothing,u_1,\dots,u_h$ be a root-to-leaf path, and write $K(u_\ell)$ for the mass at depth $\ell$. If $K(u_{\ell-1})=k\ge2$, then the children masses form an $\mathrm{Ewens}(k-1,\theta)$
partition of $k-1$, so the selected child on the path has some mass
$A_{u_\ell}=K(u_\ell)\in\{1,\dots,k-1\}$. Therefore, deterministically for the realized tree,
\begin{equation*}
\frac{K(u_\ell)}{K(u_{\ell-1})-1}=\frac{A_{u_\ell}}{K(u_{\ell-1})-1}\in(0,1].
\end{equation*}
We define the stepwise log-loss along the path by
\[
X_{u_\ell} := -\log\left(\frac{K(u_\ell)}{K(u_{\ell-1})-1}\right)\ge0,\qquad
S_h(u):=\sum_{\ell=1}^h X_{u_\ell}.
\]
Exponentiating and multiplying over $\ell=1,\dots,h$ yields the exact identity
\begin{equation*}
\mathrm{e}^{-S_h(u)}=\prod_{\ell=1}^h \frac{K(u_\ell)}{K(u_{\ell-1})-1}.
\end{equation*}
Let us convert this equation into a statement about $K(u_h)$ with an explicit remainder.
For each $\ell\ge0$,
\[
% K(u_\ell)-1 = K(u_\ell)\left(1-\frac1{K(u_\ell)}\right),
% \qquad\text{hence}\qquad
\frac1{K(u_\ell)-1}=\frac1{K(u_\ell)}\left(1-\frac1{K(u_\ell)}\right)^{-1}.
\]
Multiplying this identity over $\ell=0,\dots,h-1$ and using telescoping,
\begin{align*}
    \mathrm{e}^{-S_h(u)} = 
\prod_{\ell=1}^h \frac{K(u_\ell)}{K(u_{\ell-1})-1}
&=
\prod_{\ell=1}^h \frac{K(u_\ell)}{K(u_{\ell-1})}
\left(\prod_{\ell=0}^{h-1}\left(1-\frac1{K(u_\ell)}\right)^{-1}\right) \\
&=
\frac{K(u_h)}{n}\prod_{\ell=0}^{h-1}\left(1-\frac1{K(u_\ell)}\right)^{-1}.
\end{align*}
% or equivalently,
% \begin{equation*}
%     K(u_h)=n \,\mathrm{e}^{-S_h(u)}\prod_{\ell=0}^{h-1}\left(1-\frac1{K(u_\ell)}\right).
% \end{equation*}
Taking logarithms yields the exact decomposition
\begin{equation}
\label{eq:exact-decomposition}
\log K(u_h) = \log n - S_h(u) - R_h(u),
\end{equation}
where the remainder term is
\begin{equation*}
R_h(u) := -\sum_{\ell=0}^{h-1}\log\left(1-\frac1{K(u_\ell)}\right) \ge 0.
\end{equation*}

\begin{lemma}[Control of the remainder]\label{lem:remainder-control}
Fix $C>0$ and let $h\le C\log n$. For any $\alpha\in(0,1)$ and any vertex $u$ with $|u|=h$, on the event
\begin{equation*}
\mathcal G_{n,\alpha}(u):=\left\{\min\{K(u_\ell):0\le \ell\le h-1\}\ge
n^\alpha\right\},
\end{equation*}
we have the deterministic bound
\begin{equation}\label{eq:remainder-control}
R_h(u)\le \frac{2h}{n^\alpha}\le \frac{2C\log n}{n^\alpha}=o(\log n).
\end{equation}
Consequently, on $\mathcal G_{n,\alpha}(u)$, $
\log K(u)=\log n - S_h(u) + o(\log n)$.
Moreover, the estimate \eqref{eq:remainder-control} holds uniformly over any collection of vertices
$\mathcal U_h\subseteq\{u:|u|=h\}$ on the intersection event $\bigcap_{u\in\mathcal U_h}\mathcal G_{n,\alpha}(u)$.
\end{lemma}

\begin{proof}
    For $x\in[0,\frac{1}{2}]$,  we have the convexity inequality $-\log(1-x) \leq
    2\log(2)\,x \leq 2x$.
On $\mathcal G_{n,\alpha}(u)$, we have $K(u_\ell)\ge n^\alpha$ for all $0\le
\ell\le h-1$, and therefore $\frac{1}{K(u_\ell)} \in [0,\frac{1}{2}]$ for $n$
large. Therefore,  
\[
0\le R_h(u)
\le 2\sum_{\ell=0}^{h-1}\frac1{K(u_\ell)}
\le \frac{2h}{n^\alpha}
\le \frac{2C\log n}{n^\alpha}.
\]
This is \eqref{eq:remainder-control}, and 
% The final approximation
% $\log K(u)=\log n-S_h(u)+o(\log n)$ on $\mathcal G_{n,\alpha}(u)$ then follows immediately from the exact decomposition
% \eqref{eq:exact-decomposition}.
the uniformity over a set $\mathcal U_h$ follows by taking suprema on the intersection event
$\bigcap_{u\in\mathcal U_h}\mathcal G_{n,\alpha}(u)$.
\end{proof}
\medskip

We then define the BRW increments $X$ and introduce the one-step cumulants $\beta_k(t)$ and $\kappa_k(t)$ together with their limiting exponent $\kappa(t)$.
Let $(P_i)_{i\ge1}\sim \mathrm{PD}(\theta)$ be a Poisson--Dirichlet sequence with parameter
$\theta>0$ (see \cite[Section 5.7]{arratia2003logarithmic}); $(P_i)_{i \ge 1}$ is a random
point process on $[0,1]$. We define: 
\begin{itemize}
    \item the logarithmic displacements:
\[
X_i := -\log P_i\in(0,\infty),\qquad L := \sum_{i\ge1}\delta_{X_i},
\]
\item for $t>1$, 
the contraction coefficient and its logarithm:
$$\beta_t(\theta) := \E\left[\sum_{i\ge1}(P_i)^t\right]
= \E\left[\sum_{i\ge1} \mathrm{e}^{tX_i}\right],\qquad
\kappa(t) := \log \beta_t(\theta)~.$$
\end{itemize}

\begin{lemma}[Explicit formula for $\beta_t(\theta)$]
For any real number $t>1$,
\begin{equation*}
\beta_t(\theta) = \frac{\Gamma(t)\,\Gamma(\theta+1)}{\Gamma(\theta+t)}.
\end{equation*}
\end{lemma}

\begin{proof}
We use the $\mathrm{GEM}(\theta)$ stick-breaking representation. Let $(V_k)_{k\ge1}$ be i.i.d.
with $V_k\sim \mathrm{Beta}(1,\theta)$ and set
\[
\widetilde P_1 := V_1,\qquad \widetilde P_k := V_k\prod_{i<k}(1-V_i)\quad (k\ge2).
\]
Then the decreasing rearrangement of $(\widetilde P_k)_{k \ge 1}$ is $\mathrm{PD}(\theta)$, and for $t>1$
the sum $\sum_{i \geq 1} (P_i)^t$ is invariant under rearrangement, hence
\[
\beta_t(\theta)=\E\left[\sum_{k\ge1}(\widetilde P_k)^t\right].
\]
Let $S:=\sum_{k\ge1}(\widetilde P_k)^t$. Splitting off the first term and factoring $(1-V_1)^t$,
\[
S = (V_1)^t + \sum_{k\ge2}\left(V_k\prod_{i<k}(1-V_i)\right)^t
= (V_1)^t + (1-V_1)^t S',
\]
where $S'\overset{d}=S$ and $S'$ is independent of $V_1$.
Taking expectations gives the renewal identity
\[
\beta_t(\theta)=\E[(V_1)^t]+\E[(1-V_1)^t]\,\beta_t(\theta),
\]
so $\beta_t(\theta)=\E[V_1^t]/(1-\E[(1-V_1)^t])$.
The result follows now from:
\begin{align*}
    \E[(V_1)^t]&=\theta\int_0^1 v^t(1-v)^{\theta-1}dv=\theta B(t+1,\theta)
=\frac{\Gamma(t+1)\,\Gamma(\theta+1)}{\Gamma(t+\theta+1)} ; \\ 
    \E[(1-V_1)^t]&=\theta\int_0^1
    (1-v)^{t+\theta-1}dv=\frac{\theta}{t+\theta} .\qedhere
\end{align*}
% Substituting,
% \[
% \beta_t(\theta)
% =\frac{\Gamma(t+1)\Gamma(\theta+1)/\Gamma(t+\theta+1)}{1-\theta/(t+\theta)}
% =\frac{\Gamma(t+1)\Gamma(\theta+1)}{\Gamma(t+\theta+1)}\cdot \frac{t+\theta}{t}
% =\frac{\Gamma(t)\Gamma(\theta+1)}{\Gamma(t+\theta)}.
% \]
\end{proof}
\medskip

% In the Ewens tree, a one-step splitting from a parent mass $k$ yields a \emph{$k$-dependent} one-generation ``log-Laplace'' quantity. The height asymptotics depend only on the \emph{asymptotic} regime $k\to\infty$. The next lemma
% makes this precise and justifies writing a $k$-independent $\kappa(t)$ in the BRW embedding.
% Pierre-Loïc: I do not understand this sentence, it is a bit gibberish... 


\begin{lemma}[Poisson--Dirichlet approximation of the one-step exponents]\label{lem:kappa-rate}
Fix $t>1$. For an integer $k\ge2$, let $(A^{(u)}_i)_{1\le i\le d(u)}$ be the multiset of block sizes in the
$\mathrm{Ewens}(k-1,\theta)$ partition at a node $u$ with $K(u)=k$. We define the 
% finite-mass
one-step exponent:
\begin{equation*}
\kappa_k(t):=\log\,
\E\!\left[\sum_{i=1}^{d(u)}\left(\frac{A^{(u)}_i}{k-1}\right)^t\ \Big|\ K(u)=k\right].
\end{equation*}
Then as $k\to\infty$,
\begin{equation}
\kappa_k(t)\longrightarrow \kappa(t)=\log\beta_t(\theta).
\end{equation}
More precisely, there exists a constant $C=C(t,\theta)<\infty$,
$\gamma=\gamma(\theta)\in(0,1/2]$, and $m_0\ge 2$ such that for all $m\ge m_0$,
\[
\sup_{k\ge m}\,|\kappa_k(t)-\kappa(t)| \le C\,m^{-\gamma}.
\]
\end{lemma}


\begin{proof}
Let $m:=k-1$ and let $(C_1,\dots,C_m)$ be the $\mathrm{Ewens}(m,\theta)$ count vector at a node with $K(u)=k$,
so that $\#\{i:A^{(u)}_i=j\}=C_j$ and $\sum_i (A^{(u)}_i)^t=\sum_{j=1}^m j^t\, C_j$.
Then,
\begin{align*}
\E\left[\sum_{i=1}^{d(u)}\left(\frac{A^{(u)}_i}{m}\right)^t\ \Big|\ K(u)=k\right]
&= m^{-t} \sum_{j=1}^m j^t\,\E[C_j] \\ 
&= 
\theta\,m^{-t}\sum_{j=1}^m j^{t-1}\,
\frac{\Gamma(m+1)\, \Gamma(m-j+\theta)}{\Gamma(m-j+1)\, \Gamma(m+\theta)},
\end{align*}
using the exact formula~\eqref{eq:ECj-exact}.
Set $x_j:=\frac{j}{m} \in(0,1]$ and $ 
R_m(x_j):=\frac{\Gamma(m+1)\,\Gamma(m-j+\theta)}{\Gamma(m-j+1)\,\Gamma(m+\theta)}$.
Then the equation above becomes
\begin{equation*}
    \beta_{m,t}(\theta)=\E\left[\sum_{i=1}^{d(u)}\left(\frac{A^{(u)}_i}{m}\right)^t\ \Big|\ K(u)=k\right]
=
\theta\sum_{j=1}^m \frac1m\,(x_j)^{t-1}\,
R_m(x_j).
\end{equation*}
For each fixed $x\in(0,1)$ and integers $j=j(m)$ such that $\frac{j}{m} \to x$, the standard Gamma-ratio asymptotic gives
\begin{equation*}
R_m(x_j)\longrightarrow (1-x)^{\theta-1}\qquad (m\to\infty).
\end{equation*}
Therefore, we can expect that the Riemann sum above converges towards:
$$
\theta\int_0^1 x^{t-1}(1-x)^{\theta-1}\,dx
=\frac{\Gamma(t)\,\Gamma(\theta+1)}{\Gamma(t+\theta)}
=\beta_t(\theta),$$ 
where we used the Beta--Gamma identity and the identity $\theta\,\Gamma(\theta)=\Gamma(\theta+1)$.
Let us give a precise estimate of the rate of convergence. We set 
\begin{align*}
    g(x)&:=\theta\,x^{t-1}(1-x)^{\theta-1}\in L^1(0,1),\\ 
    g_m(x_j)&:=\theta\,(x_j)^{t-1}\,R_m(x_j).
\end{align*}
Then, the conditional expectation is $\beta_{m,t}(\theta)=\frac{1}{m}\sum_{j=1}^m g_m(x_j)$. 
\medskip

\noindent\textbf{Step 1: splitting the sum into a bulk part and an endpoint tail.}
With $L:=\lfloor m^{1/2}\rfloor$, we split
\[
    \beta_{m,t}(\theta)  =\sum_{j=1}^{m-L} \frac1m\,
g_m(x_j)\;+\;\sum_{j=m-L+1}^{m}\frac1m \,g_m(x_j)
=:S_{\rm bulk}+S_{\rm tail}.
\]
By Wendel type inequalities for Gamma ratios,
there exists a constant $C<\infty$ such that for all integers $m\ge2$ and $1\le j\le m$,
\[
    0\le g_m(x_j)\le C \left(1-x_j+\frac{1}{m}\right)^{\theta-1}\le
    C \left(\frac{r+1}{m} \right)^{\theta-1}
\]
with $r = m-j$. 
Hence
\[
S_{\rm tail}\le \sum_{r=0}^{L-1}\frac1m\,C\left(\frac{r+1}{m}\right)^{\theta-1}
= C\,m^{-\theta}\sum_{r=1}^{L} r^{\theta-1}
\le C\,m^{-\theta}\, L^{\theta}
\le C\,m^{-\frac{\theta}{2}}.
\]
Similarly, the tail of the limiting integral satisfies
\[
    \int_{1-\frac{L}{m}}^1 g(x)\,dx \le C\int_0^{L/m} y^{\theta-1}\,dy \le
    C\left(\frac{L}{m}\right)^\theta \le C\,m^{-\frac{\theta}{2}}.
\]
Therefore the endpoint contribution to $|\beta_{m,t}(\theta)-\beta_t(\theta)|$ is
$O(m^{-\frac{\theta}{2}})$.

\medskip\noindent
\textbf{Step 2: replacing the function $g_m$ by $g$ in the bulk.}
For the bulk indices $1\le j\le m-L$, we have $r=m-j\ge L\asymp m^{1/2}$.
We rewrite
\begin{align*}
    R_m(x_j)&=\frac{\Gamma(m+1)}{\Gamma(m+\theta)}\,
    \frac{\Gamma(r+\theta)}{\Gamma(r+1)}  
            = m^{1-\theta}\left(1+O\!\left(\frac1m\right)\right)
 r^{\theta-1}\left(1+O\!\left(\frac1r\right)\right)\\ 
            &= 
(1-x_j)^{\theta-1}\left(1+O\!\left(\frac1m+\frac1r\right)\right)
=(1-x_j)^{\theta-1}\left(1+O\!\left(m^{-\frac{1}{2}}\right)\right),
\end{align*}
by using the Stirling estimates; the $O(\cdot)$ is uniform 
 for $1\le j\le m-L$.
Thus, $
|g_m(x_j)-g(x_j)|\le C\,m^{-\frac{1}{2}}\,g(x_j),
$
and therefore
\[
\left| S_{\rm bulk}-\sum_{j=1}^{m-L}\frac1m\, g(x_j)\right|
\le C\,m^{-\frac{1}{2}}\sum_{j=1}^{m-L}\frac1m\, g(x_j)
\asymp C\,m^{-\frac{1}{2}}\int_0^1 g(x)\,dx
= O\!\left(m^{-\frac{1}{2}}\right).
\]

\medskip\noindent
\textbf{Step 3: Riemann sum error for the bulk.}
On the interval $[0,1-\frac{L}{m}]$, the function $g(x)$ is $C^1$ and its derivative satisfies
\begin{align*}
g'(x) &=
\theta\left((t-1)\,x^{t-2}(1-x)^{\theta-1}
-(\theta-1)\,x^{t-1}(1-x)^{\theta-2}\right).
\end{align*}
By the Euler-Maclaurin formula,
\begin{align*}
% \frac{1}{m} \sum_{j=1}^{m-L} g(x_j) - \int_0^{1-\frac{L}{m}} g(x)\,dx
%  &= \frac{g(1-\frac{L}{m})}{2m} + \frac{1}{m} \int_{0}^{1-\frac{L}{m}}
% g'(x)\left(mx-\lfloor mx \rfloor -\frac{1}{2}\right) dx ; \\ 
\left|\frac{1}{m} \sum_{j=1}^{m-L} g(x_j) - \int_0^{1-\frac{L}{m}} g(x)\,dx
    \right| &\leq 
    \frac{1}{2m}\int_0^{1-\frac{L}{m}} |g'(x)|\,dx \\ 
            &\leq \frac{\theta}{2m} \int_0^{1-\frac{L}{m}}
            \left((t-1)\, x^{t-2}\,(1-x)^{\theta-1} +
            |\theta-1|\,x^{t-1}\,(1-x)^{\theta-2}\right)dx \\ 
            &\leq \frac{1}{2m}\, 
            \frac{\Gamma(t)\,\Gamma(\theta+1)}{\Gamma(\theta+t-1)} +
            \frac{\theta\,|\theta-1|}{2m}\,\max\left(1,\left(
                \frac{L}{m}\right)^{\theta-2}\right).
 \end{align*}
 If $\theta \geq 2$, then we get a $O(m^{-1})$, and if $\theta<2$, then we
 obtain a 
 $$O\!\left(\frac{1}{m} \,m^{\frac{2-\theta}{2}}\right) =
 O\!\left(m^{-\frac{\theta+1}{2}}\right).$$
 Combining all the estimates, we conclude that $|\beta_{m,t}(\theta)-\beta_t(\theta)| =
 O(m^{-\gamma})$ with 
 $\gamma = \min(\frac{1}{2},\frac{\theta}{2})>0 .$
 Finally, $\beta_t(\theta)>0$, so for all large $m$ we have $\beta_{m,t}(\theta) \ge 
 \frac{\beta_t(\theta)}{2}$.
Using $$|\log a-\log b|\le \frac{|a-b|}{\min(a,b)}$$ for $a,b>0$ yields
\[
|\kappa_k(t)-\kappa(t)|
=|\log \beta_{m,t}(\theta)-\log \beta_t(\theta)|
\le \frac{2}{\beta_t(\theta)}\,|\beta_{m,t}(\theta)-\beta_t(\theta)|
\le C\,m^{-\gamma}.\qedhere
\]
\end{proof}

We now give a lemma that will be needed in the proof of lower bound.
\begin{lemma}[Polynomial slack implies large masses]
\label{lem:poly-slack-large-masses}
Fix constants \(C>0\), \(\rho\in(0,1)\), and let $0<\alpha<\rho$. Let \(h=h(n)\) satisfy $h\le C\log n$
for all large \(n\). Let \(b_n\) be a deterministic sequence such that
\[
b_n\le (1-\rho)\log n
\]
for all large \(n\).
Then, for all sufficiently large \(n\), 
\[
    (S_h(u)\le b_n)\Rightarrow
\mathcal G_{n,\alpha}(u).
\]
\end{lemma}
\begin{proof}
Suppose, for contradiction, that for infinitely many
\(n\) there exists a vertex \(u\) with \(|u|=h\), \(S_h(u)\le b_n\), but
\[
\min_{0\le j\le h}K(u_j)<n^\alpha .
\]
Let
\[
    \tau:=\min(\{0\le j\le h:K(u_j)<n^\alpha\})
\]
be the first time at which the mass drops below \(n^\alpha\). Since
\(K(u_0)=n\) and \(\alpha<1\), we have \(\tau\ge1\) for all large \(n\).
By the definition of \(\tau\),
\[
K(u_j)\ge n^\alpha,\qquad 0\le j\le \tau-1.
\]
We apply the exact decomposition along the prefix
\(u_0,u_1,\ldots,u_\tau\):
\[
\log K(u_\tau)
=
\log n-S_\tau(u)-R_\tau(u),
\]
where
\[
R_\tau(u)
=
-\sum_{j=0}^{\tau-1}
\log\left(1-\frac1{K(u_j)}\right).
\]
For \(n\) large, \(K(u_j)\ge n^\alpha\ge2\) for all \(j<\tau\). Hence, using
\[
-\log(1-x)\le 2x,\qquad 0\le x\le \frac12,
\]
we get
\[
0\le R_\tau(u)
\le
2\sum_{j=0}^{\tau-1}\frac1{K(u_j)}
\le
2\tau n^{-\alpha}
\le
2C(\log n)n^{-\alpha}
=o(1).
\]
Moreover, all increments in \(S\) are nonnegative, so
$S_\tau(u)\le S_h(u)\le b_n .$ 
Therefore
\[
\log K(u_\tau)
=
\log n-S_\tau(u)-R_\tau(u)
\ge
\log n-b_n-o(1)
\ge
\rho\log n-o(1)
>\alpha\log n
\]
for $n$ large enough. Equivalently,
$K(u_\tau)>n^\alpha$, which 
 contradicts the definition of \(\tau\). Hence no such first bad time
exists, and therefore
$\min_{0\le j\le h}K(u_j)\ge n^\alpha$ 
for all large \(n\). The event \(\mathcal G_{n,\alpha}(u)\) follows, as
it only requires the same lower bound for \( j\le h-1\).
\end{proof}


\subsection{Upper bound on the height}

We define the \emph{speed} and \emph{height} constant of the branching random walk:
\begin{align*}
    v_\star(\theta)& :=\sup_{t>1}\left(\frac{-\kappa(t)}{t}\right)
=\sup_{t>1}\left(\frac{-\log\beta_t(\theta)}{t}\right); \\
    c_\star(\theta)&:=\frac1{v_\star(\theta)}
=\inf_{t>1}\left(\frac{t}{-\log\beta_t(\theta)}\right).
\end{align*}
% We now prove the upper bound
% \[
% H_n\le \left(c_\star(\theta)+o(1)\right)\log n
% \qquad\text{in probability.}
% \]
In the sequel $\theta$ is fixed and we abbreviate $v_\star = v_\star(\theta)$
and $c_\star = c_\star(\theta)$. Fix $\varepsilon>0$ and set
$h:=\lfloor (c_\star + \varepsilon)\log n\rfloor$.
If the tree survives to depth $h$, then there exists a vertex $u$ with $|u|=h$ and $K(u)\ge1$.
Because of the exact decomposition \eqref{eq:exact-decomposition},
\[
\log K(u)=\log n - S_h(u)-R_h(u)\ge 0
\quad\Longrightarrow\quad
S_h(u)\le \log n - R_h(u)\le \log n.
\]
Hence, deterministically,
$\{H_n>h\}\subseteq \{\exists\,|u|=h:\ S_h(u)\le \log n\}$.
Fix $t>1$. We have:
\[
\ind_{\{S_h(u)\le \log n\}}
\le \exp\left(t(\log n-S_h(u))\right)
= \mathrm{e}^{t\log n}\,\mathrm{e}^{-tS_h(u)}.
\]
Summing over $|u|=h$ and taking expectation yields
\begin{align}
\Pp(H_n>h)
&\le \E\left[\sum_{|u|=h}\ind_{\{S_h(u)\le \log n\}}\right] \le
\mathrm{e}^{t\log n}\,\,\E\!\left[\sum_{|u|=h} \mathrm{e}^{-tS_h(u)}\right].
\label{eq:upper-markov}
\end{align}
The right-hand side is related to the Biggins martingale associated to a
branching random walk (see \cite{Big77,Big92,Big95}). 
\begin{lemma}\label{lem:supermartingale}
Fix $t>0$, and set
\[
Z_h(t)
:=
\sum_{|u|=h}
\exp\!\left(
-tS_h(u)-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right),
\]
where $u_0=\varnothing,u_1,\dots,u_h=u$ is the ancestral line of $u$ and $\kappa_k(t)$ can be defined by
\[
\kappa_k(t)
:=
\log\, \mathbb{E}\!\left[
\sum_{v:\,\mathrm{child}(u)=v}
\exp\!\left(-tX_{(u\to v)}\right)
\;\middle|\;
K(u)=k
\right].
\]
Then $(Z_h(t))_{h\ge 0}$ is a non-negative supermartingale with respect to the
filtration $(\mathcal{F}_h)_{h\ge 0}$. In particular, $\E[Z_h(t)]\le 1$ for all
$h\ge 0$.
\end{lemma}

\begin{proof}
% Let $\mathcal{F}_h$ be the $\sigma$-algebra generated by the tree up to depth $h$.
Fix $h\ge 0$. Using the decomposition $S(v)=S(u)+X_{(u\to v)}$ for a child $v$ of $u$,
we can write
\[
Z_{h+1}(t)
=
\sum_{\substack{|u|=h\\K(u)\ge 2}}\;
\sum_{v:\,\mathrm{child}(u)=v}
\exp\!\left(
-tS_h(u)-tX_{(u\to v)}-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)-\kappa_{K(u)}(t)
\right).
\]
Grouping terms by their parent $u$ gives
\[
Z_{h+1}(t)
=
\sum_{\substack{|u|=h\\ K(u) \ge 2}}
\exp\!\left(
-tS_h(u)-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right)
\left(
\exp(-\kappa_{K(u)}(t))
\sum_{v:\,\mathrm{child}(u)=v} \mathrm{e}^{-tX_{(u\to v)}}\right).
\]
For each $u$ with height $h$ and mass at least $2$, the first part of the term of the sum
corresponding to $u$ is $\mathcal{F}_h$-measurable, whereas the second part
satisfies
\[
\mathbb{E}\!\left[
\exp(-\kappa_{K(u)}(t))
\sum_{v:\,\mathrm{child}(u)=v} \mathrm{e}^{-tX_{(u\to v)}}
\;\middle|\;
\mathcal{F}_h
\right]
=
\exp(-\kappa_{K(u)}(t))\,\exp(\kappa_{K(u)}(t))=1.
\]
Therefore,
\[
\mathbb{E}[Z_{h+1}(t)\mid \mathcal{F}_h]
=
\sum_{\substack{|u|=h \\ K(u) \ge 2}}
\exp\!\left(
-tS_h(u)-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right)
\le
Z_h(t),
\]
so $(Z_h(t))_{h\ge 0}$ is a supermartingale. Taking expectations yields
$\mathbb{E}[Z_h(t)] \le \mathbb{E}[Z_0(t)]=1$.
\end{proof}
\medskip

% We now derive a uniform first-moment bound which is unconditional.

\begin{lemma}
Fix $t > 1$ and let $h = h(n) \xrightarrow[n\to\infty]{}\infty$. For every vertex $u$ with $|u|=h$,
\[
\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\le
h\kappa(t)+o(h)
\]
with a $o(\cdot)$ which is uniform with respect to $u$.
\end{lemma}

\begin{proof}
Fix a threshold $k_0=k_0(n)\to\infty$ and such that $k_0(n) = o(h)$.
By Lemma~\ref{lem:kappa-rate}, we have
\[
\eta_n:=\sup_{k\ge k_0(n)}\left|\kappa_k(t)-\kappa(t)\right| \xrightarrow[n\to\infty]{}0.
\]
Moreover, for all $k\ge 2$ and $t>1$,
\[
\kappa_k(t)=\log \E\left[\sum_i\left(\frac{A_i}{k-1}\right)^t\right]\le 0,
\]
since $\sum_i (\frac{A_i}{k-1})^t\le \sum_i (\frac{A_i}{k-1}) = 1$.
Since along any ancestral line the masses decrease by at least one at each step, we have
\[
\#\{\ell\in\{0,\ldots,h-1\}:K(u_\ell)<k_0\}\le k_0,
\]
and hence
\[
\#\{\ell\in\{0,\ldots,h-1\}:K(u_\ell)\ge k_0\}\ge h-k_0.
\]
Therefore,
\[
\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\le
\sum_{\ell:\, K(u_\ell)\ge k_0}\left(\kappa(t)+\eta_n\right)
+
\sum_{\ell:\, K(u_\ell)<k_0} 0
\le  (h-k_0)\left(\kappa(t)+\eta_n\right)
= h\kappa(t)+o(h).\qedhere
\]
\end{proof}
\medskip
 
Consequently,
\[
Z_h(t)
=
\sum_{|u|=h}
\exp\!\left(
-tS_h(u)-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right)
\ge 
\sum_{|u| = h}\mathrm{e}^{-t S_h(u)} \exp(-(h\kappa(t) + o(h))),
\]
and since $\mathbb{E}[Z_h(t)] \le 1$,
\begin{equation}\label{eq:first-moment-depth-h}
    \E\!\left[\sum_{|u|=h}\mathrm{e}^{-tS_h(u)}\right]
\le
\exp(h\kappa(t)+o(h)).
\end{equation}
Combining Equations \eqref{eq:upper-markov} and \eqref{eq:first-moment-depth-h}, we obtain
\begin{align*}
\Pp(H_n>h)\le \exp(t\log n+h\kappa(t)+o(h)) =
\exp((t+(c_\star + \varepsilon)\kappa(t) + o(1)) \log n).
\end{align*}
By definition of $c_\star $, we can choose $t>1$ such that
\[
\frac{t}{-\kappa(t)} < c_\star + \varepsilon.
\]
Thus, we have $t+(c_\star + \varepsilon)\kappa(t) < -c_1$ for some $c_1>0$, and
\[
\Pp(H_n>h)\le \exp\left(-(c_1+o(1))\log n\right) \to 0.
\]
This proves that $H_n\le (c_\star + \varepsilon)\log n$ with very high
probability, for any fixed $\eps>0$. 




\subsection{Lower bound via a second-moment argument and amplification}

We now prove the logarithmic lower bound on the height $H_n$, by considering at depth
$h=\lfloor (c_\star-\varepsilon)\log n\rfloor$ a set 
$\mathcal G_h^{\mathrm{good}}$ of ``good'' vertices whose masses are still
macroscopic (hence not leaves). The strategy is:
\begin{itemize}
    \item 
to show by a second-moment argument that this set is nonempty with a \emph{uniformly positive
probability}, 
\item 
    to upgrade this to a \emph{high probability} event
by using the amplification Lemma~\ref{lem:amplification}.
\end{itemize}
\medskip

Fix $\varepsilon_2\in(0,1)$ and choose $\varepsilon_1\in(0,1)$ such that
\begin{equation}\label{eq:eps-coupling}
  (v_{\star}+\varepsilon_1)\,(c_{\star}-\varepsilon_2) \le 1-\delta_\varepsilon
\end{equation}
for some
$\delta_\varepsilon=\delta_\varepsilon(\varepsilon_1,\varepsilon_2)\in(0,1)$;
this is possible since $v_\star c_\star = 1$.
We set 
$
h:=\lfloor (c_\star-\varepsilon_2)\log n \rfloor .
$
For a vertex $u$ at depth $h$ and $\alpha \in (0,1)$, we 
recall the definition of the pathwise large-mass event along $u$:
\[
\mathcal G_{n,\alpha}(u):=\left\{\min_{0\le \ell\le h-1}K(u_\ell)\ge
n^\alpha\right\}.
\]
Let $\omega_n\to\infty$ with $\omega_n=o(h^{1/3})$. 
\begin{definition}[Good vertices]
    The set of \emph{good vertices} at depth $h$ is:
$$\mathcal G_h^{\mathrm{good}}
:=
\left\{
u:\ |u|=h,\ \mathcal G_{n,\alpha}(u),\ S_h(u)\le (v_\star+\varepsilon_1)h-\omega_n
\right\}.$$
\end{definition}

\begin{lemma}
If $\mathcal G_h^{\mathrm{good}}\neq\varnothing$, then $H_n\ge h+1$ for all sufficiently large $n$.
\end{lemma}
\begin{proof}
Let $u\in \mathcal{G}^{\mathrm{good}}_h$. By definition,
$ S_h(u)\le (v_{\star}+\varepsilon_1)h-\omega_n.$ 
Since $h=(c_{\star}-\varepsilon_2)\log n+O(1)$ and Equation \eqref{eq:eps-coupling} holds, we have
\[
(v_{\star}+\varepsilon_1)h \le (1-\delta_\varepsilon)\log n + O(1),
\]
hence
\[
\log K(u) + R_h(u) = \log n - S_h(u) \ge \delta_\varepsilon \log n + \omega_n - O(1).
\]
By Lemma \ref{lem:remainder-control}, for good vertices, $R_h(u) = o(\log n)$,
so 
\[
\log K(u) \ge \delta_\varepsilon \log n + \omega_n - O(1) - o(\log n)\xrightarrow[n\to\infty]{}\infty.
\]
Thus, $K(u)\ge 2$ if $n$ is large enough. Hence $u$ has at least one child, and thus $H_n\ge h+1$.
\end{proof}


Thus it suffices to show that
 $$ 
\Pp\left(\mathcal G_h^{\mathrm{good}}\neq\varnothing\right)\xrightarrow[n\to\infty]{}1 .
$$
We will first prove a positive-probability version, and then amplify it. 
The positive-probability version relies on the following logarithmic-depth deep-path
proposition, to be proven in the next subsection. In the sequel, several
propositions and lemmas will rely on the following list of assumptions:
\begin{enumerate}[label=(A\arabic*)]
    \item \label{hyp_A1} We fix $a>v_\star$ and we assume that there
        exists $t>1$ such that $a=-\kappa'(t)$.
    \item \label{hyp_A2}
  We also fix
$\rho>0$ and we assume that 
$$    h=h(n)\asymp\log n,\qquad
ah\ge (1-\rho)\log n.$$ 
\item \label{hyp_A3} We finally fix a sequence $(\omega_n)_{n \in \N}$ such that 
$$\omega_n \to +\infty,\qquad \omega_n = o(h(n)^{1/3}).$$
 \end{enumerate}
\begin{proposition}[Deep paths at logarithmic depth]
\label{prop:deep_paths_log_depth}
Under the assumptions \ref{hyp_A1}, \ref{hyp_A2} and \ref{hyp_A3}, for every sufficiently small \(\alpha\in(0,\rho)\), there exists
\(p_0=p_0(a,\rho,\alpha)>0\) such that
\[
\liminf_{n\to\infty}
\mathbb P\left(
\exists u:\ |u|=h,\ \mathcal G_{n,\alpha}(u),\ S_h(u)\le ah-\omega_n
\right)
\ge p_0 .
\]
\end{proposition}
\begin{remark}
Since $a > v_\star = \sup_{t > 1} (-\frac{\kappa(t)}{t})$, we have
    $\kappa(t) + ta > 0$ 
for $t > 1$. We will frequently use this inequality.
\end{remark}
\medskip

We first prove that for $a$ sufficiently close to $v_\star$, Hypothesis
\ref{hyp_A1} is satisfied: one can choose $t>1$ such that $a=-\kappa'(t)$.
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{kappa.pdf}
\caption{Graph of $-\frac{\kappa(t)}{t}$ and $-\kappa'(t)$ for $\theta = 2$;
$t_\star \approx 2.9207$ and $v_\star \approx 0.5974$.}
\end{figure}

\begin{lemma}\label{lem:a-near-vstar}
Recall that
$
\kappa(t)=\log \Gamma(t)+\log \Gamma(\theta+1)-\log \Gamma(\theta+t)$ and $
v_\star=\sup_{t>1}(-\frac{\kappa(t)}{t})$.
There exists $\varepsilon_0>0$ such that for every
\[
a\in (v_\star,\,v_\star+\varepsilon_0),
\]
there exists a unique $t\in(1,\infty)$ satisfying
$a=-\kappa'(t)$.
\end{lemma}

\begin{proof}
Set
\[
g(t):=-\kappa'(t)=\psi(\theta+t)-\psi(t),\qquad t>1,
\]
where $\psi=\Gamma'/\Gamma$ is the digamma function.
We first note that
\[
g'(t)=-\kappa''(t)=\psi'(\theta+t)-\psi'(t)<0,\qquad t>1,
\]
because the trigamma function $\psi'$ is strictly decreasing on $(0,\infty)$.
Hence $g$ is continuous and strictly decreasing on $(1,\infty)$.
Next, let $t_\star>1$ be a maximizer of the function $t \mapsto
-\frac{\kappa(t)}{t}$.  
Since this function is differentiable, the first-order optimality condition gives
\[
0=\frac{d}{dt}\left(\frac{-\kappa(t)}{t}\right)\Big|_{t=t_\star}
=\frac{-t_\star\,\kappa'(t_\star)+\kappa(t_\star)}{(t_\star)^2}.
\]
Therefore,
\[
g(t_\star)=-\kappa'(t_\star)=-\frac{\kappa(t_\star)}{t_\star}=v_\star.
\]
Since $g$ is continuous and strictly decreasing, this proves the uniqueness of the
maximizer $t_\star$, and we have
\begin{align*}
    g(t)<g(t_\star) &=v_\star \qquad \text{for } t>t_\star,\\
    g(t)>g(t_\star) &=v_\star \qquad \text{for } 1<t<t_\star.
\end{align*}
The restriction of $g$ to $(1,t_\star)$ is a continuous decreasing bijection
from this interval to $(v_\star,g(1))$, whence the result with $v_\star +
\epsilon_0=g(1)$.
\end{proof}



Fix $\varepsilon > 0$, and choose in \eqref{eq:eps-coupling} $\varepsilon_2 < \varepsilon$. Apply Proposition~\ref{prop:deep_paths_log_depth} with
\begin{align*}
    a&:=v_\star+\varepsilon_1; \\ 
    \rho&:=\delta_\varepsilon/2; \\
    h&=h(n) = \lfloor (c_\star - \varepsilon_2)\,\log n\rfloor,
\end{align*}
where we refine the definition of $\varepsilon_1$ such that $\varepsilon_1 < \varepsilon_0$ in Lemma~\ref{lem:a-near-vstar}. 
Indeed, Equation \eqref{eq:eps-coupling} implies
\[
ah\le (1-\rho)\log n,
\]
for all sufficiently large \(n\). The proposition gives the positive-probability lower bound
\[\liminf_{n\to\infty}\mathbb P(H_n\ge h+1)\ge 
\liminf_{n\to\infty}\mathbb P(\mathcal G_h^{\mathrm{good}}\neq\varnothing)\ge p_0>0.
\]
Thus, there exists $p_0 > 0$ and $n_0$ such that:
$$    \inf_{n \ge n_0} \Pp\left(H_n\ge h(n)+1\right)\ge p_0.$$
We now upgrade this lower bound to a high-probability statement using
Lemma~\ref{lem:amplification}.
Applying Lemma~\ref{lem:amplification} with this choice of $h(\cdot)$ yields,
for any fixed $\delta\in(0,1)$,
\[
\Pp\left(H_n\ge 1+\min\{ h(j):\, \lceil (n-1)^{1-\delta}\rceil \le j\le n-1\}\right)\to 1.
\]
Since $\min\{ h(j): j\in[\lceil (n-1)^{1-\delta}\rceil,n-1]\}
=
 h(\lceil (n-1)^{1-\delta}\rceil)
=
(1-\delta)(c_\star-\varepsilon_2)\log n+O(1)$,
we obtain
\[
\Pp\left(H_n\ge (c_\star-\varepsilon_2)(1-\delta)\log n\right)\to 1.
\]
Finally, since $\delta\in(0,1)$ is arbitrary, for $\varepsilon_2\in(0,\varepsilon)$ we can choose
$\delta>0$ small enough so that $(c_\star-\varepsilon_2)(1-\delta)\ge c_\star-\varepsilon$,
and therefore
$\Pp\left(H_n\ge (c_\star-\varepsilon)\log n\right)\to 1$.
% and since $\varepsilon>0$ is arbitrary, this proves
% $H_n\ge (c_\star(\theta)-o(1))\log n$ with high probability.

\subsection{Deep paths at logarithmic depth}

In order to complete the proof of Theorem \ref{thm:height-Ewens}, we need to
prove Proposition \ref{prop:deep_paths_log_depth}. It relies on the following
technical lemma: 

\begin{lemma}[Critical barrier second moment]
\label{lem:critical_barrier_second_moment}
Under the assumptions \ref{hyp_A1}, \ref{hyp_A2} and \ref{hyp_A3}, we choose
$0<\alpha<\rho$, and we 
define the barrier event
\[
\mathcal B_h(u)
:=
\left\{\mathcal G_{n,\alpha}(u),\
ah-\omega_n-1\le S_h(u)\le ah-\omega_n, \text{ and }
S_j(u) \leq aj \text{ for all }j\leq h
\right\},
\]
and the truncated count
\[
\widetilde N_h(a)
:=
\sum_{|u|=h}\ind_{\mathcal B_h(u)}.
\]
Then, for $\alpha>0$ small enough, there exist constants $c,C>0$ such that for all large $n$,
\begin{align*}
\mathbb E[\widetilde N_h(a)]
&\ge
c\,\mathrm{e}^{h(\kappa(t)+ta)-t\omega_n}(1+\omega_n)\,h^{-\frac{3}{2}};\\
\mathbb E[(\widetilde N_h(a))^2]
&\le
C\,\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n}(1+\omega_n)^2\,h^{-3}.
\end{align*}
\end{lemma}


Assuming Lemma~\ref{lem:critical_barrier_second_moment}, Paley--Zygmund yields
\[
\mathbb P(\widetilde N_h(a)>0)
\ge
\frac{\mathbb E[\widetilde N_h(a)]^2}{\mathbb E[(\widetilde N_h(a))^2]}
\ge
\frac{c}{C} =:p_0(a, \rho, \alpha)>0.
\]
Since $\widetilde N_h(a)>0$ implies
\[
\exists u:\ |u|=h,\ \mathcal G_{n,\alpha}(u),\ S_h(u)\le ah-\omega_n,
\]
we conclude that
\[
\liminf_{n\to\infty}
\mathbb P\left(
\exists u:\ |u|=h,\ \mathcal G_{n,\alpha}(u),\ S_h(u)\le ah-\omega_n
\right)\ge p_0(a,\rho,\alpha).
\]
This proves Proposition \ref{prop:deep_paths_log_depth} modulo
Lemma~\ref{lem:critical_barrier_second_moment}. The remainder of this subsection
is devoted to a sketch of proof of this lemma; the technical details and
computations appear in Appendix \ref{sec:appendix}.


\subsubsection{Cemetery-extended trees}
The process $(Z_h(t))_{h\ge 0}$ defined in Lemma \ref{lem:supermartingale} on the original Ewens fragmentation tree is in general only a nonnegative \emph{supermartingale}, not a true martingale. The defect comes from vertices of mass $1$: such vertices contribute to $Z_h(t)$ at level $h$, but have no children at level $h+1$, so a positive amount of mass disappears.
To restore a branching random walk martingale, we enlarge the tree by adding a cemetery continuation after each leaf.
\medskip

\begin{definition}[Cemetery extension]
\label{def:cemetery}
Given $(\mathcal T,K) \in \Omega$,  for every vertex $u$ with $K(u)=1$, we attach a unique child $u^\dagger=(u1)$ and declare recursively that
\[
    \delta(u) = 1\,\, (\text{instead of }0),\qquad K(u^\dagger)=1,
\qquad
X(u\to u^\dagger)=0.
\]
Every cemetery vertex again has a unique cemetery child with the same properties. In this way, every leaf is prolonged into an infinite ray of mass $1$ vertices with zero displacement.
We write $\widetilde{\mathcal{T}}_n$ for the extended tree constructed from
$\mathcal{T}_n \sim \Pp^{(n, \theta)}$. For convenience, we also set
\[
\kappa_1(t):=0.
\]
By construction, $\widetilde{\mathcal{T}}_n$ belongs to the space $\widetilde\Omega$ of
cemetery-extended trees defined
in Subsection \ref{subsec:spaces}.
\end{definition}

The cemetery-extension map $\mathrm{Ext}:\Omega\to\widetilde\Omega$
is deterministic, hence the original law $\Pp^{(n,\theta)}$ induces a probability measure
\[
\widetilde{\Pp}^{(n,\theta)}
:=
\Pp^{(n,\theta)}\circ \mathrm{Ext}^{-1}
\qquad\text{on }(\widetilde\Omega,\widetilde{\mathcal F}).
\]
In the sequel, when no confusion is possible, we still denote this measure simply by $\Pp$.
If $u$ is a vertex of $\widetilde{\mathcal{T}}_n$ and $u_0=\varnothing,u_1,\dots,u_h=u$ is its ancestral line, define
\[
\widetilde Z_h(u;t)
:=
\exp\!\left(
-tS_h(u)-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right),
\qquad
\widetilde Z_h(t)
:=
\sum_{|u|=h}^{\mathrm{ext}}\widetilde Z_h(u;t),
\]
where the sum runs over all vertices of generation $h$ in the cemetery-extended
tree. Lemma \ref{lem:supermartingale} is replaced by:

\begin{lemma}[Additive martingale on the cemetery-extended tree]
For every $t\ge1$, the process $(\widetilde Z_h(t))_{h\ge 0}$ is a nonnegative
martingale with respect to the natural filtration $(\widetilde{\mathcal
F}_h)_{h\ge 0}$ on the probability space
$(\widetilde \Omega,\widetilde{\mathcal{F}},\widetilde{\Pp}^{(n,\theta)})$. In particular,
\[
\mathbb E[\widetilde Z_h(t)]=1
\qquad\text{for all }h\ge 0.
\]
\end{lemma}

\begin{proof}
Fix $h\ge 0$. For each vertex $u$ at depth $h$, write
\[
\widetilde Z_h(u;t)
=
\exp\!\left(
-tS_h(u)-\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right).
\]
Then
\[
\widetilde Z_{h+1}(t)
=
\sum_{|u|=h}^{\mathrm{ext}}
\widetilde Z_h(u;t)
\,
\mathrm{e}^{-\kappa_{K(u)}(t)}
\sum_{v:\, \mathrm{child}(u)=v}^{\mathrm{ext}}
\mathrm{e}^{-tX(u\to v)}.
\]
\begin{itemize}
    \item 
If $K(u)=k\ge 2$, then by definition of $\kappa_k(t)$,
\[
\mathbb E\!\left[
\sum_{v:\, \mathrm{child}(u)=v}^{\mathrm{ext}} \mathrm{e}^{-tX(u\to v)}
\,\Big|\, \widetilde{\mathcal F}_h
\right]
=
\mathrm{e}^{\kappa_k(t)}.
\]
\item
If $K(u)=1$, then in the cemetery extension $u$ has exactly one child $u^\dagger$ with
\[
X(u\to u^\dagger)=0,
\qquad
\kappa_1(t)=0,
\]
hence
\[
\mathrm{e}^{-\kappa_1(t)}
\sum_{v:\,\mathrm{child}(u)=v}^{\mathrm{ext}} \mathrm{e}^{-tX(u\to v)}
=
1.
\]
\end{itemize}
Therefore, for every depth-$h$ vertex $u$,
\[
\mathbb E\!\left[
\mathrm{e}^{-\kappa_{K(u)}(t)}
\sum_{v:\,\mathrm{child}(u)=v}^{\mathrm{ext}} \mathrm{e}^{-tX(u\to v)}
\,\Big|\, \widetilde{\mathcal F}_h
\right]
=1.
\]
Summing over $|u|=h$ yields
$\mathbb E[\widetilde Z_{h+1}(t)\mid \widetilde{\mathcal F}_h]
=
\widetilde Z_h(t).$
Thus $(\widetilde Z_h(t))_{h\ge 0}$ is a martingale. Since $\widetilde Z_0(t)=1$, we get
$\mathbb E[\widetilde Z_h(t)]=1$ for all $h \ge 0$.

\end{proof}
\begin{remark}\label{rem:trivial_martingale}
Suppose that $t=1$. For every non-cemetery vertex of mass
$k\ge2$,
\[
\sum_{v:\,\mathrm{child\ of}\ u} \mathrm{e}^{-X(u\to v)}
=
\sum_i \frac{A_i}{k-1}
=1,
\]
while for a cemetery continuation we also have exactly one child with weight
$\mathrm{e}^{-0}=1$. It follows
that
\[
\widetilde Z_h(1)=1
\qquad\text{for every }h\ge0
\]
almost surely on the extended tree.
 \end{remark}

\begin{remark}
\label{rem:ghost_paths_good_event}
The cemetery extension does not change the set of good vertices relevant for the lower bound. Indeed, along every cemetery ray all masses are equal to $1$, whereas our good event requires
\[
\min_{0\le \ell\le h-1}K(u_\ell)\ge n^\alpha.
\]
For $n$ large enough, $n^\alpha>1$, hence no cemetery vertex can satisfy the good event. Therefore, whenever the indicator of $\mathcal G_{n,\alpha}(u)$ is present, sums over the extended tree coincide with sums over genuine vertices of the original fragmentation tree.
\end{remark}

\subsubsection{Spinal change of measure}\label{subsub:spinal_change}
We now use the martingale $(\widetilde{Z}_h(t))_{h \ge 0}$ to perform a
\emph{spinal change of measure} on the space
$(\widetilde{\Omega},\widetilde{\mathcal F})$. 
This is a standard
construction in branching random walk theory (see for instance \cite[Section
4.4]{Shi15}), but which requires to add a distinguished
ancestral line (or \emph{spine}) to the cemetery-extended tree; see Figure \ref{fig:spine-cemetery-up}.
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[
    x=1cm,y=1cm,
    normal/.style={circle,draw=black,thin,minimum size=7mm,inner sep=0pt},
    spine node/.style={circle,draw=red!80!black,very thick,minimum size=7.5mm,inner sep=0pt},
    cemetery/.style={circle,draw=gray!70,thin,dashed,minimum size=7mm,inner sep=0pt,text=gray!70},
    edge/.style={draw=black,thin},
    spine edge/.style={draw=red!80!black,very thick},
    cemetery edge/.style={draw=gray!70,thin,dashed},
    lab/.style={draw=none,fill=none,font=\small}
]

% root at bottom
\node[spine node] (u0) at (0,0) {$\varnothing$};

% generation 1
\node[normal]     (a1) at (-2.3,1.8) {};
\node[spine node] (u1) at (0.7,1.8) {$U_1$};
\node[normal]     (b1) at (2.8,1.8) {};

% generation 2
\node[normal]     (a21) at (-3.4,3.6) {};
\node[normal]     (a22) at (-1.5,3.6) {};
\node[spine node] (u2)  at (-0.2,3.6) {$U_2$};
\node[normal]     (b21) at (1.9,3.6) {};
\node[normal]     (b22) at (3.8,3.6) {};

% generation 3
\node[normal]     (c31) at (-4.0,5.4) {};
\node[normal]     (c32) at (-2.0,5.4) {};
\node[spine node] (u3)  at (0.9,5.4) {$U_3$};
\node[normal]     (c34) at (2.4,5.4) {};

% generation 4
\node[normal]     (d41) at (-2.2, 7.2) {};
\node[normal]     (d42) at (-1.2,7.2) {};
\node[spine node] (u4)  at (0.1,7.2) {$U_4$};
\node[normal]     (d44) at (2.0,7.2) {};


% ordinary edges
\draw[edge] (u0)--(a1);
\draw[spine edge] (u0)--(u1);
\draw[edge] (u0)--(b1);

\draw[edge] (a1)--(a21);

\draw[edge] (u1)--(a22);
\draw[spine edge] (u1)--(u2);

\draw[edge] (b1)--(b21);
\draw[edge] (b1)--(b22);

\draw[edge] (a21)--(c31);
\draw[edge] (a22)--(c32);
\draw[spine edge] (u2)--(u3);
\draw[edge] (b21)--(c34);

\draw[edge] (c32)--(d41);
\draw[edge] (u3)--(d42);
\draw[spine edge] (u3)--(u4);
\draw[edge] (u3)--(d44);

% cemetery children
\node[cemetery] (g1) at (-4.0,7.2) {$\dagger$};
\node[cemetery] (g2) at (3.0, 7.2) {$\dagger$};
\node[cemetery] (g3) at (4.2, 5.4) {$\dagger$};
\node[cemetery] (g4) at (4.2, 7.2) {$\dagger$};

\draw[cemetery edge] (c31)--(g1);
\draw[cemetery edge] (c34)--(g2);
\draw[cemetery edge] (b22)--(g3);
\draw[cemetery edge] (g3)--(g4);


\end{tikzpicture}
\caption{The first four generations of a cemetery-extended tree. The distinguished spine $(U_h)_{h\ge0}$ is highlighted in red, while cemetery children are shown in gray dashed style.}
\label{fig:spine-cemetery-up}
\end{figure}
\medskip

We recall from Subsection \ref{subsec:spaces} the
definition of the spinal space: 
\[
\Omega^{\mathrm{sp}}
:=
\left\{(\widetilde{\mathcal T} ,K,(U_h)_{h\ge0})\in \widetilde\Omega\times \mathcal U^{\mathbb N}:
U_0=\varnothing,\ U_{h+1}\text{ is a child of }U_h,\ \forall h\ge0\right\}.
\]
We continue to denote by $\widetilde{\mathcal F}$ and $\widetilde{\mathcal F}_h$ the reverse
images of the corresponding  $\sigma$-fields on $\widetilde{\Omega}$ by the map
$\pi_{\mathrm{tree}} : \Omega^{\mathrm{sp}} \to \widetilde{\Omega}$ which
forgets the distinguished infinite path. Then, the canonical $\sigma$-field and
filtration of $\Omega^{\mathrm{sp}}$ are:
\begin{align*}
    \mathcal F^{\mathrm{sp}} &= \widetilde{\mathcal F} \vee
    \sigma(U_0,U_1,\ldots) ;\\ 
    \mathcal F_h^{\mathrm{sp}} &= \widetilde{\mathcal F}_h \vee
    \sigma(U_0,\ldots,U_h). 
\end{align*}
We construct inductively a random pair in $\Omega^{\mathrm{sp}}$:
\[
    \left(\widetilde{\mathcal{T}}_n,(U_h)_{h\ge0}\right) \sim \Q_t,
\]
starting from $U_0=\varnothing$.
At each generation $h\ge0$, conditionally on the tree and the spine up to level $h$, we proceed as follows.
\smallskip

\noindent
\textbf{Step 1: branching at the spine vertex.}
Suppose that the current spine vertex is $U_h=u$ and that $K(u)=k$.
\begin{itemize}
    \item 
If $k=1$, then $u$ is a mass-one vertex in the extended tree, and it has a unique child $u^\dagger$ with
\[
K(u^\dagger)=1,\qquad X(u\to u^\dagger)=0.
\]
In that case we simply set
$U_{h+1}=u^\dagger.$
\item
Assume now that $k\ge2$, and write $m:=k-1$.
Let
$
(A_1,\dots,A_{\delta})
$
denote the children masses of $u$, so that
$
\sum_{i=1}^{\delta} A_i = m.
$
Equivalently, if
\[
p_i:=\frac{A_i}{m},\qquad 1\le i\le \delta,
\]
then $\sum_{i=1}^{\delta} p_i=1$.
Under $\Q_t$, the offspring partition at the spine vertex is sampled according
to the $t$-tilted Ewens law: for every nonnegative measurable functional $G$ of the offspring partition,
\[
\E_{\Q_t}\!\left[ G\left((A_i)_i\right)\,\middle|\,U_h=u,\widetilde{\mathcal F}_h\right]
=
\mathrm{e}^{-\kappa_k(t)}\,
\E\!\left[\left(\sum_{i=1}^{\delta} (p_i)^t\right)G\left((A_i)_i\right)\,\middle|\,K(u)=k\right].
\]

\end{itemize}

\smallskip

\noindent
\textbf{Step 2: choice of the next spine child.}
Conditionally on the realized offspring masses $(A_i)_{1\le i\le\delta}$, the next spine vertex $U_{h+1}$ is chosen among the children $(u1,\dots,u\delta)$ of $u$ according to the size-biased rule
\[
\Q_t\left(U_{h+1}=ui \,\big|\, U_h=u,\widetilde{\mathcal F}_h,(A_j)_{1\le j\le\delta}\right)
=
\frac{(p_i)^t}{\sum_{j=1}^{\delta} (p_j)^t} = \frac{(A_i)^t}{\sum_{j=1}^{\delta}
(A_j)^t},
\qquad 1\le i\le \delta.
\]

\smallskip

\noindent
\textbf{Step 3: branching away from the spine.}
Every vertex $v$ at generation $h$ such that $v\neq U_h$ evolves independently according to the original (untilted) fragmentation rule:
if $K(v)=1$, it continues along its cemetery ray, while if $K(v)\ge2$, its offspring partition is sampled from the original Ewens law corresponding to the mass $K(v)-1$.
Moreover, conditionally on the current generation, all offspring mechanisms are independent, except for the tilt applied at the spine vertex described in Step 1.
\medskip

\noindent In particular, if $U_h=u$ and $K(u)=k\ge2$, then for every measurable set $B$ of offspring partitions,
\[
\Q_t\left((A_i)_{1\le i\le \delta}\in B,\ U_{h+1}=ui
\,\big|\, U_h=u,\widetilde{\mathcal F}_h\right)
=
\mathrm{e}^{-\kappa_k(t)}\,
\E\!\left[
\ind_{\{(A_i)_{1\le i\le\delta}\in B\}}\,(p_i)^t
\,\middle|\, K(u)=k
\right].
\]
Indeed, the tilt by $\sum_j (p_j)^t$ coming from Step 1 and the conditional choice probability
$(p_i)^t/\sum_j (p_j)^t$ from Step 2 combine into the single factor $(p_i)^t$.
\bigskip

Thus, under $\Q_t$, the evolution is the same as under the original law
 $\Pp^{(n,\theta)}$ away from the spine, while at
the spine vertex with offspring proportions $(p_i)$, the offspring partition is tilted by the factor
$\sum_i (p_i)^t$, and conditionally on the realized offspring masses, the next spine child is chosen
with probability proportional to $(p_i)^t$.
\begin{remark}[Special case $t=1$]
At $t=1$, the tilt disappears in the following sense:
\[
\sum_i (p_i)^1 = 1,\qquad \kappa_k(1)=0 \ \text{ for every }k\ge1.
\]
So, the offspring law at the spine vertex is no longer tilted, and the tree marginal of
$\Q_1$ coincides with the original cemetery-extended law
$\widetilde\Pp^{(n,\theta)}$. This is related to our previous Remark
\ref{rem:trivial_martingale}, as made clear by the following proposition. 
 \end{remark}


\begin{proposition}[Identification of the spinal construction]
    We fix $n,\theta$ and denote $\Pp = \widetilde{\Pp}^{(n,\theta)}$, which is
    a probability measure on the space $\widetilde{\Omega}$ of
    cemetery-extended trees.
%  For each $h\ge 0$, let
% $\Q_t^{(h)}$ denote the restriction of $\Q_t$ to the $\sigma$-algebra
% $\mathcal F_h$.
Then, for every $h\ge 0$,
\[
    \left. \frac{d\Q_t}{d\Pp}\right|_{\widetilde{\mathcal F}_h} :=
        \frac{d(\Q_t\circ \pi_{\mathrm{tree}}^{-1}\!\restriction_{\widetilde{\mathcal F}_h})}{d(\widetilde\Pp^{(n,\theta)}\!\restriction_{\widetilde{\mathcal F}_h})}
=
\widetilde{Z}_h(t).
\]
Moreover, for every vertex $u$ at depth $h$,
\[
\Q_t(U_h=u\mid \widetilde{\mathcal F}_h)
=
\frac{\widetilde{Z}_h(u;t)}{\widetilde{Z}_h(t)}.
\]
Consequently, the spinal construction of $\Q_t$
coincides after projection by $\pi_{\mathrm{tree}}$ with the tilted measure
associated to the martingale $(\widetilde{Z}_h(t))_{h \ge 0}$.
\end{proposition}


\begin{proof}
For each $h\ge 0$, we prove the stronger statement:
for every vertex $u$ at depth $h$ and every nonnegative
$\widetilde{\mathcal F}_h$-measurable random variable $H$,
\begin{equation}\label{eq:joint-spine-density}
\E_{\Q_t}\!\left[H\,\ind_{\{U_h=u\}}\right]
=
\E\!\left[H\,\widetilde{Z}_h(u;t)\right].
\end{equation}
Once \eqref{eq:joint-spine-density} is proven, taking
$H=\ind_A$ with $A\in \widetilde{\mathcal F}_h$ and summing over all
vertices $u$ at depth $h$ gives
\[
\Q_t(A)
=
\sum_{|u|=h}^{\mathrm{ext}}
\Q_t(A\cap\{U_h=u\})
=
\E\!\left[
\ind_A
\sum_{|u|=h}^{\mathrm{ext}} \widetilde{Z}_h(u;t)
\right]
=
\E\!\left[\ind_A \,\widetilde{Z}_h(t)\right].
\]
Hence
\[
\left. \frac{d\Q_t}{d\Pp}\right|_{\widetilde{\mathcal F}_h}
=
\widetilde{Z}_h(t).
\]
Then, for $H$ nonnegative $\widetilde{\mathcal{F}}_h$-measure random
variable and for every $u$ with $|u|=h$:
$$    \E_{\Q_t}\!\left[H\,\Q_t(U_h=u\mid \widetilde{\mathcal F}_h)\right]  =
    \E_{\Q_t}\!\left[H\,\ind_{\{U_h=u\}}\right] =
    \E\!\left[H\,\widetilde{Z}_h(u;t)\right],
$$
so \eqref{eq:joint-spine-density} also yields:
\[
\Q_t(U_h=u\mid \widetilde{\mathcal F}_h)
=
\frac{\widetilde{Z}_h(u;t)}{\widetilde{Z}_h(t)}.
\]
So it remains only to prove \eqref{eq:joint-spine-density}.
\medskip

\noindent
\textbf{Case $h=0$.}
At level $0$, the only vertex is the root $\varnothing$, and by construction
$U_0=\varnothing$ almost surely under $\Q_t$. Moreover,
$
\widetilde{Z}_0(\varnothing;t)=1.
$
Therefore, for every nonnegative $\widetilde{\mathcal F}_0$-measurable $H$,
\[
\E_{\Q_t}\!\left[H\,\ind_{\{U_0=\varnothing\}}\right]
=
\E_{\Q_t}[H]
=
\E[H]
=
\E\!\left[H\,\widetilde{Z}_0(\varnothing;t)\right].
\]
Thus \eqref{eq:joint-spine-density} holds at level $0$.
\medskip

\noindent
\textbf{Induction step.}
Assume that \eqref{eq:joint-spine-density} holds at level $h$.
Fix a vertex $v$ at depth $h+1$, and write $u=v^{-}$ for its parent.
Let
\[
\mathcal G_{h+1}
:=
\sigma\!\left(
\text{the offspring mechanisms of all vertices at depth }h
\right).
\]
Then,
$
\widetilde{\mathcal F}_{h+1} = \widetilde{\mathcal F}_h\vee \mathcal G_{h+1}.
$
For the fixed parent-child pair $(u,v)$, define
\[
R_{u,v}
:=
\frac{\widetilde{Z}_{h+1}(v;t)}{\widetilde{Z}_h(u;t)}.
\]
\begin{itemize}
    \item 
If $K(u)=1$, then $u$ has the unique cemetery child $u^\dagger$, necessarily $v=u^\dagger$, and
$ X(u\to v)=0,\ \kappa_1(t)=0 $, so
\[
R_{u,v}=1.
\]
\item
Suppose now that $K(u)=k\ge 2$.
With $m=k-1$, let $(u_1,\dots,u_\delta)$ be the children of $u$, and suppose
$v=u_i$. Set
\[
p_j:=\frac{K(u_j)}{m},\qquad 1\le j\le \delta.
\]
Then
$
X(u\to v)=-\log p_i,
$
hence
\[
R_{u,v}
=
\mathrm{e}^{-\kappa_k(t)}\,\mathrm{e}^{-tX(u\to v)}
=
\mathrm{e}^{-\kappa_k(t)} \,(p_i)^t.
\]
\end{itemize}
We now claim that for every nonnegative $\mathcal G_{h+1}$-measurable random
variable $Y$,
\begin{equation}\label{eq:one-step-kernel}
\E_{\Q_t}\!\left[
Y\,\ind_{\{U_{h+1}=v\}}
\,\middle|\,\widetilde{\mathcal F}_h,\,U_h=u
\right]
=
\E\!\left[
Y\,R_{u,v}
\,\middle|\,\widetilde{\mathcal F}_h
\right]
\qquad
\Q_t\text{-a.s. on }\{U_h=u\}.
\end{equation}
\begin{itemize}
    \item 
If $K(u)=1$, then under the direct spinal construction the next spine
vertex is deterministically $u^\dagger=v$, while every other depth-$h$ vertex
branches according to the original law. Since also $R_{u,v}=1$, the two sides of
\eqref{eq:one-step-kernel} are equal.
\item
If $K(u)=k\ge 2$, then by construction, conditionally on
$\widetilde{\mathcal F}_h$ and on $\{U_h=u\}$, all depth-$h$ vertices distinct
from $u$ evolve exactly as under $\Pp$, whereas the joint law of the offspring
partition at $u$ together with the choice of the next spine child is tilted from
the original law by the factor
$\mathrm{e}^{-\kappa_k(t)}(p_i)^t=R_{u,v}.$ 
Therefore \eqref{eq:one-step-kernel} holds in this case as well.
\end{itemize}
Now let $H$ be any nonnegative $\widetilde{\mathcal F}_h$-measurable random
variable and let $Y$ be any nonnegative $\mathcal G_{h+1}$-measurable random
variable. Since $\{U_{h+1}=v\}\subseteq\{U_h=u\}$, we have
by \eqref{eq:one-step-kernel}
\begin{align*}
\E_{\Q_t}\!\left[H Y\,\ind_{\{U_{h+1}=v\}}\right]
&=
\E_{\Q_t}\!\left[
H\,\ind_{\{U_h=u\}}\,
\E_{\Q_t}\!\left[
Y\,\ind_{\{U_{h+1}=v\}}
\,\middle|\,\widetilde{\mathcal F}_h,U_h
\right]
\right]\\  
&=
\E_{\Q_t}\!\left[
H\,\ind_{\{U_h=u\}}\,
\E\!\left[
Y R_{u,v}\,|\, \widetilde{\mathcal F}_h
\right]
\right].
\end{align*}
The random variable
$H\,\E[Y R_{u,v}\mid \widetilde{\mathcal F}_h]$ 
is nonnegative and $\widetilde{\mathcal F}_h$-measurable, so the induction
hypothesis at level $h$ gives
\[
\E_{\Q_t}\!\left[H Y\,\ind_{\{U_{h+1}=v\}}\right]
=
\E\!\left[
H\,\E\!\left[Y\,R_{u,v}\mid \widetilde{\mathcal F}_h\right]
\widetilde{Z}_h(u;t)
\right].
\]
Since
$
\widetilde{Z}_h(u;t)\,R_{u,v}=\widetilde{Z}_{h+1}(v;t),
$
we obtain
\[
\E_{\Q_t}\!\left[H Y\,\ind_{\{U_{h+1}=v\}}\right]
=
\E\!\left[
H\,\E\!\left[Y\,\widetilde{Z}_{h+1}(v;t)\mid \widetilde{\mathcal F}_h\right]
\right]
=
\E\!\left[H Y\,\widetilde{Z}_{h+1}(v;t)\right].
\]
Thus the identity
\begin{equation}\label{eq:pi-system-step}
\E_{\Q_t}\!\left[H Y\,\ind_{\{U_{h+1}=v\}}\right]
=
\E\!\left[H Y\,\widetilde{Z}_{h+1}(v;t)\right]
\end{equation}
holds for every nonnegative product random variable $HY$ with
$H\in \widetilde{\mathcal F}_h$ and $Y\in \mathcal G_{h+1}$.
Now the class of sets of the form $A\cap B$ with
$A\in \widetilde{\mathcal F}_h$ and $B\in \mathcal G_{h+1}$ is a $\pi$-system
generating $\widetilde{\mathcal F}_{h+1}=\widetilde{\mathcal F}_h\vee\mathcal G_{h+1}$.
By the monotone class theorem, \eqref{eq:pi-system-step} extends to every
nonnegative $\widetilde{\mathcal F}_{h+1}$-measurable random variable $X$:
\[
\E_{\Q_t}\!\left[X\,\ind_{\{U_{h+1}=v\}}\right]
=
\E\!\left[X\,\widetilde{Z}_{h+1}(v;t)\right].
\]
This is exactly \eqref{eq:joint-spine-density} at level $h+1$.
The induction is complete, and the proposition follows.
\end{proof}

The spinal change of measure is completed by the following many-to-one formula:
\begin{lemma}[Many-to-one formula under the spine measure]
\label{lem:many-to-one}
Let $t>1$ and $h\ge 0$. We denote $\widetilde{T}_n\!\restriction_h$ the cemetery-extended tree
truncated at generation $h$. For every nonnegative measurable functional
$
\Psi=\Psi(\widetilde{T}_n\!\restriction_h,u),
$
where $u$ is a vertex at depth $h$, one has
\[
\E\!\left[\sum_{|u|=h}^{\mathrm{ext}} \widetilde{Z}_h(u;t)\,
\Psi\!\left(\widetilde{T}_n\!\restriction_h,u\right)\right]
=
\E_{\Q_t}\!\left[\Psi\!\left(\widetilde{T}_n\!\restriction_h,U_h\right)\right].
\]
In particular, for every nonnegative $\widetilde{\mathcal F}_h$-measurable functional
$F_h(u)$ of a depth-$h$ vertex $u$,
\[
\E\!\left[\sum_{|u|=h}^{\mathrm{ext}} F_h(u)\right]
=
\E_{\Q_t}\!\left[
\exp\!\left(
tS_h(U_h)+\sum_{\ell=0}^{h-1}\kappa_{K(U_\ell)}(t)
\right)
F_h(U_h)
\right].
\]
\end{lemma}

\begin{proof}
By definition of the tilted measure,
\[
\left. \frac{d\Q_t}{d\Pp}\right|_{\widetilde{\mathcal F}_h}=\widetilde{Z}_h(t),
\qquad
\Q_t(U_h=u\mid \widetilde{\mathcal F}_h)
=
\frac{\widetilde{Z}_h(u;t)}{\widetilde{Z}_h(t)},
\qquad |u|=h.
\]
Hence
\[
\E_{\Q_t}\!\left[\Psi\left(\widetilde{T}_n\!\restriction_h,U_h\right)\right]
=
\E\!\left[
\widetilde{Z}_h(t)
\sum_{|u|=h}^{\mathrm{ext}}
\frac{\widetilde{Z}_h(u;t)}{\widetilde{Z}_h(t)}\,
\Psi\!\left(\widetilde{T}_n\!\restriction_h,u\right)
\right]=
\E\!\left[\sum_{|u|=h}^{\mathrm{ext}} \widetilde{Z}_h(u;t)\,
\Psi\!\left(\widetilde{T}_n\!\restriction_h,u\right)\right].
\]
This proves the first identity.
The second identity follows by taking 
\[
\Psi\left(\widetilde{T}_n\!\restriction_h,u\right)
=
\exp\!\left(
tS_h(u)+\sum_{\ell=0}^{h-1}\kappa_{K(u_\ell)}(t)
\right)
F_h(u).\qedhere
\]
% so that
% \[
% \widetilde{Z}_h(u;t)\,
% \Psi\left(\widetilde{T}_n\!\restriction_h,u\right)=F_h(u).
% \]
% This gives the desired many-to-one formula.
\end{proof}



\subsubsection{Sketch of proof of the technical lemma}

We present here the idea of proof, see the complete proof in the appendix.

\begin{proof}[Idea of proof of Lemma \ref{lem:critical_barrier_second_moment}]
The proof is based on a truncated counting variable and a second-moment argument under a spinal change of measure.
For
\[
\mathcal B_h(u)
:=
\left\{
\mathcal G_{n,\alpha}(u),\ 
ah-\omega_n-1\le S_h(u)\le ah-\omega_n, \text{ and }
S_j(u) \leq aj \text{ for all }j\leq h
\right\},
\]
we consider
\[
\widetilde N_h(a):=\sum_{|u|=h}\ind_{\mathcal B_h(u)}.
\]
We use the martingale  $(\widetilde{Z}_h(t))_{h \ge 0}$ and the spine measure $\Q_t$ introduced above.
The first moment is obtained by a many-to-one formula under the spine measure \(\Q_t\), with \(t>1\) chosen so that
\[
a=-\kappa'(t).
\]
On \(\mathcal B_h\), writing \(Y_r=S_r-ar\), one gets
\[
\mathbb E[\widetilde N_h(a)]
\asymp
\mathrm{e}^{h(\kappa(t)+ta)-t\omega_n}\,\,
\Q_t\left(\mathcal G_{n,\alpha}(U_h),\  -\omega_n-1\le Y_h\le -\omega_n
    \text{ and } Y_r\le 0 \text{ for all }r\le h\right),
\]
and this probability is of order \((1+\omega_n)\,,h^{-3/2}\) by the one-spine ballot estimate in Lemma~\ref{lem:one_spine_ballot}.
\medskip
 
For the second moment, we decompose pairs of depth-\(h\) vertices according to their most recent common ancestor \(w\) at depth \(r\). Writing \(m=h-r\) and \(L_r(w)=ar-S_r(w)\), the contribution below \(w\) is controlled by the two-spine continuation bound, see Lemma~\ref{lem:two-spine-bound}, while the contribution of the prefix up to \(w\) is estimated again by a many-to-one argument together with the same ballot bound. Summing over \(r\) yields
\[
\mathbb E[\widetilde N_h(a)^2]
\lesssim
\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n}(1+\omega_n)^2\,h^{-3},
\]
which matches the square of the first moment up to constants. A Paley--Zygmund argument therefore gives
\[
\mathbb P\left(\widetilde N_h(a)>0\right)\ge c>0.
\]
This proves the existence, with positive probability, of a depth-\(h\) vertex staying below the linear barrier and ending within distance \(\omega_n\) from it.
\end{proof}



\section{Conclusion}\label{sec:6}

\subsection{Identification of the constant \texorpdfstring{$c_\star(2)$}{c*2}}

We now return to the Plancherel random tree, which corresponds to the Ewens fragmentation
tree with parameter $\theta=2$ by Theorem~\ref{thm:plancherel_to_fragmentation}. Combining Theorem~\ref{thm:plancherel_to_fragmentation} with the general
height asymptotics established in Section~\ref{sec:5}, we obtain a proof of
Theorem \ref{thm:height}:
if $H_n$ is the height of a Plancherel random rooted tree $T_n$ of size $n$, 
then
\[
\frac{H_n}{\log n}\xrightarrow[n\to\infty]{\mathbb P} c_\star(2),
\]
where
\[
c_{\star}(2)=\inf_{t>1}\left(\frac{t}{-\log\beta_t(2)}\right)
=\inf_{t>1}\left(\frac{t}{\log\!\left(\frac{t(t+1)}{2}\right)}\right).
\]
In particular, the constant governing the logarithmic growth of the height of Plancherel random
trees is completely explicit. 
If one sets
\[
f(t):=\frac{t}{\log\!\left(\frac{t(t+1)}{2}\right)}, \qquad t>1,
\]
then the minimizer $t_\star$ is characterized by
\[
\log\!\left(\frac{t_\star(t_\star+1)}{2}\right)=\frac{2t_\star+1}{t_\star+1},
\]
and one obtains
$
t_\star \approx 2.92069467 $ and 
$$c_\star(2)=f(t_\star)\approx 1.67380505.
$$
Thus, the height of a Plancherel random tree satisfies
$
H_n \sim c_\star(2)\log n
$
in probability. This provides a logarithmic analogue, in the setting of rooted trees, of the law of large numbers
for the first row of a Plancherel random partition.

\subsection{Discussion and perspectives}

The main result of this paper shows that Plancherel random rooted trees have logarithmic height,
with an explicit deterministic constant. More generally, for Ewens fragmentation trees with parameter
$\theta>0$, we proved that the height satisfies
\[
\frac{H_n}{\log n}\xrightarrow[n\to\infty]{\mathbb P} c_\star(\theta),
\qquad
c_\star(\theta)=\inf_{t>1}\left(\frac{t}{-\log\beta_t(\theta)}\right).
\]
In the Plancherel case $\theta=2$, this yields the constant identified above.
Our proof combines several ingredients of rather different nature. First, the Plancherel measure on
rooted trees can be embedded into the family of Ewens fragmentation trees. Second, generating
functions and Poissonization reduce the height problem to the analysis of a threshold quantity.
Third, the upper bound is obtained by a contraction estimate on suitable $s$-mass functionals.
Finally, the lower bound is derived by identifying an underlying branching random walk structure
and by proving a variational principle for deep paths.
\medskip
There are several natural directions for further investigation.

A first question is whether one can go beyond the law of large numbers and study second-order
fluctuations of the height. In the classical Plancherel measure on partitions, the first row admits
fluctuations of order $n^{1/6}$ governed by the Tracy--Widom law. In the present tree setting, the
geometry is different and the logarithmic scale suggests a very different fluctuation theory, but it is
reasonable to expect that the branching random walk viewpoint could be used to obtain a finer
description of $H_n-c_\star(2)\log n$.

A second direction is to investigate other geometric observables of Plancherel random trees, such as
their profile, the distribution of masses across generations, or possible global scaling limits. The
projective picture behind the Plancherel measure on trees also suggests the relevance of Markovian
growth rules and of observables analogous to those appearing in the asymptotic theory of random
partitions. In particular, one may ask whether there exists a natural algebra of observables encoding
the geometry of these random trees.

A third question concerns infinite random trees and central measures. For partitions, Plancherel
measures arise as marginals of distinguished central measures on infinite standard tableaux, and the
classification of central measures is a deep theorem of Kerov and Vershik in \cite{vershik1981asymptotic}. It would be very interesting
to understand whether an analogous classification can be developed for infinite rooted trees endowed
with standard labellings, and whether the Plancherel tree measure occupies a special position inside
such a family.

Finally, it would be desirable to understand to what extent the method developed here applies to
other recursive tree models or fragmentation mechanisms. Since the proof isolates a branching random walk
variational principle as the source of the constant, one may hope that similar ideas extend beyond
the Ewens family and lead to a more general theory of logarithmic-height random trees.

\bigskip

In summary, this work shows that the Plancherel measure on rooted trees leads to a new and
tractable asymptotic regime, parallel in spirit to the classical Plancherel theory for partitions but
with its own probabilistic structure. We hope that the explicit identification of the height constant
and the techniques introduced here will provide a useful starting point for a broader asymptotic
theory of Plancherel random trees.



\appendix

\section{Results needed in the proof of lower bound}\label{sec:appendix}

\subsection{Standard random-walk results}

We record here the random-walk estimate used in the proof of Lemma~\ref{lem:critical_barrier_second_moment}.
The most direct reference for the flat-barrier joint endpoint estimate in the
non-lattice case is \cite[Proposition~19(i)]{doney2012local}. Its proof is based on the
conditioned local limit estimates for random walks conditioned to stay positive;
see in particular \cite[Theorems~3--4]{vatutin2009local}. In the Gaussian-domain case
relevant here, \cite[Theorem~1]{caravenna2005local} is the corresponding conditioned Stone
local limit theorem, while \cite[Theorem~3]{caravenna2005local} gives the density version
under the additional absolute continuity / spread-out assumption. 

We first state the estimate in the form naturally produced by the fluctuation
theory of ladder variables.

\begin{lemma}[Estimate in renewal-function form]
\label{lem:flat-barrier-renewal}
Let $(\bar Y_j)_{j\ge0}$ be a centered, non-degenerate, non-lattice random walk
with exponential moments, started from $\bar Y_0=-x$ under $\mathbb P_{-x}$.
Let $U$ and $V$ denote respectively the renewal functions of the ascending and
descending ladder-height processes of the increment law.
 There exist constants $c,C>0$ such that, uniformly for all \(m\) large enough and \(x,y\ge 0\) with \(x+y=o(\sqrt m)\), one has
\[
c\,\frac{U(x)\displaystyle\int_y^{y+1}V(w)\,dw}{m^{3/2}}
\le
\mathbb P_{-x}\!\left(\bar Y_j\le0,\ 0\le j\le m,\ -y-1< \bar Y_m\le -y\right)
\le
C\,\frac{U(x)\displaystyle\int_y^{y+1}V(w)\,dw}{m^{3/2}} .
\]
Moreover, if the increment law is absolutely continuous, and if there exists an
integer $k\ge1$ such that the $k$-fold convolution of the increment density is
bounded, then uniformly for all $\lambda\in(0,1]$,
\[
\mathbb P_{-x}\!\left(\bar Y_j\le0,\ 0\le j\le m,\ -y-\lambda< \bar Y_m\le -y\right)
\le
C\,\frac{U(x)\displaystyle\int_y^{y+\lambda}V(w)\,dw}{m^{3/2}} .
\]
\end{lemma}

\begin{proof}
For $j \ge 0$, set
$S_j:=x+\bar Y_j$.
Then $S_0=0$, and if we define
\[
T_x:=\inf\{n\ge1:S_n>x\},
\]
we have, for every $\lambda>0$,
\[
\left\{\bar Y_j\le0,\ 0\le j\le m,\ -y-\lambda< \bar Y_m\le -y\right\}
=
\left\{T_x>m,\ x-y-\lambda< S_m\le x-y\right\}.
\]
Now we apply the flat-barrier endpoint estimate from
\cite[Proposition~18]{doney2012local}: uniformly with respect to $\lambda$ in
a fixed interval $[0,\Delta)$ and uniformly as 
\[
x_m:=\frac{x}{c_m}\to0,\qquad y_m:=\frac{y}{c_m}\to0,
\]
one has
\[
\mathbb P\!\left(S_m\in(x-y-\Delta,x-y],\ T_x>m\right)
\sim
\frac{U(x)\,f(0)\,\displaystyle\int_y^{y+\Delta}V(w)\,dw}{m\,c_m},
\]
where $c_m$ is the norming sequence for the random walk and $f(0)$ is the value
at $0$ of the density of the limiting stable law.\medskip

In our setting the increments have exponential moments, hence in particular
finite variance. Therefore the walk belongs to the domain of attraction of the
Gaussian law, so $c_m\asymp \sqrt m$. Consequently,
\[
\frac{1}{m\,c_m}\asymp \frac{1}{m^{3/2}}.
\]
Taking $\Delta=1$ and absorbing the comparison constants into two positive real
numbers $c$ and $C$, we obtain the claimed estimates
uniformly for all $m$ large enough, all $\lambda\in(0,1]$, and all
$x,y\ge 0$ such that $x+y=o(\sqrt m)$.
\end{proof}

To obtain the form used in the main text, we now replace the renewal functions
by the simpler factor $(1+x)(1+y)$.

\begin{lemma}[Linear growth of the renewal functions]
\label{lem:renewal-linear}
Under the assumptions of Lemma~\ref{lem:flat-barrier-renewal}, there exist
constants $c_1,C_1>0$ such that for all $u\ge0$,
\[
c_1(1+u)\le U(u)\le C_1(1+u),
\qquad
c_1(1+u)\le V(u)\le C_1(1+u).
\]
Consequently,
\[
c_2(1+y)\le \int_y^{y+1}V(w)\,dw\le C_2(1+y),
\qquad
\int_y^{y+\lambda}V(w)\,dw\le C_2\,\lambda(1+y),
\quad \lambda\in(0,1].
\]
\end{lemma}

\begin{proof}
By standard fluctuation theory, the ascending and descending ladder-height
renewal functions are regularly varying. More precisely, for a random walk in
the domain of attraction of a stable law of index $\alpha$ and positivity
parameter $\rho$, one has
\[
U\in R_{\alpha\rho},
\qquad
V\in R_{\alpha(1-\rho)}.
\]
Here $R_\beta$ denotes the class of regularly varying functions at infinity
with index $\beta$, i.e. $f\in R_\beta$ means that
\[
\frac{f(cx)}{f(x)}\to c^\beta\qquad\text{for every }c>0,\quad x\to\infty.
\]
For the descending renewal function this is stated explicitly in
\cite[Lemma~2.1]{caravenna2008invariance}; applying the same result to the reflected walk $-S$
gives the corresponding statement for $U$.

Since the present walk is centered with finite variance, we are in the Gaussian
case $\alpha=2$ and $\rho=\frac12$. Hence both $U$ and $V$ are regularly varying
with index $1$, i.e.
\[
U(u)\sim c_+ u,\qquad V(u)\sim c_- u \qquad (u\to\infty)
\]
for some constants $c_+,c_->0$.
Because $U$ and $V$ are positive increasing renewal functions (in particular
$U(0)=V(0)=1$), these asymptotics imply the global bounds
\[
U(u)\asymp 1+u,\qquad V(u)\asymp 1+u,\qquad u\ge0.
\]
The displayed estimates for $\int_y^{y+1}V(w)\,dw$ and
$\int_y^{y+\lambda}V(w)\,dw$ follow immediately from the monotonicity of $V$.
\end{proof}

Combining Lemmas~\ref{lem:flat-barrier-renewal} and~\ref{lem:renewal-linear},
we obtain the form used in the proof.


\begin{lemma}
\label{lem:flat-barrier}
Let \((\bar Y_j)\) be a centered, non-degenerate, non-lattice random walk with exponential moments. Then there exist constants \(c_0,C_0>0\) such that, uniformly for all \(m\) large enough and \(x,y\ge 0\) with
\(x+y=o(\sqrt m)\),
\begin{equation}
c_0\,\frac{(1+x)(1+y)}{m^{3/2}}
\le
\mathbb P_{-x}\!\left(
\bar Y_j\le 0,\ \forall\,0\le j\le m,\ 
-y-1< \bar Y_m\le -y
\right)
\le
C_0\,\frac{(1+x)(1+y)}{m^{3/2}}.
\end{equation}
Moreover, if the increment law of the random walk \((\bar Y_j)\) is absolutely continuous, and there exists an integer $k\ge1$ such that the $k$-fold convolution of the increment density is bounded, then for all $\lambda\in(0,1]$,
\begin{equation}
\Pb_{-x}\!\left(
\bar Y_j\le 0,\ \forall\,0\le j\le m,\ -y-\lambda< \bar Y_m\le -y
\right)
\le
C_0\,\lambda\,\frac{(1+x)(1+y)}{m^{3/2}}.
\end{equation}
\end{lemma}
\begin{proof}
This is an immediate consequence of
Lemmas~\ref{lem:flat-barrier-renewal} and~\ref{lem:renewal-linear}.
\end{proof}

We show that the random walk we will use satisfies these conditions.
\begin{lemma}
Fix $t>1$ and $\theta>0$, and let $P\sim \mathrm{Beta}(t,\theta)$ on $(0,1)$. Set
\[
\bar X:=-\log P.
\]
Then the law of $\bar X$ is absolutely continuous on $(0,\infty)$. Moreover, there exists an
integer $k\ge 1$ such that the $k$-fold convolution density of $\bar X$ is bounded on
$(0,\infty)$.
\end{lemma}

\begin{proof}
Let
\[
c_{t,\theta}:=\frac{\Gamma(t+\theta)}{\Gamma(t)\,\Gamma(\theta)}.
\]
Since $P$ has density
\[
    f_P(x)=c_{t,\theta}\,x^{t-1}(1-x)^{\theta-1}\,\ind_{(0,1)}(x),
\]
the change of variables $x=\mathrm{e}^{-u}$ gives that $\bar X=-\log P$ has density
\[
f_{\bar X}(u)
=
c_{t,\theta}\,\mathrm{e}^{-tu}(1-\mathrm{e}^{-u})^{\theta-1}\,\ind_{(0,\infty)}(u).
\]
Hence the law of $\bar X$ is absolutely continuous.
It remains to prove that some convolution power is bounded.

\medskip
\noindent
\textbf{Case 1: $\theta\ge 1$.}
Since $0<1-\mathrm{e}^{-u}\le 1$ for all $u>0$, we have
\[
    f_{\bar X}(u)\le c_{t,\theta}\,\mathrm{e}^{-tu}, \qquad u>0.
\]
Thus $f_{\bar X}\in L^\infty(0,\infty)$, so we may simply take $k=1$.

\medskip
\noindent
\textbf{Case 2: $0<\theta<1$.}
Near $0$, one has $1-\mathrm{e}^{-u}\sim u$, hence
\[
f_{\bar X}(u)\asymp u^{\theta-1}\qquad (u\downarrow 0),
\]
while as $u\to\infty$ the factor $(1-\mathrm{e}^{-u})^{\theta-1}$ stays bounded and the density decays
exponentially like $\mathrm{e}^{-tu}$. Therefore
\[
f_{\bar X}\in L^p(0,\infty)\qquad\text{for every }1\le p<\frac1{1-\theta}.
\]
Choose an integer $k\ge 2$ such that $k\theta>1.$
Set
\[
p:=\frac{k}{k-1}.
\]
Then $p<\frac1{1-\theta},$
because $k\theta>1$ is equivalent to $\frac{k}{k-1}<\frac1{1-\theta}$. Hence
$f_{\bar X}\in L^p(0,\infty)$.
We apply Young's convolution inequality with $k$ factors, all equal to $f_{\bar X}$:
since
\[
\frac{k}{p}=k-1,
\]
the target exponent is $r=\infty$, and therefore
\[
    \|(f_{\bar X})^{*k}\|_\infty
\le
(\|f_{\bar X}\|_p)^k
<
\infty.
\]
Thus the $k$-fold convolution density is bounded.
\end{proof}
\begin{remark}
Since our walk is absolutely continuous, replacing the half-open interval
$-y-\lambda< \bar Y_m \le -y$ by the closed interval $-y-\lambda \le \bar Y_m \le -y$ does not change
the probability.
\end{remark}

\subsection{Results concerning Ewens measure}
Fix $t>1$. Conditionally on $K(U_\ell)=k\ge 2$, we 
 write the offspring masses of the current spine vertex as $A_1,A_2,\dots$, and
 we set $p_i=\frac{A_i}{m}$ and 
\[
P_{\ell+1}:=\frac{K(U_{\ell+1})}{m}\in\left\{\frac1m,\frac2m,\dots,\frac{m}{m}\right\},
\]
where $m=k-1$. We also set
\[
\beta_{m,t}(\theta)
=
\E\!\left[\sum_{i} (p_i)^t \,\middle|\, K(U_\ell)=k\right]
=
\E\!\left[\sum_{j=1}^m C_j\left(\frac{j}{m}\right)^t\right],
\]
the expectation being taken under the $\mathrm{Ewens}(m,\theta)$ measure. Recall
from Lemma \ref{lem:kappa-rate} that $\beta_{m,t}(\theta) \to \beta_t(\theta)$ as $m$
(or $k$) goes to infinity.
\begin{proposition}[One-step tilted spine law and its Beta limit]
\label{prop:ewens_onestep_beta}
 Denote by $\mu_{k,t}$ the conditional law of $P_{\ell+1}$ under the spine measure
$\Q_t$. 
\begin{enumerate}
    \item We have
$$
\mu_{k,t}\!\left(\left\{\frac{j}{m}\right\}\right)
=
\frac{\theta}{\beta_{m,t}(\theta)}\,
\frac{j^{t-1}}{m^t}\,
\frac{\Gamma(m+1)\,\Gamma(m-j+\theta)}
{\Gamma(m-j+1)\,\Gamma(m+\theta)},
$$
\item As $k$ goes to infinity, $\mu_{k,t}$ converges in distribution to a
    $\mathrm{Beta}(t,\theta)$ distribution with density 
    $$f_t(x) =
    \frac{\Gamma(t+\theta)}{\Gamma(t)\,\Gamma(\theta)}\,x^{t-1}\,(1-x)^{\theta-1}\,\mathbf
    1_{(0,1)}(x).$$
\item Consequently, if $ P\sim \mathrm{Beta}(t,\theta)$ and $X_{\ell+1} = -\log
    P_{\ell+1}$, then $X_{\ell+1}$ converges in distribution to $-\log P$.
 \end{enumerate}
\end{proposition}

\begin{proof}
Recall that under the tilted spine measure $\Q_t$: 
\begin{enumerate}
\item the offspring environment is biased by the factor $\sum_i (p_i)^t$;

\item given the realized environment $(p_i)_i$, the spine child is chosen with probability
\[
\Q_t(I=i\mid \widetilde{\mathcal F}_\ell,(p_j)_j)
=
\frac{(p_i)^t}{\sum_j (p_j)^t}.
\]
\end{enumerate}
Therefore, for every bounded measurable function $\varphi$ on $(0,1]$,
$$\E_{\Q_t}[\varphi(P_{\ell+1})\mid K(U_\ell)=k]
=
\frac{\E\!\left[\sum_i (p_i)^t\,
\varphi(p_i)\,\middle|\,K(U_\ell)=k\right]}{\beta_{m,t}(\theta)} =
    \frac{\E\!\left[\sum_{j=1}^m
    C_j\,(\frac{j}{m})^t\,\varphi(\frac{j}{m})\right]}{\beta_{m,t}(\theta)}.
$$
Substituting the explicit formula for $\E[C_j]$ under the
$\mathrm{Ewens}(m,\theta)$ measure (Equation \eqref{eq:ECj-exact}), and taking
\(\varphi=\ind_{\{\frac{j}{m}\}}\), we obtain the
claimed formula for $\mu_{k,t}(\{\frac{j}{m}\})$.
\medskip

For the convergence in distribution, since the measures considered are on
$[0,1]$, it suffices to prove the convergence of all the moments. Fix $r \geq 1$
and consider 
$$\mu_{k,t}(x^r) = \frac{1}{\beta_{m,t}(\theta)}\,\E\!\left[\sum_{j=1}^m
C_j\left(\frac{j}{m}\right)^{t+r}\right] =
\frac{\beta_{m,t+r}(\theta)}{\beta_{m,t}(\theta)}.$$
We have:
$$\beta_{m,t}(\theta)
\longrightarrow
\beta_t(\theta)
=
\frac{\Gamma(t)\,\Gamma(\theta+1)}{\Gamma(t+\theta)};$$
indeed, this is the same finite-mass normalization already used in the proof of
\(\kappa_k(t)\to \kappa(t)\). Applying the same result with $t+r$ in place of
$t$, we conclude that
$$\int_{x=0}^1 x^r \,\mu_{k,t}(dx) \longrightarrow_{k \to \infty}
\frac{\Gamma(t+r)\,\Gamma(t+\theta)}{\Gamma(t)\,\Gamma(t+r+\theta)} =
\int_{x=0}^1 x^r \,f_t(x)\,dx.$$
The convergence in distribution of $P_{\ell+1}$ conditionally on $K(U_l) = k \to
+\infty$ is thus established, and since the map \(x\mapsto -\log x\) is continuous on \((0,1)\), the convergence for
\(X_{\ell+1}=-\log P_{\ell+1}\) follows by the continuous mapping theorem.
\end{proof}

\begin{proposition}[Local comparison for the one-step tilted spine law]
\label{prop:local_cellwise_comparison}
Fix $t>1$ and let $\nu_t=\mathrm{Beta}(t,\theta)$ on $(0,1)$, with density
$
f_t(x)$.
We set
\[
I_j^{(m)}:=\left(\frac{j-1}{m},\frac{j}{m}\right],\qquad 1\le j\le m.
\]
With the same notations as in 
Proposition~\ref{prop:ewens_onestep_beta}, 
the following estimates hold.
\begin{enumerate}
\item[(i)] \textbf{Uniform cell-wise comparability.}
There exist constants \(0<c_t\le C_t<\infty\) such that for all sufficiently large \(k\) and all
\(1\le j\le m\),
\begin{equation}
c_t\,
\nu_t\!\left(I_j^{(m)}\right)
\le
\mu_{k,t}\!\left(\left\{\frac{j}{m}\right\}\right)
\le
C_t\,
\nu_t\!\left(I_j^{(m)}\right).
\label{eq:global-cellwise}
\end{equation}

\item[(ii)] \textbf{Sharp comparison in the bulk.}
There exist constants $C,\gamma>0$ such that for
every $\eta\in(0,\frac12)$, 
\begin{equation}
\sup_{\eta m\le j\le (1-\eta)m}
\left|
\frac{\mu_{k,t}(\{j/m\})}{\nu_t(I_j^{(m)})}-1
\right|
\le
C\,\eta^{-1}m^{-\gamma},
\label{eq:bulk-sharp}
\end{equation}
for all sufficiently large $k$.
\end{enumerate}
\end{proposition}
\begin{proof}
By combining:
\begin{itemize}
    \item  the first item from Proposition~\ref{prop:ewens_onestep_beta};
    \item 
 the convergence $\beta_{m,t}(\theta) \to \beta_t(\theta)$ which ensures 
 that there exist constants \(0<c_0\le C_0<\infty\) such that for all sufficiently large
\(k\),
$$    c_0\le \beta_{m,t}(\theta)\le C_0;$$
\item and the Wendel estimates, 
% there exist constants
% \(0<c_1\le C_1<\infty\) such that for all \(n\ge 0\),
% \begin{equation*}
% c_1\,(n+1)^{\theta-1}
% \le
% \frac{\Gamma(n+\theta)}{\Gamma(n+1)}
% \le
% C_1\,(n+1)^{\theta-1};
% \end{equation*}
 \end{itemize}
 we obtain
$$\mu_{k,t}\!\left(\left\{\frac{j}{m}\right\}\right)
\asymp
\frac1m
\left(\frac{j}{m}\right)^{t-1}
\left(\frac{m-j+1}{m}\right)^{\theta-1},
$$
uniformly for \(1\le j\le m\), with constants depending only on \(t,\theta\).
Let us prove that we have similarly 
\[
\nu_t(I_j^{(m)}) \asymp
\frac1m\left(\frac{j}{m}\right)^{t-1}\left(\frac{m-j+1}{m}\right)^{\theta-1},
\]
uniformly for \(1\le j\le m\),
with constants depending only on \(t,\theta\).
We treat first the cells \(2\le j\le m-1\). Notice that $x \mapsto x^{t-1}$ is
increasing, while $x \mapsto (1-x)^{\theta-1}$ is increasing for $\theta \geq 1$
and decreasing for $\theta<1$.
\begin{itemize}
    \item If $\theta \geq 1$, then 
        \begin{align*}
        \frac{\Gamma(t)\,\Gamma(\theta)}{\Gamma(t+\theta)}\,\nu_t(I_j^{(m)})
        &= \int_{\frac{j-1}{m}}^{\frac{j}{m}} x^{t-1}\,(1-x)^{\theta-1}\,dx 
        \le \frac{1}{m}
        \left(\frac{j}{m}\right)^{t-1}\,\left(\frac{m-j+1}{m}\right)^{\theta-1}
        \end{align*}
        and 
        \begin{align*}
        \frac{\Gamma(t)\,\Gamma(\theta)}{\Gamma(t+\theta)}\,\nu_t(I_j^{(m)})
        &\ge
        \frac{1}{m}\left(\frac{j-1}{m}\right)^{t-1}\,\left(\frac{m-j}{m}\right)^{\theta-1} 
        \ge 
        \frac{2^{2-t-\theta}}{m}\left(\frac{j}{m}\right)^{t-1}\,\left(\frac{m-j+1}{m}\right)^{\theta-1}.
        \end{align*}
        
    \item Similarly, if $\theta <1$, then 
        \begin{align*}
        \frac{\Gamma(t)\,\Gamma(\theta)}{\Gamma(t+\theta)}\,\nu_t(I_j^{(m)})
        \le \frac{1}{m}
        \left(\frac{j}{m}\right)^{t-1}\,\left(\frac{m-j}{m}\right)^{\theta-1} 
        \le \frac{2^{1-\theta}}{m}
        \left(\frac{j}{m}\right)^{t-1}\,\left(\frac{m-j+1}{m}\right)^{\theta-1}
        \end{align*}
        and 
        \begin{align*}
        \frac{\Gamma(t)\,\Gamma(\theta)}{\Gamma(t+\theta)}\,\nu_t(I_j^{(m)})
        &\ge
        \frac{1}{m}\left(\frac{j-1}{m}\right)^{t-1}\,\left(\frac{m-j+1}{m}\right)^{\theta-1} 
        \ge 
        \frac{2^{1-t}}{m}\left(\frac{j}{m}\right)^{t-1}\,
        \left(\frac{m-j+1}{m}\right)^{\theta-1}.
        \end{align*}
 \end{itemize}
This proves the result except for the endpoints $j=1$ and $j=m$. The endpoint $j=1$ is analogous; we detail the case $j=m$. In that case,
\[
I_m^{(m)}=\left(\frac{m-1}{m},1\right].
\]
For \(x\in I_m^{(m)}\), we have \(x\in(1/2,1]\) for all \(m\ge 2\), hence
$x^{t-1}\asymp 1$ uniformly. Thus
\[
\nu_t(I_m^{(m)})
=
\frac{\Gamma(t+\theta)}{\Gamma(t)\,\Gamma(\theta)}
\int_{1-\frac1m}^1 x^{t-1}(1-x)^{\theta-1}\,dx
\asymp
\int_{1-\frac1m}^1 (1-x)^{\theta-1}\,dx.
\]
With the change of variable \(y=1-x\), this becomes
\[
\nu_t(I_m^{(m)}) \asymp \int_0^{\frac1m} y^{\theta-1}\,dy
= \frac1\theta\, m^{-\theta}.
\]
On the other hand,
\[
\frac1m\left(\frac{m}{m}\right)^{t-1}\left(\frac{1}{m}\right)^{\theta-1}
= m^{-\theta}.
\]
Hence the same comparison also holds for \(j=m\), and 
\eqref{eq:global-cellwise} is established.
\medskip

\noindent\textbf{Step 3: sharp comparison in the bulk.}
Fix \(\eta\in(0,\frac12)\), and restrict to indices
\[
\eta m\le j\le (1-\eta)m.
\]
Then both \(j\) and \(m-j\) are of order \(m\), uniformly in \(j\). Hence the standard
Gamma-ratio asymptotics are uniform on this range:
\begin{align}
\frac{\Gamma(m+1)}{\Gamma(m+\theta)}
&=
m^{1-\theta}\left(1+O(m^{-1})\right),
\label{eq:gamma-ratio-1}\\
\frac{\Gamma(m-j+\theta)}{\Gamma(m-j+1)}
&=
(m-j)^{\theta-1}\left(1+O(\eta^{-1}m^{-1})\right).
\end{align}
Moreover, by Lemma \ref{lem:kappa-rate}, we have the estimate
\begin{equation}
    \beta_{m,t}(\theta)=\beta_t(\theta)+O(m^{-\gamma}).
\label{eq:B-sharp}
\end{equation}
Substituting \eqref{eq:gamma-ratio-1}--\eqref{eq:B-sharp} into the explicit
formula for $\mu_{k,t}$, we get
\begin{equation}
\mu_{k,t}\!\left(\left\{\frac{j}{m}\right\}\right)
=
\frac1m\,f_t\!\left(\frac{j}{m}\right)\left(1+O(\eta^{-1}m^{-\gamma})\right),
\label{eq:mu-bulk-sharp}
\end{equation}
uniformly for \(\eta m\le j\le (1-\eta)m\).
We now estimate the Beta-cell mass. Since
\[
f_t(x)=\frac{\Gamma(t+\theta)}{\Gamma(t)\Gamma(\theta)}
x^{t-1}(1-x)^{\theta-1},
\]
we have
\[
\frac{f_t'(x)}{f_t(x)}
=
\frac{t-1}{x}-\frac{\theta-1}{1-x}.
\]
Hence, for $x\in[\frac{\eta}{2},1-\frac{\eta}{2}]$,
\[
\left|\frac{f_t'(x)}{f_t(x)}\right|
\le C\eta^{-1},
\]
and therefore
$|f_t'(x)|\le C\eta^{-1} f_t(x).$ For all large $m$, if $\eta m\le j\le (1-\eta)m$, then
    $I_j^{(m)}\subset[\eta/2,1-\eta/2].$ 
    Thus, by the mean value theorem, uniformly for $x\in I_j^{(m)}$,
\[
f_t(x)
=
f_t\!\left(\frac{j}{m}\right)\left(1+O(\eta^{-1}m^{-1})\right).
\]
Integrating over $I_j^{(m)}$ yields
\begin{equation}
\nu_t(I_j^{(m)})
=
\frac1m f_t\!\left(\frac{j}{m}\right)\left(1+O(\eta^{-1}m^{-1})\right).
\label{eq:beta-bulk-sharp}
\end{equation}
Dividing \eqref{eq:mu-bulk-sharp} by \eqref{eq:beta-bulk-sharp}, we obtain
% \[
% \frac{
% \mu_{k,t}\!\left(\left\{\frac{j}{m}\right\}\right)
% }{
% \nu_t(I_j^{(m)})
% }
% =
% 1+O(\eta^{-1}m^{-\gamma}),
% \]
% uniformly for \(\eta m\le j\le (1-\eta)m\), which proves
\eqref{eq:bulk-sharp}.
\end{proof}

\subsection{Two important lemmas}
Recall that if $u_0=\varnothing,u_1,\dots,u_h$ is a root-to-leaf path, then we write $K(u_\ell)$ for the mass at depth $\ell$. We have defined in Section \ref{sec:5} the stepwise log-loss along the path by
\[
X_{u_\ell} := -\log\left(\frac{K(u_\ell)}{K(u_{\ell-1})-1}\right)\ge0,\qquad
S_h(u):=\sum_{\ell=1}^h X_{u_\ell}.
\]
In this subsection, we will compare the logarithmic displacement along the spine
with the random walk with increments distributed as $\bar{X} = -\log P$, with $P \sim \nu_t =
\Beta(t, \theta)$. 

\subsubsection{One-spine ballot estimate}
\begin{lemma}[One-spine ballot estimate]
\label{lem:one_spine_ballot}
We place ourselves under the assumptions \ref{hyp_A1}, \ref{hyp_A2} and
\ref{hyp_A3}.
We set $Y_r:=S_r(U_r)-ar.$ 
Given \(0<\alpha<\rho\), we define
\[
E_h(\omega_n)
:=
\left\{
\mathcal G_{n,\alpha}(U_h),\
Y_r\le 0,\ \forall\,0\le r\le h,\
-\omega_n-1\le Y_h\le -\omega_n
\right\}.
\]
Then there
exist constants \(c,C> 0\) for which, for all sufficiently large \(n\),
\begin{equation}
c\,\frac{1+\omega_n}{h^{3/2}}
\le
\Q_t\left(E_h(\omega_n)\right)
\le
C\,\frac{1+\omega_n}{h^{3/2}}.
\label{eq:one-spine}
\end{equation}
\end{lemma}
\begin{proof}
By Proposition~\ref{prop:ewens_onestep_beta}, conditionally on $\widetilde{\mathcal F}_r$ and $K(U_r)=k\ge2$, the ratio $P_{r+1}:=\frac{K(U_{r+1})}{K(U_r)-1}$
has law $\mu_{k,t}$ under $\Q_t$, and
\[
X_{r+1}:=-\log P_{r+1},\qquad
Y_r=\sum_{i=1}^r (X_i-a).
\]
We must prove that there exist $c,C>0$ such that
\[
c\,\frac{1+\omega_n}{h^{3/2}}
\le
\Q_t(E_h(\omega_n))
\le
C\,\frac{1+\omega_n}{h^{3/2}}
\]
for all large $n$.
Notice that by Lemma~\ref{lem:poly-slack-large-masses}, 
$Y_r \le 0$ for all $r \le h$, together with $ah \le (1 - \rho)\log n$, imply
$\mathcal G_{n, \alpha}(U_h)$. Thus, we can rewrite
\[
E_h(\omega_n)
=
\left\{
Y_r\le0,\ \forall\,0\le r\le h,\ 
-\omega_n-1\le Y_h\le-\omega_n
\right\}.
\]

\medskip
\noindent
{\bf Step 1: reference centered walk.}
Let
\[
P\sim \nu_t,\qquad \bar X:=-\log P,
\qquad \E[\bar X]=-\kappa'(t) = a,
\]
and let $(\bar X_i)_{i\ge1}$ be i.i.d.\ copies of $\bar X$. Set
\[
\bar Y_r:=\sum_{i=1}^r(\bar X_i-a),\qquad \bar Y_0=0.
\]
Since $t>1$, the law of $\bar X$ is non-degenerate, non-lattice and has exponential moments. Hence
Lemma~\ref{lem:flat-barrier} applies and gives
\begin{equation}
\Pb\!\left(
\bar Y_r\le0,\ \forall\,0\le r\le h,\ -\omega_n-1\le \bar Y_h\le-\omega_n
\right)
\asymp
\frac{1+\omega_n}{h^{3/2}},
\label{eq:A8-flat}
\end{equation}
uniformly because $\omega_n=o(h^{1/3})$. 

\medskip
\noindent
{\bf Step 2: masses along the spine on the good event.}
On the event $\mathcal G_{n,\alpha}(U_h)$, we have
\[
K(U_r)\ge n^\alpha,\qquad 0\le r\le h-1.
\]
Therefore, if we write
$m_r:=K(U_r)-1,$ 
then for all large $n$,
\[
m_r\ge n^\alpha-1\ge \frac12 n^\alpha,\qquad 0\le r\le h-1.
\]
Since $h\asymp\log n$, it follows that
\[
h\,m_r^{-\gamma}\le C(\log n)\,n^{-\alpha\gamma}\to0
\]
uniformly in $r\le h-1$.

\medskip
\noindent
{\bf Step 3: choice of a shrinking bulk window.}
Set $\eta_n:=n^{-\delta}$ with $0 < \delta < \frac{\alpha\gamma}2$.
Then $\eta_n\downarrow0$. Define the interval
\[
I_n:=[\eta_n,1-\eta_n].
\]
We split paths according to whether all ratios $P_1,\dots,P_h$ stay in $I_n$.
Let
\[
E_h^{\mathrm{bulk}}(\omega_n)
:=
E_h(\omega_n)\cap\{P_r\in I_n,\ 1\le r\le h\},
\]
and similarly for the reference walk let
\[
\bar E_h^{\mathrm{bulk}}(\omega_n)
:=
\left\{
\bar Y_r\le0,\ \forall\,0\le r\le h,\ 
-\omega_n-1\le \bar Y_h\le-\omega_n,\ 
\bar P_r\in I_n,\ 1\le r\le h
\right\},
\]
where $\bar P_r:=\mathrm{e}^{-\bar X_r}$.

\medskip
\noindent
{\bf Step 4: the endpoint contribution is negligible.}
We first estimate the probability that one increment falls outside $I_n$.
For the reference law $\nu_t$, we have
\[
\nu_t([0,\eta_n])\le C\eta_n^t,
\qquad
\nu_t([1-\eta_n,1])\le C\eta_n^\theta,
\]
because $t>1$ and near $1$ the density behaves like $(1-x)^{\theta-1}$.
Hence
$\nu_t((0,1)\setminus I_n)\le C\eta_n^\beta,$ 
where $\beta = \min\{t,\theta\}$. Since
\[
\bar E_h(\omega_n)\setminus \bar E_h^{\mathrm{bulk}}(\omega_n)
\subseteq
\{\exists\,1\le r\le h:\bar P_r\notin I_n\},
\]
we have, by a union bound,
\[
\Pb\!\left(\bar E_h(\omega_n)\setminus \bar E_h^{\mathrm{bulk}}(\omega_n)\right)
\le
\sum_{r=1}^h \Pb(\bar P_r\notin I_n)
=
h\,\nu_t((0,1)\setminus I_n).
\]
Therefore
\[
\Pb\!\left(\bar E_h(\omega_n)\setminus \bar E_h^{\mathrm{bulk}}(\omega_n)\right)
\le
Ch\eta_n^\beta.
\]
By our choice of $\eta_n$, we have $h^{5/2}\eta_n^\beta\to0$, hence
\[
Ch\eta_n^\beta
=
o(h^{-3/2})
=
o\!\left(\frac{1+\omega_n}{h^{3/2}}\right).
\]
For the spine law, Proposition~\ref{prop:local_cellwise_comparison}(i) gives, uniformly in $1\le j\le m$,
\[
\mu_{k,t}\!\left(\left\{\frac jm\right\}\right)
\le C_t\,\nu_t(I_j^{(m)}).
\]
Summing over those cells contained in $(0,1)\setminus I_n$, we obtain uniformly for all
$k\ge n^\alpha$,
\[
\mu_{k,t}((0,1)\setminus I_n)\le C\,\nu_t((0,1)\setminus I_n)\le C\eta_n^\beta.
\]
Similarly,
\[
\Q_t\left(E_h(\omega_n)\setminus E_h^{\mathrm{bulk}}(\omega_n)\right)
=o\!\left(\frac{1+\omega_n}{h^{3/2}}\right).
\]

\medskip
\noindent
{\bf Step 5: comparison of bulk path probabilities via deterministic cell sequences.}
Let
$m_0:=n-1.$ 
For a sequence \(\mathbf j=(j_1,\ldots,j_h)\), define recursively
\[
m_r(\mathbf j):=j_r-1,\qquad 1\le r\le h,
\]
and say that \(\mathbf j\) is admissible if
\[
1\le j_r\le m_{r-1}(\mathbf j),\qquad 1\le r\le h.
\]
For such a sequence set
\[
p_r(\mathbf j):=\frac{j_r}{m_{r-1}(\mathbf j)},
\qquad
x_r(\mathbf j):=-\log p_r(\mathbf j),
\qquad
y_r(\mathbf j):=\sum_{i=1}^r\bigl(x_i(\mathbf j)-a\bigr).
\]
Let \(\mathcal A_h^{\mathrm{bulk}}\) be the set of admissible sequences
\(\mathbf j=(j_1,\ldots,j_h)\) such that
\begin{itemize}
    \item $p_r(\mathbf j)\in I_n=[\eta_n,1-\eta_n]$ for $1\le r\le h$, 
    \item $y_r(\mathbf j)\le0$ for $0\le r\le h$,
    \item $-\omega_n-1\le y_h(\mathbf j)\le-\omega_n$.
\end{itemize}
Under the actual tilted spine law, the probability of a given admissible sequence
\(\mathbf j\) is
\[
\mathsf Q_n(\mathbf j)
:=
\prod_{r=1}^h
\mu_{m_{r-1}(\mathbf j)+1,t}
\left(
\left\{
\frac{j_r}{m_{r-1}(\mathbf j)}
\right\}
\right).
\]
Define the discrete Beta reference path measure by
\[
\mathsf B_n(\mathbf j)
:=
\prod_{r=1}^h
\nu_t\left(I_{j_r}^{(m_{r-1}(\mathbf j))}\right),
\]
where
\[
I_j^{(m)}:=\left(\frac{j-1}{m},\frac jm\right].
\]
Equivalently, \(\mathsf B_n\) is the law of the Markov chain which, given
\(m_{r-1}\), chooses \(j_r\in\{1,\ldots,m_{r-1}\}\) with probability
\(\nu_t(I_{j_r}^{(m_{r-1})})\), and then sets \(m_r=j_r-1\).
For every \(\mathbf j\in\mathcal A_h^{\mathrm{bulk}}\), the barrier condition
\(y_r(\mathbf j)\le0\) and the slack assumption
$ah\le (1-\rho)\log n$ 
imply, by Lemma~\ref{lem:poly-slack-large-masses}, that
\[
m_{r-1}(\mathbf j)\ge \frac12 n^\alpha,
\qquad 1\le r\le h,
\]
for all sufficiently large \(n\). Therefore, by Proposition~\ref{prop:local_cellwise_comparison}(ii),
uniformly over \(\mathbf j\in\mathcal A_h^{\mathrm{bulk}}\),
\[
\mu_{m_{r-1}+1,t}
\left(
\left\{
\frac{j_r}{m_{r-1}}
\right\}
\right)
=
\nu_t\left(I_{j_r}^{(m_{r-1})}\right)
\left(1+\varepsilon_{n,r}(\mathbf j)\right),
\]
with
\[
|\varepsilon_{n,r}(\mathbf j)|
\le
C\eta_n^{-1}m_{r-1}^{-\gamma}
\le
C\eta_n^{-1}n^{-\alpha\gamma}.
\]
Since \(\eta_n=n^{-\delta}\) with \(0<\delta<\alpha\gamma/2\), and \(h=O(\log n)\), we have
\[
\sum_{r=1}^h |\varepsilon_{n,r}(\mathbf j)|
\le
Ch\eta_n^{-1}n^{-\alpha\gamma}
=
o(1),
\]
uniformly over all \(\mathbf j\in\mathcal A_h^{\mathrm{bulk}}\). Hence
\[
\mathsf Q_n(\mathbf j)
=
(1+o(1))\,\mathsf B_n(\mathbf j),
\]
uniformly for \(\mathbf j\in\mathcal A_h^{\mathrm{bulk}}\). Summing over
\(\mathcal A_h^{\mathrm{bulk}}\), we obtain
\begin{equation}
\Q_t\left(E_h^{\mathrm{bulk}}(\omega_n)\right)
=
(1+o(1))\,\mathsf B_n\left(\mathcal A_h^{\mathrm{bulk}}\right).
\label{eq:qE-disc}
\end{equation}

It remains to compare the discrete Beta reference chain with the continuous
Beta walk.
Let \((\bar P_r)_{1\le r\le h}\) be i.i.d. with law \(\nu_t\), and define
recursively
\[
\widehat m_0:=n-1,
\qquad
\widehat \jmath_r:=\left\lceil \widehat m_{r-1}\bar P_r\right\rceil,
\qquad
\widehat m_r:=\widehat \jmath_r-1.
\]
Then
$\mathbb P(\widehat \jmath_1=j_1,\ldots,\widehat \jmath_h=j_h) = \mathsf
B_n(j_1,\ldots,j_h).$ 
Set
\[
\widehat X_r:=
-\log\left(\frac{\widehat \jmath_r}{\widehat m_{r-1}}\right),
\qquad
\widehat Y_r:=\sum_{i=1}^r(\widehat X_i-a),
\]
and let 
$\widehat E_h^{\mathrm{bulk}}(\omega_n) := \left\{ (\widehat
\jmath_1,\ldots,\widehat \jmath_h)\in\mathcal A_h^{\mathrm{bulk}} \right\}.$ 
Then
\[
\mathsf B_n(\mathcal A_h^{\mathrm{bulk}})
=
\mathbb P\left(\widehat E_h^{\mathrm{bulk}}(\omega_n)\right).
\]

On the event \(\{\bar P_r\in I_n,\ 1\le r\le h\}\), we have
$\bar P_r\le \frac{\widehat \jmath_r}{\widehat m_{r-1}} \le \bar P_r+\frac1{\widehat
m_{r-1}}$, so in particular,
$\widehat X_r\le \bar X_r.$ 
Therefore, if the continuous walk satisfies \(\bar Y_s\le0\) for \(0\le s\le h\), then
\[
\widehat Y_s\le \bar Y_s\le0,\qquad 0\le s\le h.
\]
By Lemma~\ref{lem:poly-slack-large-masses}, together with the slack
\(ah\le(1-\rho)\log n\), this implies
\[
\widehat m_{r-1}\ge \frac12 n^\alpha,
\qquad 1\le r\le h,
\]
for all large \(n\). The same conclusion holds on the discretized barrier event
\(\widehat E_h^{\mathrm{bulk}}(\omega_n)\).

Hence, on the union of the continuous and discretized bulk barrier events,
\[
\left|\bar X_r-\widehat X_r\right|
\le
\frac{C}{\eta_n \widehat m_{r-1}}
\le
C\eta_n^{-1}n^{-\alpha}.
\]
Consequently,
\[
\sup_{0\le r\le h}
|\bar Y_r-\widehat Y_r|
\le
Ch\eta_n^{-1}n^{-\alpha}
=
Chn^{-(\alpha-\delta)}
=:\varepsilon_n
\to0.
\]

Thus the events \(\widehat E_h^{\mathrm{bulk}}(\omega_n)\) and
\(\bar E_h^{\mathrm{bulk}}(\omega_n)\) can differ only if the continuous centered walk comes within
distance \(\varepsilon_n\) of the barrier \(0\), or within distance \(\varepsilon_n\) of the terminal
window endpoints \(-\omega_n-1\) and \(-\omega_n\). By the same boundary-layer estimate based
on Lemma~\ref{lem:flat-barrier},
\[
\mathbb P\left(
\widehat E_h^{\mathrm{bulk}}(\omega_n)
\triangle
\bar E_h^{\mathrm{bulk}}(\omega_n)
\right)
=
o\left(\frac{1+\omega_n}{h^{3/2}}\right).
\]
Therefore
\begin{equation}
\mathsf B_n(\mathcal A_h^{\mathrm{bulk}})
=
\mathbb P\left(\bar E_h^{\mathrm{bulk}}(\omega_n)\right)
+
o\left(\frac{1+\omega_n}{h^{3/2}}\right).
\label{eq:pE-disc}
\end{equation}
Combining \eqref{eq:qE-disc} and \eqref{eq:pE-disc}, we conclude that
\begin{equation*}
\Q_t\!\left(E_h^{\mathrm{bulk}}(\omega_n)\right)
=
(1+o(1))\,\Pb\!\left(\bar E_h^{\mathrm{bulk}}(\omega_n)\right)
+
o\!\left(\frac{1+\omega_n}{h^{3/2}}\right).
\end{equation*}


\medskip
\noindent
{\bf Step 6: conclusion.}
By Steps~4 and 5,
% \[
% \Pb\!\left(\bar E_h^{\mathrm{bulk}}(\omega_n)\right)
% =
% \Pb\!\left(\bar E_h(\omega_n)\right)
% +
% o\!\left(\frac{1+\omega_n}{h^{3/2}}\right),
% \]
% and
% \[
% \Q_t\left(E_h(\omega_n)\right)
% =
% \Q_t\left(E_h^{\mathrm{bulk}}(\omega_n)\right)
% +
% o\!\left(\frac{1+\omega_n}{h^{3/2}}\right).
% \]
\[
\Q_t\left(E_h(\omega_n)\right) = (1+o(1))\,\Pb\!\left(\bar E_h(\omega_n)\right) + o\!\left(\frac{1+\omega_n}{h^{3/2}}\right).
\]
Using \eqref{eq:A8-flat}, we conclude that
$\Q_t\left(E_h(\omega_n)\right)\asymp \frac{1+\omega_n}{h^{3/2}}.$ 
This proves \eqref{eq:one-spine}.
\end{proof}


\subsubsection{Two-spine continuation bound}
\begin{lemma}[Two-spine continuation bound]\label{lem:two-spine-bound}
    Under the assumptions \ref{hyp_A1}, \ref{hyp_A2} and \ref{hyp_A3}, choose
    \(0<\alpha<\rho\) and 
let $w$ be a vertex at depth $r\in\{0,\dots,h-1\}$, and write
\[
m:=h-r, \qquad \ell:=L_r(w):=ar-S_r(w)\ge0.
\]
Thus, if two depth-$h$ descendants have MRCA (most recent common ancestor) equal to $w$, then each continuation from $w$
to generation $h$ has length $m$, including the split step from generation $r$ to generation $r+1$.
\medskip

For $j\in\{0,\dots,m\}$, define the translated continuation barrier event
\[
E_{m,\ell}:=
\left\{
Y^{\mathrm{cont}}_j\le \ell,\ \forall\,0\le j\le m,\ 
-\omega_n-1+\ell\le Y^{\mathrm{cont}}_m\le -\omega_n+\ell
\right\},
\]
where
\[
Y^{\mathrm{cont}}_j:=\sum_{i=1}^j (X_i-a),\qquad Y^{\mathrm{cont}}_0:=0,
\]
and $(X_i)_{i\ge1}$ denotes the descendant increment process under the spine law $\Q_t$
along a continuation issued from $w$, with the first increment corresponding to the split step
from generation $r$ to generation $r+1$.
Let
\[
q_m(\ell):=\Q_t(E_{m,\ell}\cap \mathcal G^{\mathrm{cont}}_{n,\alpha}),
\]
where \(\mathcal G^{\mathrm{cont}}_{n,\alpha}\) denotes the event that the starting mass
\(K(w)\) and all masses subsequently encountered along the continuation are at
least \(n^\alpha\).
\medskip

Then there exists a constant $C<\infty$ such that the following holds for all large $n$, uniformly
for those values of $\ell=L_r(w)$ with $\ell+\omega_n=o(\sqrt m)$ (in the application to Lemma~\ref{lem:critical_barrier_second_moment}, this estimate will only be used in the regime \(m\ge (\omega_n)^3\), so that \(\omega_n=o(\sqrt m)\) holds uniformly there):

\smallskip

\noindent{\rm (i)} One-spine continuation bound:
\begin{equation}
q_m(\ell)\le C\,\frac{(1+\ell)(1+\omega_n)}{m^{3/2}}.
\label{eq:one-spine-bound}
\end{equation}

\smallskip

\noindent{\rm (ii)} Two-spine product bound:
let $\mathcal G_r(w)$ be the $\sigma$-field generated by $\widetilde{\mathcal F}_r$ together with the full offspring
configuration of $w$. Conditionally on $\mathcal G_r(w)$, consider two descendant spines
issued from two \emph{distinct} children of $w$, each evolved below its initial child according to the tilted spine law $\Q_t$ in the corresponding subtree. Let $E^{(1)}_{m,\ell}$ and $E^{(2)}_{m,\ell}$
be the two corresponding continuation events. Then
\begin{equation}
\Q_t\otimes \Q_t\left(
E^{(1)}_{m,\ell}\cap \mathcal G^{(1),\mathrm{cont}}_{n,\alpha},
\ 
E^{(2)}_{m,\ell}\cap \mathcal G^{(2),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right)
\le
C\,\frac{(1+\ell)^2(1+\omega_n)^2}{m^3}.
\label{eq:two-spine}
\end{equation}
\end{lemma}

\begin{proof}
We first prove the one-spine continuation bound, and then deduce the two-spine estimate by conditional independence below the split. Again by Lemma~\ref{lem:poly-slack-large-masses}, under our assumptions, \(\mathcal G^{\mathrm{cont}}_{n,\alpha}\) is automatic on the continuation barrier event. Indeed, if the continuation satisfies \(E_{m,\ell}\), then for \(0\le s\le m\),
\[
S_{r+s}=S_r(w)+as+Y^{\mathrm{cont}}_s
=ar-\ell+as+Y^{\mathrm{cont}}_s
\le a(r+s).
\]
Moreover the terminal condition gives
\[
S_h\le ah-\omega_n.
\]
Since \(ah\le(1-\rho)\log n\), Lemma~\ref{lem:poly-slack-large-masses} applied to the full concatenated path
from the root to generation \(h\) gives \(K(U_{r+s})\ge n^\alpha\) for all
\(0\le s\le m\).

\medskip
\noindent\textbf{Step 1: reference centered walk.}
Let
\[
P\sim \nu_t=\mathrm{Beta}(t,\theta),\qquad \bar X:=-\log P,
\]
and let $(\bar X_i)_{i\ge1}$ be i.i.d. copies of $\bar X$. Since
$\mathbb E[\bar X]=a=-\kappa'(t),$ 
the centered walk
\[
\bar Y_j:=\sum_{i=1}^j (\bar X_i-a),\qquad \bar Y_0:=0,
\]
is mean zero. Moreover, since $t>1$, the law of $\bar X$ is non-degenerate and has exponential moments.
Hence Lemma~\ref{lem:flat-barrier} applies.
Define
\[
p_m(\ell):=
\mathbb P\left(
\bar Y_j\le \ell,\ \forall\,0\le j\le m,\ 
-\omega_n-1+\ell\le \bar Y_m\le -\omega_n+\ell
\right).
\]
After the translation $Z_j:=\bar Y_j-\ell$, this becomes
\[
p_m(\ell)
=
\mathbb P_{-\ell}\left(
Z_j\le 0,\ \forall\,0\le j\le m,\ 
-\omega_n-1\le Z_m\le -\omega_n
\right).
\]
Therefore, by the upper bound in Lemma~\ref{lem:flat-barrier},
\begin{equation}
p_m(\ell)\le C\,\frac{(1+\ell)(1+\omega_n)}{m^{3/2}},
\end{equation}
uniformly whenever $\ell+\omega_n=o(\sqrt m)$.

\medskip
\noindent\textbf{Step 2: comparison with the actual continuation law.}
We compare the finite-mass continuation law with the Beta reference walk.
Fix the information available at the vertex \(w\), and put
$M_0:=K(w)-1.$ 
For a sequence \(\mathbf q=(q_1,\ldots,q_m)\), define recursively
\[
M_s(\mathbf q):=q_s-1,\qquad 1\le s\le m.
\]
We say that \(\mathbf q\) is admissible if
\[
1\le q_s\le M_{s-1}(\mathbf q),\qquad 1\le s\le m.
\]
For an admissible sequence, set
\begin{align*}
    p_s(\mathbf q):=\frac{q_s}{M_{s-1}(\mathbf q)},\qquad
x_s(\mathbf q):=-\log p_s(\mathbf q),\qquad
    y_s(\mathbf q):=\sum_{i=1}^s\bigl(x_i(\mathbf q)-a\bigr),
\qquad 0\le s\le m.
\end{align*}
Choose
\[
\eta_n=n^{-\delta},
\qquad
0<\delta<\min\left\{\frac{\alpha\gamma}{2},\frac{\alpha}{2}\right\},
\]
and set
$I_n:=[\eta_n,1-\eta_n].$ 
Let \(\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)\) be the set of admissible sequences
\(\mathbf q=(q_1,\ldots,q_m)\) such that
\begin{itemize}
    \item $p_s(\mathbf q)\in I_n$ for $1\le s\le m$,
    \item $y_s(\mathbf q)\le \ell$ for $0\le s\le m$,
    \item $-\omega_n-1+\ell\le y_m(\mathbf q)\le -\omega_n+\ell$.
\end{itemize}
Under the actual tilted continuation law, the probability of a given admissible
sequence \(\mathbf q\) is
\[
\mathsf Q_{M_0}(\mathbf q)
:=
\prod_{s=1}^m
\mu_{M_{s-1}(\mathbf q)+1,t}
\left(
\left\{
\frac{q_s}{M_{s-1}(\mathbf q)}
\right\}
\right).
\]
Define the discrete Beta reference path weight by
\[
\mathsf B_{M_0}(\mathbf q)
:=
\prod_{s=1}^m
\nu_t\left(I_{q_s}^{(M_{s-1}(\mathbf q))}\right),
\]
where
\[
I_q^{(M)}:=\left(\frac{q-1}{M},\frac qM\right].
\]
Equivalently, \(\mathsf B_{M_0}\) is the law of the Markov chain which,
given \(M_{s-1}\), chooses $q_s\in\{1,\ldots,M_{s-1}\}$
with probability $\nu_t\left(I_{q_s}^{(M_{s-1})}\right)$,
and then sets $M_s=q_s-1$. We first discard non-bulk increments. Let
\[
E^{\mathrm{bulk}}_{m,\ell}
:=
E_{m,\ell}\cap\{P_s\in I_n,\ 1\le s\le m\},
\]
where \(P_s=\mathrm e^{-X_s}\) are the actual continuation ratios. Since
\[
\nu_t((0,1)\setminus I_n)\le C\eta_n^\beta,
\qquad \beta:=\min\{t,\theta\},
\]
and since Proposition~\ref{prop:local_cellwise_comparison}(i) gives, uniformly
for all \(k\ge n^\alpha\),
\[
\mu_{k,t}((0,1)\setminus I_n)
\le C\nu_t((0,1)\setminus I_n)
\le C\eta_n^\beta,
\]
we obtain, by a union bound,
\[
\Q_t\left(
E_{m,\ell}\cap \mathcal G^{\mathrm{cont}}_{n,\alpha}
\setminus E^{\mathrm{bulk}}_{m,\ell}
\right)
\le C m\eta_n^\beta.
\]
Since \(m\le h=O(\log n)\) and \(\eta_n\) is polynomially small,
\[
m\eta_n^\beta
=
o\left(
\frac{(1+\ell)(1+\omega_n)}{m^{3/2}}
\right).
\]

Now consider a sequence $\mathbf q\in\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)$. For this sequence, the final bound $y_m(\mathbf q)\le -\omega_n+\ell$ implies that the full path from the root to generation \(h=r+m\) satisfies
\[
S_h
=
S_r(w)+am+y_m(\mathbf q)
=
ar-\ell+am+y_m(\mathbf q)
\le
ah-\omega_n.
\]
Since $ah\le(1-\rho)\log n$ and \(0<\alpha<\rho\), Lemma~\ref{lem:poly-slack-large-masses} implies, for all large \(n\),
\[
K(U_{r+s})\ge n^\alpha,\qquad 0\le s\le m.
\]
Therefore, along every such bulk admissible sequence,
\[
M_{s-1}(\mathbf q)\ge \frac12 n^\alpha,
\qquad 1\le s\le m.
\]

By Proposition~\ref{prop:local_cellwise_comparison}(ii), uniformly over
\(\mathbf q\in\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)\),
\[
\mu_{M_{s-1}+1,t}
\left(
\left\{
\frac{q_s}{M_{s-1}}
\right\}
\right)
=
\nu_t\left(I_{q_s}^{(M_{s-1})}\right)
\left(1+\varepsilon_{n,s}(\mathbf q)\right),
\]
with
\[
|\varepsilon_{n,s}(\mathbf q)|
\le
C\eta_n^{-1}M_{s-1}^{-\gamma}
\le
C\eta_n^{-1}n^{-\alpha\gamma}.
\]
Hence
\[
\sum_{s=1}^m |\varepsilon_{n,s}(\mathbf q)|
\le
Cm\eta_n^{-1}n^{-\alpha\gamma}
=
o(1),
\]
uniformly over all
\(\mathbf q\in\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)\). Therefore
\[
\mathsf Q_{M_0}(\mathbf q)
\le
(1+o(1))\,\mathsf B_{M_0}(\mathbf q),
\]
uniformly over these sequences. Summing over
\(\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)\), we get
\[
\Q_t\left(
E^{\mathrm{bulk}}_{m,\ell}\cap \mathcal G^{\mathrm{cont}}_{n,\alpha}
\right)
\le
(1+o(1))\,
\mathsf B_{M_0}\left(
\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)
\right).
\]

It remains to bound the discrete Beta reference probability. Let
\((\bar P_s)_{1\le s\le m}\) be i.i.d. with law \(\nu_t\), and define recursively
\[
\widehat M_0:=M_0,\qquad
\widehat q_s:=\left\lceil \widehat M_{s-1}\bar P_s\right\rceil,
\qquad
\widehat M_s:=\widehat q_s-1.
\]
Then, for every admissible sequence \(\mathbf q\),
\[
\mathbb P(\widehat q_1=q_1,\ldots,\widehat q_m=q_m)
=
\mathsf B_{M_0}(\mathbf q).
\]
Set
\[
\widehat X_s:=
-\log\left(\frac{\widehat q_s}{\widehat M_{s-1}}\right),
\qquad
\widehat Y_s:=\sum_{i=1}^s(\widehat X_i-a),
\]
and let
\[
\widehat E^{\mathrm{bulk}}_{m,\ell}
:=
\left\{
(\widehat q_1,\ldots,\widehat q_m)
\in
\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)
\right\}.
\]
Then
\[
\mathsf B_{M_0}\left(
\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)
\right)
=
\mathbb P\left(\widehat E^{\mathrm{bulk}}_{m,\ell}\right).
\]

On the event \(\widehat E^{\mathrm{bulk}}_{m,\ell}\), we have
\[
\widehat M_{s-1}\ge \frac12 n^\alpha,
\qquad 1\le s\le m,
\]
by the same polynomial-slack argument as above. Moreover,
\[
\bar P_s
\le
\frac{\widehat q_s}{\widehat M_{s-1}}
\le
\bar P_s+\frac1{\widehat M_{s-1}}.
\]
Since the discrete ratios are in \(I_n\), the map \(x\mapsto-\log x\) has derivative bounded by
\(\eta_n^{-1}\) on the relevant interval. Thus
\[
|\bar X_s-\widehat X_s|
\le
C\eta_n^{-1}n^{-\alpha},
\]
and therefore
\[
\sup_{0\le s\le m}
|\bar Y_s-\widehat Y_s|
\le
Cm\eta_n^{-1}n^{-\alpha}
=: \varepsilon_n
\to0.
\]

Consequently,
\[
\widehat E^{\mathrm{bulk}}_{m,\ell}
\subseteq
\left\{
\bar Y_s\le \ell+\varepsilon_n,\ 0\le s\le m,\ 
-\omega_n-1+\ell-\varepsilon_n
\le
\bar Y_m
\le
-\omega_n+\ell+\varepsilon_n
\right\}.
\]
By the upper bound in Lemma~\ref{lem:flat-barrier}, and since $\ell+\omega_n=o(\sqrt m)$ and $\varepsilon_n=o(1)$,
we obtain
\[
\mathsf B_{M_0}\left(
\mathcal A^{\mathrm{bulk}}_{m,\ell}(M_0)
\right)
\le
C\frac{(1+\ell)(1+\omega_n)}{m^{3/2}}.
\]

Combining the bulk truncation estimate and the last display gives
\[
\Q_t\left(E_{m,\ell}\cap \mathcal G^{\mathrm{cont}}_{n,\alpha}\right)
\le
C\frac{(1+\ell)(1+\omega_n)}{m^{3/2}}.
\]
This proves \eqref{eq:one-spine-bound}.

\medskip
\noindent\textbf{Step 3: conditional independence below the split.}
Condition on \(\mathcal G_r(w)\), namely on the prefix up to depth \(r\) and on the full offspring
configuration of \(w\).

Let \(c\) be a fixed child of \(w\), and write
\[
x_c:=
-\log\left(\frac{K(c)}{K(w)-1}\right)
\]
for the deterministic first increment from \(w\) to \(c\). If a continuation through \(c\) satisfies
\(E_{m,\ell}\), then necessarily $x_c-a\le \ell$. Otherwise the event is empty.

Assume therefore that \(x_c-a\le\ell\), and define the shifted slack
\[
\ell_c:=\ell-(x_c-a)\ge0.
\]
After the deterministic first step, the remaining continuation has length \(m-1\) and must satisfy
the same translated barrier condition with slack \(\ell_c\). More precisely, if
\[
Y^{(c)}_j
:=
\sum_{i=1}^j(X^{(c)}_i-a),
\qquad 0\le j\le m-1,
\]
denotes the centered walk below the child \(c\), then \(E_{m,\ell}\) implies
\begin{itemize}
    \item $Y^{(c)}_j\le \ell_c$ for $0\le j\le m-1$,
    \item $-\omega_n-1+\ell_c \le Y^{(c)}_{m-1} \le -\omega_n+\ell_c.$
\end{itemize}
Moreover, $\ell_c\le \ell+a$ because \(x_c\ge0\).

Hence, by the one-spine continuation bound \eqref{eq:one-spine-bound} already proved, uniformly over the child \(c\),
\[
\Q_t\left(
E_{m,\ell}^{(c)}\cap \mathcal G^{(c),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right)
\le
C\frac{(1+\ell_c)(1+\omega_n)}{(m-1)^{3/2}}
\le
C\frac{(1+\ell)(1+\omega_n)}{m^{3/2}}.
\]
Now take two distinct children \(c_1\neq c_2\) of \(w\). Conditionally on \(\mathcal G_r(w)\), the
subtrees below \(c_1\) and \(c_2\) are independent by the Markov branching property. Therefore
\[
\begin{aligned}
&\Q_t\otimes\Q_t\left(
E^{(1)}_{m,\ell}\cap \mathcal G^{(1),\mathrm{cont}}_{n,\alpha},
E^{(2)}_{m,\ell}\cap \mathcal G^{(2),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right)
\\
&\qquad\le
C
\frac{(1+\ell)^2(1+\omega_n)^2}{m^3}.
\end{aligned}
\]
This proves the two-spine product bound \eqref{eq:two-spine}.
\end{proof}

\subsection{Proof of Lemma~\ref{lem:critical_barrier_second_moment}}

Under the assumptions \ref{hyp_A1}-\ref{hyp_A3}, with 
 \(0<\alpha<\rho\), recall that
\[
\mathcal B_h(u):=
\left\{
\mathcal G_{n,\alpha}(u),\ 
S_j(u)\le aj,\ \forall\,0\le j\le h,\ 
ah-\omega_n-1\le S_h(u)\le ah-\omega_n
\right\},
\]
and
\[
\widetilde N_h(a):=\sum_{|u|=h}\ind_{\mathcal B_h(u)}.
\]
By Remark~\ref{rem:ghost_paths_good_event}, whenever the indicator of $\mathcal G_{n,\alpha}$ is present, sums over the cemetery-extended
tree coincide with sums over genuine vertices of the original tree. We shall therefore work on the
extended tree without changing notation.
\medskip

\noindent\textbf{Step 1: first moment.}
Applying the many-to-one formula Lemma~\ref{lem:many-to-one} with
$F_h(u):= \ind_{\mathcal B_h(u)},$ 
we obtain
\[
\E[\widetilde N_h(a)]
=
\E_{\Q_t}\!\left(
\exp\!\left(
tS_h(U_h)+\sum_{\ell=0}^{h-1}\kappa_{K(U_\ell)}(t)
\right)\ind_{\mathcal B_h(U_h)}
\right).
\]
On $\mathcal B_h(U_h)$, we have
$S_h(U_h)=ah+Y_h$ and $-\omega_n-1\le Y_h\le -\omega_n,$ 
hence
\[
\mathrm{e}^{-t}\,\mathrm{e}^{tah-t\omega_n}
\le \mathrm{e}^{tS_h(U_h)}
\le \mathrm{e}^{tah-t\omega_n}.
\]
Moreover, on $\mathcal G_{n,\alpha}(U_h)$, Lemma~\ref{lem:kappa-rate} gives
\[
\sum_{\ell=0}^{h-1}\kappa_{K(U_\ell)}(t)
=
h\kappa(t)+o(1),
\]
uniformly on $\mathcal B_h(U_h)$, since $h\asymp \log n$.
Therefore,
\[
\E[\widetilde N_h(a)]
\asymp
\mathrm{e}^{h(\kappa(t)+ta)-t\omega_n}\,
\Q_t(E_h(\omega_n)).
\]
By Lemma~\ref{lem:one_spine_ballot},
$\Q_t(E_h(\omega_n)) \asymp \frac{1+\omega_n}{h^{3/2}}$; 
since $\omega_n\to\infty$, this yields in particular
\[
\E[\widetilde N_h(a)]
\ge
c\,\mathrm{e}^{h(\kappa(t)+ta)-t\omega_n}(1+\omega_n)h^{-3/2}
\]
for some $c>0$ and all large $n$.

\medskip
\noindent\textbf{Step 2: decomposition of the second moment by the MRCA.}
Write
\[
\widetilde N_h(a)^2
=
\sum_{|u|=h}\ind_{\mathcal B_h(u)}
+
\sum_{r=0}^{h-1}
\sum_{|w|=r}
\sum_{\substack{|u|=h,\ |v|=h\\ u\wedge v=w,\ u\neq v}}
\ind_{\mathcal B_h(u)}\ind_{\mathcal B_h(v)}.
\]
The first term is just $\E[\widetilde N_h(a)]$, which we will show later to be negligible compared with the desired
upper bound because $\kappa(t)+ta>0$ and $\omega_n=o(h^{1/3})$.
Fix $r\in\{0,\dots,h-1\}$ and a vertex $w$ at depth $r$. Set
\[
m:=h-r,
\qquad
L_r(w):=ar-S_r(w).
\]
Let
\[
A_r(w)
:=
\left\{
\mathcal G_{n,\alpha}(w),\ 
S_j(w)\le aj,\ \forall\,0\le j\le r
\right\}.
\]
Only vertices $w$ such that $A_r(w)$ holds can contribute to the sum above.

For such a vertex $w$, let $\mathcal C_r(w)$ denote the contribution of all pairs
$(u,v)$ with $u\wedge v=w$:
\[
\mathcal C_r(w)
:=
\sum_{\substack{|u|=h,\ |v|=h\\ u\wedge v=w,\ u\neq v}}
\ind_{\mathcal B_h(u)}\ind_{\mathcal B_h(v)}.
\]
Then
\begin{equation}
\E[\widetilde N_h(a)^2]
\le
\E[\widetilde N_h(a)]
+
\sum_{r=0}^{h-1}
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\,\mathcal C_r(w)
\right].
\label{eq:A.6.1}
\end{equation}

\medskip
\noindent\textbf{Step 3: conditional estimate below a fixed prefix.}
Fix \(r\) and \(w\) as above, and condition on the \(\sigma\)-field \(\mathcal G_r(w)\) generated by
\(\widetilde{\mathcal F}_r\) together with the full offspring configuration of \(w\).
Let
\[
p_i:=\frac{K(wi)}{K(w)-1},\qquad i=1,\dots,D(w),
\]
be the normalized child masses of \(w\), and define
\[
Z_2(w):=\sum_{x\neq y} (p_x p_y)^t.
\]
Conditionally on \(\mathcal G_r(w)\), define the ordered distinct two-spine first-step law
\(\widehat \Q^{(2)}_{w,t}\) by
\[
\widehat \Q^{(2)}_{w,t}(\xi_1=x,\xi_2=y\mid \mathcal G_r(w))
=
\frac{p_x^t p_y^t}{Z_2(w)},
\qquad x\neq y,
\]
and, given \((\xi_1,\xi_2)\), let the two continuations issued from the edges
\(w\to \xi_1\) and \(w\to \xi_2\) evolve independently according to the tilted spine law \(\Q_t\)
in the corresponding descendant subtrees. If \(D(w)\le 1\), then \(\mathcal C_r(w)=0\), and we may define \(\widehat \Q^{(2)}_{w,t}\) arbitrarily.
Hence only the case \(D(w)\ge 2\) matters.
We claim that, conditionally on \(\mathcal G_r(w)\),
\begin{equation}
\E[\mathcal C_r(w)\mid \mathcal G_r(w)]
\le
C
\mathrm{e}^{2m(\kappa(t)+ta)-2t\omega_n+o(1)}\,
\widehat \Q^{(2)}_{w,t}\!\left(
E^{(1)}_{m,\ell}\cap \mathcal G^{(1),\mathrm{cont}}_{n,\alpha},
\,
E^{(2)}_{m,\ell}\cap \mathcal G^{(2),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right),
\label{eq:A.6.2}
\end{equation}
where $m=h-r$ and $\ell=L_r(w)$.

Indeed, for each ordered pair of distinct children \((x,y)\), let \(\mathcal C_r(w;x,y)\) denote the
contribution of those ordered pairs of depth-\(h\) descendants whose first steps after \(w\) go
respectively through \(x\) and \(y\). Then
\[
\mathcal C_r(w)=\sum_{x\neq y} \mathcal C_r(w;x,y).
\]
Now we apply the same many-to-one upper bound as in Step~1 separately to the two continuations
issued from the edges \(w\to x\) and \(w\to y\). 

More precisely, for a fixed child $x$ of $w$, let $\mathcal T_x$ be the descendant subtree issued from the edge
$w\to x$, and let $S^{(x)}_j$ be the continuation displacement along a path in $\mathcal T_x$,
counted from generation $r$ onward, so that the first increment corresponds to the split step
$w\to x$. By the one-spine many-to-one formula applied in the subtree $\mathcal T_x$ and
conditioning on the first step, we have for any nonnegative functional $F_x$,
\[
\mathbb E\!\left[\sum_{u\succ x,\ |u|=h} F_x(u)\,\middle|\,\mathcal G_r(w)\right]
=
(p_x)^t\,
\E_{\Q_{t,x}}\!\left[
\exp\!\left(
tS^{(x)}_m+\sum_{j=1}^{m-1}\kappa_{K_j}(t)
\right)
F_x(U^{(x)}_m)
\,\middle|\,\mathcal G_r(w)\right].
\]
Taking
\[
F_x(u)=\ind_{\{E^{(x)}_{m,\ell}(u)\cap \mathcal G^{(x),\mathrm{cont}}_{n,\alpha}(u)\}},
\]
together with the same estimation in Step 1,
we obtain
\begin{align*}
&\mathbb E\!\left[\sum_{u\succ x,\ |u|=h}
\ind_{\{E^{(x)}_{m,\ell}(u)\cap \mathcal G^{(x),\mathrm{cont}}_{n,\alpha}(u)\}}
\,\middle|\,\mathcal G_r(w)\right] \\
&\le
C \mathrm{e}^{(m-1)(\kappa(t)+ta)-t\omega_n+o(1)}
p_x^t
\Q_{t,x}\!\left(E^{(x)}_{m,\ell}\cap \mathcal G^{(x),\mathrm{cont}}_{n,\alpha}\,\middle|\,\mathcal G_r(w)\right).
\end{align*}
Applying this bound independently to the two descendant subtrees issued from $x$ and $y$ gives
\begin{align*}
&\E[\mathcal C_r(w;x,y)\mid \mathcal G_r(w)]\\
&\le
C\mathrm{e}^{2(m-1)(\kappa(t)+ta)-2t\omega_n+o(1)}\,p_x^t p_y^t
\Q_{t,x,y}\!\left(
E^{(1)}_{m,\ell}\cap \mathcal G^{(1),\mathrm{cont}}_{n,\alpha},
\,
E^{(2)}_{m,\ell}\cap \mathcal G^{(2),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right).
\end{align*}
Summing over \(x\neq y\) gives
\begin{align*}
&\E[\mathcal C_r(w)\mid \mathcal G_r(w)]\\
&\le
C\mathrm{e}^{2(m-1)(\kappa(t)+ta)-2t\omega_n+o(1)}\,Z_2(w)\,
\widehat \Q^{(2)}_{w,t}\!\left(
E^{(1)}_{m,\ell}\cap \mathcal G^{(1),\mathrm{cont}}_{n,\alpha},
\,
E^{(2)}_{m,\ell}\cap \mathcal G^{(2),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right).
\end{align*}
Finally, since
\[
Z_2(w)\le \left(\sum_i (p_i)^t\right)^2 \le 1
\]
after absorbing $\mathrm{e}^{-2\kappa(t)}$ into $C$, we obtain \eqref{eq:A.6.2}.
By construction of the ordered distinct two-spine change of measure at the split,
conditionally on $\mathcal G_r(w)$, the law $\widehat \Q^{(2)}_{w,t}$ first chooses
an ordered pair of distinct children $(\xi_1,\xi_2)$ of $w$ with probability
proportional to $p_{\xi_1}^t p_{\xi_2}^t$, and then evolves independently below
$\xi_1$ and $\xi_2$ according to the one-spine tilted law $\Q_t$ in the corresponding
subtrees. Hence $\widehat \Q^{(2)}_{w,t}$ is exactly the conditional law appearing
in Lemma~\ref{lem:two-spine-bound}(ii), and therefore Lemma~\ref{lem:two-spine-bound}(ii) applies:
\[
\widehat \Q^{(2)}_{w,t}\!\left(
E^{(1)}_{m,\ell}\cap \mathcal G^{(1),\mathrm{cont}}_{n,\alpha},
\,
E^{(2)}_{m,\ell}\cap \mathcal G^{(2),\mathrm{cont}}_{n,\alpha}
\ \middle|\ \mathcal G_r(w)
\right)
\le
C\,\frac{(1+\ell)^2(1+\omega_n)^2}{m^3}.
\]
Substituting this into \eqref{eq:A.6.2}, we obtain
\[
\E[\mathcal C_r(w)\mid \mathcal G_r(w)]
\le
C
\mathrm{e}^{2m(\kappa(t)+ta)-2t\omega_n+o(1)}
\frac{(1+L_r(w))^2(1+\omega_n)^2}{m^3}
\]
on that range. So,
\begin{align}
&\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m\ge (\omega_n)^3\}}
\ind_{\{L_r(w)\le (\omega_n)^{-1}\sqrt m\}}\,\mathcal C_r(w)
\right] \nonumber \\ 
&\le
C\mathrm{e}^{2m(\kappa(t)+ta)-2t\omega_n+o(1)}
\frac{(1+\omega_n)^2}{m^3} \, \E\!\left[
\sum_{|w|=r}\ind_{A_r(w)} \ind_{\{L_r(w)\le (\omega_n)^{-1}\sqrt m\}}(1+L_r(w))^2
\right].
\label{eq:A.6.3}
\end{align}
The bound obtained in Step~3 via Lemma~\ref{lem:two-spine-bound}(ii) will only be used on the range where
\[
m=h-r\ge (\omega_n)^3
\qquad\text{and}\qquad
L_r(w)\le (\omega_n)^{-1} \sqrt m .
\]
On this range,
\[
L_r(w)+\omega_n \le (\omega_n)^{-1} \sqrt m+\omega_n=o(\sqrt m)
\]
uniformly, since \(m\ge (\omega_n)^3\) implies \(\omega_n=o(\sqrt m)\), and \(r\le h\asymp \log n\).
All remaining cases will be treated separately by crude bounds.
Thus, we now split the second-moment contribution according to the remaining length $m=h-r$:
\begin{itemize}
    \item  
\emph{large remaining length:} \(m\ge (\omega_n)^3\). In this regime we shall use
Lemma~\ref{lem:two-spine-bound}(ii), but only for prefixes satisfying \(L_r(w)\le (\omega_n)^{-1} \sqrt m\).
\item 
\emph{short remaining length:} \(m<(\omega_n)^3\). In this regime we do not use
Lemma~\ref{lem:two-spine-bound}(ii); instead we use only crude continuation bounds. Since there are at most
\((\omega_n)^3\) such split levels, their total contribution will be negligible after summation over \(r\).
 \end{itemize}

\noindent\textbf{Step 4: a prefix-window estimate.}
We now control the expectation on the right-hand side of \eqref{eq:A.6.3} by splitting according to whether
\[
L_r(w)\le \min(\sqrt r,(\omega_n)^{-1}\sqrt m)
\quad\text{or}\quad
\sqrt r< L_r(w)\le (\omega_n)^{-1}\sqrt m.
\]
For $q\ge0$, define the prefix window
$I_q:=[q,q+1).$ 
Indeed, on the window $\{L_r(w)\in I_q\}$ we have
\[
S_r(w)=ar-L_r(w),
\qquad
\mathrm{e}^{tS_r(w)}=\mathrm{e}^{tar}\mathrm{e}^{-tL_r(w)}\in
\left[\mathrm{e}^{tar-t(q+1)},\,\mathrm{e}^{tar-tq}\right].
\]
Thus the factor $\mathrm{e}^{-tq}$ appears up to a multiplicative constant $\mathrm{e}^t$, which is absorbed into $C$. Using the same many-to-one identity as in Step~1, for every $q\ge0$,
\begin{align}
&\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{L_r(w)\in I_q\}}
\right] \nonumber \\
&\le
C\,\mathrm{e}^{r(\kappa(t)+ta)-tq+o(1)} \, \Q_t\left(
\mathcal G_{n,\alpha}(U_r),\ Y_j\le0,\ \forall\,0\le j\le r,\ -q-1\le Y_r\le -q
\right).
\end{align}

\begin{itemize}
    \item  
We first estimate the  part corresponding to
$q\le \min(\sqrt r,(\omega_n)^{-1}\sqrt m).$ 
Using the equation above, we obtain
\begin{align*}
    &\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}  \ind_{\{L_r(w)\le \min(\sqrt r,(\omega_n)^{-1}\sqrt m)\}}(1+L_r(w))^2
\right] \\
    &\le
C  \mathrm{e}^{r(\kappa(t)+ta)+o(1)} \\ 
    &\quad \times \sum_{0\le q\le \min(\sqrt r,(\omega_n)^{-1}\sqrt m)} \mathrm{e}^{-tq}(1+q)^2
\Q_t\left(
\mathcal G_{n,\alpha}(U_r),\ Y_j\le0,\ \forall\,0\le j\le r,\ -q-1\le Y_r\le -q
\right).
\end{align*}
By the same one-spine ballot estimate as in Lemma~\ref{lem:one_spine_ballot},
\[
\Q_t\left(
\mathcal G_{n,\alpha}(U_r),\ Y_j\le0,\ \forall\,0\le j\le r,\ -q-1\le Y_r\le -q
\right)
\le
C\,\frac{1+q}{(1+r)^{3/2}}
\]
uniformly for $0\le q\le \min(\sqrt r,(\omega_n)^{-1}\sqrt m)$. After this estimate, we can calculate the sum $ \sum_{0\le q\le \sqrt r}$ to obtain an upper bound. Hence
\begin{equation*}
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{L_r(w)\le \min(\sqrt r,(\omega_n)^{-1}\sqrt m)\}}(1+L_r(w))^2
\right]
\le
C \mathrm{e}^{r(\kappa(t)+ta)+o(1)}(1+r)^{-3/2}.
\end{equation*}

\item For the intermediate range
$\sqrt r< L_r(w)\le (\omega_n)^{-1}\sqrt m,$ 
we use only the trivial bound
\[
\Q_t\left(
\mathcal G_{n,\alpha}(U_r),\ Y_j\le0,\ \forall\,0\le j\le r,\ -q-1\le Y_r\le -q
\right)\le 1.
\]
Hence
\begin{align*}
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}
\ind_{\{\sqrt r< L_r(w)\le (\omega_n)^{-1}\sqrt m\}}
(1+L_r(w))^2
\right]
&\le
C \mathrm{e}^{r(\kappa(t)+ta)+o(1)}
\sum_{\sqrt r<q\le (\omega_n)^{-1}\sqrt m} \mathrm{e}^{-tq}(1+q)^2 \\
&\le
C \mathrm{e}^{r(\kappa(t)+ta)+o(1)} \mathrm{e}^{-c\sqrt r}.
\end{align*}
 \end{itemize}
Combining these two cases,
\begin{equation}
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{L_r(w)\le (\omega_n)^{-1}\sqrt m\}}(1+L_r(w))^2
\right]
\le
C \mathrm{e}^{r(\kappa(t)+ta)+o(1)}(1+r)^{-3/2}.
\label{eq:A.6.5}
\end{equation}

\medskip
\noindent\textbf{Step 5: summation over the split level.}
We first handle the main range
\[
m\ge (\omega_n)^3
\qquad\text{and}\qquad
L_r(w)\le (\omega_n)^{-1}\sqrt m,
\]
for which \eqref{eq:A.6.3} and \eqref{eq:A.6.5} apply. The complementary contribution, namely
\[
m<(\omega_n)^3
\qquad\text{or}\qquad
L_r(w)> (\omega_n)^{-1}\sqrt m,
\]
will be estimated by crude bounds and shown to be negligible.
\begin{itemize}
    \item  

Substituting \eqref{eq:A.6.5} into \eqref{eq:A.6.3} yields
\begin{align*}
&\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m\ge (\omega_n)^3\}}
\ind_{\{L_r(w)\le (\omega_n)^{-1} \sqrt m\}}\,\mathcal C_r(w)
\right]\\
&\le
C\,\mathrm{e}^{2(h-r)(\kappa(t)+ta)-2t\omega_n+o(1)} \,
\frac{(1+\omega_n)^2}{(h-r)^3}
\,
\mathrm{e}^{r(\kappa(t)+ta)}\,(1 + r)^{-3/2}.
\end{align*}
Equivalently,
\begin{align}
&\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m\ge (\omega_n)^3\}}
\ind_{\{L_r(w)\le (\omega_n)^{-1} \sqrt m\}}\,\mathcal C_r(w)
\right] \nonumber \\ 
&\le
C\,
\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n+o(1)}
\,
\mathrm{e}^{-r(\kappa(t)+ta)} \,
\frac{(1+\omega_n)^2}{(h-r)^3\,(1+r)^{3/2}}.
\label{eq:A.6.7}
\end{align}\smallskip

\item 
For the regime \(m<(\omega_n)^3\), we use only the crude bound
$\mathcal C_r(w)\le \left(\#\{u:|u|=h,\ u\succ w\}\right)^2.$ 
Applying the same many-to-one upper bound as above, but without any ballot factor, yields
\[
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m<(\omega_n)^3\}}\,\mathcal C_r(w)
\right]
\le
C 
\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n+o(1)}
\mathrm{e}^{-r(\kappa(t)+ta)}.
\]
Since \(m<(\omega_n)^3\) means \(r>h-(\omega_n)^3\), summing over this range gives
\[
\sum_{h-(\omega_n)^3<r\le h-1}
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m<(\omega_n)^3\}}\,\mathcal C_r(w)
\right]
\le
C 
\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n+o(1)}
\mathrm{e}^{-\lambda(h-(\omega_n)^3)},
\]
where \(\lambda:=\kappa(t)+ta>0\). This is negligible compared with
\(\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n}h^{-3}\), because \(\mathrm{e}^{-\lambda h}\)
dominates any polylogarithmic factor. Indeed, relative to the target second-moment scale
$\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n}h^{-3},$ 
the above contribution is bounded by
$h^3\,\mathrm{e}^{-\lambda(h-(\omega_n)^3)}.$ 
Since \((\omega_n)^3=o(h)\), we have
$\mathrm{e}^{-\lambda(h-(\omega_n)^3)}=\mathrm{e}^{-\lambda h+o(h)},$ 
and therefore
$h^3\,\mathrm{e}^{-\lambda(h-(\omega_n)^3)}\to 0.$ 
Hence this contribution is negligible.
\smallskip 

\item   
For the complementary regime
\[
L_r(w)>(\omega_n)^{-1}\sqrt m,
\]
still within \(m\ge (\omega_n)^3\), we use only a crude
continuation bound: for each ordered pair of distinct children below \(w\), the corresponding pair
contribution is bounded by
\[
C  \mathrm{e}^{2m(\kappa(t)+ta)-2t\omega_n+o(1)}.
\]
Therefore
\begin{align*}
&\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m\ge (\omega_n)^3\}}
\ind_{\{L_r(w)>(\omega_n)^{-1}\sqrt m\}}\, \mathcal C_r(w)
\right] \nonumber \\ 
&
\le \mathrm{e}^{2m(\kappa(t)+ta)-2t\omega_n+o(1)} \, \E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{L_r(w)>(\omega_n)^{-1}\sqrt m\}}
\right].
\end{align*}
By the prefix-window estimate and the trivial bound
\[
\Q_t\left(
\mathcal G_{n,\alpha}(U_r),\ Y_j\le 0,\ \forall\,0\le j\le r,\ -q-1\le Y_r\le -q
\right)\le 1,
\]
we have for some \(c=c(t)>0\)
\begin{align*} 
&\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{L_r(w)>(\omega_n)^{-1}\sqrt m\}}
\right] \\ 
&\le
C \mathrm{e}^{r(\kappa(t)+ta)+o(1)}
\sum_{q>(\omega_n)^{-1}\sqrt m} \mathrm{e}^{-tq}
\le
C \mathrm{e}^{r(\kappa(t)+ta)+o(1)} \mathrm{e}^{-c\,(\omega_n)^{-1}\sqrt m} \\ 
& 
\E\!\left[
\sum_{|w|=r}\ind_{A_r(w)}\ind_{\{m\ge (\omega_n)^3\}}
\ind_{\{L_r(w)>(\omega_n)^{-1}\sqrt m\}}\, C_r(w)
\right] \\ 
&\le
C  \mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n+o(1)}
\mathrm{e}^{-r(\kappa(t)+ta) -c\,(\omega_n)^{-1}\sqrt m}.
\end{align*}
Since \(m\ge (\omega_n)^3\), we have
\[
(\omega_n)^{-1}\sqrt m \ge (\omega_n)^{1/2}\to\infty,
\]
so this contribution is negligible after summation over \(r\). More precisely, split the sum over \(r\) into \(r\le h/2\)
and \(r>h/2\). If \(r\le h/2\), then \(m=h-r\ge h/2\), and hence
\[
\mathrm e^{-c(\omega_n)^{-1}\sqrt m}
\le
\mathrm e^{-c'\sqrt h/\omega_n}
=o(h^{-A})
\]
for every fixed \(A>0\), since \(\omega_n=o(h^{1/3})\). If \(r>h/2\), then
\[
\mathrm e^{-r(\kappa(t)+ta)}\le \mathrm e^{-c''h},
\]
because \(\kappa(t)+ta>0\). Thus the whole large-slack contribution is
\(o\bigl(\mathrm e^{2h(\kappa(t)+ta)-2t\omega_n}h^{-3}\bigr)\).

 \end{itemize}
Collecting all the estimates, 
we conclude that the latter two are negligible, and the main contribution is bounded by the sum of
the right-hand side of \eqref{eq:A.6.7} over \(0\le r\le h-1\).

Since
$\lambda:=\kappa(t)+ta>0,$ 
the factor $\mathrm{e}^{-r\lambda}$ is summable in $r$. Moreover,
\[
\sum_{r=0}^{h-1} \mathrm{e}^{-r\lambda}\frac{1}{(h-r)^3(1+r)^{3/2}}
=
\sum_{0\le r\le h/2} \mathrm{e}^{-r\lambda}\frac{1}{(h-r)^3(1+r)^{3/2}}
+
\sum_{h/2<r\le h-1} \mathrm{e}^{-r\lambda}\frac{1}{(h-r)^3(1+r)^{3/2}}.
\]
On the first range, $h-r\asymp h$, hence
\[
\sum_{0\le r\le h/2} \mathrm{e}^{-r\lambda}\frac{1}{(h-r)^3(1+r)^{3/2}}
\le
C h^{-3}\sum_{r\ge0} \mathrm{e}^{-r\lambda}(1+r)^{-3/2}
\le
C h^{-3}.
\]
On the second range, we use $(1+r)^{-3/2}\le C h^{-3/2}$ and the exponential decay of
$\mathrm{e}^{-r\lambda}$ to get
\[
\sum_{h/2<r\le h-1} \mathrm{e}^{-r\lambda}\frac{1}{(h-r)^3(1+r)^{3/2}}
\le
C h^{-3/2}\mathrm{e}^{-\lambda h/2}\sum_{s=1}^{h} s^{-3}
\le
C h^{-3}.
\]
Therefore
\begin{equation}
\sum_{r=0}^{h-1} \mathrm{e}^{-r\lambda}\frac{1}{(h-r)^3(1+r)^{3/2}}
\le
C h^{-3}.
\label{eq:A.6.8}
\end{equation}
Combining \eqref{eq:A.6.1}, \eqref{eq:A.6.7}, and \eqref{eq:A.6.8}, we conclude that
\[
\E[\widetilde N_h(a)^2]
\le
\E[\widetilde N_h(a)]
+
C\,\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n+o(1)}\,h^{-3}(1+\omega_n)^2.
\]
Moreover, the first-moment term is negligible with respect to the second-order bound, since
\[
\frac{
\mathrm{e}^{h(\kappa(t)+ta)-t\omega_n}(1+\omega_n)h^{-3/2}
}{
\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n}(1+\omega_n)^2h^{-3}
}
=
\mathrm{e}^{-h(\kappa(t)+ta)+t\omega_n}h^{3/2}(1+\omega_n)^{-1}\longrightarrow 0,
\]
because $\kappa(t)+ta>0$ and $\omega_n=o(h)$. So, 
$\E[\widetilde N_h(a)^2] \le
C\,\mathrm{e}^{2h(\kappa(t)+ta)-2t\omega_n}(1+\omega_n)^2h^{-3 },$ 
and this completes the proof.



\bigskip





\bibliographystyle{alpha}
\bibliography{Mybib}


\end{document}
