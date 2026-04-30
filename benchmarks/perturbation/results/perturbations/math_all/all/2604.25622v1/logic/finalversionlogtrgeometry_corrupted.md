
\documentclass[11pt]{article}
% \makeatletter
% \renewcommand\normalsize{%
%     \@setfontsize\normalsize{11.7}{14pt plus .3pt minus .3pt}%
%     \abovedisplayskip 10\p@ \@plus4\p@ \@minus4\p@
%     \abovedisplayshortskip 6\p@ \@plus2\p@
%     \belowdisplayshortskip 6\p@ \@plus2\p@
%     \belowdisplayskip \abovedisplayskip}
% \renewcommand\small{%
%     \@setfontsize\small{9.5}{12\p@ plus .2\p@ minus .2\p@}%
%     \abovedisplayskip 8.5\p@ \@plus4\p@ \@minus1\p@
%     \belowdisplayskip \abovedisplayskip
%     \abovedisplayshortskip \abovedisplayskip
%     \belowdisplayshortskip \abovedisplayskip}
% \renewcommand\footnotesize{%
%     \@setfontsize\footnotesize{8.5}{9.25\p@ plus .1pt minus .1pt}%%
%     \abovedisplayskip 6\p@ \@plus4\p@ \@minus1\p@
%     \belowdisplayskip \abovedisplayskip
%     \abovedisplayshortskip \abovedisplayskip
%     \belowdisplayshortskip \abovedisplayskip}
% % ********************* DIMENSIONS:
% % TEXT DIMENSIONS
%  \setlength\parindent    {30\p@}
%  \setlength\textwidth    {412\p@}
%  \setlength\textheight   {570\p@}
%  % PAPER AND TRIM SIZE
%  \paperwidth=210mm
%  \paperheight=260mm
%  \ifdefined\pdfpagewidth
%  \setlength{\pdfpagewidth}{\paperwidth}
%  \setlength{\pdfpageheight}{\paperheight}
%  \else
%  \setlength{\pagewidth}{\paperwidth}
%  \setlength{\pageheight}{\paperheight}
%  \fi

\usepackage[utf8]{inputenc}
\usepackage{authblk}

\usepackage{amsfonts,amsmath,amssymb,mathtools,amsthm}
\usepackage{graphicx}
\usepackage{stmaryrd}
%\usepackage[notref,notcite]{showkeys}
\usepackage{thmtools}
\DeclareGraphicsExtensions{.eps}
\usepackage{float}
\usepackage{comment}

\usepackage{xcolor}
\definecolor{linkcolour}{rgb}{0.15,0.15,0.55}
\definecolor{urlcolour}{rgb}{0.15,0.15,0.55}
\definecolor{citecolour}{rgb}{0.15,0.15,0.55}


\usepackage[linktoc=all,backref=page]{hyperref}
	\hypersetup{
		colorlinks = true,
		linkcolor = linkcolour,
		urlcolor = citecolour,
		citecolor = citecolour,
		linktoc = all,
		hypertexnames = false,
		unicode = true,
		bookmarksnumbered = false,
		pdfmenubar = true,
		pdftoolbar = true}

\usepackage[textsize=footnotesize]{todonotes}

\usepackage
	[top=2.5cm,
	bottom=2.5cm,
	left=2.5cm,
	right=2.5cm,
	a4paper]
	{geometry}
		\usepackage[margin=2cm]{caption}
	%--------------------------macros-------------------------
\renewcommand{\theequation}{\thesection.\arabic{equation}}
\newcommand{\newsection}{
\setcounter{equation}{0}
\section}

\newcommand\encadremath[1]{\vbox{\hrule\hbox{\vrule\kern8pt
\vbox{\kern8pt \hbox{$\displaystyle #1$}\kern8pt}
\kern8pt\vrule}\hrule}}
\def\enca#1{\vbox{\hrule\hbox{
\vrule\kern8pt\vbox{\kern8pt \hbox{$\displaystyle #1$}
\kern8pt} \kern8pt\vrule}\hrule}}


\newcommand{\dfn}[1]{\textit{\textbf{#1}}}
\newcommand*{\coleq}{\mathrel{\mathop:}=}
% real part
\renewcommand{\Re}{\operatorname{Re}}
% imaginary part
\renewcommand{\Im}{\operatorname{Im}}


\newcommand\framefig[1]{
\begin{figure}[bth]
\hrule\hbox{\vrule\kern8pt
\vbox{\kern8pt \vbox{
\begin{center}
{#1}
\end{center}
}\kern8pt}
\kern8pt\vrule}\hrule
\end{figure}
}

\newcommand\figureframex[3]{
\begin{figure}[bth]
\hrule\hbox{\vrule\kern8pt
\vbox{\kern8pt \vbox{
\begin{center}
{\mbox{\epsfxsize=#1.truecm\epsfbox{#2}}}
\end{center}
\caption{#3}
}\kern8pt}
\kern8pt\vrule}\hrule
\end{figure}
}
%
\newcommand\figureframey[3]{
\begin{figure}[bth]
\hrule\hbox{\vrule\kern8pt
\vbox{\kern8pt \vbox{
\begin{center}
{\mbox{\epsfysize=#1.truecm\epsfbox{#2}}}
\end{center}
\caption{#3}
}\kern8pt}
\kern8pt\vrule}\hrule
\end{figure}
}
 \makeatother

% % 
 \usepackage{mathdots}
 \usepackage{xcolor}
 \usepackage{amsfonts,amsmath,amssymb,mathtools,amsthm}
 \usepackage{graphicx}
 \usepackage{stmaryrd}
 %\usepackage[notref,notcite]{showkeys}
 \usepackage{thmtools}
 \DeclareGraphicsExtensions{.eps}
\usepackage{hyperref}



\newcommand{\rmkBE}[1]{{\color{orange}{(BE) #1}}}
\newcommand{\rmkEGF}[1]{{\color{purple}{(EGF) #1}}}
\newcommand{\rmkNO}[1]{\textcolor{red}{(NO) #1}}
\newcommand{\rmkOM}[1]{\textcolor{blue}{(OM) #1}}

\renewcommand{\thesection}{\arabic{section}}
\renewcommand{\theequation}{\arabic{section}-\arabic{equation}}
\makeatletter
\@addtoreset{equation}{section}
\makeatother
\newtheorem{theorem}{Theorem}[section]
\newtheorem{conjecture}{Conjecture}[section]

\newtheorem{proposition}{Proposition}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{corollary}{Corollary}[section]

%\newtheorem{proof}{Proof:}

\theoremstyle{definition}
\newtheorem{remark}{Remark}[section]
\newtheorem{definition}{Definition}[section]

\def\br{\begin{remark}\rm\small}
\def\er{\end{remark}}
\def\bt{\begin{theorem}}
\def\et{\end{theorem}}
\def\bd{\begin{definition}}
\def\ed{\end{definition}}
\def\bp{\begin{proposition}}
\def\ep{\end{proposition}}
\def\bl{\begin{lemma}}
\def\el{\end{lemma}}
\def\bc{\begin{corollary}}
\def\ec{\end{corollary}}
\def\beaq{\begin{eqnarray}}
\def\eeaq{\end{eqnarray}}

\theoremstyle{definition}
\newtheorem{example}{Example}[section]

\newcommand{\td}{\tilde}
\newcommand{\rf}[1]{(\ref{#1})}
\newcommand{\eq}[1]{eq.~(\ref{#1})}
\newcommand{\rfig}[1]{fig.~\ref{#1}}

\newcommand{\equ}[2]{\begin{equation}{\label{#1}}{#2}\end{equation}}

\newcommand{\be}{\begin{equation}}
\newcommand{\ee}{\end{equation}}
\newcommand{\beq}{\begin{equation}}
\newcommand{\eeq}{\end{equation}}
\newcommand{\bea}{\begin{eqnarray}}
\newcommand{\eea}{\end{eqnarray}}
\newcommand{\beqq}{\begin{equation*}}
\newcommand{\eeqq}{\end{equation*}}
\newcommand{\beaa}{\begin{eqnarray*}}
\newcommand{\eeaa}{\end{eqnarray*}}

\newcommand\eol{\hspace*{\fill}\linebreak}
\newcommand\eop{\vspace*{\fill}\pagebreak}

\newcommand{\Tr}{{\operatorname {Tr}}}
\newcommand{\tr}{{\operatorname {tr}}\,}
\newcommand{\e}{{\rm e}}
\newcommand{\ii}{{\rm i}\,}

\newcommand{\CC}{{\mathbb C}}
\newcommand{\RR}{{\mathbb R}}
\newcommand{\ZZ}{{\mathbb Z}}


\newcommand{\Tau}{{\cal T}}
\newcommand{\W}{{\cal W}}
\newcommand{\spcurve}{{\cal S}}

\newcommand{\SP}{{\mathbf{Sp}}}

\newcommand{\adj}{{\text{adj }}}
\newcommand{\curve}{{\Sigma}}
\newcommand{\curveuniv}{{\tilde\Sigma}}
\newcommand{\curverond}{\curve^{\circ}}
\newcommand{\genus}{{\overline{ g}}}
\newcommand{\genusrond}{\overset{\circ}{\genus}}
\newcommand{\xirond}{\overset{\circ}{\xi}}
\newcommand{\acycle}{{\cal A}}
\newcommand{\bcycle}{{\cal B}}
\newcommand{\acyclerond}{\overset{\circ}{\acycle}}
\newcommand{\bcyclerond}{\overset{\circ}{\bcycle}}

\renewcommand{\W}{{\mathfrak W}}


\newcommand{\omegarond}{\overset{\circ}{\omega}}
\newcommand{\Brond}{\overset{\circ}{B}}
\newcommand{\Erond}{\overset{\circ}{E}}
\newcommand{\Srond}{\overset{\circ}{S}}
\newcommand{\nurond}{\overset{\circ}{\nu}}
\newcommand{\modsp}{{\mathcal M}}
\newcommand{\modspmero}[1]{\modsp_{{#1}+\text{mero}}}
\newcommand{\bfalpha}{{\mathbf\alpha}}
\newtheorem{assumption}{Assumption}
\newcommand{\Res}{\mathop{\,\rm Res\,}}

\newcommand{\sheet}[2]{\overset{{#2}}{#1}}

\newcommand{\mbf}{\mathbf}

\newcommand{\hs}{\hspace{0.7cm}}
\newcommand{\vs}{\vspace{0.7cm}}

\newcommand{\otimessym}{{\overset{\text{sym}}{\otimes} }}

\newcommand{\diag}{{\operatorname{diag}}}
\newcommand{\Lieg}{{\mathfrak g}}
\newcommand{\Lieh}{{\mathfrak h}}
\newcommand{\LieU}{{\mathfrak U}}
\newcommand{\weyl}{{\mathfrak w}}
\newcommand{\Ker}{{\rm Ker\ }}
\newcommand{\Img}{{\rm Im\ }}
\newcommand{\Adj}{\operatorname{Adj}}
\newcommand{\slr}{\mathfrak{sl}_r}
\newcommand{\om}{\omega}
\newcommand{\HRule}{%
	\bigskip
	\begin{center}
		\rule{0.2\linewidth}{0.2mm}
			\hspace{0.5cm} $\ast\ast\ast$ \hspace{0.5cm}
		\rule{0.2\linewidth}{0.2mm}
	\end{center}
	\bigskip}


\newcommand{\bbracket}[1]{\llbracket #1 \rrbracket}
\newcommand{\bbbracket}[1]{\llbracket\mkern-5mu\llbracket #1 \rrbracket\mkern-5mu\rrbracket}


\newcommand\blfootnote[1]{%
  \begingroup
  \renewcommand\thefootnote{}\footnote{#1}%
  \addtocounter{footnote}{-1}%
  \endgroup
}

%----------------------------------------------------
% Liaisons
%

%----------------------------------------------------
% Abbreviations
%----------------------------------formattage-------------
%
%---------------------------------------------------------



\title{\bf{Hamiltonian representation of isomonodromic deformations of general rational connections on $\mathfrak{gl}_2(\mathbb{C})$}}



\date{\vspace{-5ex}}
 
\author{$_{1}$Alexander Hock\footnote{Universit\'e de Gen\`eve, Section de math\'ematiques, 24 rue du G\'en\'eral Dufour, 1211 Gen\`eve 4, Suisse}\,\,,
$_{2}$Olivier Marchal\footnote{Universit\'{e} Jean Monnet Saint-\'{E}tienne, CNRS, Institut Camille Jordan UMR 5208, Institut Universitaire de France, F-42023, Saint-\'{E}tienne, France}\,\,,
$_{3}$Nicolas Orantin%\footnote{Universit\'e de Gen\`eve, Section de math\'ematiques, 24 rue du G\'en\'eral Dufour, 1211 Gen\`eve 4, Suisse} \,\,,}
}

\begin{document}

%\maketitle
\begin{center}
\huge{Geometry of Logarithmic Topological Recursion: Dilaton Equations, Free Energies and Variational Formulas}
\end{center}
\vspace{0.5cm}
\begin{center}
$_{1}$Alexander Hock\footnote{Universit\'{e} de Gen\`{e}ve, Section de math\'{e}matiques, 24 rue du G\'{e}n\'{e}ral Dufour, 1211 Gen\`{e}ve 4, Suisse}\,\,,
$_{2}$Olivier Marchal\footnote{Universit\'{e} Jean Monnet Saint-\'{E}tienne, CNRS, Institut Camille Jordan UMR 5208, Institut Universitaire de France, F-42023, Saint-\'{E}tienne, France}\,\,,
$_{3}$Nicolas Orantin%\footnote{Universit\'e de Gen\`eve, Section de math\'ematiques, 24 rue du G\'en\'eral Dufour, 1211 Gen\`eve 4, Suisse} \,\,,
\end{center}

\vspace{1.0cm}


%\begin{abstract}
\textbf{Abstract}:
One of the most important applications of topological recursion concerns spectral curves for which the functions $(x,y)$ defining the spectral curve are allowed to have logarithmic singularities. This occurs for instance for Seiberg-Witten curves and mirror curves computing Gromov--Witten invariants of toric Calabi--Yau threefolds. A recently introduced extension of topological recursion, the so-called logarithmic topological recursion, exhibits the correct behavior under certain limits of those spectral curves. 

In this article, we derive the dilaton equations in the setting of logarithmic topological recursion, as well as variational formulas, and provide a definition of the free energies in situations where standard topological recursion was known to fail. We present examples in which the new definition of the free energies \textit{directly} (without any computation) reproduces the full perturbative part of the Nekrasov--Shatashvili partition function of 4d $\mathcal{N}=2$ pure supersymmetric gauge theory, as well as the all-genus free energies of mirror curves of strip geometries, including in particular the topological vertex and the resolved conifold. 

\blfootnote{\textit{Email Addresses:}$_{1}$\textsf{alexander.hock@unige.ch}, $_{2}$\textsf{olivier.marchal@univ-st-etienne.fr}, $_{3}$\textsf{nicolas.orantin@gmail.com}}
%\end{abstract}

\tableofcontents

\newpage

\section{Introduction}
\subsection{From Topological Recursion to Logarithmic Topological Recursion}
The topological recursion (TR) \cite{EO07} is a universal recursive procedure which defines an infinite family of symmetric multi-differentials $\omega_{h,n}^{\text{EO}}$ on $n$ copies of a Riemann surface $\Sigma$. The importance of TR lies in its wide range of applications. One of the simplest, yet most important, applications is the computation of intersection numbers on $\overline{\mathcal{M}}_{g,n}$, the moduli space of complex curves, for instance in relation to Witten's conjecture \cite{Witten}, proved by Kontsevich \cite{Kontsevich}. Other examples include Hurwitz theory \cite{Bouchard:2007hi}, Weil--Petersson volumes of the bordered moduli space \cite{Mirzakhani,EOMirzakhani}, and computations of Gromov--Witten invariants for toric Calabi--Yau threefolds \cite{BKMP,Eynard:2012nj,Fang:2013dna}. As one can see, the range of applications is very broad, and the few examples mentioned above are just the tip of the iceberg, since this list is far from complete. 

Since the original definition of TR \cite{EO07}, several extensions have been introduced, relaxing some of the initial assumptions. One example is the extension to higher order topological recursion \cite{BouchardEynard,HigherRam}, which allows for higher order ramification points, originally assumed to be simple. The correct way to define such an extension comes from the requirement that taking limits of several coalescing simple ramification points should yield the more general higher order TR. This extension has applications in the computation of spin intersection numbers on $\overline{\mathcal{M}}_{g,n}$ \cite{Wittenrspin}.

As mentioned above, another important application of TR is the computation of Gromov--Witten invariants of toric Calabi--Yau threefolds, where the spectral curve corresponds to the mirror curve. One important assumption necessary for applying TR to mirror curves is the so-called framing parameter, which must be chosen to be generic. Indeed, it was observed that taking singular limits of mirror curves leads to spectral curves where TR fails to be applicable \cite{Bouchard:2011ya}. The problem lies in the fact that mirror curves are spectral curves in $\mathbb{C}^*\times \mathbb{C}^*$, where some assumptions of the original definition of TR are violated, but are nevertheless effectively restored by choosing a generic framing parameter. 

More recently, a new extension of TR was introduced that precisely resolves this problem of taking singular limits of mirror curves. This extension is called \textit{logarithmic topological recursion} (LogTR) \cite{Alexandrov:2023tgl}. The remarkable observation that LogTR commutes with the singular limit of mirror curves was, in fact, not the original motivation for its definition. 

The origin of LogTR comes from a completely different direction related to a newly understood duality in the theory of TR. The so-called $x$-$y$ duality \cite{Alexandrov:2022ydc,Hock:2022wer,Hock:2022pbw} relates two infinite families of correlators defined on the same spectral curve, but projected either via $x$ or $y$. This duality is as universal as TR itself and has already reproduced many important explicit results in various enumerative problems \cite{Hock:2023qii,Hock:2025wlm,Alexandrov:2023oov}. 

However, the universal $x$-$y$ duality was observed to fail precisely in cases where TR does not reproduce the correct enumerative invariants \cite{Hock:2023dno}. This led to the proposal of an extension of TR obtained by enforcing the validity of the $x$-$y$ duality. This was the origin of the definition of LogTR. It was only later realized that this definition also resolves the problem of singular limits in mirror curves. 

Therefore, the understanding of the $x$-$y$ duality has reshaped our perspective on topological recursion and has led to new equivalent global definitions of TR \cite{Alexandrov:2024tjo}, which are, however, beyond the scope of this article. We only mention that this new viewpoint has also provided a deeper understanding of integrable systems and has shown that TR generally gives rise to KP integrability \cite{Alexandrov:2023jcj,Alexandrov:2024hgu} and has deep connections with isomonodromic deformations \cite{MO19_hyper,MOsl2,Quantization_2021}.\\

This article aims to provide a new geometric understanding of LogTR. Important formulas relating $\omega^{\text{EO}}_{h,n+1}$ to $\omega^{\text{EO}}_{h,n}$, and thus ultimately leading to a consistent definition of the free energies, are the so-called dilaton equations. The dilaton equations are closely related to variational formulas, which arise when considering families of spectral curves and studying how variations of the spectral curve affect the correlators $\omega^{\text{EO}}_{h,n}$ \cite{BorotGeometry}. 

For LogTR, no dilaton equations were derived in \cite{Alexandrov:2023tgl}, although general variational formulas were provided. We close this gap in the literature by deriving the dilaton equations in LogTR (\autoref{TheoremDilatonEquation}) and thereby obtaining a new definition of the free energies in this setting (\autoref{DefFreeEnergies}). 

Finally, we derive more explicit variational formulas, for instance describing how the correlators defined by LogTR vary with respect to specific logarithmic poles (\autoref{TheoVariationsLogTRpoles}). We present several examples in which our new definition of the free energies in the context of LogTR directly reproduces the full perturbative part of the Nekrasov--Shatashvili partition function of 4d $\mathcal{N}=2$ pure supersymmetric gauge theory, as well as the all-genus free energies of mirror curves of strip geometries, including in particular the topological vertex and the resolved conifold.




\subsection{Structure of the article}

We begin in \autoref{sec.defLogTR} with the set-up for this article, including the allowed geometry of the spectral curves and a review of the definition of LogTR. Then, in \autoref{sec.PropLogTR}, we list properties of LogTR which are known and which essentially follow directly from its definition. 

Next, in \autoref{sec.Dilaton}, we state the dilaton equations, starting in \autoref{sec.dilatonomehn} with the dilaton equation for the differentials $\omega_{h,k}$, and continuing in \autoref{sec.dilatonfreeenergy} with the dilaton equation for $F_h:=\omega_{h,0}$ providing a definition of the free energies.  We conclude this section with examples in \autoref{sec.dilatonfreeenergyexamples}, which already provide nontrivial results for the free energies for some interesting spectral curves.  

In \autoref{sec.parametrizeom01}, we study how $\omega_{0,1}$ parametrizes the space of spectral curves in LogTR. In this context, the local decomposition is studied in \autoref{Sec:localcorrdinate}, and the global decomposition in \autoref{SectionGlobalDec}. The resulting decomposition depends on an additional set of parameters, namely the positions of the so-called LogTR-vital singularities, which allow one to vary in the space of spectral curves. This leads to a parametrization of the spectral curve in terms of the one-form $\omega_{0,1}$ in \autoref{sec.parametrizespectralcurve}, which is further rewritten via the Bergman kernel in \autoref{SubsectionLambda}. 

The parametrization of the space of spectral curves then gives rise to the variational formulas studied in \autoref{sec.variationalformula} for LogTR. First, we provide a list of parameters in \autoref{sec.variationsof}, and then derive the variational formulas with respect to the classical parameters in \autoref{SectionVartdydx}, as well as with respect to the LogTR-vital singularities in \autoref{SectionVarVitalSing}, including also the free energies. These new variational formulas show that the dilaton equations and the definition of the free energies in LogTR are compatible with the variational formulas. This confirms that the definition of the free energies in \autoref{sec.dilatonfreeenergy} is the correct one, which is further supported by the examples.

Most of the proofs are deferred to \autoref{AppendixDilatonProof}--\autoref{AppendixVarF1LogTR} due to their length.











\subsection{Notations and reminders}
In this article, we shall use the following notations:

\begin{itemize}
    \item $\llbracket n\rrbracket=\llbracket 1,n\rrbracket= \{1,\dots,n\}$ for any $n\geq 1$. By convention $\llbracket 0\rrbracket=\emptyset$.
    \item $z_I$ denote $(z_i)_{i\in I}$ for any finite and non-empty set $I \subset \mathbb{N}$.
    \item $[u^d]$ denotes the operator that extracts the $d^{\text{th}}$ coefficient in the formal series expansion in $u$ from the whole expression to the right of it, that is: $[u^d]\left(\underset{k=-\infty}{\overset{+\infty}{\sum}} f_ku^k\right):=f_k$.
    \item $\mathcal{S}(u):=\frac{e^{\frac{u}{2}} -e^{-\frac{u}{2}} }{u}= \frac{2\sinh \frac{u}{2}}{u}$. We shall also define the sequence $(\beta_{2k})_{k\geq 0}$:
    \beq \frac{1}{\mathcal{S}(u)}=\sum_{k=0}^{\infty} \beta_{2k}u^{2k}\,\,,\,\, \beta_{2k}=\frac{(2^{1-2k}-1)B_{2k}}{(2k)!} \,,\,\forall\, k\geq 0 \eeq
    where $(B_k)_{k\geq 0}$ are the Bernoulli numbers.
    \item $\delta_{i,j}$ is the Kronecker symbol.
\end{itemize}
Moreover, for a compact Riemann surface $\Sigma$ of genus $g$, we shall use the following notations:
\begin{itemize}
    \item $\left(\mathcal{A}_i,\mathcal{B}_i\right)_{1\leq i\leq g}$ will denote a basis of homology cycles (i.e. $\mathcal{A}_i\cap \mathcal{B}_j=\delta_{i,j}$). We shall also refer to it as a choice of Torelli marking on $\Sigma$.
    \item For a given choice of Torelli marking, $\left(du_i\right)_{1\leq i\leq g}$ will denote the basis of holomorphic one-forms on $\Sigma$ that is normalized on the $\mathcal{A}$-cycles:
\beq \forall \,(i,j)\in \llbracket 1,g\rrbracket^2\,:\, \oint_{\mathcal{A}_i}du_j=\delta_{i,j}\eeq
and the corresponding Riemann's matrix of periods $\left(\tau_{i,j}\right)_{1\leq i,j\leq g}$ is defined by 
\beq  \forall \,(i,j)\in \llbracket 1,g\rrbracket^2\,:\, \tau_{i,j}:=\oint_{\mathcal{B}_i}du_j\eeq 
\item We shall denote $B$ the Bergman kernel: it is the unique bi-differential with a residueless double pole on the diagonal and that is normalized on the $\mathcal{A}$-cycles:
\bea B(p,q)&\overset{q\to p}{=}&\frac{dz(q)dz(p)}{(z(q)-z(p))^2} +O(1) \text{ in any local coordinate $z$,}\cr
\oint_{\mathcal{A}_i}B&=&0\,\,,\forall\,i \in \llbracket1,g\rrbracket.\eea
\item The modified third kind differential based on $(z_1,z_2)\in \Sigma^2$ shall be denoted $dS_{z_1,z_2}$ and is defined by
\beq dS_{z_1,z_2}(q)=\int_{z_2}^{z_1} B(.,q)\eeq
It is the unique meromorphic differential on $\Sigma$ with only two simple poles at $q=z_1$ with residue $+1$ and $q=z_2$ with residue $-1$ and normalized on the $\mathcal{A}$-cycles: $\oint_{q\in\mathcal{A}_i} dS_{z_1,z_2}(q)=0$ for all $i\in \llbracket 1,g\rrbracket$.
\item The prime form associated to $\Sigma$, denoted $E(p,q)$ is the unique $\left(-\frac{1}{2},-\frac{1}{2}\right)$ form such that it has no pole and only simple zeros on the diagonal $p=q$. In any local coordinates $z$:
\beq E(p,q)\overset{p\to q}{\sim}\frac{z(p)-z(q)}{\sqrt{dz(p)}\sqrt{dz(q)}} \eeq
It is related to the modified third kind differential by $dS_{z_1,z_2}(q)=d_q\ln \frac{E(q,z_1)}{E(q,z_2)}$.
\item  We shall denote $S_B$ the Bergman projective connection on $\Sigma$. It is defined by 
\beq B(p,q)\overset{q\to p}{=}\left(\frac{1}{(z(p)-z(q))^2}+\frac{1}{6} S_B(z(p))+ O(z(q))\right)dz(q)dz(p)\eeq
for any local coordinate $z$ around the diagonal.
\item For a meromorphic one-form $dx$ on $\Sigma$, the ramification points $(p_i)_{1\leq i\leq N}$ are defined as the zeros of $dx$. A simple ramification point $p_i$ defines a local involution, denoted $\sigma_i$, such that $x(\sigma_i(q))=x(q)$ locally around $p_i$. Following the notation of \cite{EO07}, we shall denote
\bea\label{DefVertexPropagator}
dE_{i,q}(p)&:=&\frac{1}{2}\int_q^{\sigma_i(q)} B(.,p)=\frac{1}{2} dS_{q,\sigma_i(q)}(p)\cr
\text{and }\omega_i(p)&:=&(y(p)-y(\sigma_i(p)))dx(p)
\eea
for a given meromorphic one-form $dy$ on $\Sigma$. These quantities are defined only locally around the simple ramification points $p_i$. When $dx$ has only simple ramification points the Bergman tau-function $\tau_B$ is defined by
\beq \forall \,i \in \llbracket1,N\rrbracket\,:\, \partial_{p_i}[\ln \tau_B]=-\frac{1}{12}S_B(p_i)\eeq 
\end{itemize}
Due to its importance in the present work, we also remind Riemann bilinear identity and one of its corollary.

\begin{proposition}[Riemann bilinear identity]\label{RiemannBilinearIdentity}Let $\Sigma$ be a compact Riemann surface of genus $g$ and $\left(\mathcal{A}_i,\mathcal{B}_i\right)_{1\leq i\leq g}$ a basis of homology cycles. Let $\omega_1$ and $\omega_2$ be two meromorphic differentials on $\Sigma$. Let $p_0\in\Sigma$ be an arbitrary basepoint, we consider the function $\Phi_1$ defined on the fundamental domain by
\beq \Phi_1(p):=\int^p_{p_0} \omega_1\eeq
Riemann bilinear identity states that
\beq \sum_{a\in \{\text{all poles }\omega_1 \text{ and }\omega_2\}}\Res_{q\to a} \Phi_1(q)\omega_2(q)= \frac{1}{2i\pi}\sum_{i=1}^g\oint_{\mathcal{A}_i}\omega_1\oint_{\mathcal{B}_i}\omega_2- \oint_{\mathcal{B}_i}\omega_1\oint_{\mathcal{A}_i}\omega_2
\eeq
Consequently for any meromorphic one-form $\omega$ on $\Sigma$:
\beq \label{CorollaryRiemannBilinearIdentity} 
\omega(p)= \sum_{a\in \{\text{all poles of }\omega\}}\Res_{q\to a} dS_{p_0,q}(p) \omega(q) + \sum_{i=1}^g du_i(p) \oint_{\mathcal{A}_i} \omega 
\eeq
\end{proposition}


%\begin{remark}[Genus $0$ case]\label{RemarkGenus0Case}For genus $0$ Riemann surface $\Sigma$, we have
%\bea B(p,q)&=&\frac{dp\, dq}{(p-q)^2}\cr
%dS_{z_1,z_2}(q)&=&\left(\frac{1}{q-z_1}-\frac{1}{q-z_2}\right)dq\cr
%E(p,q)&=&\frac{p-q}{\sqrt{dp}\sqrt{dq}}\cr
%S_{z_1,z_2}(q)&=&\ln\left(\frac{q-z_1}{q-z_2}\frac{\sqrt{dz_2}}{\sqrt{dz_1}}\right)=\ln\frac{q-z_1}{q-z_2}+ \ln \frac{\sqrt{dz_2}}{\sqrt{dz_1}} \cr
%dE_{i,q}(p)&=&\frac{1}{2}\left(\frac{1}{q-p}-\frac{1}{\sigma_i(q)-p} \right)dp
%\eea
%\end{remark}

\section{Definition of LogTR and its known properties}
\subsection{Definition of logarithmic topological recursion}\label{sec.defLogTR}
To define the Topological Recursion (TR) \cite{EO07}, one needs a compact Riemann surface $\Sigma$ with a choice of Torelli marking and two one-forms $dx$ and $dy$ on $\Sigma$. In the original definition of TR \cite{EO07}, the two one-forms are assumed to be meromorphic on $\Sigma$ without residue so that the corresponding function $x$ and $y$ are meromorphic functions on $\Sigma$. However, an important application of TR was found in Gromov--Witten theory for toric Calabi--Yau threefolds \cite{BKMP}. In this setting, the assumption on $x$ and $y$ has to be relaxed so that the differentials $dx$ and $dy$ are meromorphic but with possible residues at their poles. This allows $x$ and $y$ to have locally logarithmic singularities, where $dx$ and $dy$ have non-vanishing residues. Luckily, the original definition of TR provides the correct result in the presence of a so-called generic framing parameter, which ensures that $dx$ has a non-vanishing residue whenever $dy$ has a non-vanishing residue. However, it was observed that if a specific framing is chosen such that this property is not satisfied, TR does not compute the correct Gromov--Witten invariants and does not commute with limits to those specific points \cite{Bouchard:2011ya,Gukov:2011qp}. The notion of framing originates in physics, namely in topological string theory. In other areas where TR finds applications, such a generic framing may not be available. Therefore, one seeks a new definition that behaves correctly under limits and produces the correct Gromov--Witten invariants already for special framings, without assuming genericity.

\medskip

The refinement of TR resolving this problem is Logarithmic Topological Recursion (LogTR). Indeed, it incorporates in a specific way the non-vanishing residues of $dy$ if $dx$ is regular at those points. Moreover, an additional motivation for this refinement is the observation \cite{Hock:2023dno} that LogTR extends TR in the context of  the so-called $x$-$y$ duality \cite{Alexandrov:2022ydc,Hock:2022wer,Hock:2022pbw}. The final definition of LogTR has been introduced in \cite{Alexandrov:2023tgl} but several points are missing, such as the definition of free energies, the dilaton equations, and variational formulas. These relations play a crucial role in standard TR especially regarding quantization and integrable systems. In order to recap the definition and proceed with the proof of these new properties, we need the following initial data:

\begin{definition}[Initial data for LogTR]\label{InitialData} The initial data for LogTR are the following:
\begin{itemize}
    \item A Riemann surface $\Sigma$ of genus $g\geq 0$.
    \item A choice of Torelli marking for $\Sigma$, i.e. of homology cycles $\left(\mathcal{A}_i,\mathcal{B}_i\right)_{1\leq i\leq g}$ such that $\mathcal{A}_i\cap \mathcal{B}_j=\delta_{i,j}$. This choice is equivalent to the choice of a Bergman kernel $B$, i.e. the unique meromorphic bi-differential with a double pole along the diagonal with bi-residue $1$ and no further singularities and whose $\mathcal{A}$-periods vanish.
    \item Two meromorphic differentials $dx$ and $dy$ on $\Sigma$. The zeros of $dx$ are called ramification points and denoted $\text{Ram}:=\{p_1,\dots,p_N\}$. We shall denote $\mathcal{P}_x$ the set of poles of $dx$ and $\mathcal{P}_y$ the set of poles of $dy$. We shall denote $\mathcal{P}=\mathcal{P}_x\cup \mathcal{P}_y$. Finally, we shall denote $\mathcal{S}_x\subset \mathcal{P}_x$ the set of all poles of $dx$ with non-vanishing residues and $\mathcal{S}_y\subset \mathcal{P}_y$ the set of all poles of $dy$ with non-vanishing residues.
\end{itemize}
\end{definition}


In fact, we shall only consider a subset of initial data by requiring the following admissibility conditions:

\begin{assumption}[Admissible initial data for LogTR]\label{MainAssumption}In this paper, we shall always make the following assumptions:
\begin{itemize}
    \item The Riemann surface $\Sigma$ is compact.
    \item The ramification points are always simple zeros of $dx$.
    \item $dy$ is regular at the ramification points.
    \item The zero loci of $dy$ and the zero loci of $dx$ are disjoint.
\end{itemize}
These assumptions will be referred to as ``admissible conditions" for the initial data and we shall refer to $(\Sigma,B,dx,dy)$ as an admissible spectral curve or admissible initial data for LogTR.
\end{assumption}

\begin{remark}The first three assumptions are the standard assumptions of the original version of TR. There exist generalizations of TR \cite{HigherRam,Bouchard:2023yau,DN1} that deal with some of these assumptions but we let the generalizations of these cases to LogTR for future works.
\end{remark}

In the standard TR, $x$ and $y$ are meromorphic functions on $\Sigma$ and thus $dx$ and $dy$ cannot have poles with non-vanishing residue (in particular they cannot have simple poles). This originates from the fact that $x$ and $y$ are usually associated to an algebraic equation $P(x,y)=0$. On the contrary, in topological string theory, the spectral curve is given by an algebraic equation on $\mathbb{C}^*$ of the form $P(e^x,e^y)=0$ so that $X=e^x$ and $Y=e^y$ are meromorphic functions but $dx=\frac{dX}{X}$ and $dy=\frac{dY}{Y}$ have simple poles with non-vanishing residues at every zero or pole of $X$ or $Y$. Thus, in the LogTR setting, $dx$ and $dy$ are arbitrary meromorphic one-forms on $\Sigma$ and thus may have simple poles or poles with non-vanishing residues. When this happens, $x$ and $y$ are no longer meromorphic functions on $\Sigma$ because they locally exhibit logarithmic singularities that we will describe in the following definition.

\begin{definition}[Logarithmic cuts for poles of $dx$ and $dy$ with non-vanishing residues]\label{Def22} Let $o$ be a given basepoint that is assumed to be away from ramification points, poles/zeros of $dx$, poles/zeros of $dy$ and the representative $(\mathcal{A}_i,\mathcal{B}_i)$ cycles. Moreover, we choose the basepoint $o$ so that $x(o)\neq x(a)$ for any pole $a$ of $dx$ or $dy$ and such that $x(o)\neq x(p_i)$ for any $i\in \llbracket 1,N\rrbracket$. We shall use this basepoint to define the logarithmic cuts and the domain of $x$ and $y$.
\begin{itemize}
\item For any $s\in \mathcal{S}_x\cup \mathcal{S}_y$ (i.e. a pole of $dx$ or $dy$ with non-vanishing residue), we select a logarithmic cut connecting $s$ to $o$, i.e. a smooth contractible oriented curve connecting $s$ to $o$ such that it avoids all other poles/zeros of $dx$, poles/zeros of $dy$ and the holonomy cycles. We shall denote $\mathcal{C}_{o\to s}$ this logarithmic cut. Moreover, we shall take the logarithmic cuts such that they only intersect at $o$.
\item The differential $dx$ admits an antiderivative $x$ defined on $\Sigma\setminus\left(\mathcal{P}_x\cup \underset{s\in \mathcal{S}_x}{\bigcup} \mathcal{C}_{o\to s}\right)$.
\item The differential $dy$ admits an antiderivative $y$ defined on $\Sigma\setminus\left(\mathcal{P}_y \cup\underset{s\in \mathcal{S}_y}{\bigcup} \mathcal{C}_{o\to s}\right)$.
\item This choice of logarithmic cuts is equivalent to the choice of logarithmic branch of $\ln \frac{E(q,s)}{E(q,o)}$ for any point $s\in \mathcal{S}_x\cup \mathcal{S}_y$. 
\end{itemize}

\end{definition}

\begin{remark}Our choice of logarithmic cuts defines a contractible star-shaped domain based at $o$ (where $dx$ and $dy$ are regular) but other choices could be made. In particular, it is important to notice that all interesting quantities (correlation functions, free energies, etc.) should and will be independent of the choice of logarithmic cuts. 
\end{remark}

In the following definition of LogTR, only specific logarithmic singularities, known as LogTR-vital singularities, will play a role.

\begin{definition}[LogTR-vital singularities] A singularity $s\in \mathcal{S}_y$ is called a LogTR-vital singularity if $s$ is a simple pole of $dy$ and $dx$ is regular at $s$. We shall denote $\mathcal{V}=\{a_1,\dots,a_M\}\subset \mathcal{S}_y$ the finite set of all LogTR-vital singularities and $y_{a_s}:=\underset{q\to a_s}{\Res} dy$ the corresponding residue.
\end{definition}


We are now ready to define the LogTR procedure.

\begin{definition}[Definition of LogTR]\label{DefLogTR}Let $(\Sigma,B,dx,dy)$ be an admissible spectral curve. Denote $(p_i)_{1\leq i\leq N}$ the ramification points, $(a_k)_{1\leq k\leq M}$ the LogTR-vital singularities and $(y_{a_k})_{1\leq k\leq M}$ their corresponding residue. Finally, let $\sigma_i$ be the deck transformations of $x$ near $p_i$ for any $i\in \llbracket 1,N\rrbracket$.
We define the LogTR correlations functions $\left(\omega_{h,n}\right)_{h\geq 0,n\geq 1}$ by the following induction \cite{Alexandrov:2023tgl}:
\begin{itemize}
    \item $\omega_{0,1}:=ydx$ and $\omega_{0,2}:=B$.
    \item For any $h\geq 0$ and $m\geq 1$ such that $2h+m-2>0$ we define by induction 
    \bea \label{LogTRDef} \omega_{h,m}(z_1,\dots,z_m)&:=&\frac{1}{2}\sum_{i=1}^N\Res_{z\to p_i}\frac{\int_{z}^{\sigma_i(z)} \omega_{0,2}(z_1,.)}{\omega_{0,1}(\sigma_i(z))-\omega_{0,1}(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^z\omega_{0,2}(z_1,.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
    \eea   
\end{itemize}
\end{definition}

Note that the last line in \eqref{LogTRDef} is the new contribution arising in LogTR and it only contributes for $m=1$. Thus the correlations functions $(\omega_{0,n})_{n\geq 3}$ are the same as those obtained from standard TR. On the contrary, $\omega_{1,1}$ will have an additional contribution and this new contribution will propagate in the induction and contributes to $\omega_{1,2}$, $\omega_{1,3}$, etc. Note also that we have used $dy$ in the initial data. We will have to choose logarithmic cuts for $\omega_{0,1}$, as will be discussed in \autoref{sec.parametrizeom01} and accordingly to \autoref{Def22}. However, for all $\omega_{g,n}$ it is sufficient to work with $dy$, since by recursion only derivatives of $y$ appear for $2g+n-2>0$.

\begin{remark} If there are no LogTR-vital singularities, i.e. $\mathcal{V}=\emptyset$, then the definition of LogTR is the same as the standard TR. In particular, this is exactly the situation if a generic framing is chosen for the mirror curve of toric Calabi-Yau threefolds. From the perspective of TR, a framing is the choice of an integer $f\in \mathbb{Z}$ such that the two ingredients for the spectral curve are chosen to be $(x_f,y)=(x+fy,y)$. For generic $f$, $d(x+fy)$ has residues at all points where $dy$ has residues, thus the set of LogTR-vital points is empty.
\end{remark}

\begin{remark}
The additional term appearing in LogTR involves taking residues at the \emph{LogTR-vital singularities} $\mathcal{V}=\{a_1,\dots,a_M\}\subset \mathcal{S}_y$. In principle, one could include all points of $\mathcal{S}_y$ in the definition of LogTR. However, only the LogTR-vital points $\mathcal{V}\subset \mathcal{S}_y$ yield non-vanishing contributions after performing the residue computation.
\end{remark}

\begin{definition}[Alternative definition of LogTR]\label{DefLogTRAlternative} Using the same setup as in \autoref{DefLogTR} LogTR  is equivalent to
\bea \label{LogTRDefAlter} \omega_{h,m}(z_1,\dots,z_m)&=&\frac{1}{2}\sum_{i=1}^N\Res_{z\to p_i}\frac{\int_{z}^{\sigma_i(z)} \omega_{0,2}(z_1,.)}{\omega_{0,1}(\sigma_i(z))-\omega_{0,1}(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&+\delta_{m,1}\sum_{s=1}^M\left(\frac{\partial^{2h-2}}{\partial x(q)^{2h-2}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_s} [\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar)}\right)\cr
    &=&\frac{1}{2}\sum_{i=1}^N\Res_{z\to p_i}\frac{\int_{z}^{\sigma_i(z)} \omega_{0,2}(z_1,.)}{\omega_{0,1}(\sigma_i(z))-\omega_{0,1}(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&+\delta_{m,1}\sum_{s=1}^M\left(\frac{\partial^{2h-2}}{\partial x(q)^{2h-2}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_s} y_{a_s}^{1-2h}\frac{(2^{1-2h}-1)B_{2h}}{(2h)!}
    \eea   
for any $h\geq 0$ and $m\geq 1$ such that $2h+m-2>0$. In this formula, $(B_k)_{k\geq 0}$ stands for the Bernoulli numbers.
\end{definition}

\begin{proof}By integration by parts with local meromorphic differentials $\frac{dz}{z-a_s}$ and $\omega_{0,2}(z_1,z)$ we can rewrite the LogTR special term in the induction as
\bea &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^z\omega_{0,2}(z_1,.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
=\delta_{m,1}\sum_{s=1}^M\left(\frac{\partial^{2h}}{\partial x(q)^{2h}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_s}[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar)}\right)
\eea
\end{proof}

Formulations provided by \autoref{DefLogTRAlternative} are convenient for practical computations but are less practical in the theoretical proofs contrary to the residue formulation of \autoref{DefLogTR}.

\subsection{Basic properties of LogTR}\label{sec.PropLogTR}
The correlators $\left(\omega_{h,n}\right)_{h\geq 0,n\geq 1}$ constructed from LogTR  in \autoref{DefLogTR} satisfy many beautiful properties \cite{Alexandrov:2023tgl,Alexandrov:2024tjo} that we summarize in the following proposition.

\begin{proposition}[LogTR basic properties]\label{PropLogTRBasicProperties} The correlators $\left(\omega_{h,n}\right)_{h\geq 0,n\geq 1}$ constructed from LogTR in \autoref{DefLogTR} satisfy the following properties:
\begin{itemize}
    \item The correlators $\omega_{h,n}$ are meromorphic $n$-forms on $\Sigma$ except possibly for $(h,n)=(0,1)$.
    \item The correlators $\omega_{h,n}$ are symmetric forms for $n\geq 2$ and $h\geq 0$.
     \item For $2h+n-2>0$ and $n\geq 2$, the correlators $\omega_{h,n}$ have poles only at the ramification points $(p_1,\dots,p_N)$.
     \item For $h\geq 1$, the correlators $\omega_{h,1}$ have poles only at the ramification points $(p_1,\dots,p_N)$ and at the LogTR-vital singularities $(a_1,\dots,a_M)$. 
    \item For $2h+n-2\geq 0$, any $\omega_{h,n}$ is residue-free.
    \item For any $(h,n)\neq (0,1)$, the correlators $\omega_{h,n}$ have vanishing periods along the $\mathcal{A}$-cycles:
    \beq \label{VanishingAperiods}\forall\, (h,n)\neq (0,1)\,,\, \forall\, i\in \llbracket 1,g\rrbracket\,:\, \oint_{\mathcal{A}_i} \omega_{h,n}=0\eeq
    \item Linear loop equations (LLE): For any $i\in \llbracket 1,N\rrbracket$ and any $(h,m)\in \mathbb{N}^2$ such that $2h+m-1>0$, the quantity
    \beq \label{LinearLoopEquations}\omega_{h,m+1}(z_1,\dots,z_m,z)+\omega_{h,m+1}(z_1,\dots,z_m,\sigma_i(z)) \eeq 
    is holomorphic in a neighborhood of $p_i$ and has at least a simple zero in $z$ at $z = p_i$.
    \item Quadratic loop equations (QLE): For any $i\in \llbracket 1,N\rrbracket$ and any $(h,m)\in \mathbb{N}^2$ such that $2h-2+m>0$, the quadratic differential in $z$
\beq \label{QuadraticLoopEquations}\omega_{h-1,m+2}(z_1,\dots,z_m,z,\sigma_i(z))
    +\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, m\}}} \omega_{h_1,|I_1|+1}(z_{I_1},z)\, \omega_{h_2,|I_2|+1}(z_{I_2},\sigma_i(z))\eeq
is holomorphic in a neighborhood of $p_i$ and has at least a double zero at $z = p_i$.
    \item Logarithmic projection property (LPP): For any $h\geq 0$, $m\geq 1$ such that $2h-2+m>0$: 
\beq\label{LogProjectionProperty} \omega_{h,m}(z_1,\dots,z_m)=\sum_{p\in \{p_i\}_{1\leq i\leq N}\sqcup \{a_j\}_{1\leq j\leq M}}\Res_{z'\to p}\left(\int_{p}^{z'}B(.,z_1)\right)\omega_{h,m}(z',z_2,\dots,z_m)\eeq
for $m>1$, the set $\{a_j\}_{1\leq j\leq M}$ does not contribute and can be removed.
\end{itemize}
\end{proposition}

Note that the LPP immediately follows from Riemann bilinear identity \eqref{RiemannBilinearIdentity} applied to $\omega_1=B$ and $\omega_2=\omega_{h,m}$. Indeed, both differentials are normalized on the $\mathcal{A}$-cycles and the only missing pole is the double pole of $B$ at $z'=z_1$.

\begin{remark}\label{remarklooplog}
    The projection of $\omega_{h,1}$ to the singular part at the LogTR-vital singularity $a_i$ has several equivalent formulations which are very explicit. Those can be understood as the \textit{loop equations at the LogTR-vital singularity}. However, this terminology is rather misleading since it is neither a linear nor a quadratic equation. In fact, we have the following representations of $\omega_{h,1}$ projected to the LogTR-vital singularity $a_s$:
    \begin{align*}
        \Res_{z'\to a_s}\left(\int_{a_s}^{z'}B(.,z)\right)\omega_{h,1}(z')
        =&-\Res_{z\to a_s}\left(\int_{a_s}^{z'}B(.,z)\right)dx(z')[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_{x(z')})}\ln('z-a_s) \right)\\
=&\left(\frac{\partial^{2h-2}}{\partial x(z')^{2h-2}}\frac{B(z,z')}{dx(z')}\right)_{|\, z'=a_s}[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar)}\right)\cr
%=&\left(\frac{\partial^{2h-2}}{\partial x(z')^{2h-2}}\frac{B(z,z')}{dx(z')}\right)_{|\, z'=a_s}y_{a_s}^{1-2h} \frac{(2^{1-2h}-1)B_{2h}}{(2h)!}.
    \end{align*}
\end{remark}
\begin{remark}
    In the standard TR setting, the linear loop equations, the quadratic loop equations together with the projection property to the ramification points is equivalent to the definition of standard TR \cite{Borot:2013lpa}. Analogously, \autoref{DefLogTR} of LogTR is the unique solution to the linear loop equations, the quadratic loop equations, the loop equations at the LogTR-vital singularity of \autoref{remarklooplog} and the logarithmic projection properties.
\end{remark}









\section{Dilaton equations and definition of the free energies}\label{sec.Dilaton}
In standard TR, the dilaton equation is a simple formula that provides $\omega^{\text{EO}}_{h,n}$ in terms of $\omega^{\text{EO}}_{h,n+1}$ by multiplying with a primitive of $\Phi(z)=\int_o^z\omega_{0,1}$ and taking residues at all ramification points
\begin{equation}\label{standarddilaton}
    (2-2h-n)\omega^{\text{EO}}_{h,n}(z_1,...,z_n)=\sum_{p\in \text{Ram}}\Res_{z'\to p}\Phi(z')\omega^{\text{EO}}_{h,n+1}(z',z_1,...,z_n).
\end{equation}
At first glance, such a formula may not seem very surprising, since $\omega^{\text{EO}}_{h,n+1}$ is recursively defined from $\omega^{\text{EO}}_{h,n}$. However, the importance of the dilaton equations lies in the fact that they allow one to define the set of free energies $(F_h^{\text{EO}}:=\omega^{\text{EO}}_{h,0})_{h\geq 2}$, by the extension of \eqref{standarddilaton}:
\begin{equation}
    (2-2h)\omega^{\text{EO}}_{h,0}=\sum_{p\in \text{Ram}}\Res_{z'\to p}\Phi(z')\omega^{\text{EO}}_{h,1}(z').
\end{equation}
Thus, the dilaton equations are central to define the free energies that are non-trivial functions of the moduli of the spectral curve. 

\medskip

The aim of this section is to find the dilaton equations for LogTR and thereby to define the free energies $(F_h)_{h\geq 2}$ in the presence of LogTR-vital singularities. In \cite{Alexandrov:2023tgl}, where LogTR was defined, no dilaton equations were found and no definition of the free energies was proposed. A naive guess for a possible dilaton equation would be a direct extension of the standard TR dilaton equations, possibly including residues at the LogTR-vital singularities. This, however, does not work for several reasons. First, logarithmic singularities appear when integrating $ydx$, so residues at those points are not defined. Secondly, if one only takes residues at the ramification points, as in the standard TR setting then one cannot obtain poles of $\omega_{h,1}$ at the logTR-vital singularities and thus the formula cannot hold.

Some further motivations can be gained from topological string theory, where TR computes Gromov--Witten invariants of toric Calabi--Yau threefolds. For this class of examples (as mentioned before), standard TR already computes the correct invariants $\omega_{h,n}^{\text{EO}}$, but only in the presence of a generic framing. Thus, all differentials $\omega_{h,n}^{\text{EO}}$ associated with a mirror curve depend on the framing. %Sending the framing to a special value that generates LogTR-vital singular points commutes with the definition of LogTR of $\omega_{h,n}$ with $n\geq 1$. 
One important observation in the Gromov--Witten theory of toric Calabi--Yau threefolds is that the \textit{closed invariants} (i.e.\ the free energies) $F_h=\omega_{h,0}$ are independent of the framing. This remarkable property suggests that, for any framing (even in the presence of LogTR-vital singularities), one should be able to compute the free energies. An expected definition of the free energies in LogTR should therefore reproduce the same free energies as that obtained from standard TR in a generic framing of the mirror curve.




\subsection{Dilaton equations in LogTR}\label{sec.dilatonomehn}
The derivation of the dilaton equations relies on one fundamental property of the structure of the poles $(\omega_{h,1})_{h\geq 1}$ around the LogTR-vital singularities. Then the derivation essentially follows similar (but slightly extended) lines as the derivation of the dilaton equation in standard TR and is performed by induction. The important behavior of $(\omega_{h,1})_{h\geq 1}$ at logTR-vital singularities is formulated in the following lemma.

\begin{lemma}\label{LemmaIntW02Wg1}Let $s\in \llbracket 1,M\rrbracket$. For any function $F$ that is holomorphic in a neighborhood of $a_s$, we have that for any $h\geq 1$:
\beq \label{lemma1eq}\Res_{z\to a_s} F(z) d_z\Big[(x(z)-x(a_s)) \frac{\omega_{h,1}(z)}{dx(z)}\Big]= (1-2h)\Res_{z\to a_s} F(z)\omega_{h,1}(z)\eeq   
or equivalently
\beq \label{lemma2eq} \Res_{z\to a_s} \frac{\omega_{h,1}(z)}{dx(z)}  d_{z}[F(z)]= 2h\Res_{z\to a_s} F(z)\omega_{h,1}(z).\eeq  
In particular for $F(z)=\int_o^z \omega_{0,2}(.,z_1)$, we obtain (for any distinct points $(z_1,o)$ away from the ramification points and the LogTR-vital singularities)
\beq\label{EqLemmeIntW02WG1} (2h-1)\Res_{z\to a_s} \left(\int_{o}^{z} \omega_{0,2}(., z_1)\right)\omega_{h,1}(z)=\Res_{z\to a_s}\frac{x(z)-x(a_s)}{dx(z)}\omega_{h,1} (z)\omega_{0,2} (z,z_1).\eeq
\begin{proof}
    From the fact that $(x(z)-x(a_s))d_z\log(z-a_s)$ is a holomorphic form at $z\to a_s$, one can conclude for that for any $k\geq1$:
   \footnotesize{\begin{align*}
        &F(z)\bigg(d_z\frac{1}{dx(z)}\bigg)^k\bigg((x(z)-x(a_s))d_z\log(z-a_s)\bigg)\\
        &=(k-1) F(z) \bigg(d_z\frac{1}{dx(z)}\bigg)^{k-1}d_z\log(z-a_s)+F(z)\bigg(d_z\frac{1}{dx(z)}\bigg)\bigg[(x(z)-x(a_s))\bigg(d_z\frac{1}{dx(z)}\bigg)^{k-1 }d_z\log(z-a_s)\bigg]\\
        &=O\left((z-a_s)^{-1}dz\right)
    \end{align*}}
    \normalsize{is} a meromorphic one-form at $z\to a_s$ and thus has a vanishing residue. Taking $k=2h$ and multiplying with $[\hbar^{2h}]\frac{y_{a_s}}{\mathcal{S}(\hbar y_{a_s}^{-1})}$, the meromorphic form $\omega_{h,1}$ can be reconstructed locally around $z\to a_s$ in the integrand. Thus, we get the following identity:
    \begin{align*}
        0=\Res_{z\to a_s} \bigg((2h-1)F(z)\omega_{h,1}(z)+F(z) d_z\Big[(x(z)-x(a_s)) \frac{\omega_{h,1}(z)}{dx(z)}\Big]\bigg),
    \end{align*}
    which is equivalent to \eqref{lemma1eq}.
\end{proof}
\end{lemma}


We now have all the tools to prove the dilaton equations for LogTR.

\begin{theorem}[Dilaton equations in LogTR]\label{TheoremDilatonEquation}Let $\Phi(q)=\int^q_o ydx$ be any local antiderivative of $ydx$ in the neighborhoods of the ramification points $(p_i)_{1\leq i\leq N}$. We have:
\beq \label{EqSpecialDilaton}\Res_{z\to z'} \omega_{0,2}(z,z')\Phi(z)=d\Phi(z')=\omega_{0,1}(z')\eeq
and for any $h\geq 0$, $k\geq 1$ such that $(h,k)\neq (0,1)$:
\bea\label{DilatonEquation} (2-2h-k)\omega_{h,k}(z_1,\dots,z_k)&=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,k+1}(z,z_1,\dots,z_k) \cr&&
-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr&&
\eea
where $(z_1,\dots, z_k)\in \Sigma^k$ are points away from the ramification points and the LogTR-vital singularities.
\end{theorem}

\begin{proof}The proof is trivial for \eqref{EqSpecialDilaton} from the property of the Bergman kernel on the diagonal. Then, the proof is done by induction on $2h+k$. To evaluate the contributions at the LogTR-vital singularities, we assume the validity of the Dilaton equations for $\omega_{h,k}$ as stated in \autoref{TheoremDilatonEquation} and apply the operator $\sum_{s=1}^M \Res_{z\to a_s} \Phi(z)$ to both sides of the recursion. This confirms the consistency of the definition.
\end{proof}

The general form of the dilaton equations clearly extends the standard TR dilaton equation \eqref{standarddilaton} in the presence of LogTR-vital singularities. Indeed, the second line in \eqref{DilatonEquation} is new and takes all $(\omega_{h',1})_{1\leq h'\leq h}$ into account.

Note that $\Phi(z)$ is not well defined in a neighborhood of a LogTR-vital singularity because of the presence of a logarithmic cut emanating from $a_s$. This explains why, in the first line of \eqref{DilatonEquation}, no residue at $a_s$ can be taken and rather that the second line can be thought of the corresponding analogue.

\begin{remark}[Alternative formulation of the dilaton equations] For any $h\geq 0$, $k\geq 1$ such that $(h,k)\neq (0,1)$, the dilaton equations may also be rewritten into 
   \bea\label{DilatonLogTRAlt}
        &&(2-2h-k)\omega_{h,k}(z_{\llbracket k \rrbracket})=\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,k+1}(z,z_{\llbracket k \rrbracket})\cr
        &&-\frac{1}{2}\sum_{s=1}^M\Res_{z\to a_s}\frac{x(z)-x(a_s)}{dx(z)}\Big(\omega_{h-1,k+2}(z,z,z_{\llbracket k \rrbracket})+\underset{\substack{h_1+h_2=h\\ I_1\sqcup I_2={\llbracket k \rrbracket}\\(h_i,I_i)\neq (0,\emptyset)}}{\sum}\omega_{h_1,|I_1|+1} (z,z_{I_1})\omega_{h_2,|I_2|+1} (z,z_{I_2})\Big)\cr&&
    \eea
Indeed, only $\left(\om_{h,1}\right)_{h\geq 1}$ are singular at the LogTR-vital singularities so the previous formula obviously reduces to \eqref{DilatonEquation}.
\end{remark}




\subsection{Definition of the free energies in LogTR}\label{sec.dilatonfreeenergy}
As explained above, the dilaton equations may be used as a guideline to define the free energies. However, it is not possible to simply set $k=0$ in the dilaton equations \eqref{DilatonEquation}, since a term involving $\omega_{0,1}$ would appear in the second line, producing a logarithmic singularity at $a_s$. The solution to this problem comes from local integration by parts. Indeed, the exceptional term $\frac{\omega_{0,1}\,\omega_{h,1}}{dx}$ can be rewritten as $-dy \int \omega_{h,1}$, which avoids the logarithmic singularity at $a_s$ and is well-defined because $(\omega_{h,1})_{h\geq 1}$ have vanishing residues at their poles.

\begin{definition}[Definition of the free energies $(F_h:=\omega_{h,0})_{h\geq 1}$]\label{DefFreeEnergies} We shall define for any $h\geq 2$:
\bea \label{FormulasDefFg}(2-2h)\omega_{h,0}&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,1}(z)
\cr&&
-\sum_{s=1}^M\Res_{z\to a_s}\big(x(z)-x(a_s)\big)\left(\frac{1}{2}
        \overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right).\cr&&
\eea   
The definition is independent of the basepoint $o$. For $h=1$, we define:
\beq\label{F1formula}  F_1:=\omega_{1,0}:= -\frac{1}{2}\ln \tau_B -\frac{1}{24}\ln\left(\prod_{i=1}^N y'(p_i)\right) -\frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)_{\vert_{z=a_s}}\eeq
where $\tau_B$ is the Bergman tau-function and $y'(p_i)=\frac{dy(p_i)}{dz_i(p_i)}$ with $z_i(q)=\sqrt{x(q)-x(p_i)}$.
\end{definition}

\begin{remark}The definition is independent of the basepoint $o$ because $\omega_{h,1}$ is residueless at any ramification point (thus the choice of lower bound in $\Phi$ does not modify the free energy). Moreover, $(x(z)-x(a_s))dy(z)$ is regular at the LogTR-vital singularity $a_s$ (by definition of a logTR-vital singularity) thus the choice of lower bound in the second term of \eqref{FormulasDefFg} does not modify the free energy.
\end{remark}

\begin{remark}The last term in \eqref{FormulasDefFg} involving $dy$ is an exceptional contribution that was necessary in \cite{Banerjee:2025qgx} to derive the correct free energies of so-called strip geometries which are special mirror curves.  It does not appear in \autoref{TheoremDilatonEquation} because it vanishes for $k\geq 1$. Indeed, it would correspond to add the term
\beq \sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z)\int_o^z\omega_{h,k+1}(.,z_1,\dots,z_k)\eeq
but for $k\geq 1$, $\omega_{h,k+1}$ is regular at the LogTR-vital singularities so that the integrand is regular and thus the residues are trivially vanishing.
\end{remark}

\begin{remark}
 Note that we do not provide a definition of the free energy $F_0:=\omega_{0,0}$. In the original article \cite{EO07}, the definition of $F_0$ comes from the extension of the homogeneity property satisfied by the other free energies and correlation functions. However, this property is not verified in the LogTR setting  because of the presence of LogTR-vital singularities and thus no formula can be used to extend the definition to $(h,n)=(0,0)$. To the best of our understanding, the definition of $F_0$ should depend on the actual geometric origin of the spectral curve whether it comes from toric geometry or Seiberg--Witten theory.
\end{remark}





\subsection{Examples}\label{sec.dilatonfreeenergyexamples}
\begin{example}
    Take the following genus $0$ spectral curve:
    \beq
        x(z)=z,\qquad y(z)=\Lambda+\sum_{s=1}^M y_{a_s} \log(z-a_s).
    \eeq
where $z\in \mathbb{P}^1$ is a global coordinate and such that $y_\infty+\underset{s=1}{\overset{M}{\sum}} y_{a_s}=0$, where $y_\infty$ is the residue of $dy$ at infinity. This curve has no ramification points so that all $(\omega_{h,n})_{h\geq 0,n\geq 2}$ with $(h,n)\neq (0,2)$  vanish. Moreover, $(\omega_{h,1})_{h\geq 1}$ are given explicitly by 
\bea \omega_{h,1}(z)&=&-dx(z)[\hbar^{2h}]\sum_{s=1}^M\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)=-[\hbar^{2h}]\frac{1}{\mathcal{S}(\hbar)}\sum_{s=1}^M y_{a_s}^{1-2h}\frac{(2h-1)!}{(z-a_s)^{2h}}dz\cr
&=&-\sum_{s=1}^M y_{a_s}^{1-2h}\frac{(2^{1-2h}-1)B_{2h}}{2h}\frac{dz}{(z-a_s)^{2h}}.
\eea
Note that there is no contribution from $z=\infty$, since $x$ is singular at infinity ensuring that infinity is not a LogTR-vital singularity.

Inserting this into \eqref{FormulasDefFg} and evaluating the residue, it is easy to derive
    \bea\label{F2example}
       &&\forall\, h\geq 2\,:\,  F_{h}=\frac{1}{2(2h-2)  }\sum_{s=1}^M\sum_{r\neq s}\frac{ (2h-2)!}{(a_s-a_r)^{2h-2}}[\hbar^{2h}]\frac{y_{a_s}y_{a_r}}{\mathcal{S}(y_{a_s}^{-1}\hbar)\mathcal{S}(y_{a_r}^{-1}\hbar)}
       %\cr
       %&&= \frac{1}{(2-2h)}\sum_{s=1}^M\sum_{r\neq s}\frac{ (2h-2)!}{(a_s-a_r)^{2h-2}} \sum_{k=0}^h y_{a_s}^{1-2k}y_{a_r}^{1-2h+2k} \beta_{2k}\beta_{2h-2k}\cr
       %&&=  \frac{1}{(2-2h)}\sum_{s=1}^M\sum_{r\neq s}\frac{ (2h-2)!}{(a_s-a_r)^{2h-2}} \sum_{k=0}^h y_{a_s}^{1-2k}y_{a_r}^{1-2h+2k} \frac{(2^{1-2k}-1)B_{2k}}{(2k)!}\frac{(2^{1-2h+2k}-1)B_{2h-2k}}{(2h-2k)!}\cr&& 
   \eea
    and 
\beq F_1=-\frac{1}{24}\sum_{s=1}^M\sum_{r\neq s}\frac{y_{a_r}}{y_{a_s}}\log(a_r-a_s)-\frac{\Lambda}{24}\sum_{s=1}^M\frac{1}{y_{a_s}}.
\eeq
For the special values $y_{a_s}=1$ for all $s\in \llbracket1,M\rrbracket$, the free energies \eqref{F2example} simplify, using $
\frac{1}{\mathcal{S}(t)^2}
= 1 - \underset{h=1}{\overset{\infty}{\sum}} \frac{B_{2h} t^{2h}}{2h (2h-2)!}$,
 to the perturbative part of the $4d$ $\mathcal{N}=2$ pure supersymmetric gauge theory \cite{Nekrasov:2003rj}, computed from the $x$-$y$ dual of the so-called half Seiberg--Witten spectral curve \cite{Borot:2021btb,Borot:2024uos,Hock:2025wlm}.
%\todo{Olivier: we should recall there the formula}
 %\textcolor{red}{
 %\beq F_h=\frac{1}{(2-2h)}\sum_{s=1}^M\sum_{r\neq s}\frac{ (2h-1)!}{(a_s-a_r)^{2h-2}}\frac{(1-2^{1-2h})B_{2h}}{(2h-1)!}
 %=\sum_{s=1}^M\sum_{r\neq s}\frac{(1-2^{1-2h})B_{2h}}{(a_s-a_r)^{2h-2}}\eeq
 %\beq F_1=-\frac{1}{24}\sum_{s=1}^M\sum_{r\neq s}\log(a_r-a_s)-\frac{M\Lambda}{24}=-\frac{M\Lambda}{24} \text{ antisymmetry?} \eeq
 %}

\medskip

Even more interesting is the generic case with $y_{a_r} \neq y_{a_s}$. The expansion of$
\frac{y_{a_s} y_{a_r}}{\mathcal{S}(y_{a_s}^{-1}\hbar)\mathcal{S}(y_{a_r}^{-1}\hbar)}$
in \eqref{F2example} has coefficients given by so-called double Bernoulli numbers, which appear in various refined settings. For instance, they arise in a quantized Riemann--Hilbert problem \cite{Barbieri:2019yya} and also in refined topological recursion \cite{Kidwai:2023fxs}. Note, however, that allowing generic $y_{a_s}$ should maybe be understood as working with a refined spectral curve on which (Log)TR is performed, rather than refined topological recursion \cite{Osuga:2023kgw} applied to the original spectral curve. This interplay will be further investigated in the near future.
\end{example}

\begin{example}
    Consider the following genus 0 spectral curve 
    \beq
        x(z)=\log z,\qquad y(z)=\sum_{s=1}^M y_{a_s}\log\left(1- \frac{z}{a_s}\right),
    \eeq
    with $y_\infty+\underset{s=1}{\overset{M}{\sum}} y_{a_s}=0$, where $y_\infty$ is the residue of $dy$ at infinity. This curve can be understood via the parametrization $X=e^x$ and $Y=e^y$ as a curve in $\mathbb{C}^*\times \mathbb{C}^*$.

    This example has no ramification points, so that all $(\omega_{h,n})_{h\geq 0,n\geq 2}$ with $(h,n)\neq (0,2)$ vanish. However, $(\omega_{h,1})_{h\geq 1}$ are given explicitly 
\bea \omega_{h,1}(z)&=&-\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^z\omega_{0,2}(z_1,.)\right) dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\log\left(1- \frac{z}{a_s}\right) \right)\cr
&=&dx(z)[\hbar^{2h}]\sum_{s=1}^M \frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar )}\mathrm{Li}_{1-2h}\left( \frac{z}{a_s}\right)\cr
&=&dx(z)\sum_{s=1}^M y_{a_s}^{1-2h}\frac{(2^{1-2h}-1)B_{2h}}{(2h)!}\mathrm{Li}_{1-2h}\left( \frac{z}{a_s}\right)
\eea
    Note that there is no contribution from infinity, since $x$ is singular at infinity, ensuring that infinity is not a LogTR-vital singularity.
    
    Inserting this into \eqref{FormulasDefFg}, one can follow one-to-one the computation of \cite[Appendix A]{Banerjee:2025qgx} and obtain, after evaluating the residues,
    \small{\bea\label{F22example}
       &&\forall\, h\geq 2\,:\,  F_{h}=-\frac{B_{2h-2}}{2 (2h-2)}[\hbar^{2h}]\sum_{r=1}^M\left(\frac{y_{a_r}}{\mathcal{S}(y^{-1}_{a_r}\hbar )}\right)^2+\frac{1}{2}\sum_{\substack{r,s=1\\ r\neq s}}^M\mathrm{Li}_{3-2h}\left(\frac{a_s}{a_r}\right)[\hbar^{2h}]\frac{y_{a_r}y_{a_s}}{\mathcal{S}(y^{-1}_{a_r}\hbar )\mathcal{S}(y^{-1}_{a_s}\hbar )}.\cr&&
   \eea}
    \normalsize{and} 
\beq 
F_1=-\frac{1}{24}\sum_{s=1}^M\sum_{r\neq s}\frac{y_{a_r}}{y_{a_s}}\log\left(1-\frac{a_s}{a_r}\right)=\frac{1}{24}\sum_{s=1}^M\sum_{r\neq s}\frac{y_{a_r}}{y_{a_s}}\mathrm{Li}_1\left(\frac{a_r}{a_s}\right)
\eeq
    up to a constant for $F_1$ which is independent of $a_s$, arising from the limit $\log\left(1-\frac{z}{a_s}\right)-\log(x(z)-x(a_s))\vert_{z=a_s}=\text{const}.$

    In the physics literature, it is more natural to express the full asymptotic series in $\hbar$ by expanding the polylogarithm and formally interchanging the series in $\hbar$ with the series expansion of the polylogarithm. For this, different $a_r$ must be compared to ensure convergence of the polylogarithms. This is a common, but non-rigorous, computation. Let $|a_r|<|a_{r+1}|$ for all $r$, then this would lead to
\beq
\sum_{h=0}^\infty \hbar^{2h-2}F_h=\sum_{r<s}\sum_{n=1}^\infty\frac{\left(\frac{a_r}{a_s}\right)^n}{n\left(e^{\frac{n\hbar}{2y_{a_r}}}-e^{-\frac{n\hbar}{2y_{a_r}}}\right)\left(e^{\frac{n\hbar}{2y_{a_s}}}-e^{-\frac{n\hbar}{2y_{a_s}}}\right)}+\sum_{s=1}^M\sum_{k=1}^{\infty} k \log\left(1-e^{\frac{\hbar k}{y_{a_s}}}\right)
\eeq
    The reason for expressing the free energies in this form is to capture the effect of $y_{a_r}$. The usually quadratic denominator in the first line is split into two factors, as observed, for instance, in refined topological string theory. However, the McMahon-type function (last term) is not refined as the refined topological vertex \cite{Iqbal:2007ii}. The last term can be included in the first by adding $r=s$ in the sum. 
    
    For $y_{a_s}=1$, the curve is the $x$-$y$ dual of the mirror curve of strip geometries of toric Calabi--Yau threefolds \cite{Iqbal:2004ne,BKMP}, and our result recovers the known free energies, corresponding to closed string amplitudes or Gromov--Witten invariants \cite{Iqbal:2004ne}.

    In this second example, we observe again that the introduction of $y_{a_r}$ into the spectral curve has the structure of refining the spectral curve, but still using (Log)TR instead of applying a refined version of TR to the original curve. This is consistent with \cite{Eynard:2011vs}.
\end{example}


As both examples with coefficients $y_{a_r}=1$ recover known free energies associated with the corresponding $x$--$y$ dual spectral curves in the literature, we expect that this holds in general:

\begin{conjecture}
For a given genus $g=0$ admissible spectral curve on $\mathbb{P}^1$, with $dx$ and $dy$ having at most simple poles, the free energy defined in \autoref{DefFreeEnergies} is invariant under $x$--$y$ duality.
\end{conjecture}






















\section{Parametrization of the spectral curve by a decomposition of~$ydx$}\label{sec.parametrizeom01}

In this section, we shall describe a parametrization of the spectral curve by choosing a decomposition of the one-form $ydx$. This decomposition is not unique and follows from the singularity structure associated to $dx$ and $dy$ upon choosing a base point, logarithmic cuts and a fundamental domain. This will provide the set of parameters for which the variations of the correlators obtained from LogTR can be computed.

\begin{definition}[Residues of $dy$ and logarithmic part of $y$]\label{Proptdy}For any $a \in \mathcal{S}_y=\{a_1,\dots,a_M\}$, we have 
\beq \label{Vanishsumya} y_a=\underset{q\to a}{\Res}dy \in \mathbb{C}^* \,\,\text{with} \,\, \underset{a\in \mathcal{S}_y}{\sum} y_a=0.\eeq
The meromorphic one-form $\td{w}$:
\beq \td{\omega}:=dy-\sum_{a\in \mathcal{S}_y} y_a dS_{a,o}(q)  \eeq
defines a residue-free meromorphic one-form upon a choice of $\mathcal{A}$- and $\mathcal{B}$-cycles and a base point $o$.
From $\td{\omega}$, one can define by integration $\td{y}$
%\beq  d\td{y}(q)=dy-\sum_{a\in \mathcal{S}_y} y_a dS_{a,o}(q)\eeq
%and $\td{y}$ can be expressed using the prime form:
\beq \label{Vanishsumya2} \td{y}(q):=\int_o^q\td{\omega} = y(q) -\sum_{a\in \mathcal{S}_y} y_a  \ln \frac{E(q,a)}{E(q,o)}\eeq%\todo{I think one has to choose one more base point $o'$  such that $\ln \frac{E(q,a)}{E(o',a)}\frac{E(o',o)}{E(q,o)}$, this will also give $d_a\omega_{0,1}=dS_{q,o}(a)dx(q)$ which we had first.}
upon a choice of $\mathcal{A}$- and $\mathcal{B}$-cycles, and logarithmic cuts in the fundamental domain emerging at the base point $o$.
\end{definition}

\begin{remark} Note that the pole structure of  $\td{\omega}$ is independent of the basepoint $o$ since $\underset{a\in \mathcal{S}_y}{\sum} y_a=0$. Moreover note that, by definition, the function $\underset{a\in \mathcal{S}_y}{\sum} y_a \ln \frac{E(q,a)}{E(q,o)}$ is defined on $\Sigma\setminus \left(\underset{a\in \mathcal{S}_y}{\bigcup}\mathcal{C}_{o\to a}\right)$, i.e. the Riemann surface $\Sigma$ minus a set of cuts connecting $o$ to $a$ which depends on where the cuts are placed, and  everything furthermore depending on a choice of $\mathcal{A}$- and $\mathcal{B}$-cycles (Torelli marking). The choice of cuts is implicitly encoded in the definition of the logarithm function and consists of contractible paths connecting $o$ to $a$ that do not intersect (or self-intersect) except at $o$, and that avoids all poles of $dx$ and $dy$. 
%As we will show below, all interesting quantities, such as correlation functions and free energies should be independent of the choice of logarithmic cuts.
\end{remark}



\subsection{Local expansion of $ydx$}\label{Sec:localcorrdinate}
In this section, we shall define local coordinates around ramification and singular points of $ydx$. These local coordinates are the $x$-projected coordinates which will later provide canonical parameters that will be used in \autoref{SectionGlobalDec} for a parametrized decomposition of $ydx$.


\subsubsection*{Local coordinates around ramification points}
Let us first define local coordinates around a ramification point. We recall that from \autoref{MainAssumption}, the ramification points are away from the singularities of $dx$ and $dy$ and away from the logarithmic cuts. To be more specific, there exists an open neighborhood around the ramification points that do not intersect with $\mathcal{P}_x\cup \mathcal{P}_y\cup \underset{s\in \mathcal{S}_x}{\bigcup} \mathcal{C}_{o\to s}\cup \underset{s\in \mathcal{S}_y}{\bigcup} \mathcal{C}_{o\to s}$. In particular, when writing residues at ramification points, it implicitly means that the circle integral is taken within this neighborhood.

\begin{definition}[Local coordinates around a ramification point]\label{DefLocalCoordinateBranchPoint} Let $p\in \text{Ram}$ be a (simple from \autoref{MainAssumption}) ramification point. We shall define the local coordinate around $p$ as
\beq z_{p}(q):=\sqrt{x(q)-x(p)} \,\,\Rightarrow\,\, dx(q)=2z_{p}(q) dz_{p}(q)\eeq
\end{definition}

Note that $z_{p}(p)=0$ and $ydx$ is holomorphic in $z_p$ in a neighborhood of $p$.%:
%\beq ydx(q)\overset{q\to p}{=}\sum_{k=1}^\infty b_{p,k}z_{p}(q)^k dz_{p}(q)\eeq

\subsubsection*{Local coordinates around a singular point of $ydx$}

We shall now focus on local coordinates around a singular point $a$ of $ydx$. There are several cases that are described in the following definition.

\begin{definition}[Local coordinates at singularities of $ydx$]\label{DefLocalCoord}For any singularity $a$ of $ydx$, we shall define the local coordinates $z_a$ and local degree $d_a\in \mathbb{Z}$:
\begin{itemize}
    \item If $a$ is a pole of $dy$ but $x$ is regular at $a$ we shall define 
    \beq z_a(q):=%\frac{x(q)-x(a)}{x(o)-x(a)}
    x(q)-x(a)\eeq
    \item If $a$ is a pole of $dx$ of order $d_a+1\geq 2$ with possibly non-vanishing residue (i.e. $x(a)=\infty$ such that $x(q)\overset{q\to a}{=}\frac{\mu_a}{(q-a)^{d_a}} +o\left((q-a)^{-d_a}\right)$ for some $\mu_a\neq 0$) we shall define:
    \beq z_a(q):=%\left(\frac{x(o)}{x(q)}\right)^{\frac{1}{d_a}}
    \left(\frac{1}{x(q)}\right)^{\frac{1}{d_a}}
    \eeq
    where the $d_a$-branch is defined locally around $\infty=x(a)\in \mathbb{P}^1$. %and is analytically continued along a neighborhood of the logarithmic cut $\mathcal{C}_{o\to a}$ when $a\in \mathcal{S}_x$.
    \item If $a$ is a simple pole of $dx$ with non-vanishing residue $x_a$ we define $d_a=0$ and
    \beq z_a(q):=%\exp\left(\frac{x(q)-x(o)}{x_{a}}\right)
    \exp\left(\frac{x(q)}{x_{a}}\right)\eeq
\end{itemize}
In all cases, the local coordinates $z_a$ define a map from a neighborhood of $a$ into $\mathbb{P}^1$. %, including the logarithmic cut $\mathcal{C}_{o\to \alpha}$ and its neighborhood} when $\alpha\in \mathcal{S}_x$.
\end{definition}

\begin{remark}Note that from \autoref{MainAssumption}, \autoref{DefLocalCoordinateBranchPoint} and \autoref{DefLocalCoord} are consistent (because all cases are disjoint) and exhaust all possible types of singularities of $ydx$ or ramification points. 
\end{remark}

Note that in all cases we have $z_a(a)=0$. %and, if the local coordinates can be extended to the basepoint $o$ (for example if $\Sigma$ is of genus $0$), then the normalization has been set so that $z_a(o)=1$.

\medskip

The previous local coordinates at singular points of $ydx$ allow to define the local expansion of $ydx$.

\begin{proposition}[Local decomposition of $ydx$ and local potential $V_a$]\label{PropLocalCoord} Let $a\in \mathcal{P}_x\cup\mathcal{P}_y$ be a singular point of $ydx$ and denote $y_a:=\underset{q\to a}{\Res} dy \in \mathbb{C}$. Take $z_a$ the local coordinate at $a$ defined in \autoref{DefLocalCoord} and the associated value of $d_a\in \mathbb{Z}$. Then, the one-form $ydx$ can be locally written as:
\bea ydx(q)&\overset{q\to a}{=}&%y_a \ln \frac{E(q,a)}{E(q,o)} dx(q)
 y_a \ln z_a(q) dx(q)-\sum_{k=1}^{R_a} k\td{t}_{a,k}z_a(q)^{-k-1}dz_a(q)
+\td{t}_{a,0}\frac{dz_a(q)}{z_a(q)}+ d\td{v}_a(q) 
\eea
%\bea ydx(q)&\overset{q\to a}{=}&%y_a \ln \frac{E(q,a)}{E(q,o)} dx(q)
%\sum_{b\in \mathcal{P}} y_b \ln \frac{E(q,b)}{E(q,o)} dx(q)-\sum_{k=2}^{R_a+1} (k-1)\td{t}_{a,k-1}z_a(q)^{-k}dz_a(q)
%+\td{t}_{a,0}\frac{dz_a(q)}{z_a(q)}+ d\td{v}_a(q) \cr
%&:=& %y_a \ln \frac{E(q,a)}{E(q,o)} dx(q)
%\sum_{b\in \mathcal{P}} y_b \ln \frac{E(q,b)}{E(q,o)} dx(q)+d\td{V}_a(q) +\td{t}_{a,0}\frac{dz_a(q)}{z_a(q)}+ d\td{v}_a(q)
%\eea
%where the local potential $\td{V}_a$ is defined as
%\beq \td{V}_a(q):=\sum_{k=1}^{R_a} \td{t}_{a,k}z_a(q)^{-k}\eeq
where $d\td{v}_a$ is a local holomorphic one-form at $a$ and $R_a\in \mathbb{N}$ represents the order of singularity of $ydx$ at $a$. In other words, we have:
\beq \td{y}dx(q)\overset{q\to a}{=}-\sum_{k=1}^{R_a} k\td{t}_{a,k}z_a(q)^{-k-1}dz_a(q)
+\td{t}_{a,0}\frac{dz_a(q)}{z_a(q)}+ d\td{v}_a(q)\eeq
\end{proposition}

\begin{proof}The proof is similar to the one in \cite{EO07} after allowing logarithmic singularities of $y$. By Definition \ref{Proptdy}, one can subtract the logarithmic contribution 
\beq \td{y}dx(q)= ydx(q)-\sum_{b\in \mathcal{P}}y_b \ln \frac{E(q,b)}{E(q,o)} dx(q)\eeq
where $\td{y}$ is meromorphic in a neighborhood of $a$ from \autoref{Proptdy}. We assume here that $a$ is not a pole of $dx$, so that the term $\log z_a(q)dx(q)$ is always regular.
\end{proof}

\begin{definition}[Irregular times and monodromies]\label{DefTerminologyParameters}Similarly to the terminology of the standard topological recursion \cite{EO07}, we shall call the coefficients $\left(\td{t}_{a,k}\right)_{1\leq k\leq R_a}$ the \textit{irregular times} of $\td{y}dx$ at the singular point $a$, while $\td{t}_{a,0}$ is called the \textit{monodromy} of $\td{y}dx$ at $a$. Note that the sum of monodromies is vanishing:
\beq \label{VanishingMono} \underset{\alpha\in \mathcal{P}}{\sum}\td{t}_{\alpha,0}=0\eeq
since $\td{y}dx$ is a meromorphic one-form on $\Sigma$. The new coefficient $y_a$ appearing when $a\in \mathcal{S}_y$ shall be referred to as the \textit{log-time} at the singular point $a$.
\end{definition}


Similarly to the standard topological recursion, it is useful to observe that the irregular times and monodromies $\left(\td{t}_{a,k}\right)_{0\leq k\leq R_a}$ can be obtained as local residues at $a$.

\begin{proposition}[Irregular times and monodromies as local residues]\label{PropCoeffIntegralsSimple} For any singular point $a$ of $ydx$, we have:
\beq \forall \, k\in \llbracket 0,R_a\rrbracket\,:\, \Res_{q\to a}z_a(q)^k%\left(y(q)-y_a \ln \frac{E(q,a)}{E(q,o)}\right)
\td{y}dx(q)= -k\,\td{t}_{a,k}%\delta_{0<k\leq R_a}
+ \td{t}_{a,0}\delta_{k=0}\eeq
where local coordinates $z_a$ and the coefficients $\left(\td{t}_{a,k}\right)_{0\leq k\leq R_a}$ are defined from \autoref{DefLocalCoord}.
\end{proposition}

\begin{proof}The proof follows from the local decomposition of $\td{y}$ at $a$. Since $\td{y}dx$ is a meromorphic one-form, its residues $\td{t}_{a,0}$ must all be zero for the times to be well-defined in the recursion. For details, see \cite{EO07}.
\end{proof}

\begin{remark}Note that if $a$ is a pole of $dy$ with a non-vanishing residue $y_a\in \mathbb{C}^*$, then residues like $-\frac{1}{k}\underset{q\to a}{\Res} z_a(q)^k ydx$ are not well-defined since $ydx$ has a logarithmic cut at $a$ so a local circle integral is not well-defined. To avoid the confusion, we added a tilde on the irregular times and monodromies. Moreover note that
$-\frac{1}{k}\underset{q\to a}{\Res}z_a(q)^k\td{y}(q)dx(q)$ does not provide $\td{t}_{a,k}$ if $a$ is at the same time a pole of $dy$ with a non-vanishing residue $y_a\in \mathbb{C}^*$ and a pole of $dx$. %Indeed in that case the additional terms $-\frac{1}{k}\underset{q\to a}{\Res}z_a(q)^k \underset{b\neq a}{\sum}y_b \ln \frac{E(q,b)}{E(q,o)}dx(q)$ may provide a contribution from the fact that $a$ is a pole of $dx$.   
\end{remark}



%\begin{definition}[Logarithmic times]
%If $a_s\in \mathcal{S}_y$ is a LogTR-vital singular point, that is, $dy$ has non-vanishing residue and $x$ is regular, then the associate logarithmic time is defined by 
%\begin{align}
%    \Res_{q\to a_s}xdy=y_{a_s}x(a_s)=:t^{log}_{a_s}.
%\end{align}
%\end{definition}
%\begin{remark}
%    We want to emphasize that we are not associating time to singular points of $ydx$ where $dy$ and $dx$ have simultaneously poles (with or without vanishing residue, respectively). The reason is that we want a variation with respect to those times for fixed $x$ as it is done in the original paper \cite{EO07}. Thus, enforcing $x$ to be fixed as well as the singular structure of $ydx$ at these points, there is no variation possible, therefore no times associated with it. This is one way of parameterizing the moduli space of spectral curve.
%\end{remark}





\subsection{Global decomposition of $ydx$}\label{SectionGlobalDec}
Using the local decomposition of $ydx$ at its singularities, we shall propose a global decomposition of $ydx$ that will provide the canonical parameters for variations. Following \cite{EO07}, we shall first introduce the following quantities.

\begin{definition}[Definition of $(B_{a,k})_{k\geq 1}$ and $B_{a,0,o'}$]\label{DefBalphak}Let $a\in \mathcal{P}$ be a singular point of $ydx$ with local behavior given by \autoref{PropLocalCoord}. We define the following one-forms on $\Sigma$:
\beq \forall\,k\geq 1 \,:\, B_{a,k}(q):=\Res_{s\to a} B(q,s)z_a(s)^{-k}\,\,\text{ and }\, 
B_{a,0;o'}(q):=\int_{o'}^a B(.,q):=dS_{a,o'}(q)
\eeq
where $o'\in \Sigma$ is a fixed generic basepoint and the path integral is a contractible smooth path connecting $o' \to a$ avoiding all special points (ramification points, poles of $dx$ or $dy$) or special contour (logarithmic cuts).
\end{definition}

The previous quantities are meromorphic one-forms on $\Sigma$ and normalized on the $\mathcal{A}$-cycles (from the normalization of the Bergman kernel). Moreover, they have singularities that are similar to those of $ydx$ at $a$. More precisely:
\begin{itemize}
    \item For $k\geq 1$, $B_{a,k}$ is a meromorphic one-form on $\Sigma$ with only one pole at $a$ (with vanishing residue) and that locally behaves like
    \beq \forall\,k\geq 1 \,:\, B_{a,k}(q)\overset{q\to a}{=} -kz_a(q)^{-k-1}dz_a(q) + O(1)\eeq
    \item $B_{\alpha,0;o'}$ is a meromorphic one-form on $\Sigma$ with only two simple poles at $a$ and $o'$ with opposite residues. Locally around $a$ we have:
    \beq B_{a,0;o'}(q)\overset{q\to a}{=}\frac{d z_a(q)}{z_a(q)}+O(1)\eeq
\end{itemize}

We now have all the ingredients to write a global decomposition of $ydx$.

\begin{theorem}[Global decomposition of $ydx$]\label{TheoremGlobalDecompositionydx}Let $\left(\td{t}_{a,k}\right)_{a\in \mathcal{P},0\leq k\leq R_a}$ be the irregular times and monodromies defined from \autoref{PropCoeffIntegralsSimple}. Fixing a choice of logarithmic cuts for $ydx$, one can write a decomposition upon this choice as:
\bea ydx(q)&=&\sum_{a\in\mathcal{S}_y} y_a \ln \frac{E(q,a)}{E(q,o)} dx(q)+ \sum_{a\in \mathcal{P}}\left(\sum_{k=1}^{R_a}\td{t}_{a,k} B_{a,k}(q) +\td{t}_{a,0}B_{a,0,o'}(q)\right) +\sum_{i=1}^g \td{\epsilon}_i du_i(q)\cr
\text{i.e. }\td{y}dx(q)&=&\sum_{a\in \mathcal{P}}\left(\sum_{k=1}^{R_a}\td{t}_{a,k} B_{a,k}(q) +\td{t}_{a,0}B_{a,0,o'}(q)\right) +\sum_{i=1}^g \td{\epsilon}_i du_i(q)
\eea
where the parameters $(\td{\epsilon}_i)_{1\leq i\leq g}$ are defined by
$\forall\, i\in \llbracket 1,g\rrbracket\,:\, \td{\epsilon}_i:=\oint_{\mathcal{A}_i} \td{y}dx$.
\end{theorem}

\begin{proof}
Let us first mention that the decomposition is independent of the choice of $\mathcal{A}$- and $\mathcal{B}$-cycles because $ydx$ is a globally defined meromorphic differential. From Definition~\ref{Proptdy}, the one form $\td{y}dx$ has a unique decomposition regardless of the homology basis. The global definition and normalization of $B_{a,k}$ and $B_{a,0,o'}$ provides the usual decomposition of a one-form on a compact Riemann surface.
\end{proof}

\begin{remark}Note that the point $o'$ in the definition of $B_{\alpha,0,o'}$ is irrelevant for the global decomposition of $ydx$ since the sum of monodromies is vanishing from \eqref{VanishingMono}. Similarly, the point $o$ appearing in the prime form is irrelevant in the previous decomposition from \eqref{Vanishsumya2}.
\end{remark}


%\begin{remark} Note that $(\td{\epsilon}_i)_{1\leq i\leq g}$ corresponds to the filling fractions of $\td{y}dx$ and not $ydx$. Indeed, quantities like $\oint_{\mathcal{A}_i} ydx$ are not topologically well-defined. Indeed, when circling around a logarithmic cut of $y$ around a pole $a\in \mathcal{S}_y$, we get an additive factor $2i\pi$ so that $\oint_{\mathcal{A}_i} ydx\to \oint_{\mathcal{A}_i} ydx +2i\pi \oint_{\text{loop around }\alpha} dx$. And the last quantity is not necessarily null if $dx$ has a non-vanishing residue at $\alpha$. In other words, if both $dx$ and $dy$ have non-vanishing residues, then we must use $\td{y}dx$. 
%\end{remark}








\subsection{Parametrization of the spectral curve}\label{sec.parametrizespectralcurve}
\autoref{TheoremGlobalDecompositionydx} provides the set of parameters that we can use to characterize the spectral curve. 

\begin{corollary}[Parametrization of the spectral curve]\label{RemarkParametrization} The one-form  $ydx$ is parametrized by  
\begin{itemize}
    \item The positions $\left(a\right)_{a\in \mathcal{P}}$ of the singularities of $ydx$.
    \item The irregular times $\left(\td{t}_{a,k}\right)_{a\in \mathcal{P},1\leq k \leq R_a}$ of $\td{y}dx$.
    \item The monodromies $\left(\td{t}_{a,0}\right)_{a\in \mathcal{P}}$ of $\td{y}dx$.
    \item The ``filling fractions" $(\td{\epsilon}_i)_{1\leq i\leq g}$ of $\td{y}dx$.
    \item The log-times $\left(y_a\right)_{a\in \mathcal{S}_y}$ that correspond to the residues of $dy$ at its poles.
\end{itemize}
\end{corollary}

In the rest of the article, we will \textit{not} consider variations with respect to log-times. Moreover, in standard topological recursion, variations with respect to the position of poles of $ydx$ are not independent of the variations with respect to irregular times and monodromies and have therefore been omitted in \cite{EO07}. Equivalently in integrable systems, it is standard to only consider isomonodromic deformations, i.e. not to vary the monodromies but rather consider variations of the location of the poles instead. However, in the LogTR setting, it turns out that it is very natural to consider variations with respect to LogTR-vital singularities. This will provide new features that are specific to LogTR.   








\subsection{Deformations and rewriting using Bergman kernel's integrals}\label{SubsectionLambda}
For any irregular time, monodromy and filling fraction of $\td{y}dx$ associate an integral of the Bergman kernel analogously to \cite{EO07}, see also more recently \cite{Eynard:2023dha}. This formalism will be particularly convenient when dealing with variations since we will be able to regroup these cases under one notation. More precisely, to any of these parameters, denoted generically $t$,  we shall associate a one-form $\Omega_t$, a contour $\partial_{\Omega_t}$ and a function $\Lambda_t$ on $\Sigma$ such that
\beq \partial_t [\td{y}dx(q)]:=\Omega_t(q):=\int_{\partial_{\Omega_t}} B(q,s) \Lambda_t(s).\eeq
More precisely, we have:
\begin{itemize}
    \item For an irregular time $\left(\td{t}_{a,k}\right)_{a\in \mathcal{P}, k\geq 1}$, we have
    \beq \Omega_{\td{t}_{a,k}}(q):=B_{a,k}(q)=\Res_{s\to a} B(q,s)z_a(s)^{-k}=\oint_{\partial_{\Omega_{\td{t}_{a,k}}}}B(q,s)\Lambda_{\td{t}_{a,k}}(s)\eeq
    with $\Lambda_{\td{t}_{a,k}}(s):=\frac{1}{2i\pi} z_a(s)^{-k}$ and $\partial_{\Omega_{\td{t}_{a,k}}}:= \mathcal{C}_a$ a local loop around $a$.
    \item Deformations with respect to monodromies are constrained by the conditions $\underset{a \in \mathcal{P}}{\sum} \td{t}_{a,0}=0$. Thus, we may only consider $\partial_{\td{t}_{a,0}}-\partial_{\td{t}_{b,0}} $ with $a\neq b$ as deformations. In this case, we have
    \beq \Omega_{\td{t}_{a,0} -\td{t}_{b,0} }(q):= B_{a,0;o'}(q)-B_{b,0;o'}(q)=\int_{b}^{a} B(q,s)=\oint_{\partial_{\Omega_{\td{t}_{a,0}}-\td{t}_{b,0}}}B(q,s)\Lambda_{\td{t}_{a,0} -\td{t}_{b,0}}(s)\eeq
    with $\Lambda_{\td{t}_{a,0}-\td{t}_{b,0}}(s):=1$ and $\partial_{\Omega_{\td{t}_{a,0}-\td{t}_{b,0}}}:=[b,a]$ (or any oriented contractible smooth path connecting $b$ to $a$).    
    \item For a filling fraction $(\td{\epsilon}_i)_{1\leq i\leq g}$ we have 
    \beq \Omega_{\td{\epsilon}_{i}}(q):= du_i(q)=\frac{1}{2i\pi}\oint_{\mathcal{B}_i} B(s,q)=\oint_{\partial_{\Omega_{\td{\epsilon}_{i}}}}B(q,s)\Lambda_{\td{\epsilon}_{i}}(s)\eeq
    so $\Lambda_{\td{\epsilon}_{i}}(s):=\frac{1}{2i\pi}$ and $\partial_{\Omega_{\td{\epsilon}_{i}}}:=\mathcal{B}_i$.
\end{itemize}




\section{Variational formulas}\label{sec.variationalformula}
Variational formulas play an important role in the theory of standard TR. Instead of looking at a specific spectral curve, one can consider an infinitesimal deformation of the spectral curve and derive the corresponding variation of all correlators $\omega_{h,n}^{\text{EO}}$ in standard TR. The original variational formulas in \cite{EO07} are derived for variations corresponding to the parameters of $\td{y}dx$, consisting of irregular times, monodromies, and filling fractions. In the standard setting, the one-form $\omega_{0,1}^{\text{EO}}$ is assumed to be meromorphic, which implies that there is a unique expansion once a choice of $\mathcal{A}$- and $\mathcal{B}$-cycles on the compact Riemann surface is fixed. Roughly speaking, the variational formula in the standard setting has the form
\begin{align*}
    \delta_\Omega[\omega^{\text{EO}}_{h,m}(z_1,\dots,z_m)]
    =
    \int_{\partial_\Omega} \Lambda_\Omega(s)\, \omega^{\text{EO}}_{h,m+1}(z_1,\dots,z_m,s). 
\end{align*}

There is a striking compatibility between the dilaton equations and the variational formulas, even though the latter are derived from the recursive definition of standard TR. Taking the dilaton equations in the standard setting \eqref{standarddilaton}, 
\begin{equation}\label{standarddilaton2}
    (2-2h-n)\omega^{\text{EO}}_{h,n}(z_1,...,z_n)
    =
    \sum_{p\in \text{Ram}}
    \Res_{z'\to p}
    \Phi(z')\omega^{\text{EO}}_{h,n+1}(z',z_1,...,z_n),
\end{equation}
one can act on both sides with the variation $\delta_\Omega$. The variation commutes with the residue and acts by the Leibniz rule on $\Phi(z')=\int^{z'}\omega_{0,1}^{\text{EO}}$ and $\omega^{\text{EO}}_{h,n+1}(z',z_1,...,z_n)$ separately. The action on $\Phi(z')$ extracts a specific part of the decomposition of $\omega_{0,1}^{\text{EO}}$, whereas the action on $\omega^{\text{EO}}_{h,n+1}(z',z_1,...,z_n)$ produces $\delta_\Omega[(1-2h-n)\omega^{\text{EO}}_{h,n}]$. 

In summary, the action of $\delta_\Omega$ on the dilaton equation reduces to 
\begin{align*}
    \delta_\Omega[\omega^{\text{EO}}_{h,n}(z_1,...,z_n)]
    =
    \sum_{p\in \text{Ram}}
    \Res_{z'\to p}
    \delta_\Omega[\Phi(z')]\,
    \omega^{\text{EO}}_{h,n+1}(z',z_1,...,z_n),
\end{align*}
where the factor $(2-2h-n)$ on the left disappears due to the variation of $\omega^{\text{EO}}_{h,n+1}$ on the right, and only the variation of $\Phi(z')$ remains. Performing this variation and deforming the contour on a compact Riemann surface yields precisely the variational formula \eqref{standarddilaton2}. 

We mention this observation—that the variation of $\omega^{EO}_{h,n+1}$ in the dilaton equation cancels the factor $(2-2h-n)$, leaving only the variation of $\Phi(z')$—because the same structure persists in LogTR, not only for variations with respect to the classical times (irregular, monodromy, and filling fraction), but also for variations of the position of the LogTR-vital singularity.








\subsection{Variations in LogTR}\label{sec.variationsof}
In the previous section, we parametrized the spectral curve $ydx$ using several parameters described in \autoref{RemarkParametrization}. The next step is now to compute the variation of the correlators produced by LogTR with respect to these parameters.

In this paper, we shall \textbf{only consider variations at fixed map} $\mathbf{x}$ (this implies, for instance, that the ramification points are not modified by the variation). Thus, we have by definition
\beq\label{NoXvariation} \delta_\Omega[x]=0\eeq
As mentioned in \autoref{RemarkParametrization}, there are different types of parameters: location of the poles, irregular times, monodromies and filling fractions associated to $\td{y}dx$ and log-times. Note that since we only consider variations at fixed $x$, deformations with respect to the location of poles reduce only to deformations with respect to the location of poles of $dy$ where $x$ is regular. In the end, variations at fixed $x$ are provided by

\begin{itemize}
    \item Variations with respect to the location of poles of $dy$ such that $x$ is regular and $dy$ has vanishing residues.
    \item Variations with respect to the irregular times $(\td{t}_{\alpha,k})_{\alpha\in \mathcal{P},k\geq 1}$ associated to $\td{y}dx$.
     \item Variations with respect to the monodromies $(\td{t}_{\alpha,0})_{\alpha\in \mathcal{P}}$ associated to $\td{y}dx$.
     \item  Variations with respect to the filling fractions $(\td{\epsilon}_i)_{1\leq i\leq g}$ of $\td{y}dx$.
     \item Variations with respect to the location of poles of $dy$ with non-vanishing residues where $x$ is regular.
     \item Variations with respect to the log-times $y_\alpha$.
\end{itemize}


\subsection{Variational formulas with respect to parameters of $\td{y}dx$ for correlators}\label{SectionVartdydx}
In this section, we will only consider deformations generated by the first four types of parameters, i.e. location of poles of $dy$ such that $x$ is regular and $dy$ has vanishing residues, irregular times and monodromies and filling fractions associated to $\td{y}dx$, keeping the locations of poles of $dy$ with non-vanishing residues where $x$ is regular and the log-times fixed. The case of location of poles where $dy$ has residue will be done in \autoref{SectionVarVitalSing}.  

In fact, as in standard TR, these four types of deformations are not all independent. Indeed, from the global decomposition of $ydx$ given by \autoref{TheoremGlobalDecompositionydx}, variations with respect to locations of poles of $dy$ such that $x$ is regular and $dy$ has vanishing residues are given by a linear combination of the other three variations considered in this section. More precisely:
\beq \forall\, a\in \mathcal{P}_y \,/\, \Res_{q\to a}dy=0 \text{ and } x(a)\in \mathbb{C}:  \Omega_a=-x'(a)\sum_{j=2}^{R_a+1}(j-1)\td{t}_{a,j-1}\Omega_{\td{t}_{a,j}} +\td{t}_{a,0}B(a,q)  \eeq
Thus, as in standard TR \cite{EO07}, we will only consider variations with respect to irregular times, monodromies and filling fractions.

\smallskip

To simplify notations, we shall denote generically $\delta_\Omega$ the infinitesimal deformation that we consider and the deformations studied in this section are generated by linear combinations (as elements of the tangent space) of the following fundamental infinitesimal deformations:
\begin{itemize}
    \item $\delta_{\Omega}=\partial_{\td{t}_{\alpha,k}}$ for $k\in \llbracket 1,R_\alpha\rrbracket$, i.e. deformations with respect to an irregular time of $\td{y}dx$.
    \item $\delta_\Omega=\partial_{\td{t}_{\alpha_i,0}}- \partial_{\td{t}_{\alpha_j,0}}$ for $i\neq j$, i.e. deformations with respect to monodromies of $\td{y}dx$. Note that we must keep the relation $\underset{\alpha\in \mathcal{P}}{\sum}\td{t}_{\alpha,0}=0$ while performing deformations so that $\partial_{\td{t}_{\alpha,0}}$ is not possible.
    \item $\delta_\Omega=\partial_{\td{\epsilon}_i}$ for $i\in \llbracket 1,g\rrbracket$, i.e. deformations with respect to the filling fractions of $\td{y}dx$.
\end{itemize}
In other words, \textbf{we shall only consider variations with inside the Hurwitz space associated to $\td{y}dx$}. The important observation which we are going to prove is that the original variational formulas corresponding to the meromorphic one-form $\td{y}dx$ which hold in the case of standard TR perfectly extend to the LogTR correlators. Thus, LogTR is compatible with the standard variational formula.



%\underline{Variations of $\omega_{1,1}$ :}
%Let us now consider $\omega_{1,1}$ which is the first case where special terms arise in the logTR induction. In particular, it contains all the new features that appear in the proof by induction that we will perform below. By definition,
%\beq\label{Defomega11} \omega_{1,1}(z_1)=\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(z_1)}{\omega_k(q)}B(q,\sigma_k(q))-\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right) %\cr&&
%&=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}B(z,\sigma_i(z))+\sum_{s=1}^M\Res_{z\to a_s}dS_{o,z}(z_1)\omega_{1,1}(z) 
%\eeq
%The variation of the first term follows the diagrammatic rules of the variation of the standard TR because \autoref{LemmaVariationsRecursionKernel} holds. However, $\omega_{1,2}$ has factors $\omega_{1,1}$ in its decomposition that are missed by the standard diagrammatic rules. Thus, we must keep track of them.
%\bea  &&\delta_\Omega\left[\underset{i=1}{\overset{N}{\sum}}\underset{q\to p_i}{\Res}\frac{dE_{i,q}(z_1)}{\omega_i(q)}B(q,\sigma_i(q))\right] \overset{\autoref{LemmaVariationsRecursionKernel}}{=}\cr&&  2\sum_{j=1}^N\sum_{i=1}^N
%\Res_{q\to p_j}\Res_{r\to p_i}
%\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,\Omega(q)\,
%\frac{dE_{i,r}(q)}{\omega_i(r)}\, B(r,\sigma_i(r))
%+ \sum_{j=1}^N
%\Res_{q\to p_j}
%\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,
%\delta_{\Omega}[B(q,\sigma_j(q))] 
%\cr&&
%\overset{\eqref{Variationh0}}{=}2\sum_{j=1}^N\sum_{i=1}^N
%\Res_{q\to p_j}\Res_{r\to p_i}
%\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,\Omega(q)\,
%\frac{dE_{i,r}(q)}{\omega_i(r)}\, B(r,\sigma_i(r))
%\cr
%&&
%+ \int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
%\Res_{q\to p_j}
%\frac{dE_{j,q}(z_1)}{\omega_j(q)}\omega_{3,0}(s,q,\sigma_j(q)) 
%\cr&&
%\overset{\text{Def.}\Lambda_\Omega}{=}2\sum_{j=1}^N
%\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,\int_{\partial_\Omega}B(s,q)\Lambda_{\Omega}(s)\,\sum_{i=1}^N\Res_{r\to p_i}
%\frac{dE_{i,r}(q)}{\omega_i(r)}\, B(r,\sigma_i(r))
%\cr
%&&
%+ \int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
%\Res_{q\to p_j}
%\frac{dE_{j,q}(z_1)}{\omega_j(q)}\omega_{3,0}(s,q,\sigma_j(q)) 
%\cr&&
%=\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
%\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[
%\omega_{3,0}(s,q,\sigma_j(q)) +2B(s,q)\sum_{i=1}^N\Res_{r\to p_i}
%\frac{dE_{i,r}(q)}{\omega_i(r)}\, B(r,\sigma_i(r))
%\Big]\cr&&
%\overset{\eqref{Defomega11}}{=}\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
%\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[
%\omega_{3,0}(s,q,\sigma_j(q)) +B(s,q)\omega_{1,1}(\sigma_i(q))+B(s,\sigma_i(q))\omega_{1,1}(q)\Big]\cr
%&&+2\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
%\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}B(s,q)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(q)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
%\eea

%We have by definition:
%\bea \omega_{1,2}(z_1,s)=\sum_{j=1}^N\Res_{q\to p_j} \frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[\omega_{3,0}(s,q,\sigma_j(q)) +\omega_{1,1}(q)\omega_{0,2}(\sigma_j(q),s)+\omega_{1,1}(\sigma_j(q))\omega_{0,2}(q,s)\Big]\cr&&
%\eea
%Hence we get:
%\bea \label{Step1Deltaw11}
%&&\delta_\Omega\left[\underset{i=1}{\overset{N}{\sum}}\underset{q\to p_i}{\Res}\frac{dE_{i,q}(z_1)}{\omega_i(q)}B(q,\sigma_i(q))\right] =\int_{\partial_\Omega} \Lambda_\Omega(s)\omega_{1,2}(z_1,s)\cr
%&&+2\sum_{j=1}^N
%\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Omega(q)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(q)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
%\eea

%Our variations (fixed log-times) on the second term in \eqref{Defomega11} only provide contributions when acting on $dS_{a_s,z}(z_1)$ because $dx$ is kept invariant and the differential operator only depends on log-times. This variation is given by the variation of the Bergmann kernel \eqref{Rauch}:
%\bea \label{Step2Deltaw11}
%&&\delta_\Omega\left[\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\right]\cr&&
%=\sum_{s=1}^M\Res_{z\to a_s}\delta_\Omega[dS_{a_s,z}(z_1)]dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
%=-2\sum_{s=1}^M\Res_{z\to a_s}\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Omega(q)dS_{a_s,z}(q)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
%\eea
%Thus, we get by combining \eqref{Step1Deltaw11} and \eqref{Step2Deltaw11}:

%\bea \delta_\Omega[\omega_{1,1}(z_1)]&=&\int_{\partial_\Omega} \Lambda_\Omega(s)\omega_{1,2}(z_1,s)\cr
%&&+2\sum_{j=1}^N
%\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Omega(q)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(q)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
%-2\sum_{s=1}^M\Res_{z\to a_s}\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Omega(q)dS_{a_s,z}(q)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr
%&=&\int_{\partial_\Omega} \Lambda_\Omega(s)\omega_{1,2}(z_1,s)
%\eea


%\subsubsection{Variations of the correlators: Proof by induction}
In other words, we shall prove the following variational formulas:

\begin{theorem}[Variational formulas of the correlators for standard times]\label{TheoVariationalFormulas} For any variation $\delta_\Omega$ with respect to $(\td{t}_{a,k})_{a \in \mathcal{P},k\geq 0}$ and $(\td{\epsilon}_i)_{1\leq i\leq g}$ (i.e. fixed log-times and positions of the poles of $dy$ with non-vanishing residues and $x$ regular) with the associated $\Lambda_\Omega$ given in \autoref{SubsectionLambda}, then
\beq \forall \, (h,m)\in \mathbb{N}\times \mathbb{N}^*\setminus\{(0,1)\} \,:\, \delta_\Omega[\omega_{h,m}(z_1,\dots,z_m)]=\int_{\partial_\Omega} \Lambda_\Omega(s) \omega_{h,m+1}(z_1,\dots,z_m,s),\eeq
where $\omega_{h,n}$ is defined by LogTR.
%For any variation $\delta_\Omega=\underset{k=1}{\overset{M}{\sum}}\mu_j \partial_{y_j} \in \delta_{\Omega_{\text{log}}}$ (i.e. $\underset{k=1}{\overset{M}{\sum}}\mu_j=0$) we have
%\textcolor{red}{\beq \forall \, (h,m)\in \mathbb{N}\times \mathbb{N}^*\setminus\{(0,1)\} \,:\, \delta_\Omega[\omega_{h,m}(z_1,\dots,z_m)]=??
%\eeq}
%\delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j} \Res_{z'\to a_j} dS_{a_j,z'}(z_1)\omega_{h,1}(z') \eeq
\end{theorem}

\begin{proof}The proof is done by induction on $2h+m-2$. For the base case $(h,m)=(0,3)$, the variation $\delta_\Omega[\omega_{0,3}]$ is calculated by varying the spectral curve parameters in the algebraic equation $P(x,y)=0$, which matches the standard TR variation formula. The inductive step then follows.
\end{proof}

Note that we can check that the variational formulas of \autoref{TheoVariationalFormulas} are compatible with the dilaton equations of \autoref{TheoremDilatonEquation}, even if the dilaton equations differ in LogTR while the variational formula stays the same for variations with respect to the parameters of $\td{y}dx$. For completeness, this proof is presented in \autoref{AppendixCompatibilityDilatonVar}.

In addition to extending the dilaton equations, the definition of the free energies also extends the variational formulas. Indeed, we have the following theorems.


\begin{theorem}[Variational formulas of the free energies for standard times]\label{TheoVarFreenergiesStandardtimes} For any variation $\delta_\Omega$ with respect to $(\td{t}_{a,k})_{a \in \mathcal{P},k\geq 0}$ and $(\td{\epsilon}_i)_{1\leq i\leq g}$ (i.e. fixed log-times and positions of the poles of $dy$ with non-vanishing residues and $x$ regular) with the associated $\Lambda_\Omega$ given in \autoref{SubsectionLambda}, then
    \beq \forall\, h\geq 2\,:\, \delta_{\Omega}[\omega_{h,0}]=\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\omega_{h,1}(s)\eeq
\end{theorem}

\begin{proof}The proof follows by applying the variational formula for $\omega_{h,1}$ from \autoref{TheoVariationalFormulas} and integrating it. By assuming that $\delta_{\Omega}[\omega_{h,0}]$ satisfies the relation $\omega_{h,1} = d \frac{\partial \omega_{h,0}}{\partial \Omega}$, the result is obtained by substitution. 
\end{proof}

Finally, we also need to state the variational formulas for the special free energy $\omega_{1,0}=F_1$:

\begin{theorem}[Variational formulas for $F_1$ for standard times]\label{ThVarFormulaF1StandardTimes}For any variation $\delta_\Omega$ with respect to $(\td{t}_{a,k})_{a \in \mathcal{P},k\geq 0}$ and $(\td{\epsilon}_i)_{1\leq i\leq g}$ (i.e. fixed log-times and positions of the poles of $dy$ with non-vanishing residues and $x$ regular) with the associated $\Lambda_\Omega$ given in \autoref{SubsectionLambda}, then
    \beq \delta_\Omega[\omega_{1,0}]= \int_{\partial_\Omega} \omega_{1,1}(q) \Lambda_\Omega(q)\eeq
\end{theorem}

\begin{proof}\autoref{ThVarFormulaF1StandardTimes} is proved by considering variations of the irregular times $\td{t}_{a,k}$ for $k \geq 1$. The case of the residue $\td{t}_{a,0}$ is omitted as it does not contribute to the variation of the Bergman kernel in the $F_1$ formula.   
\end{proof}




\subsection{Variational formulas with respect to LogTR-vital singularities}\label{SectionVarVitalSing}
In this section, we shall now consider variations with respect to the positions of poles of $dy$ with non-vanishing residues and where $x$ is regular. This implicitly means that all other parameters are fixed (including the log-times $(y_\alpha)_{\alpha \in \mathcal{S}_y}$). For clarity let us define:
\beq \mathcal{S}_{y,0}=\{a\in \mathcal{P}_y\,/\, \Res_{q\to a} dy=y_a\neq 0\, \text{ and } x(a)\in \mathbb{C}\}.\eeq
Note that from \autoref{MainAssumption}, for any $a\in \mathcal{S}_{y,0}$ we have $dx(a)\neq 0$ because ramification points are assumed to differ from the poles of $dy$.

Performing variations with respect to the positions of poles $a\in \mathcal{S}_{y,0}$ generates two different contributions: the first one from the variations of the logarithmic part of $ydx$ at $a$ (i.e. variations of $y_a\ln \frac{E(q,a)}{E(q,o)} dx$) and the second one from variations of $(B_{a,k})_{k\geq 1}$ and $B_{a,0,o'}$ appearing in the global decomposition of $ydx$ (\autoref{TheoremGlobalDecompositionydx}). However, similarly to the position of poles of $dy$ with vanishing residues, this second contribution corresponds to a linear combination of variations with respect to the irregular times $(t_{a,k})_{k\geq 1}$ and monodromy $t_{a,0}$ of $\td{y}dx$ at $a$. Therefore, this second contribution is already encoded by the results of \autoref{TheoVariationalFormulas} and of \autoref{SectionVartdydx} and we shall ignore it in this section.
\smallskip

Thus, in this section, we will focus only on the variations of the position of a pole $a\in \mathcal{S}_{y,0}$ which is a simple pole of $dy$, i.e. \textbf{only variations with respect to a LogTR-vital singularity $\left(a_s\right)_{1\leq s\leq M}$} and we shall denote it $\delta_\Omega=\partial_{a_s}$ for $s\in \llbracket 1,M\rrbracket$ in the rest of this section. 

The main theorem is the following:

\begin{theorem}[Variations of the correlators with respect to LogTR-vital singularities]\label{TheoVariationsLogTRpoles}Let $r\in \llbracket 1,M\rrbracket$ then we have for any $(h,n)\in \mathbb{N}\times\mathbb{N}^*\setminus \{(0,1)\}$:
%\bea &&d_{a_r}[\omega_{h,n}(z_1,\dots,z_n)]%= %y_{a_r}\Big[dx(a_r)\int_o^{a_r} \omega_{h,n+1}(z_1,\dots,z_n,.) \cr&&
%- \frac{1}{2i\pi}\sum_{j=1}^g\left(\oint_{s\in\mathcal{A}_j} dS_{o,s}(a_r) dx(s)\right)\left(\oint_{B_j} \omega_{h,n+1}(z_1,\dots,z_n,.)\right)\cr&&
%+\sum_{\beta \text{ poles of } dx} \Res_{q\to \beta} dS_{o,q}(a_r) dx(q)\left(\int_o^q\omega_{h,n+1}(z_1,\dots,z_n,.)\right)\Big]\cr
%= y_{a_r}\sum_{i=1}^N \Res_{q\to p_i} %\left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right)
%d_{a_r}[\Phi_{p_i}(q)]
%\omega_{h,n+1}(z_1,\dots,z_n,q)\cr
%&&+ y_{a_r}da_r\sum_{k=1}^h \left([\hbar^{2k}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k,n+1}(z_1,\dots,z_n,q)}{dx(q)} \right)_{|\, q=a_r}\cr&&
%\eea
\bea d_{a_r}[\omega_{h,n}(z_1,\dots,z_n)] 
&=& \sum_{i=1}^N \Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)] \omega_{h,n+1}(z_1,\dots,z_n,q)\cr\label{NewVariation}
&&+  \Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,n+1}(q,z_1,\dots,z_n).
\cr&&
\eea
where $d_{a_r}[\Phi_{p_i}(q)]=\int_{p_i}^q \Omega_{a_r}$ is the local anti-derivative of $\Omega_{a_r}(q)=y_{a_r}d_{a_r}[\ln E(a_r,q)] dx(q)$ defined locally around $p_i$ and we have denoted $d_{a_r}[f]:=da_r\, \partial_{a_r}[f]$. 
\end{theorem}

\begin{proof}The proof is done by showing that the variation with respect to the position of a pole $a_r$ is equivalent to a variation of the complex structure of the surface $\Sigma$. Since the free energies are topological invariants, this variation must vanish, leading to the formula.
\end{proof}


%\autoref{TheoVariationsLogTRpoles} is equivalent to the following formulation:  

%\begin{corollary}[Equivalent formula for the variational formula for $\omega_{h,n}$]\label{ReformulationVar}
%    A more compact form of the variational formula is
%    \bea d_{a_r}[\omega_{h,n}(z_1,\dots,z_n)] 
%&=& \sum_{i=1}^N \Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)] \omega_{h,n+1}(z_1,\dots,z_n,q)\cr\label{NewVariation}
%&&+  \Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,n+1}(q,z_1,\dots,z_n).
%\cr&&
%\eea
%\end{corollary}
%\begin{proof}The proof is done in \autoref{SectionReform}.
%\end{proof}

For completeness, one can check that the variational formulas \autoref{TheoVariationsLogTRpoles} are compatible with the dilaton equations of \autoref{TheoremDilatonEquation}. This is carried out in \autoref{AppendixCompatVarLogTR}.

Returning to the discussion at the beginning of the section on how the variational formula can be compared with the dilaton equation, we would like to emphasize the following structure. Recall the dilaton equation in LogTR (\autoref{TheoremDilatonEquation}):
\bea\label{DilatonEquation2}
(2-2h-k)\omega_{h,k}(z_1,\dots,z_k)
&=&
\sum_{i=1}^N \Res_{z\to p_i} \Phi(z)\omega_{h,k+1}(z,z_1,\dots,z_k)
\cr&&
-\sum_{j=1}^M \Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
\overset{h}{\underset{h_1=1}{\sum}}
\omega_{h_1,1}(z)\omega_{h-h_1,k+1}(z,z_1,\dots,z_k).
\cr&&
\eea

Acting on this equation with a variation with respect to $a_r$ yields a remaining contribution on $\Phi(z)$ and on $\frac{x(z)-x(a_j)}{dx(z)}$, with $j=r$. The action on the correlators produces precisely a cancellation of the prefactor $(2-2h-k)$ on the left-hand side. It is striking that this structural feature persists in the setting of LogTR, in particular for variations of LogTR-vital singularities.\\




Finally, we derive the variational formulas for the free energies defined in the setting of LogTR (see \autoref{DefFreeEnergies}). We have the following variational formulas



\begin{theorem}[Variations of the free energies with respect to LogTR-vital singularities]\label{VariationalFormulaLogTRPole}\sloppy{For any $r\in \llbracket 1,M\rrbracket$ and any $h\geq 2$, we have:
\bea \label{EqToProve}&& d_{a_r}[\omega_{h,0}]=\sum_{i=1}^N\Res_{z\to p_i} d_{a_r}[\Phi_{p_i}(z)]\omega_{h,1}(z) +\frac{1}{2}\Res_{z\to a_r}\frac{dx(a_r)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,1} (z)\cr&&
-\Res_{z\to a_r} dx(a_r) dy(z) \int_o^z\omega_{h,1}-\sum_{j=1}^M\Res_{z\to a_j} d_{a_r}[y(z)] dx(z)\int_o^z\omega_{h,1}
\eea
where $d_{a_r}[\Phi_{p_i}(z)]=y_{a_r}\int_{q=p_i}^{q=z} d_{a_r}[\ln (E(a_r,q))] dx(q)$ that is locally holomorphic near the ramification points. The last formula is equivalent to 
\bea \label{EqToProve2}&& d_{a_r}[\omega_{h,0}]=\Res_{z\to \{p_i\}\cup \{a_j\}} d_{a_r}[\Phi(z)]\omega_{h,1}(z) +\frac{1}{2}\Res_{z\to a_r}\frac{dx(a_r)}{dx(z)}\overset{h}{\underset{h_1=0}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,1} (z)
\eea
provided that we regroup $\underset{z\to a_r}{\Res} d_{a_r}[\Phi(z)] \omega_{h,1}(z)$ with $\underset{z\to a_r}{\Res} \frac{dx(a_r)}{dx(z)} \omega_{h,1}(z) ydx(z)=dx(a_r)\underset{z\to a_r}{\Res} \omega_{h,1}(z) y(z)$ to have something well-defined in the second formulation.}
\end{theorem}

\begin{proof}The proof is done in \autoref{AppendixProofVarationalFormulasLogR}.
\end{proof}

We also state separately the variational formula for the special free energy $\omega_{1,0}=F_1$:



\begin{theorem}[Variational of $F_1$ with respect to LogTR-vital singularities]\label{ThVarFormulaF1LogTRTimes}
For any $r\in \llbracket 1,M\rrbracket$:
\beq d_{a_r}[\omega_{1,0}] =\Res_{z\to \{p_i\}\cup \{a_j\}} d_{a_r}[\Phi(z)]\omega_{1,1}(z) +\Res_{z\to a_r}dx(a_r)y(z)\omega_{1,1} (z).\eeq
\end{theorem}

\begin{proof}\autoref{ThVarFormulaF1LogTRTimes} is proved in \autoref{AppendixVarF1LogTR}.
\end{proof}

Let us compare, for the free energies, the dilaton equations with the variational formulas, as mentioned at the beginning of the section for the standard TR setting. The definition of the free energies was rather involved \autoref{DefFreeEnergies}:
\bea \label{FormulasDefFg2}
(2-2h)\omega_{h,0}
&=&
\sum_{i=1}^N \Res_{z\to p_i} \Phi(z)\omega_{h,1}(z)
\cr&&
-\sum_{s=1}^M \Res_{z\to a_s}\big(x(z)-x(a_s)\big)\left(\frac{1}{2}
\overset{h-1}{\underset{h_1=1}{\sum}}
\frac{\omega_{h_1,1}(z)\omega_{h-h_1,1}(z)}{dx(z)}
- dy(z)\int_o^z \omega_{h,1}\right).
\cr&&
\eea

However, taking the derivative with respect to $a_r$ again yields precisely the remaining action in \eqref{EqToProve} on $\Phi(z)$, $\big(x(z)-x(a_s)\big)$, and $dy(z)$, after canceling the factor $(2-2h)$ coming from the variation of the correlators. Even more interesting is the formulation of the variational formula in \eqref{EqToProve2}, which can be written in this form precisely because there is a corresponding cancellation arising from the quadratic term in the correlators. 

Even though $\Phi(z)$ and $\omega_{0,1}$ have logarithmic singularities where the residue is not defined, our derivation shows how this is regularized in the correct manner. This type of regularization is not needed for algebraic curves (standard TR), i.e.\ when $x$ and $y$ are meromorphic.

Finally, let us emphasize that all computations regarding the dilaton equation and the variational formulas are derived purely from the recursive definition of LogTR. However, the striking compatibility and similarity between the dilaton equation and the variational formula constitute a nontrivial consequence.



\section{Conclusion and future directions}

In this article, we have studied global and local geometric properties arising in LogTR, an extension of the standard Eynard--Orantin topological recursion obtained by allowing $dy$ to have residues at points where $dx$ is regular. It is known that standard TR yields incorrect enumerative invariants in this situation, whereas LogTR produces the expected ones. This can also be understood via limiting procedures, where TR converges to LogTR precisely in this regime.

We derived the dilaton equation for LogTR for all $\omega_{h,n}$, which naturally leads to a definition of the free energies in this framework. We have verified that this definition reproduces the expected free energies in two examples: for the half Seiberg--Witten curve, corresponding to the perturbative sector of $4d$ $\mathcal{N}=2$ pure supersymmetric gauge theory, and for the mirror curve of strip geometries, reproducing the Gromov--Witten invariants of the corresponding Calabi--Yau threefold.

We then studied, under suitable assumptions, a decomposition of $\omega_{0,1}$ (analogous to the standard TR setting), allowing for additional logarithmic contributions. Based on this decomposition, we analyzed the variation of the LogTR differentials with respect to the associated parameters. In particular, we investigated variations with respect to the LogTR-vital singularities, namely those points responsible for the difference between TR and LogTR. All such variations are shown to be compatible with the dilaton equations, providing further support for the proposed definition of the free energies.

We emphasize that the variational formulas with respect to LogTR-vital singularities differ significantly from the usual variational formulas. This suggests that these parameters do not belong to the same class as the standard times used in TR. It would therefore be interesting to study variations of both TR and LogTR with respect to alternative sets of parameters, such as the positions of the ramification points. This cannot be done while keeping $x$ fixed. It is natural to expect that LogTR-vital singularities play a role analogous to ramification points, since in certain limits of standard TR, the latter converge to the former. We plan to investigate this in future work. We hope that this will lead to a better understanding of variational formulas, in particular for mirror curves, where such results have not yet been rigorously established.

There are several further research directions arising from the geometric understanding of LogTR:
\begin{itemize}
    \item \textbf{Quantum curves in $\mathbb{C}^*$:} One of the main motivations for studying variational formulas in LogTR is their application to quantum curve constructions, where such formulas are essential. It is known that, under suitable assumptions, standard TR with meromorphic $x,y$ leads to quantum curves constructed from the Eynard--Orantin differentials \cite{Norbury_survey,BouchardEynard_QC,Iwaki-P1,MO19_hyper,EGF19,Quantization_2021}. In higher genus, non-perturbative contributions related to filling fractions arise through variational formulas. However, for curves in $\mathbb{C}^*$, no general results on quantum curves are known; only case-by-case studies exist \cite{Marchal:2017ntz,ALS,Banerjee:2025shz}. From our perspective, this is largely due to the lack of a systematic understanding of variational formulas in this setting. The present work constitutes an important step in this direction. In particular it should be essential to write the corresponding KZ equations and obtain the difference equations that are expected to replace standard differential equations as derived in \cite{Quantization_2021}.

    \item \textbf{Applications to knot theory:} One expected application of standard TR (and hence also LogTR) is to knot theory \cite{Gukov:2011qp,Brini:2011wi,BEApol}. Certain spectral curves give rise to knot invariants via the associated differentials. While no general framework is currently available, these curves typically lie in $\mathbb{C}^* \times \mathbb{C}^*$, suggesting that LogTR is the appropriate formalism, especially in situations involving limits, where it behaves well. Examples include the $A$-polynomial and related constructions \cite{Brini:2011wi}.


\item \textbf{Augmentation varieties:} Another class of spectral curves of interest in knot theory, motivated by large $N$ duality and knot contact homology, is given by augmentation varieties \cite{Aganagic:2012jb}. These curves also lie in $\mathbb{C}^*\times\mathbb{C}^*$. A modified topological-recursion framework for augmentation varieties was proposed in \cite{Gu:2014yba}, where a calibrated annulus kernel is introduced and checked for torus knots. Moreover, the planar free energy extracted from augmentation varieties was shown to agree with the quantum part of the planar free energy of the resolved conifold in several examples. This suggests that it would be very interesting to revisit augmentation varieties from the viewpoint of LogTR, in particular to understand whether logarithmic effects and the corresponding variational formulas provide a more natural and possibly more general framework for knot-theoretic spectral curves.


    \item \textbf{Refined structures:} In our examples for the free energies, we observed that residues of $dy$ at LogTR-vital singularities generate structures reminiscent of refined topological string theory. In particular, the usual Bernoulli numbers are replaced by double Bernoulli numbers when allowing general residues $y_{a_s}$. Such structures also appear in various refined settings. It remains unclear how these different refinements are related. It is conceivable that they arise from higher-dimensional theories, such as Calabi--Yau fivefolds recently studied in \cite{Brini:2024gtn,schuler2026gromovwitteninvariantsmembraneindices}, which reduce to known refinements under suitable specializations.
\end{itemize}























\renewcommand{\theequation}{\thesection-\arabic{equation}}
\appendix




\begin{comment}

\section{Proof of  \autoref{LemmaRegularityComb}}\label{AppendixLemmaRegularityComb}
Let us first observe that the quantity involved in \autoref{LemmaRegularityComb} is obviously meromorphic in a neighborhood of $z=a_s$. Indeed, the logTR-vital singularities are away from the logarithmic cuts of $x$ so that $x(z)$ is holomorphic in a punctured neighborhood of $z=a_s$. Thus, \autoref{LemmaRegularityComb} is equivalent to prove that
\small{\beq \partial_z\Big[(x(z)-x(a_s))[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\Big]
+(2h-1)x'(z) [\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\overset{z\to a_s}{=}O(1)\eeq}
This holds for $h=0$ since it simplifies into $\frac{x(z)-x(a_s)}{z-a_s}\overset{z\to a_s}{=}O(1)$.

\medskip

Let us now consider $h\geq 1$. Since $\partial_z= x'(z) \partial_x$ and $x'(z)$ is regular at $z=a_s$, \autoref{LemmaRegularityComb} is equivalent to
\beq  \label{EqOO}\partial_x\Big[(x(z)-x(a_s))[\hbar^{2h}]\left(\frac{1}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\Big]
+(2h-1) [\hbar^{2h}]\left(\frac{1}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\overset{z\to a_s}{=} O(1)\eeq
Let us write 
\beq \frac{1}{\mathcal{S}(u)}=\frac{u}{e^{\frac{u}{2}} -e^{-\frac{u}{2}}}:=\sum_{j=0}^{\infty} \beta_{2j} u^{2j} \,\,,\,\, \forall \, u\in \mathbb{C}\eeq
Then \eqref{EqOO} is equivalent to 
\beq  \partial_x\Big[(x(z)-x(a_s))\beta_{2h}y_{a_s}^{-2h}\frac{\partial^{2h}}{\partial x^{2h}} \ln(z-a_s) \Big]
+(2h-1) \beta_{2h} y_{a_s}^{-2h}\frac{\partial^{2h}}{\partial x^{2h}} \ln(z-a_s)\overset{z\to a_s}{=} O(1)\eeq
i.e.
\beq  \partial_x\Big[(x(z)-x(a_s))\frac{\partial^{2h}}{\partial x^{2h}} \ln(z-a_s) \Big]
+(2h-1) \frac{\partial^{2h}}{\partial x^{2h}} \ln(z-a_s)\overset{z\to a_s}{=} O(1)\eeq
or equivalently
\beq (x(z)-x(a_s))\frac{\partial^{2h+1}}{\partial x^{2h+1}} \ln(z-a_s) 
+2h \frac{\partial^{2h}}{\partial x^{2h}} \ln(z-a_s)\overset{z\to a_s}{=} O(1)\eeq
From the fact that $(x(z)-x(a_s))\frac{\partial}{\partial x}\ln(z-a_s)= \frac{x(z)-x(a_s)}{x'(z)(z-a_s)}$ is holomorphic at $z=a_s$, we have
\beq \forall \, j\geq 0\,:\, 
(x(z)-x(a_s)) \frac{\partial^{j+1}}{\partial x^{j+1}} \ln(z-a_s) +j \frac{\partial^{j}}{\partial x^{j}}\ln(z-a_s)=\frac{\partial^{j}}{\partial x^j}\left((x(z)-x(a_s))\frac{\partial}{\partial x} \ln(z-a_s)\right)=O(1)\eeq
Taking $j=2h$ gives
\beq (x(z)-x(a_s)) \frac{\partial^{2h+1}}{\partial x^{2h+1}} \ln(z-a_s) +2h \frac{\partial^{2h}}{\partial x^{2h}}\ln(z-a_s)=O(1)\eeq 
ending the proof of the \autoref{LemmaRegularityComb}.


%\section{Proof of \autoref{LemmaIntW02Wg1}}\label{AppendixDilatonProofTechLemma}
%Let $h\geq 1$ and insert the definition of LogTR in the r.h.s. of \eqref{EqLemmeIntW02WG1}:
%\small{\bea &&\text{RHS}_h(z_1):=\sum_{s=1}^M\Res_{z'\to a_s}\frac{(x(z')-x(a_s))}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z_1)\cr
%&&\overset{\eqref{DefLogTR}}{=}-\sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{0,2} (z',z_1)\sum_{i=1}^M\Res_{z\to a_i}\left(\int_{a_i}^z\omega_{0,2}(z',.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)\cr
%&&=-\sum_{s=1}^M\Res_{z'\to a_s}\frac{(x(z')-x(a_s))}{dx(z')}\omega_{0,2} (z',z_1)\sum_{i=1}^M\Res_{z\to a_i}\left(\int_{a_i}^z\omega_{0,2}(.,z')\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)\cr
%&&\eea}
%\normalsize{where} we have used the fact that the residues at $z'=a_s$ only require the singular part of $\omega_{h,1}(z')$ at $z'=a_s$. Moreover, the last equality comes from the symmetry of the Bergman kernel. We now exchange the residues:
%\beq \label{ExchangeRes2} \sum_{s=1}^M\Res_{z'\to a_s}\sum_{i=1}^M\Res_{z\to a_i}=\sum_{i=1}^M\Res_{z\to a_i}\sum_{s=1}^M\Res_{z'\to a_s}+\sum_{s=1}^M\Res_{z'\to a_s}\Res_{z\to z'}
%\eeq
%The first residue is
%\small{\beq 0=\sum_{i=1}^M\Res_{z\to a_i} dx(z) [\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)  \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{0,2} (z',z_1)\left(\int_{a_i}^z\omega_{0,2}(.,z')\right)
%\eeq}
%\normalsize{Indeed}, in the last residue $z'\mapsto \frac{x(z')-x(a_s)}{dx(z')}\omega_{0,2} (z',z_1)$ is regular at $z'=a_s$. Moreover, $z'\mapsto \int_{a_i}^z\omega_{0,2}(.,z')$ has only (simple) poles at $z'=a_i$ and $z'=z$. Thus, if $s\neq i$, the integrand is regular at $z'=a_s$ and the residue is null. For $s=i$, $z'\mapsto \int_{a_i}^z\omega_{0,2}(.,z')$ has a simple pole at $z'=a_s$ but $\frac{x(z')-x(a_s)}{dx(z')}\omega_{0,2} (z',z_1)= O(z'-a_s)$ so the integrand is also regular at $z'=a_s$ and the residue is null too. \todo{One could directly use the same argument  $\frac{x(z')-x(a_s)}{dx(z')}\omega_{0,2} (z',z_1)= O(z'-a_s)$ directly for the case $i\neq s$ as well to make the proof shorter.}

%\medskip

%Since the first residue is vanishing, we end up with:
%\small{\bea &&\text{RHS}_h(z_1)=-\sum_{s=1}^M\Res_{z'\to a_s} \frac{x(z')-x(a_s)}{dx(z')}\omega_{0,2} (z',z_1)\Res_{z\to z'}\left(\int_{a_s}^z\omega_{0,2}(.,z')\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
%=-\sum_{s}\Res_{z'\to a_s} \frac{(x(z')-x(a_s))}{dx(z')}\omega_{0,2} (z',z_1)dx(z')[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z'-a_s) \right)\cr&&
%=-\sum_{s=1}^M\Res_{z\to a_s}\omega_{0,2} (z,z_1) (x(z)-x(a_s))[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
%\eea}
%\normalsize{where} we have used the fact that $z'\mapsto \int_{a_s}^z\omega_{0,2}(.,z')\overset{z'\to z}{=} \frac{1}{z'-z} +O(1)$. We now integrate by part in the residue to get:
%\small{\beq\label{RHSRes} \text{RHS}_h(z_1)=\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^{z}\omega_{0,2} (.,z_1)\right) \partial_z\Big[ (x(z)-x(a_s))[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\Big]dz
%\eeq}

%\normalsize{Let} us now proceed from the l.h.s. of \eqref{EqLemmeIntW02WG1} using the definition of logTR:
%\bea  &&\text{LHS}_{h}(z_1):=(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{o}^{z'} \omega_{0,2}(., z_1)\right)\omega_{h,1}(z')\cr
%&&\overset{\eqref{DefLogTR}}{=}-(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{o}^{z'} \omega_{0,2}(., z_1)\right)
%\sum_{i=1}^M\Res_{z\to a_i}\left(\int_{a_i}^z\omega_{0,2}(z',.)\right)dx(z)\cr&&
%[\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)
%\eea
%where we have used the fact that the residues at $z'=a_s$ only require the singular part of $\omega_{h,1}(z')$ at $z'=a_s$. Note that we also used the symmetry of the Bergman kernel. We exchange the residues using \eqref{ExchangeRes2}. The first residue is 
%\small{\bea\label{FirstPartRes}  &&-(2h-1)\sum_{i=1}^M\Res_{z\to a_i} [\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)   dx(z)
%\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{o}^{z'} \omega_{0,2}(., z_1)\right)\left(\int_{a_i}^z\omega_{0,2}(z',.)\right) \cr&&
%=(2h-1)\sum_{i=1}^M\Res_{z\to a_i} [\hbar^{2g}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)   dx(z) \left(\int_{o}^{a_i} \omega_{0,2}(., z_1)\right)\cr&&
%=(2h-1)\sum_{i=1}^M\Res_{z\to a_i}\left(\int_{o}^{a_i} \omega_{0,2}(., z_1)\right)dx(z) [\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)   
%\eea}
%\normalsize{where} we have used the fact that $z'\mapsto \int_{a_i}^z\omega_{0,2}(z',.)\overset{z'\to a_i}{=} -\frac{1}{z'-a_i} +O(1)$ and is regular at $z'=a_s$ is $s\neq i$. The second residue is
%\small{\bea\label{SecondPartRes}&&-(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{o}^{z'} \omega_{0,2}(., z_1)\right)
%\Res_{z\to z'}\left(\int_{a_s}^z\omega_{0,2}(z',.)\right)dx(z)
%[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right) \cr&&
%= -(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{o}^{z'} \omega_{0,2}(., z_1)\right)dx(z')[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z'-a_s) \right)
%\eea}
%\normalsize{where} we have used the fact that $z'\mapsto \int_{a_s}^z\omega_{0,2}(z',.)\overset{z\to z'}{=} \frac{1}{z-z'} +O(1)$. Combining \eqref{FirstPartRes} with \eqref{SecondPartRes} into \eqref{ExchangeRes2} we find:
%\bea \label{LHSRes} &&\text{LHS}_{h}(z_1)=(2h-1)\sum_{i=1}^M\Res_{z\to a_i}\left(\int_{o}^{a_i} \omega_{0,2}(., z_1)\right) dx(z)[\hbar^{2h}]\left(\frac{y_{a_i}}{\mathcal{S}(y_{a_i}^{-1}\hbar \partial_x)}\ln(z-a_i) \right)    \cr&&
%-(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{o}^{z'} \omega_{0,2}(., z_1)\right)dx(z')[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z'-a_s) \right)\cr&&
%=-(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \left(\int_{a_s}^{z'} \omega_{0,2}(., z_1)\right)dx(z')[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z'-a_s) \right)\cr&&
%=-(2h-1)\sum_{s=1}^M \Res_{z\to a_s} \left(\int_{a_s}^{z} \omega_{0,2}(., z_1)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
%\eea
%Thus, combining \eqref{RHSRes} and \eqref{LHSRes}, we have
%\bea &&\text{RHS}_h(z_1)-\text{LHS}_h(z_1)=\cr&&
%\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^{z}\omega_{0,2} (.,z_1)\right) \partial_z\Big[(x(z)-x(a_s))[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\Big]dz\cr&&
%+(2h-1)\sum_{s=1}^M \Res_{z\to a_s} \left(\int_{a_s}^{z} \omega_{0,2}(., z_1)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
%= \sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^{z}\omega_{0,2} (.,z_1)\right) \Bigg( \partial_z\Big[(x(z)-x(a_s))[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\Big]dz \cr&&
%+(2h-1) dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\Bigg)
%\eea
%Using \autoref{LemmaRegularityComb} and the fact that $z\mapsto \int_{a_s}^{z}\omega_{0,2} (.,z_1)$ is regular at $z=a_s$, we get that the integrand is regular at $z=a_s$ so that the residue is vanishing. In the end, we find:
%\beq \text{RHS}_h(z_1)-\text{LHS}_h(z_1)=0\eeq
%ending the proof.

\end{comment}

\section{Proof of \autoref{TheoremDilatonEquation}}\label{AppendixDilatonProof}
The proof is done by induction on $2h+k$. Initialization is a direct consequence of the fact that the dilaton equations holds for any $(h=0,k)$ with $k\geq 2$. Indeed, correlation functions $\omega_{0,k}(z_1,\dots,z_k)$ are the same as in the standard topological recursion (in its local version since $(x,y)$ are not necessarily meromorphic function on $\Sigma$) and thus satisfying the standard topological recursion dilaton equations:
\beq -(k-2)\omega_{0,k}(z_1,\dots,z_k)=\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{0,k+1}(z,z_1,\dots,z_k)\eeq
Finally, for $h=0$, the sum with respect to the LogTR-vital singularities in the r.h.s. of the dilaton equation is empty hence proving that \eqref{DilatonEquation} holds for $h=0$. In particular, the induction is initialized as the subcase $(h,k)=(0,2)$. 


\medskip

Let $k\geq 1$ and $h\geq 0$ with $(h,k)\notin\{(0,1)\}$ and assume that the property  \eqref{DilatonEquation} holds for any $(h',m)\neq (0,1)$ such that $2h'+m<2h+k$. Consider the r.h.s. of \eqref{DilatonEquation} and insert the definition of LogTR:
\bea &&\text{RHS}_{h,k}(z,z_1,\dots,z_{k-1}):=\sum_{i=1}^N\Res_{z_k\to p_i} \Phi(z_k)\omega_{h,k+1}(z,z_1,\dots z_k)\cr&&
-\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr
&&\overset{\eqref{LogTRDef}}{=}\sum_{i=1}^N\sum_{j=1}^N\Res_{z_k\to p_i}\Res_{q\to p_j} \Phi(z_k)\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\Big(\omega_{h-1,k+2}(q,\sigma_j(q),z_1,\dots,z_{k})\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \Big)\bigg) \cr
    && -\sum_{j=1}^M\Res_{z'\to a_j}\frac{(x(z')-x(a_j))}{dx(z')}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})
\eea
Note that in the use of the definition of LogTR used above, there is no need for the $\delta_{m,1}$ special LogTR term since we have $k+1\geq 2$. We now put aside the term involving $\omega_{0,2}(q,z_k)$ and $\omega_{0,2}(\sigma_j(q),z_k)$. We get
\bea \text{RHS}_{h,k}&=&\frac{1}{2}\sum_{i=1}^N \sum_{j=1}^N \Res_{z_k\to p_i}\Res_{q\to p_j} \Phi(z_k)\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\cr&&
\bigg(\omega_{0,2}(\sigma_j(q),z_k)\omega_{h,k}(q,z_1,\dots,z_{k-1}) + \omega_{0,2}(q,z_k)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}) \bigg)
\cr&&
+\sum_{i=1}^N\sum_{j=1}^N\Res_{z_k\to p_i}\Res_{q\to p_j} \Phi(z_k)\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\Big(\omega_{h-1,k+2}(q,\sigma_j(q),z_1,\dots,z_{k})\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k\} \\(h_i,|I_i|)\neq (0,0)\\(h_i,I_i)\neq (0,\{z_k\})}} \omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \Big)\bigg) \cr
    && -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})
\eea

The next step is to exchange the residues. At every ramification point, we have:
\bea \label{ResidueExchange}\Res_{z \to p_i}\Res_{q\to p_j}&=&\Res_{q\to p_j} \Res_{z \to p_i} +\delta_{i=j}\Res_{q \to p_i} \Res_{z \to q, \sigma_i(q)} \cr
\Res_{z \to p_i}\Res_{q\to p_j}&=&\Res_{q\to p_j} \Res_{z \to p_i} -\delta_{i=j}\Res_{z\to p_i}\Res_{q \to z, \sigma_i(z)} 
\eea
Note that this formula is valid locally around the ramification points even if $\Phi(z)$ has other singularities far away from the ramification points.  Thus we get:
\beq \label{RHSgk}\text{RHS}_{h,k}(z,z_1,\dots,z_{k-1})= \text{(I)} + \text{(II)} + \text{(III)} + \text{(IV)} \eeq
with
\bea \label{TermI} \text{(I)}&:=&\frac{1}{2}\sum_{i=1}^N \sum_{j=1}^{N} \Res_{z_k\to p_i}\Res_{q\to p_j} \Phi(z_k)\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\cr&&
\bigg(\omega_{0,2}(\sigma_j(q),z_k)\omega_{h,k}(q,z_1,\dots,z_{k-1}) + \omega_{0,2}(q,z_k)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}) \bigg)
\eea
\bea\label{TermII} \text{(II)}&:=&\sum_{i=1}^N\sum_{j=1}^N\Res_{q\to p_j}\Res_{z_k\to p_i} \Phi(z_k)\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\Big(\omega_{h-1,k+2}(q,\sigma_j(q),z_1,\dots,z_{k})\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k\} \\(h_i,|I_i|)\neq (0,0)\\(h_i,I_i)\neq (0,\{z_k\}) }} \omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \Big)\bigg)
\eea
\bea\label{TermIII} \text{(III)}&:=&\sum_{i=1}^N\Res_{q \to p_i} \Res_{z_k \to q, \sigma_i(q)}  \Phi(z_k)\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_i(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}\Big(\omega_{h-1,k+2}(q,\sigma_i(q),z_1,\dots,z_k)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k\} \\(h_i,|I_i|)\neq (0,0)\\(h_i,I_i)\neq (0,\{z_k\})}} \omega_{h_1,|I_1|+1}(\sigma_i(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \Big)\bigg)
\eea
\bea \label{TermIV} \text{(IV)}&:=&-\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})
\eea

We shall then discuss each of the four contributions $\text{(I)}$, $\text{(II)}$, $\text{(III)}$ and $\text{(IV)}$ separately.

\subsection{Contribution from $\text{(III)}$}
Term $\text{(III)}$ is the simplest one. In the integrand, we do not have term like $\omega_{0,2}(q,z_k)$ nor $\omega_{0,2}(\sigma_j(q),z_k)$ because they have been put aside inside $\text{(I)}$. Thus the integrand is regular at $z_k=q$ and $z_k=\sigma_{i}(q)$ for any $i\in \llbracket 1,N\rrbracket$. Hence the residue is vanishing:
\beq \label{ContributionIII}\text{(III)}=0\eeq

\subsection{Contribution from $\text{(I)}$}
Let us now look at the contribution of $\text{(I)}.$  We exchange the contour of integration using \eqref{ResidueExchange} %\todo{Where does the - sign come from after the exchange of integration contours?}

%\todo{What is the difference between the 4th and 5th expression?}:
\bea &&\text{(I)}:=\frac{1}{2}\sum_{i=1}^N \sum_{j=1}^N \Res_{z_k\to p_i}\Res_{q\to p_j} \Phi(z_k)\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\cr&&
\bigg(\omega_{0,2}(\sigma_j(q),z_k)\omega_{h,k}(q,z_1,\dots,z_{k-1}) + \omega_{0,2}(q,z_k)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}) \bigg)\cr
&&\overset{q\to \sigma_j(q)}{=}\sum_{i=1}^N \sum_{j=1}^N \Res_{z_k\to p_i}\Res_{q\to p_j} \Phi(z_k)\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{0,2}(q,z_k)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\cr
&&\overset{\eqref{ResidueExchange}}{=}\sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_{i=1}\Res_{z_k\to p_i}\Phi(z_k)
 \omega_{0,2}(q,z_k) \cr&&
- \sum_{j=1}^N\Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\Res_{z_k\to q} \Phi(z_k)
\omega_{0,2}(q,z_k)\cr&&
\overset{\eqref{EqSpecialDilaton}}{=} %\sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_{i=1}\Res_{z_k\to p_i}\Phi(z_k)
 %\omega_{0,2}(q,z_k) \cr&&
- \sum_{j=1}^N\Res_{q\to p_j}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}) \omega_{0,1}(q)\cr&&
%=- \sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_{i=1}\Res_{z_k\to p_i}\Phi(z_k)
% \omega_{0,2}(q,z_k) \cr&&
%- \sum_{j=1}^N\Res_{q\to p_j}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}) \omega_{0,1}(q)\cr&&
\overset{\text{LLE}}{=} %\sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_{i=1}^N\Res_{z_k\to p_i}\Phi(z_k)
 %\omega_{0,2}(q,z_k) \cr&&
- \frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}) (\omega_{0,1}(q)-\omega_{0,1}(\sigma_j(q)))\cr&&
= %\sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_{i=1}^N\Res_{z_k\to p_i}\Phi(z_k)
 %\omega_{0,2}(q,z_k) \cr&&
+ \frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\left(\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)\right)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}),
\eea
where we have used in the third step
\beq \forall \,i \in \llbracket 1,N\rrbracket\,:\, \sum_{i=1}^N\Res_{z_k\to p_i}\Phi(z_k)\omega_{0,2}(q,z_k)=0\eeq
since the integrand is regular at the ramification points. Thus,
\beq \label{ContributionI}\text{(I)}=\frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\left(\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)\right)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1}).\eeq


\subsection{Contribution from $\text{(II)}$}
Let us now compute the contribution of $\text{(II)}$. First separating $z_k$, the double sum can be written as
\bea &&\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k\} \\(h_i,|I_i|)\neq (0,0)\\(h_i,I_i)\neq (0,\{z_k\}) }} \omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \cr&&
    %= \sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\omega_{h_1,|I_1|+2}(\sigma_j(q),z_{I_1},z_k) \omega_{h-h_1,|I_2|+1}(q,z_{I_2})\cr&&
    %+ \sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h-h_1,|I_2|+2}(q,z_{I_2},z_k)\cr
     %&&\overset{h_1\to h-h_1}{=} \sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\omega_{h_1,|I_1|+2}(\sigma_j(q),z_{I_1},z_k) \omega_{h-h_1,|I_2|+1}(q,z_{I_2})\cr&&
   % + \sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (h,\emptyset)\\(h_1,I_2)\neq (0,\emptyset) }}\omega_{h-h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_1,|I_2|+2}(q,z_{I_2},z_k)\cr
     %&&\overset{I_1\leftrightarrow I_2}{=} 
     =\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\omega_{h_1,|I_1|+2}(\sigma_j(q),z_{I_1},z_k) \omega_{h-h_1,|I_2|+1}(q,z_{I_2})\cr&&
    + \sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_2)\neq (h,\emptyset)\\(h_1,I_1)\neq (0,\emptyset) }}\omega_{h_1,|I_1|+2}(q,z_{I_1},z_k)\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})
\eea
We may now apply the induction on each term since we have excluded in the double sums the cases  $\underset{i=1}{\overset{N}{\sum}}\underset{z_k\to p_i}{\Res}\Phi(z_k)\omega_{0,2}(q,z_k) $ and $\underset{i=1}{\overset{N}{\sum}}\underset{z_k\to p_i}{\Res}\Phi(z_k)\omega_{0,2}(\sigma_j(q),z_k)$.  We find:

\small{\bea  \text{(II)}& \overset{\text{ind.}}{=}&
%-(2h+k-3)\sum_{j=1}^N\Res_{q\to p_j} \bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\Big(\omega_{h-1,k+1}(q,\sigma_j(q),z_1,\dots,z_{k-1})\cr
   % &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \Big)\bigg) \cr  
 %&&+\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
  %  &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})\cr&&
 %   +\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1} \omega_{h',1}(z')\omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2})\cr&&
  %  + \sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_2)\neq (h,\emptyset)\\(h_1,I_1)\neq (0,\emptyset) }}\sum_{h'=1}^{h_1}\omega_{h',1}(z')\omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2}) \Big)\cr
  %  &=&
-(2h+k-3)\sum_{j=1}^N\Res_{q\to p_j} \bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\Big(\omega_{h-1,k+1}(q,\sigma_j(q),z_1,\dots,z_{k-1})\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(\sigma_j(q),z_{I_1}) \omega_{h_2,|I_2|+1}(q,z_{I_2}) \Big)\bigg) \cr  
 &&+\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s}\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
     \omega_{h',1}(z')[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})] \Big)\cr&&
\eea}
\normalsize{Note} that in the last sums, we need to rule out $(h_1,I_1)=(0,\emptyset)$ and $(h_1,I_2)=(0,\emptyset)$ because it would have corresponded to a term $\Phi(z_k)\omega_{0,2}(\sigma_j(q),z_k)$ or $\Phi(z_k)\omega_{0,2}(q,z_k)$ that were put aside in $\text{(I)}$. We observe now that the first contribution corresponds to $\omega_{h,k}(z,z_1,\dots,z_{k-1})$  up to the new LogTR terms for $k=1$ in \eqref{LogTRDef}. Thus, we get:
\bea  &&\text{(II)}=
-(2h+k-3)\omega_{h,k}(z,z_1,\dots,z_{k-1})
\cr&&
-\delta_{k,1}(2h-2)\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{a_s}^q\omega_{0,2}(z,.)\right)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}\ln(q-a_s) \right)dx(q)\cr
 &&+\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s}\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
     \omega_{h',1}(z')\left[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})\right]\Big)\cr&&
\eea

Using the logarithmic projection property \eqref{LogProjectionProperty} we end up with the fact that for all $k\geq 1$ and $(h,k)\neq (0,1)$:
\bea \label{ContributionII}&&\text{(II)}%= 
%-(2h+k-3)\omega_{h,k}(z,z_1,\dots,z_{k-1})\cr&&
%+(2h-2)\delta_{k,1}\omega_{h,1}(z)-(2h-2)\delta_{k,1}\sum_{i=1}^N \Res_{z'\to p_i} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr
%&&+\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s}\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
%    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
%     \omega_{h',1}(z')\left[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})\right]\Big)\cr&&
    = -(2h+k-3)\omega_{h,k}(z,z_1,\dots,z_{k-1})\delta_{k\neq 1}-(2h-2)\delta_{k,1}\sum_{i=1}^N \Res_{z'\to p_i} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr
 &&+\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s}\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
     \omega_{h',1}(z')\left[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})\right]\Big)\cr&&
\eea

\subsection{Collecting terms}
Let us now collect \eqref{ContributionI}, \eqref{ContributionII} and \eqref{ContributionIII} and insert them into \eqref{RHSgk}. We find:
\bea \label{InductionStep2} &&\text{RHS}_{h,k}(z,z_1,\dots,z_{k-1})=%- \sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{g,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_{i=1}^N\Res_{z_k\to p_i}\Phi(z_k)
% \omega_{0,2}(q,z_k) \cr&&
%+ 
\frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\left(\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)\right)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\cr&&
-(2h+k-3)\omega_{h,k}(z,z_1,\dots,z_{k-1})\delta_{k\neq 1}-(2h-2)\delta_{k,1}\sum_{i=1}^N \Res_{z'\to p_i} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr
&&+ \text{ (A)}
\eea
where 
\small{\bea &&\label{DefTermA}\text{(A)}:=\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s}\bigg( \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
     \omega_{h',1}(z')\left[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})\right]\Big)\cr&&
    -\sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})
\eea}
\normalsize{}

\subsection{Computation of the term $\text{(A)}$}
Let us evaluate the contribution from $\text{(A)}$.

\bea&&\label{ContributionA}\text{(A)}%=\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
   % &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
     %\omega_{h',1}(z')[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})]\Big)\cr&&
   % -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
      %  \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr&&
%=\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{x(z')-x(a_s)}{dx(z')} \cr
%    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=1}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\sum_{h'=1}^{h_1}\cr&&
%     \omega_{h',1}(z')[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})]\Big)\cr&&
%    -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
%        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr&&
%=\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
%    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h'=1}^{h}\sum_{h_1=h'}^h\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_1)\neq (0,\emptyset)\\(h_1,I_2)\neq (h,\emptyset) }}\cr&&
%     \omega_{h',1}(z')[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1-h',|I_1|+2}(z',q,z_{I_1})\omega_{h-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})]\Big)\cr&&
%    -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
%        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr&& 
%\overset{h_1\to h_1-h'}{=}\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
%    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h'=1}^{h}\sum_{h_1=0}^{h-h'}\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1+h',I_1)\neq (0,\emptyset)\\(h_1+h',I_2)\neq (h,\emptyset) }}\cr&&
%     \omega_{h',1}(z')[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h'-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1,|I_1|+2}(z',q,z_{I_1})\omega_{h-h'-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})]\Big)\cr&&
%    -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
%        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr&& 
%=\sum_{j=1}^N\sum_{s=1}^M\Res_{q\to p_j}\Res_{z'\to a_s} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\frac{(x(z')-x(a_s))}{dx(z')} \cr
%    &&\Big(\sum_{h'=1}^{h-1}\omega_{h',1}(z')\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h'=1}^{h-1}\sum_{h_1=0}^{h-h'}\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1+h',I_2)\neq (h,\emptyset) }}\cr&&
%     \omega_{h',1}(z')[ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h'-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1,|I_1|+2}(z',q,z_{I_1})\omega_{h-h'-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})]\cr&&
%    +\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\I_2\neq \emptyset }}\cr&&
%     \omega_{h,1}(z')[ \omega_{0,|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{0,|I_2|+1}(q,z_{I_2}) + \omega_{0,|I_1|+2}(z',q,z_{I_1})\omega_{0,|I_2|+1}(\sigma_j(q),z_{I_2})]\Big)\cr&&
%    -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
%        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr&& 
=\sum_{s=1}^M\Res_{z'\to a_s}\sum_{h'=1}^{h-1}\omega_{h',1}(z')\frac{x(z')-x(a_s)}{dx(z')}\sum_{j=1}^N\Res_{q\to p_j} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)} \cr
    &&\Big(\omega_{h-1-h',k+2}(z',q,\sigma_j(q),z_1,\dots,z_{k-1})+\sum_{h_1=0}^{h-h'}\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\(h_1,I_2)\neq (h-h',\emptyset) }}\cr&&
     [ \omega_{h-h',|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{h-h'-h_1,|I_2|+1}(q,z_{I_2}) + \omega_{h_1,|I_1|+2}(z',q,z_{I_1})\omega_{h-h'-h_1,|I_2|+1}(\sigma_j(q),z_{I_2})]\Big)\cr&&  
    +\sum_{s=1}^M\Res_{z'\to a_s}\omega_{h,1}(z')\frac{(x(z')-x(a_s))}{dx(z')}\sum_{j=1}^N\Res_{q\to p_j} \frac{1}{2}\frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\sum_{\substack{I_1\sqcup I_2=\{1,\dots, k-1\} \\I_2\neq \emptyset }}\cr&&
     [ \omega_{0,|I_1|+2}(z',\sigma_j(q),z_{I_1})  \omega_{0,|I_2|+1}(q,z_{I_2}) + \omega_{0,|I_1|+2}(z',q,z_{I_1})\omega_{0,|I_2|+1}(\sigma_j(q),z_{I_2})]\cr&&
    -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z')\omega_{h-h_1,k+1} (z',z,z_1,\dots,z_{k-1})\cr&&
=\sum_{s=1}^M\Res_{z'\to a_s}\sum_{h'=1}^{h-1}\omega_{h',1}(z')\frac{x(z')-x(a_s)}{dx(z')}\omega_{h-h',k+1}(z',z,z_1,\dots,z_{k-1})\cr&& 
    +\sum_{s=1}^M\Res_{z'\to a_s}\omega_{h,1}(z')\frac{x(z')-x(a_s)}{dx(z')}\omega_{0,k+1}(z,z',z_1,\dots,z_{k-1})\delta_{k\geq 2}\cr&&
    -\sum_{j=1}^M\Res_{z'\to a_j}\frac{x(z')-x(a_j)}{dx(z')}\bigg(
        \overset{h}{\underset{h'=1}{\sum}}\omega_{h',1} (z')\omega_{h-h',k+1} (z',z,z_1,\dots,z_{k-1})\bigg)\cr&& 
=-\delta_{k,1} \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}
        \omega_{h,1} (z')\omega_{0,2} (z',z)
\eea

\subsection{End of the proof}
Inserting \eqref{ContributionA} into \eqref{InductionStep2} gives
\bea \label{InductionStep4} &&\text{RHS}_{h,k}=%- \sum_{j=1}^N \Res_{q\to p_j} \frac{\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_j(q))-\omega_{0,1}(q)}\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\sum_i\Res_{z_k\to p_i}\Phi(z_k)
% \omega_{0,2}(q,z_k) \cr&&
%+
\frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\left(\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)\right)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})\cr&&
-(2h+k-3)\omega_{h,k}(z,z_1,\dots,z_{k-1})\delta_{k\neq 1}-(2h-2)\delta_{k,1}\sum_{i=1}^N \Res_{z'\to p_i} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr&&
-\delta_{k,1} \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z)
\eea

Let us now split cases depending on the value of $k$. 

\medskip

\textbf{First Case: $k\geq 2$}

When $k\geq 2$, we have
\bea \forall \,k\geq 2&:&
\frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\left(\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)\right)\omega_{h,k}(\sigma_j(q),z_1,\dots,z_{k-1})%\cr
% &\overset{\text{LLE}}{=}& \sum_{j=1}^N\Res_{q\to p_j}\left(\int_{0}^{q} \omega_{0,2}(z,.)\right)\omega_{h,k}(q,z_1,\dots,z_{k-1})\cr
 %&=&-\Res_{q\to z}\left(\int_{0}^{q} \omega_{0,2}(z,.)\right)\omega_{h,k}(q,z_1,\dots,z_{k-1})\cr
 %&=&
 =-\omega_{h,k}(z,z_1,\dots,z_{k-1})\cr&&
 \eea
 because we can use the linear loop equation and move the contour of the residue and only pick poles at $q=z$. Inserting into \eqref{InductionStep4} we eventually get:
\beq\forall \, k\geq 2\,:\, \text{RHS}_{h,k}(z,z_1,\dots,z_{k-1})=-(2h+k-2)\omega_{h,k}(z,z_1,\dots,z_{k-1})
\eeq 
ending the induction procedure.

\medskip

\textbf{Second case: $k=1$}

When $k=1$, we also get pole at the LogTR-vital singularities:
\bea &&\frac{1}{2}\sum_{j=1}^N\Res_{q\to p_j}\left(\int_{q}^{\sigma_j(q)} \omega_{0,2}(z,.)\right)\omega_{h,1}(\sigma_j(q))%\cr
% &&\overset{\text{LLE}}{=} \sum_{j=1}^N\Res_{q\to p_j}\left(\int_{0}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)\cr
 %&&=-\Res_{q\to z}\left(\int_{0}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)
 %-\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{0}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)
% \cr
 %&&
 =-\omega_{h,1}(z)-\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{o}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)\cr&&
 \eea
 which following from the linear loop equation and the logarithmic projection property.
Inserting into \eqref{InductionStep4} we eventually get:
\bea  \text{RHS}_{h,1}(z)%&=&-\omega_{h,1}(z)-\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{o}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)\cr&&
%-(2h-2)\sum_{i=1}^N \Res_{z'\to p_i} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr&&
%- \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z)\cr
%&=&-\omega_{h,1}(z)-\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{o}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)\cr&&
%+(2h-2) \Res_{z'\to z} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')+(2h-2)\sum_{s=1}^M \Res_{z'\to a_s} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr&&
%- \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z)\cr
%&=&-\omega_{h,1}(z)-\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{o}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)\cr&&
%-(2h-2)\omega_{h,1}(z)+(2h-2)\sum_{s=1}^M \Res_{z'\to a_s} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr&&
%- \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z)\cr
%&=&-(2h-1)\omega_{g,1}(z)  -\sum_{s=1}^M\Res_{q\to a_s}\left(\int_{o}^{q} \omega_{0,2}(z,.)\right)\omega_{h,1}(q)\cr&&
%+(2h-2)\sum_{s=1}^M \Res_{z'\to a_s} \int_{o}^{z'} \om_{0,2}(., z)\omega_{h,1}(z')\cr&&
%- \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z)\cr
&=&-(2h-1)\omega_{h,1}(z)  +(2h-1)\sum_{s=1}^M \Res_{z'\to a_s} \int_{o}^{z'} \omega_{0,2}(., z)\omega_{h,1}(z')\cr&&
- \sum_{s=1}^M\Res_{z'\to a_s}\frac{x(z')-x(a_s)}{dx(z')}\omega_{h,1} (z')\omega_{0,2} (z',z)
\eea

Finally, using \autoref{LemmaIntW02Wg1}, we observe that the last two terms cancel and we eventually get:
\beq \text{RHS}_{h,1}(z)=-(2h-1)\omega_{h,1}(z)\eeq
ending the induction procedure.




\section{Proof of some lemmas: variations of the kernels}\label{AppendixLemmaVariations}
We have by definition
\beq \label{FixedLogTimes}\delta_{\Omega}[ydx]= \delta_{\Omega}[\td{y}dx].\eeq
Following the notations of \cite{EO07} and as explained in \autoref{SubsectionLambda} and \autoref{sec.variationsof}, we shall denote $\Omega$ the one-form such that
\beq\label{DefOmegaVariations} \delta_{\Omega}[y dx]\overset{\eqref{FixedLogTimes}}{=}\delta_{\Omega}[\td{y}dx]\overset{\eqref{NoXvariation}}{=}\delta_{\Omega} [\td{y}]dx= \Omega\eeq
%For the infinitesimal variations described above, we have from \autoref{TheoremGlobalDecompositionydx}:
%\begin{itemize}
%\item For $\delta_{\Omega}=\partial_{t_\alpha,k}$ an irregular time, we have $\Omega(q)=B_{\alpha,k}(q)$. 
%\item For $\delta_{\Omega}=\partial_{t_{\alpha_i,0}}-\partial_{t_{\alpha_j,0}} $ a deformation with respect to monodromies, we have $\Omega(q)=B_{\alpha_i,0;o'}(q)-B_{\alpha_j,0;o'}(q)=dS_{\alpha_i,\alpha_j}(q)$.
%\item For $\delta_\Omega=\partial_{\epsilon_i}$ a filling fraction, we have $\Omega(q)=2i\pi \,du_i(q)$.
%\item For $\delta_\Omega=\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}$ a deformation with respect to log-times, we have $\Omega(q)=\ln \frac{E(q,a_{\alpha_i})}{E(q,o)} dx(q)- \ln \frac{E(q,a_{\alpha_j})}{E(q,o)} dx(q)= \ln \frac{E(q,a_{\alpha_i})}{E(q,a_{\alpha_j})} dx(q)$.
%\end{itemize}


%For practical reasons, we shall put apart the variations with respect to log-times.

%\begin{definition}[Split of the variations]\label{DefSplitVariations} We shall define 
%\beq \delta_{\Omega_{\text{st}}}=\text{Span}\left\{ (\partial_{t_{\alpha,k}})_{\alpha \in \mathcal{P}, 1\leq k\leq R_\alpha}, (\partial_{t_{\alpha_i,0}}-\partial_{t_{\alpha_j,0}})_{(\alpha_i,\alpha_j)\in \mathcal{P}^2} , (\partial_{\epsilon_i})_{1\leq i\leq g} \right\}
%\eeq
%the set of variations excluding variations with respect to the log-times $(y_\alpha)_{\alpha\in \mathcal{S}_y}$. On the contrary, we shall define
%\beq \delta_{\Omega_{\text{log}}}=\text{Span}\left\{(\partial_{y_\alpha})_{\alpha\in \mathcal{S}_y}) \right\}\eeq
%The set of variations with respect to log-times only.
%\end{definition}

Finally, we observe the following property:
\begin{lemma}[Local symmetry of $\Omega$ around ramification points]\label{PropLocalSymmetryOmegaBranchpoints} For any variation considered in this section, we have locally around a ramification point $p_j$
\beq \forall\, j\in \llbracket 1,N \rrbracket\,:\, \Omega(\sigma_j(r))=-\Omega(r)\eeq    %\todo{Does this mean that $\Omega$ at a ramification point is 0 or infinity? Comparing with (7-6) this doesnot make sense.}
\end{lemma}

\begin{proof}The proof simply follows from the fact that variations considered in this article are done at fixed $x$. Hence, $\Omega=\delta_\Omega[y] dx$ and $y\circ \sigma_j=-y$ around a ramification point $p_j$ and so is $\Omega$.  
\end{proof}


The proof of the variational formulas for the correlators generated by LogTR will be done by induction. To perform it, one needs to compute first the variations of the Bergman kernel and of the recursion kernel.

%\subsection{Variations with respect to irregular times, monodromies and filling fractions}
%In this section, we will consider variations $\delta_\Omega\in \delta_{\Omega_{\text{st}}}$.

\subsection{Variations of the Bergman kernel}
Rauch variational formula may be used to compute the variations of the Bergmann kernel. In our context, assuming that $\Omega$ has not pole at the ramification points, it states that (see \cite{EO07}) for deformations fixing $x$:
\bea \label{Rauch} \delta_{\Omega}B(p,q)&=&\sum_{i=1}^N\frac{\Omega(p_i)}{dy(p_i)}\Res_{r\to p_i}\frac{B(r,p)B(r,q)}{dx(r)}\cr
&=&\sum_{i=1}^N\Res_{r\to p_i}\frac{\Omega(r)B(r,p)B(r,q)}{dx(r)dy(r)}\cr
&=&-2\sum_{i=1}^N\Res_{r\to p_i}\frac{\Omega(r)dE_{i,r}(p)B(r,q)}{(y(r)-y(\sigma_i(r))dx(r)}=-2\sum_{i=1}^N\Res_{r\to p_i}\frac{\Omega(r)dE_{i,r}(p)B(r,q)}{\omega_i(r)}\cr
&=&\sum_{i=1}^N\Res_{r\to p_i}\frac{dE_{i,r}(p)}{\omega_i(r)}\left[\Omega(r)B(\sigma_i(r),q)+\Omega(\sigma_i(r))B(r,q)\right]
\eea
Note that $dy(p_i)\neq 0$ from \autoref{MainAssumption} (the zero loci of $dy$ and $dx$ are assumed disjoint). The third equality comes from the fact that the ramification points are simple and:
\beqq \frac{dE_{i,r}(p)}{y(r)-y(\sigma_i(r))}=\frac{-B(p_i,p)+O(r-p_i)}{2y'(p_i) +O(r-p_i)}=\left(\frac{-B(r,p)}{2dy(r)}\right)_{r=p_i}+O(r-p_i)
\eeqq Moreover, $\Omega(r)$ has no pole at the ramification points for any of our infinitesimal transformations. We recall that $dE_{i,r}$ and $\omega_i$ are defined locally around the ramification point $p_i$ by \autoref{DefVertexPropagator}.

\subsection{Variations of the recursion kernel}
By integrating once with respect to $q$ the variation $\delta_{\Omega}B(p,q)$, near each ramification point we get for all $j\in \llbracket 1,N\rrbracket$:
\bea \label{VariationdE} \delta_{\Omega}[dE_{j,q}(p)]
&=&\sum_{i=1}^N\Res_{r\to p_i}\frac{dE_{i,r}(p)}{\omega_i(r)}\left[\Omega(r)dE_{j,q}(\sigma_i(r))+\Omega(\sigma_i(r))dE_{j,q}(r)\right]
\eea

This implies that one may compute the variation of the recursion kernel (See \cite[Lemma $5.1$]{EO07}).
\begin{lemma}[Variations of the recursion kernel]\label{LemmaVariationsRecursionKernel} For any symmetric bilinear form $f(q,p)=f(p,q)$ on $\Sigma^2$ and any variation $\delta_\Omega$ considered in this section, one has
\bea
\delta_\Omega\left[
\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, f(q,\sigma_k(q))
\right]
&=&
2\sum_{j=1}^N\sum_{i=1}^N
\Res_{q\to p_j}\Res_{r\to p_i}
\frac{dE_{j,q}(p)}{\omega_j(q)}\,\Omega(q)\,
\frac{dE_{i,r}(q)}{\omega_i(r)}\, f(r,\sigma_j(r))
\cr
&&
+ \sum_{j=1}^N
\Res_{q\to p_j}
\frac{dE_{j,q}(p)}{\omega_j(q)}\,
\delta_{\Omega}[f(q,\sigma_j(q))] 
\eea
\begin{proof}
    The computation is similar to \cite[Appendix B]{EO07} but for completeness, we repeat the computation in the setting of LogTR and show that nothing changes.
    
%For any $(h,m)\in \mathbb{N}^2$ such that $2h+m-2>0$, logTR is given by: 
%\bea \label{LogTRDef2} \omega_{h,m}(z_1,\dots,z_m)&:=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
%    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
%    &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
%    \eea  

%\underline{Variations of $(\omega_{0,m})_{m\geq 3}$:} 
Variations of $(\omega_{0,m})_{m\geq 3}$ with respect to the irregular times, monodromies and filling fractions are identical to the standard TR case since the recursion is the same in LogTR and in TR for these correlators and that \autoref{LemmaVariationsRecursionKernel} holds. Indeed, the computations of the correlators $(\omega_{0,m})_{m\geq 3}$ is the same in TR and LogTR and the diagrammatic proof of \cite{EO07} holds immediately as soon as \autoref{LemmaVariationsRecursionKernel} is verified and that variations can be rewritten as integrals of the Bergman kernel on a contour that is away from the ramification points. This is the case for these variations so that :
\beq \label{Variationh0}\forall\, m\geq 2\,:\, \delta_{\Omega}[ \omega_{0,m}(z_1,\dots,z_m)]=\int_{\partial_\Omega}\omega_{0,m+1}(z_1,\dots,z_m,q)\Lambda_\Omega(q)
\eeq
where $\Lambda_\Omega$ is defined in \autoref{SubsectionLambda}.



Application of the chain rule and of \eqref{VariationdE} together with the definition of the differential form $\Omega$ \eqref{DefOmegaVariations} provides:
\small{\bea &&\delta_{\Omega}\left[
\sum_{j=1}^N\Res_{q\to p_i}\frac{dE_{j,q}(p)}{\omega_j(q)}\, f(q,\sigma_j(q))
\right]=\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(p)}{\omega_j(q)}\, \delta_{\Omega}[f(q,\sigma_j(q))] \cr&&- \sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(p)}{\omega_j(q)^2}(\Omega(q)-\Omega(\sigma_j(q))) f(q,\sigma_j(q))+ 2 \sum_{j=1}^N\Res_{q\to p_j}\sum_{i=1}^N\Res_{r\to p_i}\frac{dE_{i,r}(p)}{\omega_i(r)}\Omega(r) \frac{dE_{j,q}(r)}{\omega_j(q)}\, f(q,\sigma_j(q))\cr&&
=\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(p)}{\omega_j(q)}\, \delta_{\Omega}[f(q,\sigma_j(q))] -2 \sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(p)}{\omega_j(q)^2}\Omega(q) f(q,\sigma_j(q))\cr&&+ 2 \sum_{j=1}^N\Res_{q\to p_j}\sum_{i=1}^N\Res_{r\to p_i}\frac{dE_{i,r}(p)}{\omega_i(r)}\Omega(r) \frac{dE_{j,q}(r)}{\omega_j(q)}\, f(q,\sigma_j(q))\cr&&
=\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(p)}{\omega_j(q)}\, \delta_{\Omega}[f(q,\sigma_j(q))] -2 \sum_{j=1}^N\Res_{q\to p_j}\Res_{r\to q}\frac{dE_{j,q}(r)dE_{j,r}(p)}{\omega_j(q)\omega_j(r)}\Omega(r) f(q,\sigma_j(q))\cr&&+ 2 \sum_{j=1}^N\Res_{q\to p_j}\sum_{i=1}^N\Res_{r\to p_i}\frac{dE_{i,r}(p)}{\omega_i(r)}\Omega(r) \frac{dE_{j,q}(r)}{\omega_j(q)}\, f(q,\sigma_j(q))\cr&&
=\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(p)}{\omega_j(q)}\, \delta_{\Omega}[f(q,\sigma_j(q))] +2 \sum_{i=1}^N\Res_{r\to p_i}\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{i,r}(p)}{\omega_{i}(r)} \Omega(r)\frac{dE_{j,q}(r)}{\omega_j(q)}f(q,\sigma_j(q))\cr&&
\eea
}
\normalsize{where} we have used $\Omega(\sigma_j(q))=-\Omega(q)$ in the first equality from \autoref{PropLocalSymmetryOmegaBranchpoints}. Moreover, for the second equality, the residue at $r\to q$ makes sense because $q$ is around the ramification point $p_j$ so $r$ is too. Finally the last equality comes from the inversion of the residues at the ramification points that are given by
\beqq \sum_{i=1}^N\Res_{r\to p_i}\sum_{j=1}^N\Res_{q\to p_j}= \sum_{j=1}^N\Res_{q\to p_j}\sum_{i=1}^N\Res_{r\to p_i}-\sum_{j=1}^N\Res_{q\to p_j}\Res_{r\to q}\eeqq

\end{proof}
\end{lemma}


\section{Proof of \autoref{TheoVariationalFormulas}}\label{AppendixVariationProof}
%\subsection{Variations in $\delta_{\Omega_{\text{st}}}$}
We will proceed by induction on $2h+m$. Let us first mention that the initialization $(h,m)=(0,2)$ is valid from the knowledge of the variations of $(\omega_{0,m})_{m\geq 2}$. Consider $h\geq 1$ and $m\geq 0$ such that $(h,m)\neq(0,1)$. Let us consider a variation with respect to irregular times, monodromies of filling fractions of $\td{y}dx$ (i.e. fixed log-times) with the associated $\Lambda_\Omega$ given in \autoref{SubsectionLambda} and assume that the formulas in \autoref{TheoVariationalFormulas} hold for the first correlators up to $2h'+m'<2h+m$. %From \eqref{LogTRDef}, we have by definition:
%\bea \label{Defomegahm}\omega_{h,m}(z_1,\dots,z_m)&:=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
%    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
%    &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
%    \eea  
Applying the variation to the definition of LogTR \eqref{LogTRDef} and using \autoref{LemmaVariationsRecursionKernel} with the symmetric two form: $f_{h,m}(q,p):=\omega_{h-1,m+1}(p,q,z_2,\dots,z_m)
    +\underset{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}}{\sum} \omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+1}(p,z_{I_2})$ gives
\bea &&\delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]=-\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\delta_{\Omega}\Big[\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big]\cr
    &&+2\sum_{j=1}^N\sum_{i=1}^N
\Res_{q\to p_j}\Res_{z\to p_i}
\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,\Omega(q)\,
\frac{dE_{i,z}(q)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}\delta_{\Omega}[dS_{a_s,z}(z_1)]dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
    \eea  
Applying the induction assumption, using the relation between $\Omega(q)$ and $\Lambda_\Omega$ and finally computing the variation of $dS_{a_s,z}(z_1)$ using \eqref{Rauch}, we get
 
\bea \label{InductionVarStep1} &&\delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]=-\int_{\partial_\Omega} \Lambda_\Omega(s) \sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[\omega_{h-1,m+2}(q,\sigma_j(q),z_2,\dots,z_m,s)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(q,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_j(q),z_{I_2})+\omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_j(q),z_{I_2},s) \Big]\cr
    &&+2\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N\sum_{i=1}^N
\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,B(q,s)\Res_{z\to p_i}
\,
\frac{dE_{i,z}(q)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&+2\delta_{m,1}\sum_{k=1}^M\Res_{z\to a_k}\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Omega(q)dS_{a_k,z}(q)dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)
    \eea  
Replacing $\Omega(q)$ as a integral involving $\Lambda_\Omega$ in the last line and regrouping with the third line, we get:
\bea \label{InductionVarStep2} &&\delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]=-\int_{\partial_\Omega} \Lambda_\Omega(s) \sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[\omega_{h-1,m+2}(q,\sigma_j(q),z_2,\dots,z_m,s)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(q,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_j(q),z_{I_2})+\omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_j(q),z_{I_2},s) \Big]\cr
    &&+2\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,B(q,s)\Big[ \sum_{i=1}^N\Res_{z\to p_i}
\,
\frac{dE_{i,z}(q)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big) \cr&&
    +\delta_{m,1}\sum_{k=1}^M\Res_{z\to a_k}dS_{a_k,z}(q)dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\Big]
    \eea 
The quantity in bracket is precisely the definition of $\omega_{h,m}(q,z_2,\dots,z_m)$ (given by \eqref{LogTRDef} with $z_1$ replaced by $q$) even when $m=1$ so that we end up with:
\bea \label{InductionVarStep3} &&\delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]=-\int_{\partial_\Omega} \Lambda_\Omega(s) \sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[\omega_{h-1,m+2}(q,\sigma_j(q),z_2,\dots,z_m,s)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(q,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_j(q),z_{I_2})+\omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_j(q),z_{I_2},s) \Big]\cr
    &&+2\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,B(q,s)\omega_{h,m}(q,z_2,\dots,z_m)
\eea 
Using the symmetry around ramification points $\Omega(\sigma_j(q))=-\Omega(q)$ and also the linear loop equation, it is equivalent to
\bea \label{InductionVarStep4} &&\delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]=-\int_{\partial_\Omega} \Lambda_\Omega(s) \sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big[\omega_{h-1,m+2}(q,\sigma_j(q),z_2,\dots,z_m,s)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(q,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_j(q),z_{I_2})+\omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_j(q),z_{I_2},s) \Big]\cr
    &&-\int_{\partial_\Omega} \Lambda_\Omega(s)\sum_{j=1}^N
\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\,(B(q,s)\omega_{h,m}(\sigma_j(q),z_2,\dots,z_m)+B(\sigma_j(q),s)\omega_{h,m}(q,z_2,\dots,z_m))\cr&& 
\eea 

Let us now observe that by definition for all $m\geq 1$ ($m+1\geq 2$ so there are no special LogTR terms).
%\small{\bea&&\omega_{h,m+1}(z_1,\dots,z_m,s):=\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big(\omega_{h-1,m+2}(q,\sigma_j(q),z_2,\dots,z_m,s)\cr
%    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_2,|I_2|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(q,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_j(q),z_{I_2})+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_1,|I_1|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_j(q),z_{I_2},s)
%    \Big)\cr&&
%=\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{j,q}(z_1)}{\omega_j(q)}\Big(\omega_{h-1,m+2}(q,\sigma_j(q),z_2,\dots,z_m,s)\cr
%    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(q,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_j(q),z_{I_2})+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_j(q),z_{I_2},s)\cr
%    &&-B(q,s) \omega_{h,m}(\sigma_j(q),z_2,\dots z_m)
%-B(\sigma_j(q),s) \omega_{h,m}(q,z_2,\dots z_m)
%    \Big)\cr&& 
%    \eea }
\normalsize{Thus}, combining with \eqref{InductionVarStep4}, we get
\beq \delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]=\int_{\partial_\Omega} \Lambda_\Omega(s) \omega_{h,m+1}(z_1,\dots,z_m,s)\eeq
ending the induction process.



\section{Compatibility of dilaton equations with variational formulas for standard times}\label{AppendixCompatibilityDilatonVar}

In this appendix, we prove that the dilaton equations for the correlators \autoref{TheoremDilatonEquation} are compatible with the variational formulas of the correlators \autoref{TheoVariationalFormulas}. 
\medskip
The dilaton equations for $h\geq 0, k\geq 1$ and $(h,k)\neq (0,1)$ are
\bea -(2h+k-2)\omega_{h,k}(z_1,\dots,z_k)&=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,k+1}(z,z_1,\dots,z_k) \cr&&
-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr&&
\eea
Applying $\delta_\Omega$, using \autoref{TheoVariationalFormulas} and the fact that
\beq \label{VarPhi} \delta_\Omega[\Phi(z)]= \int_o^z \delta_{\Omega} [ydx]= \int_o^z \Omega= \int_{\partial_\Omega} \Lambda_\Omega(s) dS_{z,o}(s)\eeq
together with the fact that the contour $\partial_\Omega$ is away from ramification points and $\mathcal{S}_y$ gives that
\small{\bea\label{Compat1} &&-(2h+k-2)\int_{\partial_\Omega}\Lambda_\Omega(s) \omega_{h,k+1}(z_1,\dots,z_k,s)=\int_{\partial_{\Omega}}\Lambda_\Omega(s) \sum_{i=1}^N\Res_{z\to p_i} dS_{z,o}(s)\omega_{h,k+1}(z,z_1,\dots,z_k)\cr
&&+ \int_{\partial_{\Omega}}\Lambda_\Omega(s)\sum_{i=1}^N\Res_{z\to p_i}\Phi(z)\omega_{h,k+2}(z,z_1,\dots,z_k,s)\cr&&
-\int_{\partial_{\Omega}}\Lambda_\Omega(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,2} (z,s)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr&&
-\int_{\partial_{\Omega}}\Lambda_\Omega(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+2} (z,z_1,\dots,z_k,s)
\eea}
\normalsize{From} the logarithmic projection property and $k\geq1$, we get that
\bea  &&\sum_{i=1}^N\Res_{z\to p_i} dS_{z,o}(s)\omega_{h,k+1}(z,z_1,\dots,z_k)= \omega_{h,k+1}(s,z_1,\dots,z_k).
\eea
Similarly, since $k\geq 1$ we have that $(\omega_{h',r})_{h'\geq 0,r\geq 2}$ are regular at the $(a_j)_{1\leq j\leq M}$, hence
\beq \sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,2} (z,s)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)=0\eeq
Thus, \eqref{Compat1} is equivalent to
%\bea &&-(2h+k-2)\int_{\partial_\Omega}\Lambda_\Omega(s) \omega_{h,k+1}(z_1,\dots,z_k,s)=\int_{\partial_{\Omega}}\Lambda_\Omega(s) \omega_{h,k+1}(s,z_1,\dots,z_k)\cr
%&&+ \int_{\partial_{\Omega}}\Lambda_\Omega(s)\sum_{i=1}^N\Res_{z\to p_i}\Phi(z)\omega_{h,k+2}(z,z_1,\dots,z_k,s)\cr&&
%-\int_{\partial_{\Omega}}\Lambda_\Omega(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+2} (z,z_1,\dots,z_k,s)
%\eea
%i.e.
\small{\bea\label{Compat2} &&-(2h+k-1)\int_{\partial_\Omega}\Lambda_\Omega(s) \omega_{h,k+1}(z_1,\dots,z_k,s)=
 \int_{\partial_{\Omega}}\Lambda_\Omega(s)\Big[\sum_{i=1}^N\Res_{z\to p_i}\Phi(z)\omega_{h,k+2}(z,z_1,\dots,z_k,s) \cr&&
 -\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+2} (z,z_1,\dots,z_k,s)\Big]
\eea}
\normalsize{This} equation is consistent with the dilaton equation for $\omega_{h,k+1}(z_1,\dots,z_k,s)$, 
%is
%\bea &&-(2h+k-1)\omega_{h,k+1}(z_1,\dots,z_k,s)=\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,k+2}(z,z_1,\dots,z_k,s) \cr&&
%-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
%        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+2} (z,z_1,\dots,z_k,s)\cr&&
%\eea
such that \eqref{Compat2} is consistent.

\section{Proof of variational formulas for the free energies with respect to standard times}
\subsection{Proof of \autoref{TheoVarFreenergiesStandardtimes}: Variational formulas for $\omega_{h\geq 2,0}$}\label{AppendixCompatibilityDilatonVarFreEnergies}
Let $h\geq 2$ and recall that the free energies $\omega_{h,0}$ are defined by \autoref{DefFreeEnergies}:
\small{\beq (2-2h)\omega_{h,0}=\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,1}(z)
-\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\left(\frac{1}{2}
        \overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z)}{dx(z)}  -dy(z)\int_o^z\omega_{h,1}\right)
\eeq}
\normalsize{and} recall that
\beq \int_{\partial_\Omega} \Lambda_\Omega(s) B(s,.)= \Omega=\delta_{\Omega}[ydx].\eeq
Applying $\delta_\Omega$ and using \autoref{TheoVariationalFormulas} yields to 
\bea \label{VarFreeEnergies1} &&(2-2h)\delta_{\Omega}[\omega_{h,0}]= \int_{\partial_\Omega}\Lambda_\Omega(s) \sum_{i=1}^N \Res_{z\to p_i}  dS_{o,z}(s) \omega_{h,1}(z)+\Res_{z\to p_i} \int_{\partial_\Omega}\Lambda_\Omega(s)  \sum_{i=1}^N \Res_{z\to p_i}\Phi(z) \omega_{h,2}(z,s)
\cr&&
-\int_{\partial_\Omega}\Lambda_\Omega(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\frac{1}{2}
        \overset{h-1}{\underset{h_1=1}{\sum}}\left(\omega_{h_1,2} (z,s)\omega_{h-h_1,1} (z)+  \omega_{h_1,1} (z)\omega_{h-h_1,2} (z,s)\right)\cr&& 
+\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\delta_{\Omega}\left[dy(z)\int_o^z\omega_{h,1}\right]
\eea
Since $dS_{o,z}(s) \omega_{h,1}(z)$ is a meromorphic one-form in $z$ with only poles at the ramification points, $(a_j)_{1\leq j\leq M}$ and $s$ we have from Riemann bilinear identity (\autoref{RiemannBilinearIdentity}) and the normalization of the Bergmann kernel and of the $(\omega_{h,1})_{h\geq 1}$:
\bea \sum_{i=1}^N \Res_{z\to p_i}  dS_{o,z}(s) \omega_{h,1}(z)%&=& -\Res_{z\to s}  dS_{o,z}(s) \omega_{h,1}(z)-\sum_{j=1}^M \Res_{z\to a_j}  dS_{o,z}(s) \omega_{h,1}(z)\cr
&=&\omega_{h,1}(s)+\sum_{j=1}^M \Res_{z\to a_j}  B(s,z) \left(\int_o^z\omega_{h,1}\right)
\eea
Note that contrary to the verification for the other correlators, the last term is not vanishing. Thus, \eqref{VarFreeEnergies1} is equivalent to (perform $h_1\to h-h_1$ in one of the sum)
\small{\bea \label{VarFreeEnergies2} &&(2-2h)\delta_{\Omega}[\omega_{h,0}]=\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\omega_{h,1}(s) +\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M \Res_{z\to a_j}  B(s,z) \left(\int_o^z\omega_{h,1}\right)\cr&&
+ \int_{\partial_\Omega}\Lambda_\Omega(s)  \sum_{i=1}^N \Res_{z\to p_i}\Phi(z) \omega_{h,2}(z,s)
-\int_{\partial_\Omega}\Lambda_\Omega(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}
        \overset{h-1}{\underset{h_1=1}{\sum}}\omega_{h_1,2} (z,s)\omega_{h-h_1,1}(z)\cr&&  
+\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\delta_{\Omega}\left[dy(z)\int_o^z\omega_{h,1}\right]
\eea}
\normalsize{Inserting} the dilaton equation for $\omega_{h,1}(s)$ %is
%\small{\bea (1-2h)\omega_{h,1}(s)%&=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,2}(z,s) 
%-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
%        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,2} (z,s)\cr
%&=& \sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,2}(z,s) 
%-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
%        \overset{h-1}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,2} (z,s)\cr
%        &&+ \sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\omega_{h,1} (z)\omega_{0,2} (z,s)
%\eea}
%\normalsize{Inserting }this 
in the r.h.s. of \eqref{VarFreeEnergies2} provides
\bea \label{VarFreeEnergies3} (2-2h)\delta_{\Omega}[\omega_{h,0}]&=&(2-2h)\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\omega_{h,1}(s) +\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M \Res_{z\to a_j}  B(s,z) \left(\int_o^z\omega_{h,1}\right)\cr&&
+\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\omega_{h,1} (z)\omega_{0,2} (z,s)
\cr&&+\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\delta_{\Omega}\left[dy(z)\int_o^z\omega_{h,1}\right]\cr
&:=&(2-2h)\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\omega_{h,1}(s) +(A)
\eea
where we have defined $(A)$ as:
\small{\bea \label{DefAVar} (A)&:=&\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M \Res_{z\to a_j}  B(s,z) \left(\int_o^z\omega_{h,1}\right)
+\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\omega_{h,1} (z)B(z,s)
\cr&&
+\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\delta_{\Omega}\left[dy(z)\int_o^z\omega_{h,1}\right]
\eea}

\normalsize{Let} us study the last term in details:
\small{\bea&& \sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\delta_{\Omega}\left[dy(z)\int_o^z\omega_{h,1}\right]= \int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)d_z\Big(\frac{B(s,z)}{dx(z)}\Big)\left(\int_o^z\omega_{h,1}\right)\cr&& +\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}B(s,z)dy(z)\left(\int_o^z\omega_{h,2}(s,.)\right)\cr
&&
=\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)d_z\Big(\frac{B(s,z)}{dx(z)}\Big)\left(\int_o^z\omega_{h,1}\right)
\eea}
\normalsize{where} we have used for the last equality the fact that $\int_o^z\omega_{h,2}(s,.)$ is regular at $z=a_j$ %so that $\frac{\big(x(z)-x(a_j)\big)}{dx(z)}B(s,z)dy(z)\left(\int_o^z\omega_{h,2}(s,.)\right)$ is also regular at $z=a_j$. 
Indeed, $a_j$ is a simple pole of $dy$ but $(x(z)-x(a_j))$ has a simple zero at $z=a_j$ so the integrand is regular.

Thus \eqref{DefAVar} reduces to
\bea \label{DefAVar2} (A)&=&\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M \Res_{z\to a_j}  B(s,z) \left(\int_o^z\omega_{h,1}\right)
+\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\omega_{h,1} (z)B(z,s)\cr&&
+\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)d_z\Big(\frac{B(s,z)}{dx(z)}\Big)\left(\int_o^z\omega_{h,1}\right)\cr
&=&\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\sum_{j=1}^M \Res_{z\to a_j}d_z\left(\frac{\big(x(z)-x(a_j)\big)}{dx(z)}B(z,s)\left(\int_o^z\omega_{h,1}\right)\right)\cr
&=&0
\eea
where the last equality holds because %$d_z\left(\frac{\big(x(z)-x(a_j)\big)}{dx(z)}B(z,s)\left(\int_o^z\omega_{h,1}\right)\right)$ 
is the integrand is a exact one-form.

In the end, inserting \eqref{DefAVar2} into \eqref{VarFreeEnergies3} yields
\beq (2-2h)\delta_{\Omega}[\omega_{h,0}]=(2-2h)\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\omega_{h,1}(s)\eeq
ending the proof.


\subsection{Proof of \autoref{ThVarFormulaF1StandardTimes}: Variational formula for $\omega_{1,0}$}\label{AppendixVarF1}
Let us first compute the special LogTR term in $\omega_{1,1}$:
\bea\label{SingPartomega11}[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)%&=&-\frac{1}{24y_{a_s}}\frac{\partial^2}{\partial x^2}\ln(z-a_s)\cr
%&=&-\frac{1}{24y_{a_s}}\left( \frac{1}{x'(z)^2}\frac{\partial^2}{\partial z^2} \ln (z-a_s) -\frac{x''(z)}{x'(z)^3}\frac{\partial}{\partial z} \ln (z-a_s)\right)\cr
&=& \frac{1}{24y_{a_s}}\left( \frac{1}{x'(z)^2(z-a_s)^2} +\frac{x''(z)}{x'(z)^3(z-a_s)}\right)
\eea
Thus, we get that for any variation $\delta_\Omega$ with respect to isomonodromic times, monodromies, and filling fractions of $\td{y}dx$:
\bea && -\int_{\partial_\Omega}\Lambda_\Omega(p)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&= -\int_{\partial_\Omega}\Lambda_\Omega(p)\sum_{s=1}^M\frac{1}{24y_{a_s}}\Res_{z\to a_s}dS_{a_s,z}(p)\left( \frac{1}{x'(z)(z-a_s)^2} +\frac{x''(z)}{x'(z)^2(z-a_s)}\right)dz
\eea
Let us now observe that $dS_{a_s,z}(p)=\int_{a_s}^z B(.,p)$ has a simple zero at $z=a_s$. Moreover, from \autoref{MainAssumption}, $x'(a_s)\neq 0$ (because $a_s$ is not a ramification point since $dy$ has a simple pole at $a_s$ by definition). Thus, $\frac{dS_{a_s,z}(p)x''(z)}{x'(z)^2(z-a_s)}$ is regular at $z=a_s$ and so does not contribute to the residue. In the end, we have
\small{\bea -\int_{\partial_\Omega}\Lambda_\Omega(p)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)&=& -\sum_{s=1}^M\frac{1}{24y_{a_s} dx(a_s)}\int_{\partial_\Omega}\Lambda_\Omega(p) B(a_s,p)\cr
&=& -\sum_{s=1}^M\frac{1}{24y_{a_s} dx(a_s)}\Omega(a_s)
\eea}
\normalsize{where} we have used the fact that contours $\partial_\Omega$ are away from the $(a_s)_{1\leq s\leq M}$ and that $\Omega(p)=\int_{\partial_\Omega} B(p,q)\Lambda_{\Omega}(q)$. Variations with respect to isomonodromic times, monodromies or filling fractions are by definition fixing $(y_{a_s})_{1\leq s\leq M}$ and $x(z)$. Moreover, from \eqref{DefOmegaVariations}, we have $\Omega(a_s)=\delta_{\Omega}[\td{y}(a_s)] dx(a_s)$ (note that $\td{y}(a_s)$ makes sense whereas $y(a_s)$ diverges) so that  %the global decomposition of $ydx$ \autoref{TheoremGlobalDecompositionydx}, we have that:
%\beq \forall \, \delta_\Omega\in \delta_{\Omega_{\text{st}}}\,:\, \delta_\Omega[ydx(z)]=\delta_\Omega[\td{y}dx]\eeq
%where we recall that 
%\beq \td{y}(z)=y(z)-\sum_{\alpha \in \mathcal{S}_y} y_\alpha \ln \frac{E(q,\alpha)}{E(q,o)}\eeq
%In particular, $\td{y}(a_s)$ makes sense (whereas $y(a_s)$ is infinite). Hence we have
%\beq  \forall \, \delta_\Omega\in \delta_{\Omega_{\text{st}}}\,:\,\delta_\Omega[\td{y}dx(p)]=\Omega(p)\eeq
%In the end, we get:
\small{\bea\label{AppendixSpecialTermOmega10} -\int_{\partial_\Omega}\Lambda_\Omega(p)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)&=&\delta_{\Omega}\left[-\frac{1}{24}\sum_{s=1}^M\frac{1}{y_{a_s} dx(a_s)}\td{y}(a_s)dx(a_s)\right]\cr
&=&\delta_{\Omega}\left[-\frac{1}{24}\sum_{s=1}^M\frac{\td{y}(a_s)}{y_{a_s} }\right]
\eea}
\normalsize{Moreover}:
\beq\delta_{\Omega}\left[\frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)\right]=\frac{1}{24}\sum_{s=1}^M\frac{\delta_{\Omega}[y(z)]}{y_{a_s} }=\frac{1}{24}\sum_{s=1}^M\frac{\delta_{\Omega}[\td{y}(z)]}{y_{a_s} }\eeq
so that 
\beq \delta_{\Omega}\left[\frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)_{z=a_s}\right]= \frac{1}{24}\sum_{s=1}^M\frac{\delta_{\Omega}[\td{y}(a_s)]}{y_{a_s} }
\eeq
\medskip

\normalsize{Let} us now finish the proof. Recall that
\beq \omega_{1,1}(p)=\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}B(q,\sigma_k(q))-\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\eeq
Thus,
\bea \int_{\partial_\Omega}\omega_{1,1}(p)\Lambda_{\Omega}(p)&=&\sum_{i=1}^N\Res_{q\to p_i}\int_{\partial_\Omega}\frac{dE_{i,q}(p)\Lambda_{\Omega}(p)}{\omega(q)}B(q,\sigma_i(q))\cr
&&-  \int_{\partial_\Omega}\Lambda_{\Omega}(p)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr
&=&\sum_{i=1}^N\Res_{q\to p_i}\int_{\partial_\Omega}\frac{dE_{i,q}(p)\Lambda_{\Omega}(p)dz_i(q)dz_i(\sigma_i(q))}{\omega(q)}\left[\frac{1}{(z(q)-z(\sigma_i(q)))^2}+\frac{1}{6}S_B(q)\right]\cr&&
-  \int_{\partial_\Omega}\Lambda_{\Omega}(p)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
\eea
where  $z_i$ is a local variable near the ramification points $p_i$ and $S_B$ is the corresponding Bergmann projective connection. Since the last term has a simple pole at the ramification point $p_i$, one can write
\bea \sum_{i=1}^N\Res_{q\to p_i}\int_{\partial_\Omega}\frac{dE_{i,q}(p)\Lambda_{\Omega}(p)dz_i(q)dz_i(\sigma_i(q))}{\omega_i(q)}\frac{1}{6}S_B(q)&=& -\frac{1}{2}\sum_{i=1}^N\frac{\Omega(p_i)}{dy(p_i)}\Res_{q\to p_i}\frac{B(q,\sigma_i(q))}{dx(q)}\cr
&=&-\frac{1}{2}\delta_\Omega[\ln \tau]
\eea

Since $z_i(\sigma_i(q))=-z_i(q)$, we have also
\bea &&\Res_{q\to p_i}\int_{\partial_\Omega}\frac{dE_{i,q}(p)\Lambda_{\Omega}(p)dz_i(q)dz_i(\sigma_i(q))}{\omega_i(q)}\frac{1}{(z(q)-z(\sigma_i(q)))^2}\cr
&&= \int_{\partial_\Omega}\Lambda_{\Omega}(p)\Res_{q\to p_i}\frac{dE_{i,q}(p)dz_i(q)dz_i(\sigma_i(q))}{\omega_i(q)}\frac{1}{(z(q)-z(\sigma_i(q)))^2}=-\frac{1}{24}\frac{\delta_\Omega[y'(p_i)]}{y'(p_i)}\eea
Indeed, recall that $\delta_\Omega[y(z)]dx(z)=\Omega(z)=\int_{\partial_\Omega} \Lambda_\Omega(p)B(p,z)$  so that since the ramification points are not varied (because $x$ is not varied):
\beq -\frac{1}{24}\frac{\delta_{\Omega}[y'(p_i)]}{y'(p_i)}=-\frac{1}{24y'(p_i)}\left[\int_{\partial_\Omega} \Lambda_\Omega(p) \partial_{z}\left(\frac{B(p,z)}{dx(z)}\right)\right]_{|\,z=p_i}\eeq

Eventually, collecting the previous results, we get
\bea \int_{\partial_\Omega}\omega_{1,1}(p)\Lambda_{\Omega}(p)&=&-\frac{1}{24}\sum_{i=1}^N\delta_\Omega[y'(p_i)]-\frac{1}{2}\delta_\Omega[\ln \tau]\cr
&&-  \int_{\partial_\Omega}\Lambda_{\Omega}(p)\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(p)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
\eea 
We end up with
\beq \int_{\partial_\Omega}\omega_{1,1}(p)\Lambda_{\Omega}(p)=-\frac{1}{24}\sum_{i=1}^N\delta_\Omega[y'(p_i)]-\frac{1}{2}\delta_\Omega[\ln \tau]-\delta_{\Omega}\left[\frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)_{z=a_s}\right]
\eeq
and thus
\beq \int_{\partial_\Omega}\omega_{1,1}(p)\Lambda_{\Omega}(p)= \delta_{\Omega}\left[-\frac{1}{24}\sum_{i=1}^Ny'(p_i) -\frac{1}{2}\ln \tau-\frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)_{z=a_s}\right] \eeq
ending the proof.




\section{Proof of variational formulas with respect to LogTR-vital singularities for correlators}\label{AppendixVariationProofLogPoles}
\subsection{Properties of $\Omega_{a_r}$}
From the global decomposition of $ydx$ and the skew-symmetry of the prime form $E(q,p)=-E(p,q)$, we have that
\beq  ydx(q)=\sum_{a_s} y_{a_s}\ln \frac{E(q,a_s)}{E(q,o)} dx(q) + \td{y}dx(q)\eeq
Thus,
\beq d_{a_r}[ydx(q)]= y_{a_r}\frac{d_{a_r}[E(q,a_r)]}{E(q,a_r)}dx(q)= y_{a_r}d_{a_r}[\ln (E(q,a_r))] dx(q) \eeq
which defines
\beq \Omega_{a_r}(q):=%d_{a_r}[ydx(q)]= y_{a_r}\frac{d_{a_r}[E(a_r,q)]}{E(a_r,q)}dx(q)= 
y_{a_r}d_{a_r}[\ln (E(a_r,q))] dx(q) \eeq
Thus $\Omega_{a_r}$ is a differential with the following properties:
\begin{itemize}
    \item It is holomorphic on $\Sigma$ except a simple pole at $q=a_r$.
    \item It has non-vanishing monodromies along the homology cycles
\end{itemize}
The fact that it has monodromies on the homology cycles implies that one needs to be careful in the computations. Computations make sense locally, hence residues involving $\Omega_{a_r}$ are allowed and can be handled standardly, but identities using global properties (for example the Riemann bilinear identity) should be handled with care. 

\subsection{Proof of \autoref{TheoVariationsLogTRpoles}}


%Let us first prove that the two formulations of the right side are identical. We start from Riemann bilinear identity (\autoref{RiemannBilinearIdentity}) for $\omega_1(q)=dS_{o,q}(a_r)dx(q)$ and $\omega_2(q)=\omega_{h,n+1}(z_1,\dots,z_n,q)$. Since $n+1\geq 2$, the poles of $\omega_1$ and $\omega_2$ are $q=a_r$, the poles of $dx$, and the branchpoints $q=p_i$ (there are no poles at the other logTR-vital singularities). Moreover, $\omega_2$ is normalized on the $A$-cycles so that we get:
%\small{\bea &&\Res_{q\to a_r} dS_{o,q}(a_r)dx(q) \left(\int_o^q\omega_{h,n+1}(z_1,\dots,z_n,.)\right) + \sum_{\beta \text{ poles of } dx} \Res_{q\to \beta}dS_{o,q}(a_r) dx(q)\left(\int_o^q\omega_{h,n+1}(z_1,\dots,z_n,.)\right)  \cr&&
%+ \sum_{i=1}^N \Res_{q\to p_i} dS_{o,q}(a_r)dx(q) \left(\int_o^q\omega_{h,n+1}(z_1,\dots,z_n,.)\right)
%=\frac{1}{2i\pi}\sum_{j=1}^g\left(\oint_{s\in\mathcal{A}_j} dS_{o,s}(a_r) dx(s)\right)\left(\oint_{B_j} \omega_{h,n+1}(z_1,\dots,z_n,.)\right)\cr&&
%\eea}
%\normalsize{Thus}, we have
%\bea R&:=&y_{a_r}\Big[dx(a_r)\int_o^{a_r} \omega_{h,n+1}(z_1,\dots,z_n,.) \cr&&
%- \frac{1}{2i\pi}\sum_{j=1}^g\left(\oint_{s\in\mathcal{A}_j} dS_{o,s}(a_r) dx(s)\right)\left(\oint_{B_j} \omega_{h,n+1}(z_1,\dots,z_n,.)\right)\cr&&
%+\sum_{\beta \text{ poles of } dx} \Res_{q\to \beta} dS_{o,q}(a_r) dx(q)\left(\int_o^q\omega_{h,n+1}(z_1,\dots,z_n,.)\right)\Big]\cr
%&=& y_{a_r}\Big[dx(a_r)\int_o^{a_r} \omega_{h,n+1}(z_1,\dots,z_n,.) - \Res_{q\to a_r} dS_{o,q}(a_r)dx(q) \left(\omega_{h,n+1}(z_1,\dots,z_n,.)\right)\cr&&-\sum_{i=1}^N \Res_{q\to p_i} dS_{o,q}(a_r)dx(q) \left(\omega_{h,n+1}(z_1,\dots,z_n,.)\right)\Big]\cr
%&=&y_{a_r}\Big[-\sum_{i=1}^N \Res_{q\to p_i} dS_{o,q}(a_r)dx(q) \left(\omega_{h,n+1}(z_1,\dots,z_n,.)\right)\Big]
%\eea
%We now use the fact that $dS_{o,q}(a_r)dx(q)$ is holomorphic at the branchpoints and that $\omega_{h,n+1}(z_1,\dots,z_n,q)$ is meromorphic at the branchpoints. \textcolor{blue}{Thus, we get by local integration by part:}
%\beq R=y_{a_r}\sum_{i=1}^N \Res_{q\to p_i} \left(\int^{s=q}_{s=o} dS_{o,s}(a_r)dx(s)\right) \omega_{h,n+1}(z_1,\dots,z_n,q)\eeq
%Since $\omega_{h,n+1}(z_1,\dots,z_n,q)$ is residueless at $q=p_i$ we can change the lower bound in each residue:
%\beq R=y_{a_r}\sum_{i=1}^N \Res_{q\to p_i} \left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \omega_{h,n+1}(z_1,\dots,z_n,q)\eeq
%which recover the second formulation for the r.h.s.

%\medskip

In the formula, the contour of integration $\partial_{\Omega_{a_r}}$ includes a small loop around the ramification points. This case was excluded in the proof of \cite{EO07} and for the other variational formulas. This is why we need a specific proof for these variations and complications appear when exchanging the residues.

\medskip

Let us perform the induction procedure on $2h+n\geq 2$. We first need to initialize the induction for $(h,n)=(0,2)$. The Bergman kernel does not vary when we consider variations with respect to $a_r$, hence the l.h.s. is zero for $(h,n)=(0,2)$. The r.h.s. for $(h,n)=(0,2)$ reduces to
\beq \label{RHS02}\text{RHS}_{0,2}(z_1,z_2):=y_{a_r}\sum_{i=1}^N \Res_{q\to p_i}  %\left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) 
\left(\int_{p_i}^q \Omega_{a_r}\right)
\omega_{0,3}(z_1,z_2,q)\eeq
Moreover, recall that
\beq \omega_{0,3}(z_1,z_2,q)= \frac{1}{2}\sum_{i=1}^N \Res_{z\to p_i} \frac{dS_{z,\sigma_i(z)}(q)}{y(\sigma_i(z))dx(z) -y(z)dx(z)}\left(B(z,z_1)B(\sigma_i(z),z_2)+ B(\sigma_i(z),z_1)B(z,z_2) \right)\eeq
so that $\omega_{0,3}$ has at most double poles at $z_1=p_i$ (because the Bergman kernel has a double pole on the diagonal and no other singularities) and thus by symmetry of $\omega_{0,3}$, it may have at most double poles at $q=p_i$. On the contrary, we have:
%\beq \int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\overset{q\to p_i}{=} 0+ dS_{o,p_i}(a_r)dx(p_i)(q-p_i)  + O\left((q-p_i)^2\right)=O\left((q-p_i)^2\right)\eeq
\beq \int_{p_i}^q \Omega_{a_r}\overset{q\to p_i}{=} 0+ \frac{\Omega_{a_r}(p_i)}{dp_i}(q-p_i) + O\left((q-p_i)^2\right)=O\left((q-p_i)^2\right)\eeq
because $\Omega_{a_r}(p_i)= d_{a_r}[y(p_i)] dx(p_i)=0$ since $dx(p_i)$ because $p_i$ is a ramification point. Thus the integrand in the residue of \eqref{RHS02} is regular at $q=p_i$ so that the residue is zero and $\text{RHS}_{0,2}(z_1,z_2)=0$ initializing the induction procedure.

\medskip 

Let us now proceed with the induction and assume that the formula holds for any $(h',n')$ such that $2h'+n'< 2h+n$. We now look at $d_{a_r}\omega_{h,m}(z_1,\dots, a_m)$ and we recall that
%\beq \label{ExprOmegaar}\Omega_{a_r}(z)da_r:= d_{a_r}[ydx(z)]=y_{a_r}dS_{o,z}(a_r) dx(z)\eeq
\beq \label{ExprOmegaar}\Omega_{a_r}(z)da_r:= d_{a_r}[ydx(z)]=y_{a_r}d_{a_r}[\ln (E(a_r,z))] dx(z)\eeq
From \eqref{LogTRDef}, we have by definition:
\bea \label{DefomegahmlogTR}\omega_{h,m}(z_1,\dots,z_m)&:=&-\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)
    \eea  
Thus, applying the variation and using the fact that the Bergmann kernel and $x$ do not vary, we get
%\bea &&d_{a_r}[\omega_{h,m}(z_1,\dots,z_m) ]=\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1) (\Omega_{a_r}(z) -\Omega_{a_r}(\sigma_i(z))da_rdx(z)}{\omega_i(z)^2}\cr&&\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
%    &&+ \sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}d_{a_r}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
%    &&+\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}B(a_s,z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr
%    &&+ \delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\frac{1}{z-a_s} \right)\cr&&
%:= (A) + (B) +(C)
%\eea
\beq d_{a_r}[\omega_{h,m}(z_1,\dots,z_m) ]=(A)+(B)+(C)\eeq
with
\footnotesize{\bea (A)&:=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1) (\Omega_{a_r}(z) -\Omega_{a_r}(\sigma_i(z))da_r}{\omega_i(z)^2}\cr&&\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
(B)&:=& - \sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}d_{a_r}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
(C)&:=& \delta_{m,1}\Res_{z\to a_r}B(a_r,z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\ln(z-a_r) \right)\cr&&+ \delta_{m,1}da_r\Res_{z\to a_r}dS_{a_r,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\frac{1}{z-a_r} \right)
\eea}
\normalsize{}
We now apply the induction results on the terms in $(B)$. We find:
\small{\bea \frac{(B)}{da_r}&=&(B_1)+ (B_2) \,\text{ with }\cr
(B_1)&:=&-y_{a_r}\sum_{i=1}^N\sum_{j=1}^N\Res_{z\to p_i}\Res_{s\to p_j}\frac{dE_{i,z}(z_1)}{\omega_i(z)}%\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]
\Big[\omega_{h-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,s)\cr&&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(z,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \cr&& 
+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_i(z),z_{I_2},s)
\Big]\cr
(B_2)&:=&-y_{a_r}\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big[\cr&&
\sum_{k=1}^{h-1}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}dx(q)\left(\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-1-k,m+2}(z,\sigma_i(z),z_2,\dots,z_m,q)}{dx(q)}\right)_{|\, q=a_r}\cr&&
+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \sum_{k=1}^{h_1}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_1-k,|I_1|+2}(z,z_{I_1},q)}{dx(q)}\right)_{|\, q=a_r} \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2})\cr&&
+ \sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1})\sum_{k=1}^{h_2}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_2-k,|I_2|+2}(\sigma_{i}(z),z_{I_2},q)}{dx(q)}\right)_{|\, q=a_r} 
\Big]\cr&&
\eea}
\normalsize{Let} us focus first on $(B_1)$. We exchange the residues using \eqref{ResidueExchange}:
\bea (B_1)&=&-y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big[\omega_{h-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,s)\cr&&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(z,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \cr&& 
+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_i(z),z_{I_2},s)
\Big]\cr&&
- y_{a_r}\sum_{i=1}^N\Res_{z\to p_i}\Res_{s\to z,\sigma_{i}(z)}\frac{dE_{i,z}(z_1)}{\omega_i(z)}%\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\Big[\omega_{h-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,s)\cr&&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(z,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \cr&& 
+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_i(z),z_{I_2},s)
\Big]
\eea
Let us now observe that the residues at $s=z$ or $z=\sigma_i(z)$ do not provide any contribution. Indeed, the only cases where they should contribute would be $\omega_{0,2}(z,s)$ or $\omega_{0,2}(\sigma_i(z),s)$. However, these terms never appear in the sum because we exclude $(h_i,|I_i|)=(0,0)$ so that $\omega_{h_i,|I_i|+2}$ can never be equal to $\omega_{0,2}$. Thus, we get:
\bea (B_1)&=&-y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big[\omega_{h-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,s)\cr&&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+2}(z,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \cr&& 
+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+2}(\sigma_i(z),z_{I_2},s)
\Big]
\eea

Since $m+1\geq 2$, we have by definition (there are no special LogTR terms):
\bea &&\omega_{h,m+1}(z_1,\dots,z_m,s):=-\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\omega_{h-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,s)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m,s\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
&&= -\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\omega_{h-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,s)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_2,|I_2|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_1,|I_1|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1},s) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2},s)  \Big)
\eea 
\sloppy{Thus in $(B_1)$ we lack the extra-terms $\omega_{0,2}(z,s)\omega_{h,m}(\sigma_i(z),z_2,\dots,z_m)$ and $\omega_{0,2}(\sigma_i(z),s)\omega_{h,m}(z,z_2,\dots,z_m)$.}
\bea (B_1)&=&y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\omega_{h,m+1}(z_1,\dots,z_m,s) \cr
&&+ y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\omega_{0,2}(z,s)\omega_{h,m}(\sigma_i(z),z_2,\dots,z_m)\cr&&
+ y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\omega_{0,2}(\sigma_i(z),s)\omega_{h,m}(z,z_2,\dots,z_m)\cr
&\overset{z\to \sigma_i(z)}{=}&y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\omega_{h,m+1}(z_1,\dots,z_m,s) \cr
&&+ 2y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\omega_{0,2}(z,s)\omega_{h,m}(\sigma_i(z),z_2,\dots,z_m)\cr&&
\eea
Let us again exchange the residues in the last term using \eqref{ResidueExchange}. \\
We observe that $\underset{s\to p_j}{\Res}\, \omega_{0,2}(z,s) %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]=0$, because the integrand is regular at $s=p_j$. The residue at $s=z$ simply gives the derivative with respect to $s$ of the integral. Thus, we get:
\bea \label{B1Expression} (B_1)&=&y_{a_r}\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]\omega_{h,m+1}(z_1,\dots,z_m,s) \cr
&&+ 2y_{a_r}\sum_{j=1}^N\Res_{z\to p_j} %dS_{o,z}(a_r)dx(z)
d_{a_r}[ydx(z)]\frac{dE_{j,z}(z_1)}{\omega_j(z)}\omega_{h,m}(\sigma_j(z),z_2,\dots,z_m)
\eea

\medskip
Let us now look at term $(A)$. We shall denote
\beq f_{h,m}(z,z',z_2,\dots,z_m):=\omega_{h-1,m+1}(z,z',z_2,\dots,z_m)+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(z',z_{I_2})\eeq
the symmetric form appearing on the r.h.s. We have
\bea (A)
&=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1) (\Omega_{a_r}(z) -\Omega_{a_r}(\sigma_i(z))da_r}{\omega_i(z)^2} f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr
&=&2\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1) \Omega_{a_r}(z)da_r}{\omega_i(z)^2} f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr
&=&2\sum_{j=1}^N\Res_{z\to p_j}\Res_{s\to z}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r dE_{j,z}(s)}{\omega_j(z)\omega_{j}(s)}f_{h,m}(z,\sigma_j(z),z_2,\dots,z_m)
\eea

Rauch variational formula \eqref{VariationdE} implies that
\bea 0&=&\sum_{i=1}^N \Res_{z\to p_i}\frac{d_{a_r}[dE_{i,z}(z_1)]}{\omega_i(z)}f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr
&=&\sum_{i=1}^N\Res_{z\to p_i}\sum_{j=1}^N \Res_{s\to p_j} \frac{dE_{j,s}(z_1)}{\omega_{j}(s)\omega_{i}(z)}\left(\Omega_{a_r}(s)dE_{i,z}(\sigma_j(s))+\Omega_{a_r}(\sigma_j(s))dE_{i,z}(s)\right)da_r f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr
&=&2\sum_{i=1}^N\Res_{z\to p_i}\sum_{j=1}^N \Res_{s\to p_j} \frac{dE_{j,s}(z_1)}{\omega_{j}(s)\omega_{i}(z)}\Omega_{a_r}(s)dE_{i,z}(\sigma_j(s))da_r f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)
\eea
Exchanging residues using \eqref{ResidueExchange} gives
\bea 0&=& 2\sum_{j=1}^N\Res_{s\to p_j} \sum_{i=1}^N\Res_{z\to p_i}  \frac{dE_{j,s}(z_1)}{\omega_{j}(s)\omega_{i}(z)}\Omega_{a_r}(s)dE_{i,z}(\sigma_j(s))da_r f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr&&
+2\sum_{j=1}^N\Res_{z\to p_j} \Res_{s\to z} \frac{dE_{j,s}(z_1)}{\omega_{j}(s)\omega_{j}(z)}\Omega_{a_r}(s)dE_{j,z}(\sigma_j(s))da_r f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)
\eea
so that
\bea (A)&=&2\sum_{j=1}^N\Res_{s\to p_j} \sum_{i=1}^N\Res_{z\to p_i}  \frac{dE_{j,s}(z_1)}{\omega_{j}(s)\omega_{i}(z)}\Omega_{a_r}(s)dE_{i,z}(\sigma_j(s))da_r f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr
&=&2\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r}{\omega_{j}(s)} \sum_{i=1}^N\Res_{z\to p_i}  \frac{dE_{i,z}(\sigma_j(s))}{\omega_{i}(z)} f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr&&
\eea
By definition, we have
\bea \omega_{h,m}(s,z_2,\dots,z_m)&=&-\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(s)}{\omega_i(z)} f_{h,m}(z,\sigma_i(z),z_2,\dots,z_m)\cr
&&-\delta_{m,1}\sum_{k=1}^M\Res_{z\to a_k}\left(\int_{a_k}^z\omega_{0,2}(s,.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\cr&&
\eea
Thus we get
\bea (A)&:=&(A_1)+(A_2)\,\text{ with }\cr
(A_1)&=&-2\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r}{\omega_{j}(s)}\omega_{h,m}(\sigma_j(s),z_2,\dots,z_m)\cr
(A_2)&:=& -2\delta_{m,1}\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r}{\omega_{j}(s)}\cr&&\left(\sum_{k=1}^M\Res_{z\to a_k}\left(\int_{a_k}^z\omega_{0,2}(\sigma_j(s),.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\right)
\eea
Since $\Omega_{a_r}(s)=y_{a_r}d_{a_r}[y(s)] dx(s)$, we have: 
\beq (A_1)=-2y_{a_r}\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1) %dS_{o,s}(a_r)
d_{a_r}[y(s)]dx(s)}{\omega_{j}(s)}\omega_{h,m}(\sigma_j(s),z_2,\dots,z_m)
\eeq
Thus, using the expression of $(B_1)$ given by \eqref{B1Expression}, we find:
\beq \label{ExpressionAPlusB1} (A)+(B_1)da_r=y_{a_r}da_r\sum_{j=1}^N\Res_{s\to p_j} %\left(\int^{q=s}_{q=p_i} dS_{o,q}(a_r)dx(q)\right)
d_{a_r}[\Phi_{p_i}(s)]
\omega_{h,m+1}(z_1,\dots,z_m,s) \eeq 

\medskip
At this point, the term $(A)+(B_1)da_r$ corresponds to the first part of the induction. In order to prove the induction, we need to prove that
\beq \label{SecondPartProof}(A_2)+(B_2)da_r+ (C)=y_{a_r}da_r\sum_{k=1}^h [\hbar^{2k}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k,m+1}(z_1,\dots,z_m,q)}{dx(q)}\right)_{|\, q=a_r}\eeq
where
\small{\bea (C)&:=& \delta_{m,1}\Res_{z\to a_r}B(a_r,z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\ln(z-a_r) \right)\cr&&+ \delta_{m,1}da_r\Res_{z\to a_r}dS_{a_r,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\frac{1}{z-a_r} \right)\cr
(A_2)&:=& -2\delta_{m,1}\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r}{\omega_{j}(s)}\cr&&\left(\sum_{k=1}^M\Res_{z\to a_k}\left(\int_{a_k}^z\omega_{0,2}(\sigma_j(s),.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\right)\cr
(B_2)&:=&-y_{a_r}\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big[\cr&&
\sum_{k=1}^{h-1}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-1-k,m+2}(z,\sigma_i(z),z_2,\dots,z_m,q)}{dx(q)}\right)_{|\, q=a_r}\cr&&
+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \sum_{k=1}^{h_1}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_1-k,|I_1|+2}(z,z_{I_1},q)}{dx(q)}\right)_{|\, q=a_r} \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2})\cr&&
+ \sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1})\sum_{k=1}^{h_2}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_2-k,|I_2|+2}(\sigma_{i}(z),z_{I_2},q)}{dx(q)}\right)_{|\, q=a_r} 
\Big]\cr&&
\eea
}
\normalsize{}In the third line, note that $(h_1,|I_1|)=(0,0)$  can be added since it does not contribute because the sum over $k$ is empty. Moreover, the case $h_2=h$ provides an empty sum over $k$. Similarly, in the fourth line, the term $(h_2,|I_2|)=(0,0)$ can be added and the case $h_1=h$ also provides an empty sum over $k$. Thus, we can rewrite $(B_2)$ as:
\small{\bea\label{RformulationB2} &&(B_2)=-
y_{a_r}\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big[\cr&&
\sum_{k=1}^{h-1}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-1-k,m+2}(z,\sigma_i(z),z_2,\dots,z_m,q)}{dx(q)}\right)_{|\, q=a_r}\cr&&
+\sum_{\substack{0\leq h_2\leq h-1\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_2,|I_2|)\neq (0,0)}} \sum_{k=1}^{h-h_2}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-h_2-k,|I_1|+2}(z,z_{I_1},q)}{dx(q)}\right)_{|\, q=a_r} \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2})\cr&&
+ \sum_{\substack{0\leq h_1\leq h-1\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_1,|I_1|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1})\sum_{k=1}^{h_2}[\hbar^{2k}]\frac{1}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-h_1-k,|I_2|+2}(\sigma_{i}(z),z_{I_2},q)}{dx(q)}\right)_{|\, q=a_r} 
\Big]\cr&&
\eea}

\normalsize{Let} us start from the expected result. Since $m+1\geq 2$ (there are no special LogTR terms), we have for $(h-k,m+1)\neq (0,2)$:
\small{\bea 
&&\frac{\omega_{h-k,m+1}(z_1,\dots,z_m,q)}{dx(q)}=-\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\frac{\omega_{h-k-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,q)}{dx(q)}\cr
    &&+\sum_{\substack{h_1+h_2=h-k\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_2,|I_2|)\neq (0,0)}} \frac{\omega_{h_1,|I_1|+1}(z,z_{I_1},q)}{dx(q)} \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2})+\sum_{\substack{h_1+h_2=h-k\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_1,|I_1|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \frac{\omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2},q)}{dx(q)} \Big)\cr&&
\eea}
\normalsize{Thus}, the r.h.s. $R$ of \eqref{SecondPartProof} is for $m\neq 1$
\footnotesize{\bea \label{Casemneq1} &&\frac{R}{da_r}\delta_{m\neq1}=-
\delta_{m\neq1}y_{a_r}\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)} \Big[\sum_{k=1}^{h} [\hbar^{2k}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,q)}{dx(q)}\right)_{|\, q=a_r}\cr&&
+ \sum_{k=1}^h [\hbar^{2k}]\sum_{\substack{h_1+h_2=h-k\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_2,|I_2|)\neq (0,0)}}\omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2})\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}} \frac{\omega_{h_1,|I_1|+2}(z,z_{I_1},q)}{d(q)}\right)_{|\, q=a_r}\cr&&
+\sum_{k=1}^h [\hbar^{2k}]\sum_{\substack{h_1+h_2=h-k\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_1,|I_1|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_2,|I_2|+2}(\sigma_i(z),z_{I_2},q)}{dx(q)}\right)_{|\, q=a_r}\Big]
\eea}
\normalsize{while} it is for $m=1$:
\bea\label{Casemequal1}&&\frac{R}{da_r}\delta_{m=1}= \delta_{m=1}y_{a_r}da_r  [\hbar^{2h}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_r}\cr&& 
-y_{a_r}\delta_{m=1}\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)} \Big[\sum_{k=1}^{h-1} [\hbar^{2k}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k-1,3}(z,\sigma_i(z),q)}{dx(q)}\right)_{|\, q=a_r}\cr&&
+ \sum_{k=1}^{h-1} [\hbar^{2k}]\sum_{\substack{h_1+h_2=h-k\\h_2\neq 0}}\omega_{h_2,1}(\sigma_i(z))\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}} \frac{\omega_{h_1,2}(z,q)}{d(q)}\right)_{|\, q=a_r}\cr&&
+\sum_{k=1}^{h-1} [\hbar^{2k}]\sum_{\substack{h_1+h_2=h-k \\h_1\neq 0}} \omega_{h_1,1}(z) \frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_2,2}(\sigma_i(z),q)}{dx(q)}\right)_{|\, q=a_r}
\Big]
\eea

In the first sum of \eqref{Casemneq1}, the case $k=h$ gives $\omega_{-1,m+2}=0$ so it is null by definition. Thus, we get:
\footnotesize{\bea \label{Rexpression}&&\frac{R}{da_r}\delta_{m\neq 1}=-y_{a_r}\delta_{m\neq 1}\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)} \Big[\sum_{k=1}^{h-1} [\hbar^{2k}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k-1,m+2}(z,\sigma_i(z),z_2,\dots,z_m,q)}{dx(q)}\right)_{|\, q=a_r}\cr&&
+ \sum_{k=1}^h [\hbar^{2k}]\sum_{\substack{0\leq h_2\leq h-k\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_2,|I_2|)\neq (0,0)}}\omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2})\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}} \frac{\omega_{h-k-h_2,|I_1|+2}(z,z_{I_1},q)}{d(q)}\right)_{|\, q=a_r}\cr&&
+\sum_{k=1}^h [\hbar^{2k}]\sum_{\substack{0\leq h_1 \leq h-k\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_1,|I_1|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k-h_1,|I_2|+2}(\sigma_i(z),z_{I_2},q)}{dx(q)}\right)_{|\, q=a_r}
\Big]\cr&&
\eea}
\normalsize{We} can exchange the sums: $\underset{k=1}{\overset{h}{\sum}}\underset{h_2=0}{\overset{h-k}{\sum}}= \underset{h_2=0}{\overset{h-1}{\sum}}\underset{k=1}{\overset{h-h_2}{\sum}}$. For $|I_2|=0$, we have the reduced sum $\underset{k=1}{\overset{h}{\sum}}\underset{h_2=1}{\overset{h-k}{\sum}}=\underset{h_2=1}{\overset{h-1}{\sum}}\underset{k=1}{\overset{h-h_2}{\sum}}$. Similar identities hold for $h_1$. In particular, after this exchange we observe that the expression of $R$ matches with the expression of $(B_2)$ given by \eqref{RformulationB2}.
Similarly, for $m=1$, we have $\underset{k=1}{\overset{h-1}{\sum}}\underset{h_2=1}{\overset{h-k}{\sum}}=\underset{h_2=1}{\overset{h-1}{\sum}}\underset{k=1}{\overset{h-h_2}{\sum}}$. The first double sum appears in \eqref{Casemequal1}  while the second one appear in \eqref{RformulationB2}. Thus we get:
\beq\label{IdentityRB2} \forall \,m\geq 1\,:\, R=(B_2)da_r +\delta_{m=1}y_{a_r}da_r  [\hbar^{2h}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_r}\eeq

In the end, from \eqref{SecondPartProof}, the induction is equivalent to prove that
\beq (A_2)+(C)=\delta_{m=1}y_{a_r}da_r  [\hbar^{2h}]\frac{1}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_r}\eeq
In $(A_2)$, we can exchange the residues because there are located at different points:
\small{\bea (A_2)&:=&- 2\delta_{m,1}\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r}{\omega_{j}(s)}\cr&&\left(\sum_{k=1}^M\Res_{z\to a_k}\left(\int_{a_k}^z\omega_{0,2}(\sigma_j(s),.)\right)dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\right)\cr
&=&- 2\delta_{m,1}\sum_{k=1}^M\Res_{z\to a_k}dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)\Omega_{a_r}(s)da_r}{\omega_{j}(s)}dS_{a_k,z}(\sigma_j(s))\cr&&
\eea}
\normalsize{Using} \eqref{ExprOmegaar}, it gives
\small{\beq (A_2)= -2y_{a_r}\delta_{m,1}\sum_{k=1}^M\Res_{z\to a_k}dx(z)[\hbar^{2h}]\left(\frac{y_{a_k}}{\mathcal{S}(y_{a_k}^{-1}\hbar \partial_x)}\ln(z-a_k) \right)\sum_{j=1}^N\Res_{s\to p_j}\frac{dE_{j,s}(z_1)%dS_{o,s}(a_r)
d_{a_r}[y(s)]dx(s)}{\omega_{j}(s)}dS_{a_k,z}(\sigma_j(s))
\eeq}
\normalsize{Since} $\omega_j(s)=(y(s)-y(\sigma_j(s)))dx(s)$, it has a double zero at $s=p_j$. Similarly $dx(s)$ has a simple zero and $dE_{j,s}(z_1)=\int_{\sigma_j(s)}^s B(.,z_1)$ as a simple zero at $s=p_j$. Finally %$dS_{o,s}(a_r)$ 
$d_{a_r}[y(s)]$ and $dS_{a_k,z}(\sigma_j(s))$ are regular at $s=p_j$ so that the integrand is regular at $s=p_j$ and we find
\beq (A_2)=0\eeq
The expression for $(C)$ is
\bea (C)&:=&(C_1)+(C_2) \text{ with }\cr
(C_1)&:=&\delta_{m,1}B(a_r,z_1)\Res_{z\to a_r}dx(z)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\ln(z-a_r) \right)\cr
(C_2)&:=&\delta_{m,1}da_r\Res_{z\to a_r}dS_{a_r,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\frac{1}{z-a_r} \right)
\eea
The expression for $(C_1)$ is:
\bea (C_1)&=&\delta_{m,1}B(a_r,z_1)\Res_{z\to a_r}dx(z)\left(\frac{\partial^{2h}}{\partial x(z)^{2h}}\ln(z-a_r)\right) [\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right) \cr
&=& \delta_{m,1}B(a_r,z_1)\Res_{z\to a_r}\, dx(z) \frac{\partial}{\partial x(z)}\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\ln(z-a_r)\right)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right) \cr&&
\eea
Since $dx(z)\frac{\partial}{\partial x(z)}= d_z$ we get
\beq (C_1)=\delta_{m,1}B(a_r,z_1)\Res_{z\to a_r}dz\, \frac{\partial}{\partial z}\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\ln(z-a_r)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right)\right)=0 \eeq
because we are computing the residue of the total derivative of a meromorphic form at $z=a_r$. ($2h-1\geq 1$ so $\frac{\partial^{(2h-1)}}{\partial x(z)^{2h-1}}\ln(z-a_r)$ is meromorphic at $z=a_r$).

A similar computation for $(C_2)$ gives
\bea (C_2)&=&\delta_{m,1}da_r\Res_{z\to a_r}dS_{a_r,z}(z_1)dx(z)\left(\frac{\partial^{2h}}{\partial x(z)^{2h}}\frac{1}{z-a_r}\right) [\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right)\cr
&=&\delta_{m,1}da_r\Res_{z\to a_r}dS_{a_r,z}(z_1)dx(z)\frac{\partial}{\partial x(z)}\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}\right) [\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right)\cr
&=&\delta_{m,1}da_r\Res_{z\to a_r}dz \,dS_{a_r,z}(z_1)\frac{\partial}{\partial z}\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right)\right) \cr
&=&-\delta_{m,1}da_r[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right)\Res_{z\to a_r} \,B(z,z_1)\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}\right)
\eea
Performing multiple integrations by parts for local meromorphic functions and computing the residue, we get that
\beq\label{AppFCorTerm} (C_2)=\delta_{m=1}da_r  [\hbar^{2h}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_r}.\eeq

Let us bring this term into another more compact form.
We can use the identity
\bea &&[\hbar^{2h}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{h,k+1}(z,z_1,\dots,z_k)}{dx(q)}\right)_{|\, q=a_r}\cr
&&=-[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\right)\Res_{z\to a_r} \,\omega_{h,k+1}(z,z_1,\dots,z_k)\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}\right)\cr
&&=\Res_{z\to a_r} \,dx(z)\left(\int_o^z\omega_{h,k+1}(.,z_1,\dots,z_k)\right)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{z-a_r}
\eea
to reformulate \eqref{AppFCorTerm} into
\bea &&d_{a_r}[\omega_{h,n}(z_1,\dots,z_n)] 
= y_{a_r}\sum_{i=1}^N \Res_{q\to p_i} \left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \omega_{h,n+1}(z_1,\dots,z_n,q)\cr\label{Gnewform}
&&+ da_r\sum_{k=1}^h \Res_{z\to a_r} dx(z)\left(\int_o^z \omega_{h-k,n+1}(.,z_1,\dots,z_n)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{z-a_r}
\eea

Next we have the following lemma.
\begin{lemma}\label{Lem:trick2}
    Let $F(q)$ be a smooth 1-form at $a$.
    We have the following relations (for any $k\in \mathbb{N}$):
   \bea 
dx(a)\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^k \log(q-a) &=&-\Res_{q\to a} \left(\int^q_oF(q)\right)dx(q)\left(\frac{\partial}{\partial x(q)}\right)^k \frac{1}{q-a}\cr
&=&\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^{k-1} \frac{1}{q-a}
\eea
and 
\beq \Res_{q\to a} (x(q)-x(a))F(q)\left(\frac{\partial}{\partial x(q)}\right)^k \frac{1}{q-a}=-k\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^{k-1} \frac{1}{q-a}.
\eeq
\end{lemma}
\begin{proof}
The first relation follows from the fact $dx(a)\frac{\partial}{\partial x(q)}\log(q-a)-\frac{1}{q-a}$ is regular at $q\to a$. Acting on this with $k-1$ derivative wrt $x(q)$ and multiplying it with $F(q)$ gives a 1-form which is regular at $q\to a$ and has therefore a vanishing residue:
\beq\Res_{q\to a} F(q)\frac{\partial^{k-1}}{\partial x(q)^{k-1}}\left(dx(a)\frac{\partial}{\partial x(q)}\log(q-a)-\frac{1}{q-a}\right)=0.\eeq
The last identity is achieved by integration by parts and the fact that $\frac{x(q)-x(a)}{q-a}$ is regular at $q\to a$. Thus, acting with $k$ derivatives wrt $x(q)$ on it and multiplying with $F(q)$ gives a regular 1-form at $q\to a$, thus vanishing residue.
\beq\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^k\frac{x(q)-x(a)}{q-a}=0,
\eeq
where one can perform the $x(q)$ derivative $\left(\frac{\partial}{\partial x(q)}\right)^k\frac{x(q)-x(a)}{q-a}=(x(q)-x(a))\left(\frac{\partial}{\partial x(q)}\right)^k\frac{1}{q-a}+k\left(\frac{\partial}{\partial x(q)}\right)^{k-1}\frac{1}{q-a}$.
\end{proof}


Eventually, taking \eqref{Gnewform}, integrating once by parts and using  the first equation of \autoref{Lem:trick2} with $F(q)=\omega_{h-h_1,n+1}(I,q)$ and the remaining part corresponds to the singular part of $\omega_{h_1,1}(q)$ at the LogTR-vital singularity $a_r$ provides the proof.



%\begin{remark}
 %   Note that the first term in \eqref{NewVariation} corresponds to a regularized version of the missing term in the second line. In the second line the term with $h_1=0$ is excluded. $d_{a_r}[\Phi(q)]$ behaves at $q\to a_r$ like $dx(a_r)\frac{\omega_{0,1}(q)}{dx(q)}$ (the constant term is already different). However, since logarithm appear, the contour can not be moved around $q\to a_r$ easily just after integration by parts. The result is
 %   \begin{align*}
 %       d_{a_r}[\omega_{h,n}(z_1,\dots,z_n)]= \Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\underset{h_1=1}{\overset{h}{\sum}} \omega_{h_1,1}(q)\omega_{h-h_1,n+1}(I,q)-dx(a_r)\Res_{q\to a_r}dy(q)\int_o^q\omega_{h,n+1}(I,q)+\text{const}(o).
 %   \end{align*}
 %   This seems to be similar to the third kind differentials. 
%\end{remark}


\section{Compatibility of the variational formulas for a log pole with the dilaton equations}\label{AppendixCompatVarLogTR}
In this section we prove that \autoref{TheoVariationsLogTRpoles} is compatible with \autoref{TheoremDilatonEquation}. Let $k\geq 1$ and $h\geq 0$ with $(k,h)\neq (1,0)$. The dilaton equation is
\bea -(2h+k-2)\omega_{h,k}(z_1,\dots,z_k)&=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\omega_{h,k+1}(z,z_1,\dots,z_k) \cr&&
-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr&&
\eea
Applying $d_{a_r}$ on the l.h.s. provides from \autoref{TheoVariationsLogTRpoles}:
\bea \label{LHSToCheck} &&d_{a_r}[\text{LHS}]:=(2-2h-k)\sum_{i=1}^N \Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)] \omega_{h,k+1}(z_1,\dots,z_k,q)\cr
&&+  (2-2h-k)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)
\eea
Applying $d_{a_r}$ on the r.h.s. provides
\bea d_{a_r}[\text{RHS}]&:=& (A)+(B)+(C)+(D)+(E) \,\text{ with}\cr
(A)&:=&\sum_{i=1}^N\Res_{z\to p_i} d_{a_r}[\Phi_{p_i}(z)]\omega_{h,k+1}(z,z_1,\dots,z_k) \cr
(B)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)d_{a_r}[\omega_{h,k+1}(z,z_1,\dots,z_k)] \cr
(C)&:=&dx(a_r)\Res_{z\to a_r} \frac{1}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr
(D)&:=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}d_{a_r}[\omega_{h_1,1} (z)]\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr
(E)&:=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
        \overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)d_{a_r}[\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)]
\eea
Using \autoref{TheoVariationsLogTRpoles}, we can split $(B)$ into two terms
\bea (B)&:=&(B_1)+(B_2) \text{ with}\cr
(B_1)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\sum_{j=1}^N \Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)] \omega_{h,k+2}(q,z,z_1,\dots,z_k) \cr
(B_2)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k) 
\eea 
Since $k+2\geq 3$, we have $\omega_{h,k+2}\neq \omega_{0,2}$ so we can exchange the two residues in $(B_1)$ without having a special term:
\bea 
(B_1)&:=&\sum_{j=1}^N \Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)]\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)  \omega_{h,k+2}(q,z,z_1,\dots,z_k) \cr
(B_2)&:=&\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h\omega_{h_1,1}(q)\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z) \omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k)
\eea
Let us now focus on $(D)$. Using \autoref{TheoVariationsLogTRpoles}, it splits into two parts:
\bea (D)&:=&(D_1)+(D_2)\, \text{ with}\cr
(D_1)&:=& -\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\sum_{i=1}^N \Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)]\omega_{h_1,2}(q,z)\cr
(D_2)&:=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h_1}\omega_{u,1}(q)\omega_{h_1-u,2}(q,z) \cr&&
\eea
Exchanging the residues in $(D_1)$, we have that all terms are regular at $z=a_j$ because we have $k+1\geq 2$ so that all correlation functions are regular at $z=a_j$ and $x(z)$ is regular at $z=a_j$. Thus, we get $(D_1)=0$. The same argument holds for $(D_2)$ but we get an extra term when $a_j=a_r$. From \eqref{ResidueExchange}, we have
\bea (D)&=&-\Res_{q\to a_r} \Res_{z\to q} \frac{x(z)-x(a_r)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h_1}\omega_{u,1}(q)\omega_{h_1-u,2}(q,z) \cr
&=&-\overset{h}{\underset{h_1=1}{\sum}}\Res_{q\to a_r}\omega_{h_1,1}(q)\frac{dx(a_r)}{dx(q)} \Res_{z\to q} \frac{x(z)-x(a_r)}{dx(z)}\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\omega_{0,2}(q,z) \cr
&=&-\overset{h}{\underset{h_1=1}{\sum}}\Res_{q\to a_r}\omega_{h_1,1}(q)\frac{dx(a_r)}{dx(q)} d_q\left(\frac{x(q)-x(a_r)}{dx(q)}\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)\right)\cr&&
\eea
Let us now decompose $(E)$. Using \autoref{TheoVariationsLogTRpoles}, we have
\bea (E)&:=&(E_1)+(E_2)\,\text{ with}\cr
(E_1)&:=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\sum_{i=1}^N\Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)]\omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k)\cr
(E_2)&:=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-h_1}\omega_{u,1}(q)\omega_{h-h_1-u,k+2}(q,z,q_1,\dots,z_k)\cr&&
\eea
Since $k+2\geq 3$, we can exchange the residues in $(E_2)$:
\bea 
(E_1)&=&-\sum_{i=1}^N\Res_{q\to p_i}d_{a_r}[\Phi_{p_i}(q)] \sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z) \omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k)\cr
(E_2)&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\overset{h}{\underset{h_1=1}{\sum}}\sum_{u=1}^{h-h_1}\sum_{j=1}^M\Res_{z\to a_j}\omega_{h_1,1} (z)\omega_{u,1}(q) \frac{x(z)-x(a_j)}{dx(z)}
\omega_{h-h_1-u,k+2}(q,z,q_1,\dots,z_k)\cr&&
\eea
We exchange the double sum $\underset{h_1=1}{\overset{h}{\sum}}\underset{u=1}{\overset{h-h_1}{\sum}}=\underset{u=1}{\overset{h-1}{\sum}}\underset{h_1=1}{\overset{h-u}{\sum}}$ so that
\bea (E_2)&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1}\omega_{u,1}(q)\sum_{h_1=1}^{h-u}\sum_{j=1}^M\Res_{z\to a_j}\omega_{h_1,1} (z) \frac{x(z)-x(a_j)}{dx(z)}
\omega_{h-h_1-u,k+2}(q,z,q_1,\dots,z_k)\cr&&
\eea

Let us now regroup $(A)$, $(B_1)$ and $(E_1)$. We have
\bea &&(A)+(B_1)+(E_1)=\sum_{i=1}^N\Res_{q\to p_i}d_{a_r}[\Phi_{p_i}(q)]\Big[\omega_{h,k+1}(q,z_1,\dots,z_k) \cr&&
-\sum_{j=1}^N\Res_{z\to p_j} \Phi_{p_j}(z)  \omega_{h,k+2}(q,z,z_1,\dots,z_k)+\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z) \omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k)\Big]\cr&&
\eea
In the second line, we recognize from \autoref{TheoremDilatonEquation} $(2-2h-k-1)\omega_{h,k+1}(q,z_1,\dots,z_k)$ so that
\beq (A)+(B_1)+(E_1)=(2-2h-k)\sum_{i=1}^N \Res_{q\to p_i}d_{a_r}[\Phi_{p_i}(q)]\omega_{h,k+1}(q,z_1,\dots,z_k)\eeq
which is precisely the first part of \eqref{LHSToCheck}. Thus, we are left with
\bea (B_2)&=&\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h\omega_{h_1,1}(q) \sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k)  \cr
(C)&=&dx(a_r)\Res_{z\to a_r} \frac{1}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\cr
(D)&=&-\overset{h}{\underset{h_1=1}{\sum}}\Res_{q\to a_r}\omega_{h_1,1}(q)\frac{dx(a_r)}{dx(q)} d_q\left(\frac{x(q)-x(a_r)}{dx(q)}\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)\right)\cr
(E_2)&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1}\omega_{u,1}(q)\sum_{h_1=1}^{h-u}\sum_{j=1}^M\Res_{z\to a_j} \frac{x(z)-x(a_j)}{dx(z)}\omega_{h_1,1} (z)
\omega_{h-h_1-u,k+2}(q,z,q_1,\dots,z_k)\cr
&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h}\omega_{u,1}(q)\sum_{h_1=1}^{h-u}\sum_{j=1}^M\Res_{z\to a_j} \frac{x(z)-x(a_j)}{dx(z)}\omega_{h_1,1} (z)
\omega_{h-h_1-u,k+2}(q,z,q_1,\dots,z_k)\cr&&
\eea
where we can add $u=h$ in the last equality because it provides an empty sum. Note that we should recover
\beq (2-2h-k)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)\eeq
Let us regroup $(B_2)+(E_2)$. The dilaton equation \autoref{TheoremDilatonEquation} gives:
\small{\bea &&(2-2h+2h_1-k-1)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)=(2-2h-k+2h_1-1)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)\cr
&&=\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\omega_{h-h_1,k+2}(q,z,z_1,\dots,z_k)
-\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}
        \overset{h-h_1}{\underset{u=1}{\sum}}\omega_{u,1} (z)\omega_{h-h_1-u,k+2} (q,z,z_1,\dots,z_k)\cr&&
\eea}
\normalsize{Thus}, we get:
\beq (B_2)+(E_2)=\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h(2-2h-k+2h_1-1)\omega_{h_1,1}(q)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)
\eeq
Thus, the compatibility of the dilaton equations with the variational formulas with respect to the LogTR-vital singularities are equivalent to prove that
\bea &&\sum_{h_1=1}^h\Res_{q\to a_r}(1-2h_1)\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)= (C)+(D)\cr&&
=\sum_{h_1=1}^h\Res_{q\to a_r} \frac{ dx(a_r)}{dx(q)}\omega_{h_1,1} (q)\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)\cr
&&-\sum_{h_1=1}^h \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) d_q\left(\frac{x(q)-x(a_r)}{dx(q)}\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)\right)
\eea
i.e.
\bea &&\sum_{h_1=1}^h\Res_{q\to a_r}2h_1\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q)\omega_{h-h_1,k+1}(q,z_1,\dots,z_k)\cr
&&=\sum_{h_1=1}^h \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) d_q\left(\frac{x(q)-x(a_r)}{dx(q)}\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)\right)
\eea
which is precisely the application of \autoref{LemmaIntW02Wg1} with $F(q)=\frac{x(q)-x(a_r)}{dx(q)}\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)$ which is holomorphic in a neighborhood of $q=a_r$.  







\section{Proof of \autoref{VariationalFormulaLogTRPole}: Variational formulas with respect to LogTR-vital singularities for free energies}\label{AppendixProofVarationalFormulasLogR}
%In this section, we want to prove the following theorem
%\begin{theorem}[Variation of the free energies with respect to logTR vital singularities]\label{VariationalFormulaLogTRPole}For any $r\in \llbracket 1,M\rrbracket$ and any $h\geq 2$, we have:
%\bea \label{EqToProve}&& d_{a_r}[\omega_{h,0}]=\sum_{i=1}^N\Res_{z\to p_i} d_{a_r}[\Phi_{p_i}(z)]\omega_{h,1}(z) +\frac{1}{2}\Res_{z\to a_r}\frac{dx(a_r)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,1} (z)\cr&&
%-\Res_{z\to a_r} dx(a_r) dy(z) \int_o^z\omega_{h,1}-\sum_{j=1}^M\Res_{z\to a_j} d_{a_r}[y(z)] dx(z)\int_o^z\omega_{h,1}
%\eea
%where $d_{a_r}[\Phi_{p_i}(z)]=y_{a_r}\int_{q=p_i}^{q=z} d_{a_r}[\ln (E(a_r,q))] dx(q) $\todo{AH: We don't need the branch point here $\Phi_{p_i}$, since $\omega_{h,1}$ is residue-free} that is locally holomorphic near the branchpoints. 
%{\color{blue} The formula is equivalent to 
%\bea \label{EqToProve2}&& d_{a_r}[\omega_{h,0}]=\Res_{z\to \{p_i\}\cup \{a_j\}} d_{a_r}[\Phi(z)]\omega_{h,1}(z) +\frac{1}{2}\Res_{z\to a_r}\frac{dx(a_r)}{dx(z)}\overset{h}{\underset{h_1=0}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,1} (z)
%\eea}
%\textcolor{red}{Technically, I agree that the reformulation are identical, but in the second one, we need to group $\Res_{z\to a_r} d_{a_r}[\Phi(z)] \omega_{h,1}(z)$ with $\Res_{z\to a_r} \frac{dx(a_r)}{dx(z)} \omega_{h,1}(z) ydx(z)=dx(a_r)\Res_{z\to a_r} \omega_{h,1}(z) y(z)$ because only $d_{a_r}[\Phi(z)]+dx(a_r)y(z)$ or (after integration by parts) $d_{a_r}[y(z)]dx(z)+dx(a_r)dy(z)$ is locally meromorphic at $z=a_r$. The first version does not have this ambiguity. Both should be mentioned but in the second one, ths important remark should be stated (put a tilde or "..." to indicate that the formula requires precision for its evaluation. }
%\end{theorem}

By definition, we have
\bea (2-2h)\omega_{h,0}&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\omega_{h,1}(z)
\cr&&
-\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\left(\frac{1}{2}
        \overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1}(z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right)\cr&&
\eea
where $\Phi_{p_i}(z)=\int_{p_i}^z ydx$. Since $x$ is not varied and $d_{a_r}[ydx(z)]=y_{a_r}dS_{o,z}(a_r) dx(z) $, 
we get that
\small{\bea (2-2h)d_{a_r}[\omega_{h,0}]&=&(A)+(B)+(C)+ (D)+ (E)+ (F)\text{ with}\cr
(A)&:=&\sum_{i=1}^N\Res_{z\to p_i} d_{a_r}[\Phi_{p_i}(z)]\omega_{h,1}(z)\cr 
(B)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)d_{a_r}[\omega_{h,1}(z)]\cr
(C)&:=&dx(a_r)\Res_{z\to a_r} \left(\frac{1}{2}\overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right)\cr
(D)&:=&-\frac{1}{2}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\left(\overset{h-1}{\underset{h_1=1}{\sum}}\frac{d_{a_r}[\omega_{h_1,1} (z)]\omega_{h-h_1,1}(z) +\omega_{h_1,1} (z)d_{a_r}[\omega_{h-h_1,1}(z)]}{dx(z)}\right)\cr
(E)&:=&y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)B(z,a_r)\int_o^z\omega_{h,1} \cr
(F)&:=& \sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z)\int_o^zd_{a_r}[\omega_{h,1}]
\eea}
\normalsize{From} \autoref{TheoVariationsLogTRpoles} we have:
\beq d_{a_r}[\omega_{h,1}(z)] 
= \sum_{i=1}^N \Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)] \omega_{h,2}(q,z)+ \Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,2}(q,z)
\eeq
Note that $d_{a_r}[\omega_{h,1}(z)]$ has only poles at the ramification points and at $z=a_r$ but not at the other LogTR-vital singularities. Thus we get from the fact that $(x(z)-x(a_j))dy(z)$ is regular at $z=a_j$:
\bea (F)&=&(F_1)+(F_2) \text{ with }\cr
(F_1)&:=&\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\sum_{i=1}^N \Res_{q\to p_i} d_{a_r}[\Phi_{p_i}(q)] \int_o^z\omega_{h,2}(q,.)\cr
(F_2)&:=&\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\int_o^z\omega_{h-h_1,2}(q,.)
\eea
Since the ramification points are away from $a_r$, we can swap the residues in $(F_1)$. But since $x(z)-x(a_r)$ has a simple zero, $dy(z)$ has a simple pole at $z=a_r$ and $\int_o^z\omega_{h,2}(.,q)$ is regular at $z=a_r$, we get that the integrand is regular at $z=a_r$ so that the residue is vanishing: $(F_1)=0$. A similar argument holds for $(F_2)$: $\big(x(z)-x(a_r)\big)dy(z)$ is regular at $z=a_r$ and for $h-h_1\neq 0$, $\omega_{h-h_1,2}(z,a_r)$ is regular at $z=a_r$. Thus the integrand is regular at $z=a_r$ and hence the residue is vanishing. Thus, we get from \eqref{ResidueExchange} (we isolate first the case $h_1=h$):
\bea (F)&=&\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\omega_{h,1}(q)\int_o^z\omega_{0,2}(q,.)\cr
&&+\Res_{q\to a_r} \Res_{z\to q}\big(x(z)-x(a_r)\big)dy(z)\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1} \omega_{h_1,1}(q)\int_o^z\omega_{h-h_1,2}(q,z)\cr
&=& \Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\omega_{h,1}(q)\int_o^z\omega_{0,2}(q,.)
\eea
because for $h_1\neq h$, $\omega_{h-h_1,2}(q,z)$ is regular at $z=q$.

Let us now deal with $(B)$:
\bea (B)&:=&(B_1)+(B_2) \text{ with }\cr
(B_1)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\sum_{j=1}^N \Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)] \omega_{h,2}(q,z)\cr
(B_2)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^h \omega_{h_1,1}(q)\omega_{h-h_1,2}(q,z)
\eea
For $h_1=h$, we get that the integrand in $(B_2)$ is regular at $z=p_i$ and hence: 
\beq (B_2)=\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}\omega_{h_1,1}(q)\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z) \omega_{h-h_1,2}(q,z)
\eeq
In $(B_1)$ we swap the residue using \eqref{ResidueExchange}:
\beq (B_1)=\sum_{j=1}^N \Res_{q\to p_j} d_{a_r}[\Phi(q)]\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)  \omega_{h,2}(q,z)+\sum_{j=1}^N \Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)] \Res_{z\to q,\sigma_j(q)} \Phi(z)  \omega_{h,2}(q,z)
\eeq
Since $\omega_{h,2}(q,z)$ is regular at $z=q$, the last term is vanishing. Thus, we get:
\beq (B_1)=\sum_{j=1}^N \Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)]\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)  \omega_{h,2}(q,z)\eeq
Let us now deal with $(D)$ that immediately simplifies into (perform $h_1\to h-h_1$ in one of the sum):
\beq (D)=-\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}d_{a_r}[\omega_{h-h_1,1} (z)]\omega_{h_1,1}(z)\eeq
Inserting the expression of $d_{a_r}[\omega_{h_1,1}(z)]$ for $h_1\geq 1$, we find:
\small{\bea (D)&:=&(D_1) +(D_2)\text{ with}\cr
(D_1)&:=&- \sum_{j=1}^M\Res_{z\to a_j}\sum_{i=1}^N \Res_{q\to p_i}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}d_{a_r}[\Phi_{p_i}(q)] \omega_{h-h_1,2}(z,q)\omega_{h_1,1}(z)\cr
&=&-\sum_{j=1}^N \Res_{q\to p_j}d_{a_r}[\Phi_{p_j}(q)] \sum_{i=1}^M\Res_{z\to a_i}\frac{\big(x(z)-x(a_i)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}} \omega_{h-h_1,2}(z,q)\omega_{h_1,1}(z)\cr
(D_2)&:=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}} \omega_{h_1,1}(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-h_1} \omega_{u,1}(q)\omega_{h-h_1-u,2}(q,z)
\cr
&=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{u=1}^{h-1}\sum_{h_1=1}^{h-u} \omega_{h_1,1}(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)} \omega_{u,1}(q)\omega_{h-h_1-u,2}(q,z)
\eea}
\normalsize{Let us} now write the dilaton equation for $\omega_{h,1}(z_1)$ from \autoref{TheoremDilatonEquation}:
\beq \label{DilatonReduced} (1-2h)\omega_{h,1}(q)=\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\omega_{h,2}(z,q) -\sum_{i=1}^M\Res_{z\to a_i}\frac{x(z)-x(a_i)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,2} (z,q) \eeq
Thus we get that regrouping $(B_1)+(D_1)$ we have:
\small{\bea&&(B_1)+(D_1)=\sum_{j=1}^N\Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)]\Big[\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)  \omega_{h,2}(q,z)
- \sum_{i=1}^M\Res_{z\to a_i}\frac{\big(x(z)-x(a_i)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}} \omega_{h-h_1,2}(z,q)\omega_{h_1,1}(z) \Big]\cr
&&= (1-2h)\sum_{j=1}^N\Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)]\omega_{h,1}(q) +\sum_{j=1}^N\Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)]\sum_{i=1}^M\Res_{z\to a_i}\frac{\big(x(z)-x(a_i)\big)}{dx(z)}\omega_{0,2}(z,q)\omega_{h,1}(z)\cr&&
\eea}
\normalsize{}
In the last term, we may swap the residue that are located at different points and the residue at $q=p_j$ is vanishing because all the terms in the integrand are regular at $q=p_j$. Thus, we get:
\beq (B_1)+(D_1)=(1-2h)\sum_{j=1}^N\Res_{q\to p_j} d_{a_r}[\Phi_{p_j}(q)]\omega_{h,1}(q) \eeq
Combining with $(A)$, we get
\beq \label{FirstPartTheorem} (A)+(B_1)+(D_1)= (2-2h)\sum_{j=1}^N\Res_{q\to p_j} d_{a_r}[\Phi(q)]\omega_{h,1}(q)\eeq
which is the first term of the r.h.s. of \eqref{EqToProve}.

\medskip

We are left with $(B_2)$, $(C)$, $(D_2)$, $(E)$ and $(F)$ that are given by
\bea (B_2)&=&\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}\omega_{h_1,1}(q)\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z) \omega_{h-h_1,2}(q,z)\cr
(C)&=&dx(a_r)\Res_{z\to a_r} \left(\frac{1}{2}\overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right)\cr
(D_2)&=&-\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{u=1}^{h-1}\sum_{h_1=1}^{h-u} \omega_{h_1,1}(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)} \omega_{u,1}(q)\omega_{h-h_1-u,2}(q,z)\cr
(E)&=&y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)B(z,a_r)\int_o^z\omega_{h,1} \cr
(F)&=&\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\omega_{h,1}(q)\int_o^z\omega_{0,2}(q,.)
\eea
We swap the residues in $(B_2)$ and $(D_2)$. This can be done for $(B_2)$ but for $(D_2)$, it provides an additional term. This term is non-zero except when the Bergman kernel is involved corresponding to $h-h_1-u=0$, i.e. $h_1=h-u$.  From \eqref{ResidueExchange}, we get:
\bea (D_2)&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1} \omega_{u,1}(q) \sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{h_1=1}^{h-u} \omega_{h_1,1}(z) \omega_{h-h_1-u,2}(q,z)\cr&&
-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1} \omega_{u,1}(q) \Res_{z\to q}\frac{\big(x(z)-x(a_r)\big)}{dx(z)}\sum_{h_1=1}^{h-u} \omega_{h_1,1}(z) \omega_{h-h_1-u,2}(q,z)\cr
&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1} \omega_{u,1}(q) \sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{h_1=1}^{h-u} \omega_{h_1,1}(z) \omega_{h-h_1-u,2}(q,z)\cr&&
-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1} \omega_{u,1}(q) \Res_{z\to q}\frac{\big(x(z)-x(a_r)\big)}{dx(z)} \omega_{h-u,1}(z) \omega_{0,2}(q,z)\cr
&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1} \omega_{h_1,1}(q) \sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{u=1}^{h-h_1} \omega_{u,1}(z) \omega_{h-u-h_1,2}(q,z)\cr&&
-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1} \omega_{u,1}(q) d_q\left[\frac{\big(x(q)-x(a_r)\big)}{dx(q)} \omega_{h-u,1}(q)\right] 
\eea


We now use the dilaton equation \autoref{TheoremDilatonEquation} for $\omega_{h-h_1,2}$ with $h-h_1\geq 1$:
\small{\beq \label{Dilatwhk} (1-2h+2h_1)\omega_{h-h_1,1}(q)=\sum_{i=1}^N\Res_{z\to p_i} \Phi_{p_i}(z)\omega_{h-h_1,2}(z,q) -\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h-h_1}{\underset{u=1}{\sum}}\omega_{u,1} (z)\omega_{h-h_1-u,2} (z,q)
\eeq}
\normalsize{Thus,} combining $(B_2)$ and $(D_2)$ provides
\bea \label{B2PlusD2} (B_2)+(D_2)
&=& \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}(1-2h+2h_1)\omega_{h_1,1}(q)\omega_{h-h_1,1}(q) \cr&&
-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{u=1}^{h-1} \omega_{u,1}(q) d_q\left[\frac{\big(x(q)-x(a_r)\big)}{dx(q)} \omega_{h-u,1}(q)\right] 
\eea
Let us denote 
\beq (G):=-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1} \omega_{h_1,1}(q) d_q\left[\frac{\big(x(q)-x(a_r)\big)}{dx(q)} \omega_{h-h_1,1}(q)\right] \eeq

and 
\beq (H):=\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}(1-2h_1)\omega_{h_1,1}(q)\omega_{h-h_1,1}(q)\eeq
Note that
\bea (H)&=& \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}(1-2h_1)\omega_{h_1,1}(q)\omega_{h-h_1,1}(q)\cr
&\overset{h_1\to h-h_1}{=}& \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}(1-2h+2h_1)\omega_{h-h_1,1}(q)\omega_{h_1,1}(q)
\eea
so that
\bea 2(H)&=& \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}(1-2h_1+1-2h+2h_1)\omega_{h_1,1}(q)\omega_{h-h_1,1}(q)\cr
&=&(2-2h)\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}\omega_{h_1,1}(q)\omega_{h-h_1,1}(q)
\eea
Thus:
\beq (H)=\frac{1}{2}(2-2h)\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}\omega_{h_1,1}(q)\omega_{h-h_1,1}(q)\eeq



so that we have that
\beq (B_2)+(D_2) -(G)= \frac{1}{2}(2-2h)\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1}\omega_{h_1,1}(q)\omega_{h-h_1,1}(q) \eeq
Hence, $(A)+(B)+(D)-(G)$ provides the first two terms of \eqref{EqToProve}. Let us now prove that we can obtain the second and third lines of the r.h.s. of \eqref{EqToProve} from 
\beq (N):=(C)+(E)+(F)+(G)\eeq

We shall first decompose:
\bea (C)&:=&(C_1)+(C_2)\text{ with}\cr
(C_1)&:=&\frac{1}{2}dx(a_r)\Res_{z\to a_r} \overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z) }{dx(z)}\cr
(C_2)&:=& -dx(a_r)\Res_{z\to a_r} dy(z)\int_o^z \omega_{h,1}
\eea

Let us now focus on $(G)$. We have
\small{\bea \label{weirdId}0&=&dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r}d_q\left[ \frac{\omega_{h_1,1}(q)}{dx(q)} \big(x(q)-x(a_r)\big)\frac{\omega_{h-h_1,1}(q)}{dx(q)} \right]\cr
&=&dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r}\frac{\omega_{h_1,1}(q) \omega_{h-h_1,1}(q)}{dx(q)} + dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r} \frac{\omega_{h_1,1}(q)}{dx(q)} \big(x(q)-x(a_r)\big)d_q\left[\frac{\omega_{h-h_1,1}(q)}{dx(q)} \right] \cr
&&+dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r}d_q\left[ \frac{\omega_{h_1,1}(q)}{dx(q)}\right] \big(x(q)-x(a_r)\big)\frac{\omega_{h-h_1,1}(q)}{dx(q)}\cr
&=& dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r}\frac{\omega_{h_1,1}(q) \omega_{h-h_1,1}(q)}{dx(q)} + 2dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r} \frac{\omega_{h_1,1}(q)}{dx(q)} \big(x(q)-x(a_r)\big)d_q\left[\frac{\omega_{h-h_1,1}(q)}{dx(q)} \right]\cr&&
\eea}
\normalsize{where} we have changed $h_1\to h-h_1$ in the third term. A direct computation provides: 
\small{\bea (G)&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\sum_{h_1=1}^{h-1} \omega_{h_1,1}(q) d_q\left[\frac{\big(x(q)-x(a_r)\big)}{dx(q)} \omega_{h-h_1,1}(q)\right]\cr
&=& -\sum_{h_1=1}^{h-1} \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) \omega_{h-h_1,1}(q)- \Res_{q\to a_r}dx(a_r)\sum_{h_1=1}^{h-1} \frac{\omega_{h_1,1}(q)}{dx(q)} \big(x(q)-x(a_r)\big) d_q\left[\frac{\omega_{h-h_1,1}(q)}{dx(q)}\right]\cr&&
\eea}
\normalsize{Inserting} \eqref{weirdId} into the last identity, we get
\beq (G)=-\sum_{h_1=1}^{h-1} \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) \omega_{h-h_1,1}(q)+\frac{1}{2}dx(a_r)\sum_{h_1=1}^{h-1}\Res_{q\to a_r}\frac{\omega_{h_1,1}(q) \omega_{h-h_1,1}(q)}{dx(q)}
\eeq
so that
\beq\label{C1PlusG} (C_1)+(G)=0
\eeq
and $(N)=(C_2)+(E)+(F)$. Let us now observe that
\beq\label{C2PlusE} (C_2)+(E)=-dx(a_r)\Res_{z\to a_r}dy(z)\int_o^z\omega_{h,1}+y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)B(z,a_r)\int_o^z\omega_{h,1}\eeq


Finally, let us turn to
\beq (F)=\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\Res_{q\to a_r} \frac{dx(a_r)}{dx(q)}\omega_{h,1}(q)\int_o^z\omega_{0,2}(q,.)\eeq
We exchange the residues using \eqref{ResidueExchange}:
\bea (F)&=&\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h,1}(q) \Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z) \int_o^z\omega_{0,2}(q,.)\cr
&&+ \Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h,1}(q) \Res_{z\to q}\big(x(z)-x(a_r)\big)dy(z) \int_o^z\omega_{0,2}(q,.)
\eea
The first residue is vanishing because the integrand in $z$ is holomorphic at $z=a_r$. Thus, we get:
\bea \label{eqF} (F)&=&\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h,1}(q) \Res_{z\to q}\big(x(z)-x(a_r)\big)dy(z) \int_o^z\omega_{0,2}(q,.)\cr
&=&-\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h,1}(q) dy(q) (x(q)-x(a_r))
\eea
Thus, combining \eqref{C2PlusE} and \eqref{eqF} we get that $(C_2)+(E)+(F)$ provides the second and third lines of \eqref{EqToProve} ending the proof for this formulation. 

To obtain the second formulation, we shall us the following lemma.

\begin{lemma}
    We have the following relation 
    \begin{align*}
        &-\frac{1}{2-2h}\Res_{z\to a_r}dx(a_r)dy(z)\int_o^z\omega_{h,1}+\frac{1}{2-2h}y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)B(z,a_r)\int_o^z\omega_{h,1}\\
&-\frac{1}{2-2h}\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h,1}(q) dy(q) (x(q)-x(a_r))\\
=&-\Res_{z\to a_r} dx(a_r) dy(z) \int_o^z\omega_{h,1}-\sum_{j=1}^M\Res_{z\to a_j} d_{a_r}[y(z)] dx(z)\int_o^z\omega_{h,1}.
    \end{align*}
    \begin{proof}
        The first and the third term together with the second at $j=r$ can be written as (neglecting the $1/(2-2h)$ factor and after integration by parts)
        \begin{align*}
            &dx(a_r)\Res_{z\to a_r}\bigg(\int_o^z\omega_{h,1}\bigg) \bigg(d_z\bigg[\frac{dy(z)(x(z)-x(a_r))}{dx(z)}\bigg]- dy(z)+\frac{(x(z)-x(a_r)))d_{a_r}[dy(z)]}{dx(a_r)}\bigg)\\
            =&dx(a_r)\Res_{z\to a_r}\bigg(\int_o^z\omega_{h,1}\bigg) (x(z)-x(a_r))\bigg(d_z\bigg[\frac{dy(z)}{dx(z)}\bigg]+\frac{d_{a_r}[dy(z)]}{dx(a_r)}\bigg).        
        \end{align*}
        Note that $\bigg(d_z\bigg[\frac{dy(z)}{dx(z)}\bigg]+\frac{d_{a_r}[dy(z)]}{dx(a_r)}\bigg)$ is regular at $z=a_r$. Thus, we can integrate by parts again to get $\omega_{h,1}$ (without an integral). Since just the singular part of $\omega_{h,1}$ contributes, we insert the definition of this part from LogTR. Changing the order of the residues gives on the one hand a vanishing contribution and on the other hand  a contribution if $q\to z$. This is easily evaluated and we remain with the following:
        \begin{align*}
            =&-dx(a_r)\Res_{q\to a_r}[\hbar^{2h}]\bigg(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar )}\frac{\partial^{2h}}{\partial x(q)^{2h}}\log(q-a_r)\bigg)dx(q) \int_o^q(x(t)-x(a_r))\bigg(d_t\bigg[\frac{dy(t)}{dx(t)}\bigg]+\frac{d_{a_r}[dy(t)]}{dx(a_r)}\bigg)\\
            =&dx(a_r)\Res_{q\to a_r}[\hbar^{2h}]\bigg(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\log(q-a_r)\bigg) (x(q)-x(a_r))\bigg(d_q\bigg[\frac{dy(q)}{dx(q)}\bigg]+\frac{d_{a_r}[dy(q)]}{dx(a_r)}\bigg)\\
            =&dx(a_r)(2-2h)\Res_{q\to a_r}[\hbar^{2h}]\bigg(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar)}\frac{\partial^{2h-2}}{\partial x(q)^{2h-2}}\log(q-a_r)\bigg)\bigg(d_q\bigg[\frac{dy(q)}{dx(q)}\bigg]+\frac{d_{a_r}[dy(q)]}{dx(a_r)}\bigg)\\
            =&-dx(a_r)(2-2h)\Res_{q\to a_r}\bigg(\int_o^q\omega_{h,1}\bigg)\bigg(dy(q)+dx(q)\frac{d_{a_r}[y(q)]}{dx(a_r)}\bigg).
        \end{align*}
        In the second last line we used a version of \autoref{LemmaIntW02Wg1} and in the last line integration by parts together with the explicit expression of the LogTR-vital singular term of $\omega_{h,1}$ at  $a_r$. This produces the terms of the lemma for the residues at $a_r$. For the second term with residue at $a_{j}$ with $j\neq r$, the same computation and arguments hold. Bringing everything together, the lemma is proved. 
    \end{proof}
\end{lemma}

\section{Variation of $\omega_{1,0}$ with respect to LogTR-vital singularities}\label{AppendixVarF1LogTR}
Let us study the variations of $F_1=\omega_{1,0}$ with respect to LogTR-vital singularities. Let us recall that $\omega_{1,0}$ is defined in \autoref{DefFreeEnergies} and more precisely by the specific formula:
\beq \omega_{1,0}:= -\frac{1}{2}\ln \tau -\frac{1}{24}\ln\left(\prod_{i=1}^N y'(p_i)\right) -\frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)\bigg\vert_{z=a_s}\eeq
where  $y'(p_i)=\frac{dy(p_i)}{dz_i(p_i)}$ with $z_i(q)=\sqrt{x(q)-x(p_i)}$. 

The proof consists of two steps, first computing the variation of \eqref{F1formula} wrt $a_r$, and second comparing this with the RHS of the variational formula \eqref{EqToProve2} for $(h,n)=(1,0)$.



1.) Rauch variational formula (See \cite[Section $5$]{EO07}) implies that for variations at fixed $x$, we have:
\beq \label{Defomega10}\delta_{\Omega}[\tau]=2i\pi \sum_{i=1}^N \Res_{z\to p_i}\frac{\Omega(z)d\mathbf{u}(z)d\mathbf{u}(z)^t}{dx(z)dy(z)}\eeq 
\sloppy{Therefore, for a LogTR-vital singularity $a_r\in \mathcal{S}_y$, we have from $\Omega_{a_r}(z):=d_{a_r}[ydx(z)]=y_{a_r} \frac{\partial_{a_r} E(z,a_r)}{E(z,a_r)} dx(z)$ that $d_{a_r}[\tau]=0$. Indeed, in that case the integrand simplifies into $y_{a_r}\frac{\partial_{a_r} E(z,a_r)}{E(z,a_r)}\frac{d\mathbf{u}(z)d\mathbf{u}(z)^t}{dy(z)}$ which is regular at the ramification points so that the residue is vanishing.}  From \autoref{TheoremGlobalDecompositionydx} and the fact that $a_r$ is a LogTR-vital singularity (i.e. $\td{y}dx$ is regular at $a_r$), we get that 
\beq d_{a_r}[\td{y}(z)]=0\eeq
However, for each $y(z)$ there is a term locally of the form $y_{a_r}\ln \frac{E(z,a_r)}{E(z,o)}=y_{a_r}\log(z-a_r) +O(1)$. Combining with $\log(x(z)-x(a_s))$ yields in the limit a term of the form $-\log(x'(a_r))$.
Thus the variations of the last term in \eqref{Defomega10} give two contributions, either acting on $a_r$ in $y(z)$ or on the argument $z=a_r$. We find
\beq d_{a_r}\left[ \frac{1}{24}\sum_{s=1}^M\bigg(\frac{y(z)}{y_{a_s} }-\log(x(z)-x(a_s))\bigg)\bigg\vert_{z=a_s}\right]
=\frac{1}{24} \sum_{\substack{s=1\\ s\neq r}}^M\frac{y_{a_r}}{y_{a_s}}%\frac{1}{a_r-a_s}
\frac{\partial_{a_r} E(a_s,a_r)}{E(a_s,a_r)}
+\frac{1}{24}\left(\frac{dy_r(a_r)}{y_{a_r}}-\frac{x''(a_r)}{x'(a_r)}\right)\eeq
where $y_r(z):=y(z)-y_{a_r}\ln \frac{E(z,a_r)}{E(z,o)} $, is the regular part of $y(z)$ at $z=a_r$.

Finally since $d_{a_r}[y'(z)]=y_{a_r}B(z,a_r)$ and using the fact that the ramification points (defined by $dx(p_i)=0$) are also invariant under deformations at fixed $x$, we get that
\beq d_{a_r}\left[-\frac{1}{24}\ln\left(\prod_{i=1}^N y'(p_i)\right)\right]=-\frac{1}{24}\sum_{i=1}^N\frac{d_{a_r}[y'(p_i)]}{y'(p_i)}=-\frac{1}{24}\sum_{i=1}^N\frac{d_{a_r}[dy(p_i)]}{dy(p_i)}=-\frac{1}{24}\sum_{i=1}^N y_{a_r}\frac{B(p_i,a_r)}{dy(p_i)}\eeq
Thus, we find:
\beq \label{VariationOmega10ar} d_{a_r}[\omega_{1,0}]= -\frac{1}{24}\sum_{i=1}^N y_{a_r}\frac{B(p_i,a_r)}{dy(p_i)}-\frac{1}{24} \sum_{\substack{s=1\\ s\neq r}}^M\frac{y_{a_r}}{y_{a_s}}%\frac{da_r}{a_r-a_s}
%dS_{o,a_s}(a_r)
\frac{\partial_{a_r} E(a_s,a_r)}{E(a_s,a_r)}
-\frac{1}{24}\left(\frac{dy_r(a_r)}{y_{a_r}}-\frac{x''(a_r)}{x'(a_r)}da_r\right)\eeq



2.) Let us now compare with the r.h.s. of \eqref{EqToProve2}, we have:
\bea \label{RHSF1Proof}&&\Res_{z\to \{p_i\}\cup \{a_j\}} d_{a_r}[\Phi(z)]\omega_{1,1}(z) +\Res_{z\to a_r}dx(a_r)y(z)\omega_{1,1} (z).
\eea
%We have $d_{a_r}[\Phi(z)]=\int_{t=o}^{t=z}y_{a_r} dx(t) \,da_r dS_{o,t}(a_s)+ O(1)%\frac{y_{a_r} dx(t) \,da_r }{a_r-t}
%$ and 
For $\omega_{1,1}(z)$ near $a_s$, we have 
from \autoref{DefLogTR}:
\bea \omega_{1,1}(z) &=& -\frac{1}{24y_{a_s}}\Res_{q\to a_s} dS_{a_s,q}(z)dx(q)\left( \frac{1}{x'(q)^2(q-a_s)^2} +\frac{x''(q)}{x'(q)^3(q-a_s)}\right) +O(1)\cr
&=& -\frac{dz}{24y_{a_s}x'(a_s)(z-a_s)^2} +O(1)
\eea 

In particular, we get that for the residue at $t\to a_s\neq a_r$
\bea 
\Res_{z\to a_s}d_{a_r}[\Phi(z)]\omega_{1,1}(z)
%&=&\Res_{z\to a_s} \int_{t=o}^{t=z}y_{a_r} dx(t) \,da_r dS_{o,t}(a_s)\frac{dz}{24y_{a_s}x'(a_s)(z-a_s)^2} \cr
%&=&-\Res_{z\to a_s }d_{a_r}[ydx(z)] \int_{t=o}^{t=z}\omega_{1,1}(t) %\frac{dz}{24y_{a_s}x'(a_s)(z-a_s)}
%\cr
%&=&-\Res_{z\to a_s }y_{a_r} x'(z) %dS_{o,z}(a_r)
%\frac{\partial_{a_r} E(z,a_r)}{E(z,a_r)}
%\frac{dz}{24y_{a_s}x'(a_s)(z-a_s)}\cr
&=&-\frac{1}{24}\frac{y_{a_r} }{y_{a_s}} \frac{\partial_{a_r} E(a_s,a_r)}{E(a_s,a_r)}%dS_{o,a_s}(a_r) (a_s-a_r)}
\eea


For the residue at a ramification point $p_i$ we compute
\bea
\Res_{z\to p_i}d_{a_r}[\Phi(z)]\omega_{1,1}(z)
&=&\Res_{z\to p_i}d_{a_r}[\Phi(z)]\Res_{q\to p_i}\frac{1}{2}\frac{\int_{q}^{\sigma_i(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}\omega_{0,2}(q,\sigma_i(q))\cr
&=& -\Res_{q\to p_i}\Res_{z\to q,\sigma_i(q)}d_{a_r}[\Phi(z)]\frac{1}{2}\frac{\int_{q}^{\sigma_i(q)} \omega_{0,2}(z,.)}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}\omega_{0,2}(q,\sigma_i(q))\cr
&=& \Res_{q\to p_i}\frac{1}{2}\frac{d_{a_r}[\Phi(q)]-d_{a_r}[\Phi(\sigma_i(q))]}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}\omega_{0,2}(q,\sigma_i(q)).
\eea
Note that $\frac{\omega_{0,2}(q,\sigma_i(q)}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}$ is residue-free at $q\to p_i$. This means it can be integrated locally such that we can use integration by parts. Then, $d_qd_{a_r}[\Phi(q)]$ vanishes at $q\to p_i$, which means finally, that we just have to consider the third and fourth order term of $\frac{\omega_{0,2}(q,\sigma_i(q)}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}$ in the Laurent expansion at $q\to p_i$, which are of the form
\beq
\frac{\omega_{0,2}(q,\sigma_i(q))}{\omega_{0,1}(\sigma_i(q))-\omega_{0,1}(q)}=-\frac{dq}{8 (q-p_i)^4 x''(p_i) y'(p_i)}+
\frac{x'''(p_i)dq}{24 (q-p_i)^3 x''(q)y'(p_i)}+O((q-p_i)^{-2}dq).
\eeq

Inserting this, it is an easy computation to show that 
\bea
&&\Res_{z\to p_i}d_{a_r}[\Phi(z)]\omega_{1,1}(z)=-\frac{1}{24}\frac{B(p_i,a_r)}{y_{a_r}dy(p_i)}.
\eea


Lastly, we have to compute the residue at $z\to a_r$. First, we observe that $d_{a_r}[\Phi(z)]+dx(a_r)y(z)$ is regular near $z\to a_r$ (it is easier to see after taking its derivative, which does not have a pole $z\to a_r$ concluding that its local integral is regular). Thus, the only contribution for a possible pole of the integrand comes from $\omega_{1,1}(z)$. Integrating by parts again, we find
\beq\Res_{z\to a_r} (d_{a_r}[\Phi(z)]+dx(a_r)y(z))\omega_{1,1}(z) 
= -\Res_{z\to a_r} \left(y_{a_r}\frac{dx(z)da_r}{a_r-z}+dx(a_r)dy(z)\right)\frac{dz}{24y_{a_r}x'(a_r)(z-a_r)}.
\eeq

For the second term in the brackets, we split $dy(z)=dy_r(z)+y_{a_r}dS_{o,a_r}(z)$%\frac{dz}{z-a_r}
. The residue of the regular part $dy_r(z)$ gives the expected result $-\frac{1}{24}\frac{dy_r(a_r)}{y_{a_r}}$. The other term has the residue
\beq-\Res_{z\to a_r} \left(y_{a_r}\frac{dx(z)da_r}{a_r-z}+dx(a_r)y_{a_r}\frac{dz}{z-a_r}\right)\frac{1}{24y_{a_r}x'(a_r)(z-a_r)}
%&=& -\Res_{z\to a_r} \frac{dx(z)da_r}{24x'(a_r)(z-a_r)^2}
=da_r\frac{x''(a_r)}{24 x'(a_r)}.
\eeq
This ends the proof of the variational formula for the free energy $F_1$ in the presence of LogTR-vital singularities. 











\newpage
%\addcontentsline{toc}{section}{References}
\bibliographystyle{plain}
\bibliography{Biblio}
\end{document}















































\subsection{Global decomposition of $ydx$}
The next step is to rewrite $ydx$ using one-forms that are globally defined on $\Sigma$ and that reproduces the singular behavior of $ydx$ at one of its singularities.

\begin{definition}[Definition of $B_{\alpha,k}$ and $B_{\alpha,0,o'}$]\label{DefBalphak}Let $\alpha\in \mathcal{P}$ be a singular point of $ydx$ with local behavior given by \autoref{PropLocalCoord}. We define the following one-forms:
\bea \forall\,k\in \llbracket 1,R_\alpha\rrbracket\,:\, B_{\alpha,k}(q)&=&\Res_{s\to \alpha} B(q,s)z_\alpha(s)^{-k}\cr
B_{\alpha,0;o'}(q)&=&\int_{o'}^\alpha B(.,q):=dS_{\alpha,o'}(q)
\eea
where $o'\in \Sigma$ is a fixed generic basepoint and the path integral is a contractible path connecting $o' \to \alpha$ avoiding all special points or special contour.
\end{definition}

\autoref{DefBalphak} makes sense since the local coordinates are defined in a punctured neighborhood of $\alpha$ so that the residue is computable. By definition, the one-forms have the following properties:
\begin{itemize}
    \item For $k\in \llbracket 1,R_\alpha\rrbracket$, $B_{\alpha,k}$ is a meromorphic one-form on $\Sigma$ with only one pole at $\alpha$ (with vanishing residue) and that locally behaves like
    \beq B_{\alpha,k}(q)\overset{q\to \alpha}{=} -kz_\alpha(q)^{-k-1}dz_\alpha(q) + O(1)\eeq
    \item $B_{\alpha,0;o'}$ is a meromorphic one-form on $\Sigma$ with only two simple poles at $\alpha$ and $o'$ with opposite residues. Locally around $\alpha$ we have:
    \beq B_{\alpha,0;o'}(q)\overset{q\to \alpha}{=}\frac{d z_\alpha(q)}{z_\alpha(q)}+O(1)\eeq
\end{itemize}

We can regroup these differentials together to obtain the meromorphic singular part of $ydx$ at $\alpha$:
\beq M(q):=\sum_{\alpha\in \mathcal{P}}\left(\sum_{k=2}^{R_\alpha} t_{\alpha,k} B_{\alpha,k}(q)+ t_{\alpha,0}B_{\alpha,0;o'}(q)\right)\eeq
is a meromorphic one-form on $\Sigma$ with only poles at $\alpha\in \mathcal{P}$ and at $o'$ such that the local behavior of $M(q)$ at each $\alpha\in \mathcal{P}$ matches with the rational singular behavior of $ydx$ at $\alpha$.

\medskip

The main novelty is to insert the logarithmic terms in this framework when $\alpha\in \mathcal{S}_y$.

\begin{definition}[Logarithmic differentials]\label{DefLogDifferentials}For $\alpha\in \mathcal{S}_y$, we define the differential
\beq dS_{\alpha,o}(q)=\int_o^{\alpha} B(q,.)\eeq
it is holomorphic on $\Sigma$ except two simple poles at $q=\alpha$ with residue $1$ and $q=o$ with residue $-1$. Then we define
\beq S_{\alpha,o;o'}(p):=\int_{o'}^p dS_{\alpha,o}(q)\eeq
$S_{\alpha,o;o'}$ is a function on $\Sigma$ with a logarithmic cut from $o$ to $\alpha$ and no other singularities. 
\end{definition}

Let us observe that if we define $y_\alpha=\Res_{q\to\alpha} dy$ for any $\alpha\in \mathcal{S}_y$, we have:
\beq dy- \sum_{\alpha\in \mathcal{S}_y}  y_\alpha dS_{\alpha,o}(q) \text{  is residueless}\eeq
    

\begin{definition}[One-form for $\alpha\notin \mathcal{S}_y$]\label{DefOneFormSmero}Let $\alpha\in \mathcal{P}\setminus\mathcal{S}_y$. From \autoref{PropLocalCoord}, the local expansion of $ydx$ is 
\beq ydx(q)=dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eeq
with $du_\alpha$ holomorphic in a punctured neighborhood of $\alpha$. The local potential is $V_\alpha(q)=\underset{k=1}{\overset{R_\alpha}{\sum}} t_{\alpha,k}z_\alpha(q)^{-k}$. We define the one form $B_{\alpha,o'}(q)$ on $\Sigma$ by
\beq B_{\alpha,o'}(q):=\sum_{k=1}^{R_\alpha} t_{\alpha,k} B_{\alpha,k}(q) + t_{\alpha,0}\int_{o'}^\alpha B(.,q)\eeq
where $o'$ is a fixed basepoint and
\beq \forall \, k\in \llbracket 1,R_\alpha\rrbracket\,:\, B_{\alpha,k}(q):=-\Res_{s\to \alpha} B(q,s) z_\alpha(s)^{-k}\eeq
\end{definition}




\subsubsection{One forms for $\alpha\notin \mathcal{S}_y$}
Let us consider $\alpha\notin \mathcal{S}_y$, then the local decomposition of $ydx$ at $\alpha$ only involves irregular times and monodromies and $ydx$ is locally meromorphic in a punctured neighborhood of $\alpha$. Following \cite{EO07}, we shall define the following one-form.

\begin{definition}[One-form for $\alpha\notin \mathcal{S}_y$]\label{DefOneFormSmero}Let $\alpha\in \mathcal{P}\setminus\mathcal{S}_y$. From \autoref{PropLocalCoord}, the local expansion of $ydx$ is 
\beq ydx(q)=dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eeq
with $du_\alpha$ holomorphic in a punctured neighborhood of $\alpha$. The local potential is $V_\alpha(q)=\underset{k=1}{\overset{R_\alpha}{\sum}} t_{\alpha,k}z_\alpha(q)^{-k}$. We define the one form $B_{\alpha,o'}(q)$ on $\Sigma$ by
\beq B_{\alpha,o'}(q):=\sum_{k=1}^{R_\alpha} t_{\alpha,k} B_{\alpha,k}(q) + t_{\alpha,0}\int_{o'}^\alpha B(.,q)\eeq
where $o'$ is a fixed basepoint and
\beq \forall \, k\in \llbracket 1,R_\alpha\rrbracket\,:\, B_{\alpha,k}(q):=-\Res_{s\to \alpha} B(q,s) z_\alpha(s)^{-k}\eeq
\end{definition}

The main interest of this definition is that $B_{\alpha,o'}$ is a meromorphic one form on $\Sigma$ with only poles at $\alpha$ and a simple pole at $o'$ such that
\beq \forall\, \alpha\in \mathcal{P}\setminus \mathcal{S}_y\,:\, ydx(q)-B_{\alpha,o'}(q) \text{ is holomorphic around } \alpha\eeq

\subsubsection{One forms for $\alpha\in \mathcal{S}_y$}
Let us now adapt the definition when $\alpha\in \mathcal{S}_y$, i.e. when $ydx$ has a logarithmic singularity at $\alpha$. 

\begin{definition}[One-form for $\alpha\in \mathcal{S}_y$]\label{DefOneFormSlog}Let $\alpha\in \mathcal{S}_y$. From \autoref{PropLocalCoord}, the local expansion of $ydx$ is 
\beq ydx(q)=dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} +s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q)\eeq
where the local potential is
\beq V_\alpha(q)=\sum_{k=1}^{R_\alpha} t_{\alpha,k}z_\alpha(q)^{-k}\eeq
and where $du_\alpha(q)$ stands for a one-form which is holomorphic in a neighborhood of $\mathcal{C}_{o\to \alpha}$. 
We shall define
\textcolor{red}{\bea B_{\alpha,o'}(q)&:=&-\oint_{s\in\mathcal{C}_{\alpha}} \left(\int_{o'}^s B(q,.)\right)ydx(s)\cr
&:=&-\frac{1}{2i\pi}\underset{s \in \mathcal{C}_{o\to q_\alpha}}{\text{Disc}} \left(\int_{o'}^s B(q,.)\right)ydx(s) -\oint_{s\in\mathcal{C}_{\alpha, q_\alpha}} \left(\int_{o'}^s B(q,.)\right)ydx(s)\cr
&=& -\int_o^{q_\alpha} \left(\int_{o'}^s B(q,.)\right)ds -s_\alpha \oint_{s\in\mathcal{C}_{\alpha, q_\alpha}} \left(\int_{o'}^s B(q,.)\right)z_\alpha(s)^{-d_\alpha-1}\ln \frac{z_\alpha(s)-1}{z_\alpha(s)} dz_\alpha(s) \cr
&=& -\int_o^{q_\alpha} \left(\int_{o'}^s B(q,.)\right)ds +s_\alpha \oint_{s\in\mathcal{C}_{\alpha, q_\alpha}} \left(\int_{o'}^s B(q,.)\right)z_\alpha(s)^{-d_\alpha-1}\ln z_\alpha(s) dz_\alpha(s) \cr
\eea}
\textcolor{blue}{The meromorphic part should be dealt with exactly as in the other case:
\beq B_{\alpha,o'}(q):=\sum_{k=1}^{R_\alpha} t_{\alpha,k} B_{\alpha,k}(q) + t_{\alpha,0}\int_{o'}^\alpha B(.,q)\eeq
where $o'$ is a fixed basepoint and
\beq \forall \, k\in \llbracket 1,R_\alpha\rrbracket\,:\, B_{\alpha,k}(q):=-\Res_{s\to \alpha} B(q,s) z_\alpha(s)^{-k}\eeq
The last quantity is well-defined I think because $z_\alpha$ is well-defined in a neighborhood of $\alpha$? This is true if $x$ is regular for example. It will give a meromorphic form with only poles at $q=\alpha$ with behavior $z_\alpha^k$. Only the new coefficient remains to be written using the Bergman kernel.
}
\end{definition}

\textcolor{red}{\begin{remark}Note that if we change the basepoint $o'$ in the previous definition, it simply adds a term $\left(\int_{o'}^{o''}B(q,.)\right)\oint_{s\in\mathcal{C}_{\alpha}} z_\alpha(d)^{-d_\alpha-1}\ln \frac{z_\alpha(d)-1}{z_\alpha(d)} dz_\alpha(d)=0$ so that the definition of $B_\alpha(q)$ does not depend on the choice of basepoint $o'$.
\end{remark}}

\textcolor{red}{What are the properties of $B_{\alpha,o'}(q)$?}



\subsubsection{Decomposition of $ydx$ using the Bergmann kernel}
Let us now rewrite the singular part of $ydx$ at each pole using the Bergmann kernel. We define
\bea B_{\alpha}(p)&:=& \oint_{q\in\mathcal{C}_{\alpha}} B(p,q)\left( \int_{o'}^qz_\alpha(s)^{-d_\alpha-1}\ln \frac{z_\alpha(s)-1}{z_\alpha(s)} dz_\alpha(s)\right)\cr
&=&-\oint_{q\in\mathcal{C}_{\alpha}} \left(\int_{o'}^qB(p,.)\right)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)\eea
Using the notation of \cite{EO07}:
\beq dS_{q_1,q_2}(p):=\int_{q_1}^{q_2} B(p,.)\eeq
it is equivalent to
\beq B_{\alpha}(p)=-\oint_{q\in\mathcal{C}_{\alpha}} dS_{o',q}(p)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)\eeq
If we change the basepoint $o'$, it adds a term $\left(\int_{o'}^{o''}B(p,.)\right)\oint_{q\in\mathcal{C}_{\alpha}} z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)=0$ so that the definition of $B_\alpha(p)$ does not depend on the choice of basepoint $o'$.

Let us now analyze the properties of the one form $B_\alpha(p)$. First it is normalized on the $\mathcal{A}$-cycles similarly to the Bergmann kernel (because the contour $\mathcal{C}_\alpha$ is disjoint from the holonomy cycles). Then, it is holomorphic except when $p$ belongs to $\mathcal{C}_\alpha$. Indeed, $dS_{o',q}(p)$ has a simple pole when $q$ is closed to $p$: $dS_{o',q}(p)=\frac{dp dq}{p-q} +O(1)$. This provides a jump contribution which is given by $z_\alpha(p)^{-d_\alpha-1}\ln \frac{z_\alpha(p)-1}{z_\alpha(p)} dz_\alpha(p)$. In the end, we have

\begin{proposition}[Log-forms]\label{PropLogForms}Let $\alpha$ be a singular point of $ydx$. The one-form
\beq B_\alpha(p):=-\oint_{q\in\mathcal{C}_{\alpha}} \left(\int_{o'}^qB(p,.)\right)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q) \eeq
has the following properties:
\begin{itemize}
    \item It is holomorphic except on the contour $\mathcal{C}_\alpha$.
    \item On the contour $\mathcal{C}_\alpha$ it has a jump given by
    $z_\alpha(p)^{-d_\alpha-1}\ln \frac{z_\alpha(p)-1}{z_\alpha(p)} dz_\alpha(p)$ for all $p\in \mathcal{C}_\alpha$.
    \item It is normalized on the $\mathcal{A}$-cycles:
    \beq \oint_{\mathcal{A}_i} B_\alpha(p) =0 \,\,,\,\, \forall\,i\in \llbracket 1,g \rrbracket.\eeq
\end{itemize}
\end{proposition}

The one-form $B_\alpha$ encodes the logarithmic singularities at $\alpha$ of $ydx$. Using \autoref{PropLocalCoord} we get the following theorem.

\begin{theorem}[Decomposition of $ydx$]\label{TheoydxDecomposition}The one-form $ydx$ can be rewritten as
\beq ydx(p)= \sum_{\alpha} s_\alpha B_\alpha(p)+ \sum_{\alpha,k\geq 1} t_{\alpha,k} B_{\alpha,k}(p) +\sum_{\alpha} t_{\alpha,0}\int_{o'}^\alpha B(.,p) +\sum_{i=1}^g \epsilon_i du_i(p)  \eeq
where 
\beq \forall \, k\geq 1\,:\, B_{\alpha,k}(p):=-\Res_{q\to \alpha} B(p,q) z_\alpha(q)^{-k}\eeq
\end{theorem}
\begin{proof}The one-form
\beq ydx(p)- \left(\sum_{\alpha} s_\alpha B_\alpha(p)+ \sum_{\alpha,k\geq 1} t_{\alpha,k} B_{\alpha,k}(p) +\sum_{\alpha} t_{\alpha,0}\int_{o'}^\alpha B(.,p)\right)\eeq
 is regular at each pole $\alpha$ and has no jumps across each of the log-cuts. Therefore it is holomorphic on $\Sigma$. Moreover, its integral on $\mathcal{A}_i$ is $\epsilon_i$ and thus it is necessarily $\underset{i=1}{\overset{g}{\sum}} \epsilon_i du_i$.   
\end{proof}





\subsection{Coefficients of the local decomposition as integrals}
\textcolor{red}{This subsection may not be useful anymore}
\subsubsection{Logarithmic integrals}
Let us first starts with a technical lemma:
\begin{lemma}[Logarithmic integrals]\label{LemmaLogIntegrals}Let $0<r<1$ and let $\mathcal{C}_r$ be the counterclockwise circle of radius $r$ centered at $0$ parametrized by $z_0=re^{i\theta}$ with $\theta\in [0,2\pi]$. Let $\td \ln\, z_0$ be the logarithm with a branch taken on the positive real axis and such that $\td{\ln}(t+i\epsilon)=\td{\ln}(t-i\epsilon)+2i\pi$ for any $t\in \mathbb{R}_+^*$. In other words: $\td{\ln}(z_0)=-\ln(-z_0)$ where $\ln$ stands for the usual logarithm with its usual branch on the negative real axis. We have for any $z\in \mathbb{Z}$:
\beq \frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\td{\ln}\, z_0\, dz_0=\left\{
    \begin{array}{ll}
        -\frac{r^{k+1}}{k+1} & \mbox{if } k\neq -1 \\
        -\ln r & \mbox{if } k=-1
    \end{array}
\right.
\eeq    
\end{lemma}

\begin{proof}The proof is done in \autoref{AppendixTechnicalIntegrals}.
\end{proof}


\subsubsection{Definition of the contour $\mathcal{C}_{\alpha}$}
If $\alpha\notin \mathcal{S}_y$, we define $\mathcal{C}_\alpha$ as a small loop around $\alpha$:
\beq \alpha\notin \mathcal{S}_y \,\,\Rightarrow\,\, \mathcal{C}_\alpha:= \oint_{\alpha}= 2i\pi \Res_{\alpha}\eeq

Let us now define $\mathcal{C}_{\alpha}$ for $\alpha\in \mathcal{S}_y$. In that case, $y$ has a logarithmic cut $\mathcal{C}_{o\to \alpha}$ connecting $o$ to $\alpha$ and thus residues around $\alpha$ of $ydx$ cannot be defined. When $\alpha\in \mathcal{S}_y$, we define the contour $\mathcal{C}_\alpha$ as the contour starting from $o$ above the logarithmic cut $\mathcal{C}_{o\to \alpha}$ oriented from $o$ to $\alpha$ and then circling around $\alpha$ counterclockwise and ending at $o$ below the logarithmic cut $\mathcal{C}_{o\to \alpha}$. This definition implicitly assume that the contour $\mathcal{C}_\alpha$ only circles the log-cut connecting $o$ to $\alpha$ and $\alpha$ without circling any other singular point or crossing holonomy cycles. Moreover, $\mathcal{C}_\alpha$ is taken in a immediate neighborhood of $\mathcal{C}_{o\to \alpha}$ and $\alpha$ where the local coordinate $z_\alpha$ is well-defined.

\medskip
When $\alpha\in \mathcal{S}_y$, the contour $\mathcal{C}_{\alpha}$ can be split into two parts:
\begin{itemize}
    \item Let $q_\alpha$ be a point on $\mathcal{C}_{o\to \alpha}$ such that $z_\alpha(q_\alpha):=r_\alpha$ satisfies $|r_\alpha|<1$ in the $z_\alpha$-plane. Then, the first part of the contour corresponds to the discontinuity across $\mathcal{C}_{o\to \alpha}$ from $o$ to $q_\alpha$.
    \item The second part corresponds to a circle integral starting at $q_\alpha$, circling once around $\alpha$ counterclockwise and ending at $q_\alpha$. 
\end{itemize}

\textcolor{blue}{Insert a picture}

\subsubsection{Local coefficients as integrals over $\mathcal{C}_\alpha$}
We may use \autoref{LemmaLogIntegrals} to obtain the coefficients of the singular part of $ydx$ at $\alpha$. Indeed, let us consider  for any $k\in \mathbb{N}$: \beq I_{\alpha,k}:=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha} z_\alpha(q)^k ydx\eeq
Following the previous decomposition of $\mathcal{C}_\alpha$, the discontinuity across the log-cut can be evaluated  from \autoref{PropLocalCoord}.

\begin{proposition}[Local coefficients as integrals]\label{PropCoeffIntegrals} For any singular point $\alpha$ of $ydx$, coefficients of \autoref{PropLocalCoord} are given by:
\beq \forall \, k\in \mathbb{N}\,:\, I_{\alpha,k}=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha}z_\alpha(q)^kydx= -k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+\frac{s_\alpha}{k-d_\alpha} \delta_{k\neq d_\alpha}.\eeq
where $d_\alpha$, local coordinates $z_\alpha$ and the coefficients $(t_{\alpha,k})_{k\geq 1}$ and $s_\alpha$ are defined from \autoref{DefLocalCoord} and \autoref{PropLocalCoord}. We recall here that $s_\alpha\neq 0$ iff $\alpha\in \mathcal{S}_y$.
\end{proposition}

\begin{proof}The discontinuity (from above to below the cut) of $ydx$ is $-2i\pi s_\alpha z_\alpha^{-d_\alpha-1} dz_\alpha$. Thus the first contribution of $I_{\alpha,k}$ is 
\beq -s_\alpha\int_{\mathcal{C}_{o\to\alpha}} z_\alpha(q)^{k-d_\alpha-1} dz_\alpha(q)=-s_\alpha\int_{1}^{r_\alpha} z_\alpha^{k-d_\alpha-1} dz_\alpha
= \left\{
    \begin{array}{ll}
        s_\alpha\frac{1-r_\alpha^{k-d_\alpha}}{k-d_\alpha} & \mbox{if } k\neq d_\alpha\\
        -s_\alpha\ln r_\alpha & \mbox{ if } k=d_\alpha
    \end{array}
\right.
\eeq
This first contribution is vanishing if $\alpha\notin\mathcal{S}_y$.
The second contribution of $I_{\alpha,k}$ corresponds to the circle integral around $\alpha$ with radius $|q_\alpha|$. It is given by \autoref{LemmaLogIntegrals}. For any $k\in \mathbb{N}$:
\bea \oint_{\mathcal{C}_{q_\alpha}} z_\alpha(q)^{k-d_\alpha-1} ydx&=&\oint_{\mathcal{C}_{q_\alpha}} \left(z_\alpha(q)^{k} ydx(q)-s_\alpha z_\alpha(q)^{k-d_\alpha-1} \ln (1-z_\alpha(q)^{-1}) \right)dz_\alpha(q) \cr&&+ s_\alpha\oint_{\mathcal{C}_{r_\alpha}} z_\alpha(q)^{k-d_\alpha-1} \ln (1-z_\alpha^{-1}) dz_\alpha\cr
&=& -k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+ \left\{
\begin{array}{ll}
        s_\alpha\frac{r_\alpha^{k-d_\alpha}}{k-d_\alpha}  & \mbox{if } k\neq d_\alpha\\
        s_\alpha\ln r_\alpha & \mbox{ if } k=d_\alpha
    \end{array}
    \right.
\eea
Thus, we get that
\beq I_{\alpha,k}=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha}z_\alpha(q)^kydx=-k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+\frac{s_\alpha}{k-d_\alpha} \delta_{k\neq d_\alpha}
\eeq
ending the proof.
\end{proof}

\autoref{PropCoeffIntegrals} is a general formula that can be used either if $\alpha\in \mathcal{S}_y$ or $\alpha \notin \mathcal{S}_y$ (in which case $s_\alpha=0$). It is easy to see that one can use linear combinations of $(I_{\alpha,k})_{k\geq 0}$ to extract each irregular times, each monodromy or each log-time separately.



%However, as mentioned above, we may only face subcases of this formula depending on the situation. In particular we cannot have a non-trivial coefficient $s_\alpha$ with a non-trivial potential $V_\alpha$ or a non-trivial monodromy $t_{\alpha,0}$ so it is easy to invert the previous relation.

%\begin{corollary}[Local coefficients as integrals]\label{CorollaryLocalCoeffsAsIntegrals}We have:
%\begin{itemize}
%    \item If $s_\alpha=0$, then $ydx$ and $z_\alpha$ are meromorphic in a neighborhood of $\alpha$ and thus 
%    \bea \forall \,k>0\,:\,  t_{\alpha,k}&=&-\frac{I_{\alpha,k}}{k}=-\frac{1}{k} \Res_{q\to \alpha} z_\alpha(q)^k ydx(q)\cr
%    t_{\alpha,0}&=&I_{\alpha,0}=\Res_{q\to \alpha} ydx(q).
%    \eea
%    \item If $s_\alpha\neq 0$, then all $t_{\alpha,k}$ are vanishing for $k\geq 0$. Thus we get
%    \beq s_\alpha =(k-d_\alpha)I_{\alpha,k}\delta_{k\neq d_\alpha}\eeq
%\end{itemize}
%\end{corollary}






\textcolor{blue}{\subsection{Variations with respect to log-times}}
\textcolor{blue}{\begin{remark}\label{RemarkLogTimes}Let us observe that for a variation $\delta_\Omega=\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}$ with respect to the log-time $y_\alpha$, we have $\Omega(q)= \ln \frac{E(q,\alpha_i)}{E(q,\alpha_j)} dx(q)$ so that $\Omega(p_i)=0$ because $dx(p_i)=0$ for any ramification point $(p_i)_{1\leq i\leq N}$. This implies that 
\beq \label{VarLogTimesBergmannKernel} [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][B(p,q)]=0\eeq
\end{remark}}

\textcolor{blue}{\autoref{RemarkLogTimes} implies from the first line that
\beq \label{LogtimesKernel} \forall\, k\in \llbracket 1,N\rrbracket\,:\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][dE_{k,q}(p)]=0\eeq}

\textcolor{blue}{Since $dE_{k,q}(p)=\frac{1}{2}\int_q^{\sigma_k(q)} B(.,p)$ has a simple zero at $q=p_k$ and $\ln \frac{E(q,a_{\alpha_i})E(\sigma_k(q),a_{\alpha_j})}{E(q,a_{\alpha_j}) E(\sigma_k(q),a_{\alpha_i})} $ also has a simple zero at $q=p_k$, w get that the integrand in the first term is regular at the ramification points. Hence we get that for all $(i,j)\in \llbracket 1,M\rrbracket^2$:
\beq\label{SpecialLogTimes2} [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}]\left[
\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, f(q,\sigma_k(q))
\right]=\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][f(q,\sigma_k(q))]\eeq
} 
\textcolor{blue}{For log-times, the variations can be simplified from \autoref{RemarkLogTimes} and \eqref{LogtimesKernel}:
\bea\label{SpecialLogTimes}&& [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}]\left[
\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, f(q,\sigma_k(q))
\right]\cr
&&=-\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p) [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][y(q)-y(\sigma_k(q))]}{(y(q)-y(\sigma_k(q)))\omega_k(q)}\, f(q,\sigma_k(q))\cr
&&+ \sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][f(q,\sigma_k(q))]\cr
&&=-\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p) 
\ln \frac{E(q,a_{\alpha_i})E(\sigma_k(q),a_{\alpha_j})}{E(q,a_{\alpha_j}) E(\sigma_k(q),a_{\alpha_i})} }{(y(q)-y(\sigma_k(q)))^2}\, f(q,\sigma_k(q))\cr
&&+ \sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][f(q,\sigma_k(q))]
\eea
}

%\beq [\partial_{y_i}-\partial_{y_j}][\omega_{1,1}(z_1)]=\frac{1}{y_i}\Res_{z\to a_i} dS_{a_i,q}(z_1)\omega_{1,1}(q) -\frac{1}{y_j}\Res_{z\to a_j} dS_{a_j,q}(z_1)\omega_{1,1}(q)\eeq
%Indeed, let us first write
%\beq \frac{1}{\mathcal{S}(u)}=\frac{u}{e^{\frac{u}{2}} -e^{-\frac{u}{2}}}:=\sum_{j=0}^{\infty} \beta_{2j} u^{2j} \,\,,\,\, \forall \, u\in \mathbb{C}\eeq
%so that
%\beq \frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}=\sum_{j=0}^{\infty}\beta_{2j}\hbar^{2j}y_{a_s}^{1-2j}\frac{\partial^{2j}}{\partial x^{2j}}\eeq
%In particular, we have by definition:
%\bea(\text{Sing part at } a_s)[\omega_{1,1}(z_1)]&=&\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr
%&=&\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)\beta_2 y_{a_s}^{-1} \frac{\partial^2}{\partial x^2}\ln(z-a_s)\eea
%From the property of the third type differential, the singular part of the meromorphic differential $\omega_{1,1}$ at $a_s$ can be rewritten as
%\beq (\text{Sing part at } a_s)[\omega_{1,1}(z_1)]=\Res_{z'\to a_s}dS_{a_s,z'}(z_1)\omega_{1,1}(z') +\text{Reg}_s(z_1)\eeq
%where $\text{Reg}_s(z_1)$ is a meromorphic one-form that is regular at $z_1=a_s$.
%A similar observation leads to the fact that:
%\bea&& \frac{1}{y_i}(\text{Sing part at } a_i)[\omega_{1,1}(z_1)]-\frac{1}{y_j}(\text{Sing part at } a_j)[\omega_{1,1}(z_1)] \cr&&=\frac{1}{y_i}\Res_{z'\to a_i}dS_{a_i,z'}(z_1)\omega_{1,1}(z')-\frac{1}{y_j}\Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{1,1}(z') +\text{Reg}_{i,j}(z_1)
%\eea
%where $\text{Reg}_{i,j}(z_1)$ is a meromorphic one-form that is regular at $z_1=a_i$ and at $z_1=a_j$.
%Finally, the variation of $\omega_{1,1}$ is given by
%\small{\bea&& [\partial_{y_i}-\partial_{y_j}][\omega_{1,1}(z_1)]\cr&&
%=\beta_2\Res_{z\to a_i}dS_{a_i,z}(z_1)dx(z) y_{a_i}^{-2}\frac{\partial^2}{\partial x^2}\ln(z-a_i) -\beta_2\Res_{z\to a_j}dS_{a_j,z}(z_1)dx(z) y_{a_j}^{-2}\frac{\partial^2}{\partial x^2}\ln(z-a_j)\cr
%&&=\frac{1}{y_i} \left(\Res_{z\to a_i}dS_{a_i,z}(z_1)dx(z)  \beta_2 y_{a_i}^{-1}\frac{\partial^2}{\partial x^2}\ln(z-a_i)\right) -\frac{1}{y_j}\left(\Res_{z\to a_j}dS_{a_j,z}(z_1)dx(z) \beta_2 y_{a_j}^{-2}\frac{\partial^2}{\partial x^2}\ln(z-a_j)\right)\cr
%&&=\frac{1}{y_i}(\text{Sing part at } a_i)[\omega_{1,1}(z_1)]-\frac{1}{y_j}(\text{Sing part at } a_j)[\omega_{1,1}(z_1)] \cr
%&&=\frac{1}{y_i}\Res_{z'\to a_i}dS_{a_i,z'}(z_1)\omega_{1,1}(z')-\frac{1}{y_j}\Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{1,1}(z') +\text{Reg}_{i,j}(z_1)
%\eea}
%\normalsize{However} the l.h.s. is a meromorphic one form with only possible poles at $z_1=a_i$ or $z_1=a_j$ from the first equality. Hence $\text{Reg}_{i,j}(z_1)$ is an holomorphic one-form (it is meromorphic with no poles at $a_i$ nor $a_j$ and by difference it cannot have any other poles). Thus, it is a linear combination of the holomorphic one-forms $(du_k)_{1\leq k\leq g}$. However since $\omega_{1,1}$ has vanishing integrals on the $\mathcal{A}$-cycles (\eqref{VanishingAperiods}) and the third kind differential $dS_{a_s,z'}(z_1)$ also has vanishing periods on the $\mathcal{A}$-cycles, we get that $\text{Reg}_{i,j}(z_1)$ has vanishing periods on the $\mathcal{A}$-cycles and thus that it is null. In the end, we find
%\beq [\partial_{y_i}-\partial_{y_j}][\omega_{1,1}(z_1)]=\frac{1}{y_i}\Res_{z'\to a_i}dS_{a_i,z'}(z_1)\omega_{1,1}(z')-\frac{1}{y_j}\Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{1,1}(z')\eeq



\textcolor{blue}{\subsubsection{Variation of the logTR terms with respect to log-times}}
\textcolor{blue}{Let us first discuss the variations of the new term arising in logTR with respect to log-times.
Let us now consider variations of $\omega_{0,3}$ with respect to log-times. By definition,
\beq \omega_{0,3}(z_1,z_2,z_3)=\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}(B(z_2,z)B(z_3,\sigma_i(z))+B(z_2,\sigma_i(z))B(z_3,z) ) \eeq
Using $f_{0,3}(q,p):=B(z_2,q)B(z_3,p)+B(z_2,p)B(z_3,q)$ which is a symmetric bilinear form that is regular at the ramification points, \eqref{SpecialLogTimes2} implies that  
%\bea&&[\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][\omega_{0,3}(z_1,z_2,z_3)]= [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}]\left[
%\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, f_{0,3}(q,\sigma_k(q))
%\right]\cr
%&&=-\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p) 
%\ln \frac{E(q,a_i)E(\sigma_k(q),a_j)}{E(q,a_j) E(\sigma_k(q),a_i)} }{(y(q)-y(\sigma_k(q)))^2}\, f_{0,3}(q,\sigma_k(q))\cr
%&&+\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][B(z_2,q)B(z_3,\sigma_k(q))+B(z_2,\sigma_k(q))B(z_3,q)]
%\eea
\bea&&[\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][\omega_{0,3}(z_1,z_2,z_3)]= [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}]\left[
\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, f_{0,3}(q,\sigma_k(q))
\right]\cr
&&=\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p)}{\omega_k(q)}\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][B(z_2,q)B(z_3,\sigma_k(q))+B(z_2,\sigma_k(q))B(z_3,q)]
\eea
The chain rule combined with the fact that the variations of the Bergmann kernel with respect to the log-times is vanishing \eqref{VarLogTimesBergmannKernel} implies that the last term is vanishing.
%\beq [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][\omega_{0,3}(z_1,z_2,z_3)]=-\sum_{k=1}^N\Res_{q\to p_k}\frac{dE_{k,q}(p) 
%\ln \frac{E(q,a_i)E(\sigma_k(q),a_j)}{E(q,a_j) E(\sigma_k(q),a_i)} }{(y(q)-y(\sigma_k(q)))^2}\, f_{0,3}(q,\sigma_k(q))\eeq
\beq [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][\omega_{0,3}(z_1,z_2,z_3)]=0\eeq
It is then a straightforward induction for $\omega_{0,4}$, $\omega_{0,5}$, etc. to get that:
\beq \forall\, m\geq 3\,:\, [\partial_{y_{\alpha_i}}- \partial_{y_{\alpha_j}}][\omega_{0,m}(z_1,\dots,z_m)]=0\eeq
\begin{lemma}[Variations of the logTR term with respect to log-times]\label{LemmaVarLogTRTermsLogTimes}For any variation $\delta_\Omega:=\underset{j=1}{\overset{M}{\sum}} \mu_j \partial_{\delta_j}\in \delta_{\Omega_{\text{log}}}$ (i.e.$\underset{j=1}{\overset{M}{\sum}} \mu_j=0$ ) we have
\bea &&\delta_\Omega\left[-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\right]\cr&&
=\delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j} \Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{h,1}(z')
\eea
\end{lemma}
\begin{proof}The proof is given in Appendix \ref{AppendixProofVarLogTRTermsLogTimes}
\end{proof}
%Combining with \autoref{LemmaIntW02Wg1}, we get:
%\begin{proposition}[Variations of the logTR term with respect to log-times]\label{PropVarLogTRTermsLogTimes}For any variation $\delta_\Omega:=\underset{j=1}{\overset{M}{\sum}} \mu_j \partial_{\delta_j}\in \delta_{\Omega_{\text{log}}}$ (i.e.$\underset{j=1}{\overset{M}{\sum}} \mu_j=0$ ) we have
%\bea &&\delta_\Omega\left[-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\right]\cr&&
%=\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}\frac{x(z)-x(a_s)}{dx(z)}\omega_{h,1} (z)\omega_{0,2} (z,z_1)
%\eea
%\end{proposition}
}



\subsection{Variations of the correlators}


\textcolor{blue}{Even if we do not have a description of the decomposition of $ydx$ in terms of times, here is something that we can do. Assume that there exist a parameter such that the deformation of the induction kernel is given by Lemma 5.1 of \cite{EO07} and moreover that this parameter can be obtained as an integral of something times the Bergman kernel, i.e. eq 5.13 of \cite{EO07}. In other words, we start from 
\bea &&D_{\Omega}\left[\sum_{i=1}^N\Res_{q\to p_i}\frac{dE_{q}(p)}{\omega_{0,1}(q)- \omega_{0,1}(\sigma_i(q))}f(q,\sigma_i(q))\right]\cr&&=2\sum_{i=1}^N\sum_{j=1}^N \Res_{r\to p_i}\Res_{q\to p_j}\frac{dE_{r}(p)}{\omega_{0,1}(r)-  \omega_{0,1}(\sigma_i(r))}\Omega(r)\frac{dE_{q}(r)}{\omega_{0,1}(q)- \omega_{0,1}(\sigma_j(q))}f(q,\sigma_j(q))\cr
&&+\sum_{j=1}^N\Res_{q\to p_j}\frac{dE_{q}(p)}{\omega_{0,1}(q)- \omega_{0,1}(\sigma_j(q))}D_{\Omega}[f(q,\sigma_j(q))]\eea
and 
\beq \Omega(p)=\int_{\partial \Omega} B(p,q)\Lambda(q)\eeq
and we should prove by induction that
\beq D_{\Omega} [\omega_{h,n}(z_1,\dots,z_n)]=\int_{\partial \Omega} \omega_{h,n+1}(z,z_1,\dots,z_n) \Lambda(z)\eeq
and also for any $h\geq 1$:
\beq  D_{\Omega}[\omega_{h,0}]=\int_{\partial \Omega} \omega_{h,1}(z) \Lambda(z)\eeq
The difficulty in this approach is that we need to know how to take variations of the new term in the logTR definition. How can we define:
\beq D_\Omega\left[\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^z\omega_{0,2}(z_1,.)\right)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}\ln(z-a_s) \right)dx(z)\right] ?\eeq
Note that from \eqref{LogProjectionProperty} we have
\bea &&D_\Omega\left[\sum_{s=1}^M\Res_{z\to a_s}\left(\int_{a_s}^z\omega_{0,2}(z_1,.)\right)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}\ln(z-a_s) \right)dx(z)\right]\cr
&&=-D_\Omega\left[\sum_{s=1}^M\Res_{z'\to a_s}\left(\int_{o}^{z'}B(.,z_1)\right)\omega_{h,1}(z')\right]
\eea
but this cannot be used directly in the induction process since it includes $\omega_{h,1}$ in the r.h.s.
}

\textcolor{green}{We should be able to describe the decomposition of $ydx$. Indeed, $dx$ and $dy$ are meromorphic forms on $\Sigma$ (they are not arbitrary differentials). The new parameters are the monodromies of these differentials because of the non-vanishing residues. This creates a complication for $ydx$ because $y$ is not a meromorphic function. But we can use the decomposition that I proposed using logarithmic integrals. We should also consider variations with respect to $\alpha_s$ and this will have impact on the new term of logTR.}


\section{Limits when we have a logTR-vital singularity}
\textcolor{red}{Are there examples in which we can trade a ramification point for a logTR-vital singularity and show that the correlation function provided by logTR are continuous at the transition? For example, in genus $0$, take $x(z)=z+\frac{t^2}{z}$, then for $t=0$ there is no ramification point but for $t\neq 0$, we have two ramification points: $z_\pm=\pm t$. If we take $dy(z)=\frac{dz}{z}$ then $z=0$ and $z=\infty$ are two simple pole of $dy$. But they are no LogTR-vital singularities for $t\neq 0$ because $dx$ also has a pole there. For $t=0$, $dx(z)=1$ so $z=0$ and $z=\infty$ becomes LogTR-vital singularities. Can we prove that the correlation functions are continuous at $t=0$ using logTR? }

\section{Quantization when there is no ramification point but only logTR-vital singularities}
When there is no ramification point, only $(\omega_{h,1})_{h\geq 1}$, $\omega_{0,1}$, $\omega_{0,2}$ and $(\omega_{h,0})_{h\geq 0}$ are non trivial. Moreover, $\omega_{h,1}$ have only poles at the logTR-vital singularities. We have from LPP:
\beq \sum_{h=1}^\infty \hbar^{2h}\omega_{h,1}(z_1)=-\sum_{s=1}^M\Res_{z'\to a_s}\left(\int_{a_s}^{z'} B(.,z_1)\right)\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_{x'})}\ln(z'-a_s)\right)dx(z')\eeq
\textcolor{red}{Can we get the differential/difference equation satisfied by the formal wave function? }
\textcolor{red}{Can we characterize $dx$? It is a meromorphic differential on $\Sigma$ with no zero, this puts a lot of constraints on the genus and the possible values for $dx$. In genus $0$, the only possible choice is $dx=dz$. In genus $1$, $dx=c du$ where $du$ is the unique normalized holomorphic form is the only possible choice. For $g\geq 2$, I am not sure that it is possible.
In fact, I think we have from Riemann-Roch theorem:
\beq \text{(total order of zeros)-(total order of poles)}=2g-2\eeq
If we have no zero, then we get
\beq 2g-2=-\text{ (total order of poles) }\leq 0 \,\,\Rightarrow\,\, g\leq 1\eeq
For $g=0$, it implies at most two poles: either one double pole or two simple poles with opposite residues. Up to automorphisms of $\mathbb{P}^1$ it corresponds to $dx=dz$. For $g=1$, the formula gives no poles, so $dx$ is holomorphic on $\Sigma$.
}



\subsection{Proof of \autoref{LemmaVarLogTRTermsLogTimes}}\label{AppendixProofVarLogTRTermsLogTimes}
Let $\delta_\Omega=\underset{j=1}{\overset{M}{\sum}}\mu_j \partial_{y_j}$ with $\underset{j=1}{\overset{M}{\sum}}\mu_j=0$ and define
\beq (A):=-\delta_{\Omega}\left[\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\right]\eeq
Since the variations of the Bergmann kernel and of $x(z)$ with respect to log-times are vanishing (\autoref{VarLogTimesBergmannKernel}) we have:
\beq (A)=-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)\delta_{\Omega}\left[[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\right]\eeq

We write
\beq \frac{1}{\mathcal{S}(u)}=\frac{u}{e^{\frac{u}{2}} -e^{-\frac{u}{2}}}:=\sum_{j=0}^{\infty} \beta_{2j} u^{2j} \,\,,\,\, \forall \, u\in \mathbb{C}\eeq
so that
\beq \frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}=\sum_{j=0}^{\infty}\beta_{2j}\hbar^{2j}y_{a_s}^{1-2j}\frac{\partial^{2j}}{\partial x^{2j}}\eeq
In particular, we have by definition:
\bea(\text{Sing part at } a_s)[\omega_{h,1}(z_1)]&=&\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr
&=&\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)\beta_{2h} y_{a_s}^{1-2h} \frac{\partial^{2h}}{\partial x^{2h}}\ln(z-a_s)\eea
From the property of the third type differential, the singular part of the meromorphic differential $\omega_{h,1}$ at $a_s$ can be rewritten as
\beq (\text{Sing part at } a_s)[\omega_{h,1}(z_1)]=\Res_{z'\to a_s}dS_{a_s,z'}(z_1)\omega_{h,1}(z') +\text{Reg}_{h,s}(z_1)\eeq
where $\text{Reg}_{h,s}(z_1)$ is a meromorphic one-form that is regular at $z_1=a_s$.
A similar observation leads to the fact that:
\beq\label{RelationAppendix} \sum_{j=1}^M\frac{\mu_j}{y_j}(\text{Sing part at } a_j)[\omega_{h,1}(z_1)]=\sum_{j=1}^M\frac{\mu_j}{y_j}\Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{h,1}(z')+\text{Reg}_{h}(z_1)
\eeq
where $\text{Reg}_{h}(z_1)$ is a meromorphic one-form that is regular at $z_1\in \{a_1,\dots,a_M\}$.
Finally, the variation of $\omega_{h,1}$ is given by
\small{\bea (A)
&=&\delta_{m,1}(2h-1)\sum_{j=1}^M\mu_j \beta_{2h}\Res_{z\to a_i}dS_{a_j,z}(z_1)dx(z) y_{a_j}^{-2h}\frac{\partial^{2h}}{\partial x^{2h}}\ln(z-a_j)\cr
&=& \delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j} \beta_{2h}\Res_{z\to a_i}dS_{a_j,z}(z_1)dx(z) y_{a_j}^{1-2h}\frac{\partial^{2h}}{\partial x^{2h}}\ln(z-a_j)\cr
&=&\delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j}(\text{Sing part at } a_j)[\omega_{h,1}(z_1)]\cr
&\overset{\eqref{RelationAppendix}}{=}&\delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j} \Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{h,1}(z')+\text{Reg}_{h}(z_1)
\eea}
\normalsize{However} the l.h.s. is a meromorphic one-form with only possible poles at $z_1\in \{a_1,\dots,a_M\}$ from the first equality. Hence $\text{Reg}_{h}(z_1)$ is an holomorphic one-form (it is meromorphic with no poles at $(a_1,\dots,a_M)$ and by difference it cannot have any other poles). Thus, it is a linear combination of the holomorphic one-forms $(du_k)_{1\leq k\leq g}$. However since $\omega_{h,1}$ has vanishing integrals on the $\mathcal{A}$-cycles \eqref{VanishingAperiods} and the third kind differential $dS_{a_s,z'}(z_1)$ also has vanishing periods on the $\mathcal{A}$-cycles, we get that $\text{Reg}_{h}(z_1)$ has vanishing periods on the $\mathcal{A}$-cycles and thus that it is null. In the end, we find
\beq  (A)=\delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j} \Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{h,1}(z')\eeq

\subsection{Variations with respect to log-times}
\textcolor{red}{We will proceed by induction on $2h+m$. Let us first mention that the initialization $(h,m)=(0,2)$ is valid from the knowledge of the variations of $(\omega_{0,m})_{m\geq 2}$. Consider $h\geq 1$ and $m\geq 0$ such that $(h,m)\neq(0,1)$. Let us consider a variation $\delta_\Omega=\underset{j=1}{\overset{M}{\sum}}\mu_j \partial_{y_j}\in\delta_{\Omega_{\text{log}}}$ (i.e. $\underset{j=1}{\overset{M}{\sum}}\mu_j=0$)  and assume that the formulas in \autoref{TheoVariationalFormulas} hold for the first correlators up to $2h'+m'<2h+m$. We recall in particular that the Bergmann kernel has vanishing variations and that \eqref{SpecialLogTimes2} holds. From \eqref{LogTRDef}, we have by definition:
\bea \label{Defomegahmbis}\omega_{h,m}(z_1,\dots,z_m)&:=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big(\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big)\cr
    &&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\cr&&
    \eea 
\autoref{SpecialLogTimes} implies that when we vary with respect to log-times, since the two-form $f_{h,m}(q,p):=\omega_{h-1,m+1}(p,q,z_2,\dots,z_m)
    +\underset{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}}{\sum} \omega_{h_1,|I_1|+1}(q,z_{I_1}) \omega_{h_2,|I_2|+1}(p,z_{I_2})$ is regular at the ramification points, we only get
\bea \delta_\Omega[\omega_{h,m}(z_1,\dots,z_m) ]&=&(A)+ (B) \text{  with }\cr
(A)&:=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\delta_{\Omega}\Big[\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big]\cr
(B)&:=&-\delta_{m,1}\sum_{s=1}^M\Res_{z\to a_s}dS_{a_s,z}(z_1)dx(z)\delta_{\Omega}\left[[\hbar^{2h}]\left(\frac{y_{a_s}}{\mathcal{S}(y_{a_s}^{-1}\hbar \partial_x)}\ln(z-a_s) \right)\right]\cr&&
\eea  
The $(B)$ term is given by \autoref{LemmaVarLogTRTermsLogTimes}:
\beq \label{AppendixTermB}  (B)=\delta_{m,1}(2h-1)\sum_{j=1}^M\frac{\mu_j}{y_j} \Res_{z'\to a_j}dS_{a_j,z'}(z_1)\omega_{h,1}(z')\eeq
\medskip
Let us discuss term $(A)$. Observe first that $m+1\geq 2$ so that the first contribution is vanishing by induction. We shall isolate terms involving $(\omega_{h',1})_{h'\geq 1}$ in the second term:
\bea (A)&=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\delta_{\Omega}\Big[\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big]\cr 
    &=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\delta_{\Omega}\Big[\omega_{h-1,m+1}(z,\sigma_i(z),z_2,\dots,z_m)\cr
    &&+\sum_{h'=1}^{h} \omega_{h',1}(z)\omega_{h-h',m}(\sigma_i(z),z_2,\dots,z_m)+ \sum_{h'=1}^{h} \omega_{h',m}(z,z_2,\dots,z_m)\omega_{h-h',1}(\sigma_i(z))\cr
    &&+
    \sum_{\substack{h_1+h_2=h\\I_1\sqcup I_2=\{2,\dots, m\} \\(h_i,|I_i|)\neq (0,0)\\
    I_1\neq \emptyset\,,\, I_2\neq \emptyset}} \omega_{h_1,|I_1|+1}(z,z_{I_1}) \omega_{h_2,|I_2|+1}(\sigma_i(z),z_{I_2}) \Big]\cr
&=&\sum_{i=1}^N\Res_{z\to p_i}\frac{dE_{i,z}(z_1)}{\omega_i(z)}\Big[\cr
    &&+\sum_{h'=1}^{h} \delta_{\Omega}[\omega_{h',1}(z)]\omega_{h-h',m}(\sigma_i(z),z_2,\dots,z_m)+ \sum_{h'=1}^{h} \omega_{h',m}(z,z_2,\dots,z_m)\delta_{\Omega}[\omega_{h-h',1}(\sigma_i(z))]\Big]\cr
&&
\eea
}





\subsection{Log-times and other global parametrizations of $ydx$}
In this section, we discuss about some other possible ways to parametrize $ydx$. Indeed, for poles $\alpha \in \mathcal{P}\setminus \mathcal{S}_y$, i.e. poles for which $dy$ is either regular or has a pole with vanishing residues, one can define
\bea \forall\,\alpha\in \mathcal{P}\setminus\mathcal{S}_y\,:\, t_{\alpha,k}&:=&-\frac{1}{k}\Res_{q\to \alpha} z_\alpha(q)^k ydx\,,\, \,,\,\forall\, k\geq 1 \cr
t_{\alpha,0}&:=&\Res_{q\to \alpha} ydx
\eea
that in general do not match with $(\td{t}_{\alpha,k})_{k\geq 0}$ as explained in \autoref{RemarkTerminologyTimes}. In fact, one could also define local coefficients for poles $\alpha\in \mathcal{S}_y$.

\begin{proposition}[Another local decomposition of $ydx$ at a singular point]\label{PropLocalCoord2} Let $\alpha\in \mathcal{P}$ be a singularity of $ydx$. Take $z_\alpha$ the local coordinate at $\alpha$ defined in \autoref{DefLocalCoord} and the associated value of $d_\alpha\in \mathbb{Z}$. Then, the one-form $ydx$ can be locally written as:
\bea ydx(q)&=&-\sum_{k=2}^{R_\alpha+1} (k-1)t_{\alpha,k-1}z_\alpha(q)^{-k}dz_\alpha(q)+t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} \cr&&
+s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q) \cr
&:=&dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} +s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q)
\eea
where
\beq V_\alpha(q)=\sum_{k=1}^{R_\alpha} t_{\alpha,k}z_\alpha(q)^{-k}\eeq
Moreover, $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$. 
\end{proposition}

\begin{proof}Let us consider the first case where $x$ is regular at $\alpha$. In this case, only the case of a logarithmic cut for $y$ remains to prove compared to \cite{EO07}. Let us thus assume that $dy$ has a non-vanishing residue $-y_\alpha$ at $\alpha$, in other words, the simple pole of $dy$ is given by $-y_\alpha\frac{dx}{x-\alpha}$. In order to produce a cut from $\alpha$ to $o$, we must have $ydx- y_\alpha\ln \frac{x(q) -x(o)}{x(q)-x(\alpha)} dx$ is meromorphic at $\alpha$. Thus taking $s_\alpha=(x(\alpha)-x(o))y_\alpha$ provides the result since $\frac{x(q) -x(o)}{x(q)-x(\alpha)}=1-z_\alpha(q)^{-1}$.
Let us consider the second case where $\alpha$ is a pole of $x$ of order $d_\alpha$, i.e. $x(\alpha)=\infty$. Locally around $\infty$, $x$ has $d_\alpha$ distinct pre-images and $\alpha$ is one of them. In order to remove only the singularity at $\alpha$ but not at any other pre-images of $x(\alpha)=\infty$, we must remove only $\ln \frac{x(o)^{\frac{1}{d_\alpha}} -x(q)^{\frac{1}{d_\alpha}}}{x(o)^\frac{1}{d_\alpha}} =\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} $. Moreover, in this case we have $dx(q)=-d_\alpha z_{\alpha}^{-d_\alpha-1}dz_\alpha$. The prefactor can be absorbed in the meromorphic part but remains in front of the logarithmic term.  
Let us finally consider the third case where $\alpha$ is a simple pole of $dx$ (with non vanishing residue): $dx=\frac{x_\alpha}{q-\alpha} +\text{reg}(q)$. In this case $dx=\frac{dz_\alpha}{z_\alpha}$ and the log-term in $y$ is $\ln \frac{x(q)-x(o)}{-x(o)}=\ln \left(1-\frac{x(q)}{x(o)}\right)=\ln \left(1-z_\alpha^{-1}\right)$.
\end{proof}

\sloppy{\begin{remark}$du_\alpha(q)$ is divergent at $q=o$ because $ydx$ is regular at $q=o$ but $s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)$ is divergent.
\end{remark}}

At this stage, it is important to notice that $(s_\alpha)_{\alpha\in \mathcal{S}_y}\cup,(t_{\alpha,k})_{\alpha\in \mathcal{P},k\geq 0}$ also encode the local behavior of $ydx$ at each pole $\alpha \in \mathcal{P}$. But these parameters differ from $(y_\alpha)_{\alpha\in \mathcal{S}_y}\cup,(\td{t}_{\alpha,k})_{\alpha\in \mathcal{P},k\geq 0}$ defined in \autoref{PropLocalCoord} because $du_\alpha(q)\neq d\td{u}_\alpha(q)$.

\textcolor{red}{Can we relate $s_\alpha$ to $y_\alpha$? In particular, along the cut, $ydx$ has a jump given by $2i\pi y_\alpha dx$ by definition. In local coordinates, the jump is given by the $s_\alpha$ factor. If we remove this term, do we have 
\beq ydx(q)-s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q) \text{ regular along cut?}\eeq
$du_\alpha(q)$ is singular at $q=o$ because of the other log-cuts. Can we say that the discontinuity along the cut ignore $du_\alpha(q)$? 
}

Note that one can extract the coefficients $(t_{\alpha,k})_{\alpha\in \mathcal{P},k\geq 0}$ using contour integrals that are more complicated than residues of $ydx$ when $\alpha \in \mathcal{S}_y$ (residues of $ydx$ ar not well-defined at  $\alpha\in \mathcal{S}_y$ because of the logarithmic cut from $\alpha$ to $o$). Let us first starts with a technical lemma:
\begin{lemma}[Logarithmic integrals]\label{LemmaLogIntegrals}Let $0<r<1$ and let $\mathcal{C}_r$ be the counterclockwise circle of radius $r$ centered at $0$ parametrized by $z_0=re^{i\theta}$ with $\theta\in [0,2\pi]$. Let $\td \ln z_0$ be the logarithm with a branch taken on the positive real axis and such that $\td{\ln}(t+i\epsilon)=\td{\ln}(t-i\epsilon)+2i\pi$ for any $t\in \mathbb{R}_+^*$. In other words: $\td{\ln}(z_0)=-\ln(-z_0)$ where $\ln$ stands for the usual logarithm with its usual branch on the negative real axis. We have for any $z\in \mathbb{Z}$:
\beq \frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\td{\ln}\, z_0\, dz_0=\left\{
    \begin{array}{ll}
        -\frac{r^{k+1}}{k+1} & \mbox{if } k\neq -1 \\
        -\ln r & \mbox{if } k=-1
    \end{array}
\right.
\eeq    
\end{lemma}

\begin{proof}The proof is done in \autoref{AppendixTechnicalIntegrals}.
\end{proof}

Let us now define the following contour:

\begin{definition}[Contour at log-singularities of $ydx$]\label{DefContourlogpoles}For any $\alpha \in \mathcal{S}_y$, we define $\mathcal{C}_{o\to \alpha}$ as the contour starting from $o$ above the log-cut connecting $o$ to $\alpha$ and then circling around $\alpha$ counterclockwise and ending at $o$ below the log-cut connecting $o$ to $\alpha$. This definition implicitly assume that the contour only circles the log-cut connecting $o$ to $\alpha$ and $\alpha$ without circling any other singular point of the integrand or crossing any holonomy cycles. Moreover, it is taken in a immediate neighborhood of the cut and $\alpha$ where the coordinate $z_\alpha$ is well-defined.
\end{definition}

In practice, this contour can be split into two parts:
\begin{itemize}
    \item Let $q_\alpha$ be a point on the log-cut connecting $o$ to $\alpha$ such that $z_\alpha(q_\alpha):=r_\alpha$ satisfies $|r_\alpha|<1$ in the $z_\alpha$-plane. Then, the first part of the contour corresponds to the discontinuity across the log-cut from $o$ to $q_\alpha$.
    \item The second part corresponds to a circle integral starting at $q_\alpha$ and circling once around $\alpha$ counterclockwise and ending at $q_\alpha$. 
\end{itemize}

\textcolor{blue}{Insert a picture}


We may now use \autoref{LemmaLogIntegrals} to obtain the coefficients of the singular part of $ydx$ at $\alpha$. Indeed, let us consider  for any $k\in \mathbb{N}$: \beq I_{\alpha,k}:=\frac{1}{2i\pi}\oint_{\mathcal{C}_{o\to \alpha}} z_\alpha(q)^k ydx\eeq
As mentioned above, these integrals can be used to extract the coefficients $(t_{\alpha,k})_{k\geq 0}$.

\begin{proposition}[Local coefficients as integrals]\label{PropCoeffIntegrals} For any singular point $\alpha$ of $ydx$, coefficients of \autoref{PropLocalCoord} are given by:
\beq \forall \, k\in \mathbb{N}\,:\, I_{\alpha,k}:=\frac{1}{2i\pi}\oint_{\mathcal{C}_{o\to \alpha}}z_\alpha(q)^kydx= -k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+\frac{s_\alpha}{k-d_\alpha} \delta_{k\neq d_\alpha}.\eeq
where $d_\alpha$, local coordinates $z_\alpha$ and the coefficients $(t_{\alpha,k})_{k\geq 1}$ and $s_\alpha$ are defined from \autoref{DefLocalCoord} and \autoref{PropLocalCoord}. 
\end{proposition}

\begin{proof}Note that $ydx(q)$ is regular at $q=o$ and so is $z_\alpha(q)^k ydx(q)$. The discontinuity (from above to below the cut) of $ydx$ is $-2i\pi s_\alpha z_\alpha^{-d_\alpha-1} dz_\alpha$. \textcolor{red}{Is this correct?, because $du_\alpha(q)$ is singular at $q=o$ as mentioned above.} Thus the first contribution of $I_{\alpha,k}$ is 
\beq -s_\alpha\int_{\text{Cut } o\to q_\alpha} z_\alpha(q)^{k-d_\alpha-1} dz_\alpha(q)=-s_\alpha\int_{1}^{r_\alpha} z_\alpha^{k-d_\alpha-1} dz_\alpha
= \left\{
    \begin{array}{ll}
        s_\alpha\frac{1-r_\alpha^{k-d_\alpha}}{k-d_\alpha} & \mbox{if } k\neq d_\alpha\\
        -s_\alpha\ln r & \mbox{ if } k=d_\alpha
    \end{array}
\right.
\eeq
The second contribution of $I_{\alpha,k}$ corresponds to the circle integral which is given by \autoref{LemmaLogIntegrals}. For any $k\in \mathbb{N}$:
\bea \oint_{\mathcal{C}_{q_\alpha}} z_\alpha(q)^{k-d_\alpha-1} ydx&=&\oint_{\mathcal{C}_{q_\alpha}} \left(z_\alpha(q)^{k} ydx(q)-s_\alpha z_\alpha(q)^{k-d_\alpha-1} \ln (1-z_\alpha(q)^{-1}) \right)dz_\alpha(q) \cr&&+ s_\alpha\oint_{\mathcal{C}_{r_\alpha}} z_\alpha(q)^{k-d_\alpha-1} \ln (1-z_\alpha^{-1}) dz_\alpha\cr
&=& -k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+ \left\{
\begin{array}{ll}
        s_\alpha\frac{r_\alpha^{k-d_\alpha}}{k-d_\alpha}  & \mbox{if } k\neq d_\alpha\\
        s_\alpha\ln r & \mbox{ if } k=d_\alpha
    \end{array}
    \right.
\eea
Thus, we get that
\beq I_{\alpha,k}=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha}z_\alpha(q)^kydx=-k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+\frac{s_\alpha}{k-d_\alpha} \delta_{k\neq d_\alpha}
\eeq
ending the proof.
\end{proof}

The problem when using the coordinates ($s_\alpha,t_{\alpha,k})$ is to obtain a global decomposition of $ydx$. 

\textcolor{red}{
\begin{proposition}[Log-forms]\label{PropLogForms}Let $\alpha$ be a singular point of $ydx$. The one-form
\beq B_\alpha(p):=-\oint_{q\in\mathcal{C}_{o\to \alpha}} \left(\int_{o'}^qB(p,.)\right)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q) \eeq
has the following properties:
\begin{itemize}
    \item It is holomorphic except on the contour $\mathcal{C}_{o\to\alpha}$.
    \item On the contour $\mathcal{C}_{o\to \alpha}$ it has a jump given by
    $z_\alpha(p)^{-d_\alpha-1}\ln \frac{z_\alpha(p)-1}{z_\alpha(p)} dz_\alpha(p)$ for all $p\in \mathcal{C}_{o\to\alpha}$.
    \item It is normalized on the $\mathcal{A}$-cycles:
    \beq \oint_{\mathcal{A}_i} B_\alpha(p) =0 \,\,,\,\, \forall\,i\in \llbracket 1,g \rrbracket.\eeq
\end{itemize}
\end{proposition}
This proposition cannot be true, because there does not exist any differential satisfying the properties listed. We may still define $B_{\alpha,k}(q)$ and $B_{\alpha,0,o'}$ as in \autoref{DefBalphak} where we can replace the residue by the contour $\mathcal{C}_{o\to \alpha}$ without changing anything. But the logarithmic contributions require to create a new singularity somewhere (at $dx$ or somewhere else). This is why it is natural to take $dx$ because we can have a simple global decomposition.
}

\textcolor{green}{Mention that for quantization, $y_\alpha$ are orders of poles/zeros so they are necessarily fixed. In the case where $x(z)=z^2$ and $y(z)=y_1 \ln\frac{z-1}{z+1}$ we have no other parameters than $y_1$. But $z=\infty$ is a pole of $dx$ and regular for $dy$ and at infinity we have $ydx= 2y_1 \frac{dz}{z}$ so that $2y_1$ can also be considered as a irregular time of $ydx$. But somehow, we do not know how to variate it because $\td{y}=0$.  }



However, it seems natural to use integrals of $ydx$ to define times rather than integrals of $\td{y}dx$. The main problem of using integrals of $ydx$ arises for log-poles. Indeed, in the decomposition of $ydx$, the obstruction is the following: for a pole $\alpha\in \mathcal{S}_y$, $y$ has a logarithmic cut from $\alpha$ to $o$ given by $\ln \frac{E(q,\alpha)}{E(q,o)}$. Since the local coordinates is $z_\alpha(q)=\frac{x(q)-x(\alpha)}{x(o)-x(\alpha)}$ because $dx$ is regular at $\alpha \in \mathcal{S}_y$, the local decomposition of $ydx$ is $(x(o)-x(\alpha))\ln \frac{E(q,\alpha)}{E(q,o)}x'(q) dq +\text{reg}_\alpha$ or equivalently $\ln \frac{E(q,\alpha)}{E(q,o)}dx(q) +\text{reg}_\alpha$. However, for the global decomposition, we need a globally defined differential so we cannot use $dz_\alpha$ which is only local. Instead we used $dx$ which is global but has other poles and is not normalized on the $\mathcal{A}$-cycles generating a difference between the irregular times of $ydx$ (when they can be defined) and the irregular times of $\td{y}dx$ and a difference between filling fractions of $ydx$ and filling fractions of $\td{y}dx$. However, there is no possible way to avoid this situation. Indeed, for the global decomposition we would need a differential $\omega\neq 0$ such that $\omega$ is normalized on the $\mathcal{A}$-cycles and is holomorphic on $\Sigma$ which is impossible. Equivalently, we would like a differential $\omega_\alpha$ holomorphic on $\Sigma\setminus\mathcal{C}_{o\to \alpha}$, normalized on the $\mathcal{A}$-cycles and such that it has a jump through $\mathcal{C}_{o\to \alpha}$ given by $2i\pi dx$ and such differential cannot be defined.   



\section{Logarithmic integrals}\label{AppendixTechnicalIntegrals}
In this section, we prove the following result
\beq \frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\td{\ln}\, z_0\, dz_0=\left\{
    \begin{array}{ll}
        -\frac{r^{k+1}}{k+1} & \mbox{if } k\neq -1 \\
        -\ln r & \mbox{if } k=-1
    \end{array}
\right.
\eeq
where $\mathcal{C}_r$ is a counterclockwise circle of radius $0<r<1$ and $\td \ln z_0$ stands for the fact that the log-cut of the logarithm is taken on the positive real axis (and not the negative real axis), i.e. $\td{\ln}(t+i\epsilon)=\td{\ln}(t-i\epsilon)+2i\pi$ for any $t\in \mathbb{R}_+^*$. It corresponds to $\td{\ln}(z_0)=-\ln(-z_0)$ for the standard logarithm.
\beq  \frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\td{\ln}\, z_0\, dz_0=-\frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\ln (-z_0)\, dz_0
\eeq

Let us first consider $k\neq -1$, the contour integral is parametrized by $z_0=r e^{i\theta}$ with $\theta\in [0,2\pi]$. Thus the integral reads
\bea\frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\td{\ln}\, z_0\, dz_0&=&-\frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\ln (-z_0)\, dz_0\cr
&\overset{z=-z_0}{=}&\frac{1}{2i\pi}\oint_{-\mathcal{C}_r} (-z)^k \,\ln z\, dz\cr
&=&\frac{(-1)^kr^{k+1}}{2\pi}\int_{-\pi}^{\pi}e^{i(k+1)\theta} \left( \ln r+ i\theta\right) d\theta\cr
&=&\frac{(-1)^kr^{k+1}}{2\pi}\left( \ln r\left[\frac{e^{i(k+1)\theta}}{i(k+1)}\right]_{\theta=-\pi}^{\theta=\pi} + \left[\frac{\theta}{k+1}e^{i(k+1)\theta}  \right]_{\theta=-\pi}^{\theta=\pi} -\frac{1}{2\pi}\int_{-\pi}^{\pi} e^{i(k+1)\theta}d\theta\right)\cr
&\overset{k\neq-1}{=}&\frac{(-1)^kr^{k+1}}{2\pi}\left( \frac{\pi e^{i(k+1)\pi}}{k+1} - \frac{(-\pi) e^{-i(k+1)\pi}}{k+1} \right)\cr
&=&-\frac{r^{k+1}}{k+1}
\eea
because$-\mathcal{C}_r$ corresponds to the counterclockwise circle of radius centered at $z=0$ going from $-r-i\epsilon$ to $-r+i\epsilon$ and thus is parametrized by $z=e^{i\theta}$ with $\theta\in [-\pi,\pi]$ which is the standard parameterization for the usual logarithm.

Let us now consider the case $k=-1$. We have
\bea\frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^{-1} \,\td{\ln}\, z_0\, dz_0&=&-\frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^{-1} \,\ln (-z_0)\, dz_0\cr
&\overset{z=-z_0}{=}&-\frac{1}{2i\pi}\oint_{-\mathcal{C}_r} z^{-1} \,\ln z\, dz\cr
&=&-\frac{1}{2\pi}\int_{-\pi}^{\pi}\left( \ln r+ i\theta\right) d\theta\cr
&=&-\ln r
\eea



\section{Old global decomposition}
\subsection{Local coordinates and decomposition of $ydx$}
Let us first study what happens in a neighborhood of a ramification point. Since ramification points are assumed to be distinct from the singularity of $ydx$, they are necessarily away from the log-cuts and therefore residues around them only needs local coordinates. The situation is thus the same as in \cite{EO07} and does not depend on the relation between $(x,y)$ and $(X,Y)$. 

\begin{definition}[Local coordinate around a ramification point]\label{DefLocalCoordinateBranchPoint} Let $p$ be a ramification point. We shall define the local coordinate around $p$ as
\beq z_{p}(q)=\sqrt{x(q)-x(p)} \,\,\Rightarrow\,\, dx(q)=2z_{p}(q) dz_{p}(q)\eeq
\end{definition}

Note that $z_{p}(p)=0$, $ydx$ is holomorphic in $z_p$ in a neighborhood of $p$:
\beq ydx(q)\overset{q\to p}{=}\sum_{k=1}^\infty b_{p,k}z_{p}(q)^k dz_{p}(q)\eeq

\medskip

We shall now focus on local coordinates around a singular point $\alpha$ of $ydx$. Let us recall that $o$ is a generic point on $\Sigma$ such that $o$ is neither a ramification point nor a singularity of $dx$ nor $dy$. Moreover, we take the ramification point such that $x(o)\neq x(\alpha)$ for any singularity of $dx$ or $dy$ or any ramification point $\alpha$. We shall now consider the following local coordinates.

\begin{definition}[Local coordinates at singularities of $ydx$]We shall define the following local coordinates around singularities of $ydx$ that may happen in our four different cases.
\begin{itemize}
    \item If $\alpha$ is a pole of $dy$ but $x$ is regular at $\alpha$ we shall define $d_\alpha=-1$ and
    \beq z_\alpha(q)=\frac{x(q)-x(\alpha)}{x(o)-x(\alpha)}\eeq
    \item $\alpha$ is a pole of $x$ of order $d_\alpha\geq 1$, i.e. such that $x(q)=\frac{\mu}{(q-\alpha)^{d_\alpha}} +o\left((q-\alpha)^{-d_\alpha}\right)$. In particular $x(\alpha)=\infty$. We shall define
    \beq z_\alpha(q)=\left(\frac{x(o)}{x(q)}\right)^{\frac{1}{d_\alpha}}\eeq
    where the $d_\alpha$-branch is defined locally around $\infty=x(\alpha)$ and is analytically continued along a neighborhood of the cut from $\alpha$ to $o$.  
    \item If $\alpha$ is a simple pole of $dx$ with an integer-valued residue, i.e. $x(q)=x_{\alpha} \ln(q-\alpha) +O(1)$ where $x_{\alpha}=\underset{q\to \alpha}{\Res} dx \in \mathbb{Z}^*$, we define $d_\alpha=0$ and
    \beq z_\alpha(q)=\exp\left(\frac{x(q)-x(o)}{x_{\alpha}}\right)\eeq
\end{itemize}
\end{definition}

Note that in all cases we have $z_\alpha(\alpha)=0$ and $z_\alpha(o)=1$. Moreover, the coordinates $z_\alpha(q)$ are defined in a neighborhood of $\alpha$ and of the log-cut connecting $\alpha$ to $o$. In the $z_\alpha$-plane, it corresponds to a neighborhood of $0$ and a neighborhood of the cut connecting $0$ to $1$. In all three cases, the local expansion of $ydx$ is given by the following proposition.

\begin{proposition}[Local decomposition of $ydx$ at a singular point] Let $\alpha$ be a singularity of $ydx$ arising in the four cases depending on the relation between $(x,y)$ and $(X,Y)$. Take $z_\alpha$ the local coordinate at $\alpha$ defined in \autoref{DefLocalCoord} and the associated value of $d_\alpha\in \mathbb{Z}$. Then, the one-form $ydx$ can be locally written as:
\bea ydx(q)&=&-\sum_{k=2}^{R_\alpha+1} (k-1)t_{\alpha,k-1}z_\alpha(q)^{-k}dz_\alpha(q)+t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} \cr&&
+s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q) \cr
&=&dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} +s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q)
\eea
where
\beq V_\alpha(q)=\sum_{k=1}^{R_\alpha} t_{\alpha,k}z_\alpha(q)^{-k}\eeq
is called the ``potential" at $\alpha$. Moreover, $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$. 
\end{proposition}

\begin{proof}Let us consider the first case where $x$ is regular at $\alpha$. In this case, only the case of a logarithmic cut for $y$ remains to prove compared to \cite{EO07}. Let us thus assume that $dy$ has a non-vanishing residue $-y_\alpha$ at $\alpha$, in other words, the simple pole of $dy$ is given by $-y_\alpha\frac{dx}{x-\alpha}$. In order to produce a cut from $\alpha$ to $o$, we must have $ydx- y_\alpha\ln \frac{x(q) -x(o)}{x(q)-x(\alpha)} dx$ is meromorphic at $\alpha$. Thus taking $s_\alpha=(x(\alpha)-x(o))y_\alpha$ provides the result since $\frac{x(q) -x(o)}{x(q)-x(\alpha)}=1-z_\alpha(q)^{-1}$.
Let us consider the second case where $\alpha$ is a pole of $x$ of order $d_\alpha$, i.e. $x(\alpha)=\infty$. Locally around $\infty$, $x$ has $d_\alpha$ distinct pre-images and $\alpha$ is one of them. In order to remove only the singularity at $\alpha$ but not at any other pre-images of $x(\alpha)=\infty$, we must remove only $\ln \frac{x(o)^{\frac{1}{d_\alpha}} -x(q)^{\frac{1}{d_\alpha}}}{x(o)^\frac{1}{d_\alpha}} =\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} $. Moreover, in this case we have $dx(q)=-d_\alpha z_{\alpha}^{-d_\alpha-1}dz_\alpha$. The prefactor can be absorbed in the meromorphic part but remains in front of the logarithmic term.  
Let us finally consider the third case where $\alpha$ is a simple pole of $dx$ (with non vanishing residue): $dx=\frac{x_\alpha}{q-\alpha} +\text{reg}(q)$. In this case $dx=\frac{dz_\alpha}{z_\alpha}$ and the log-term in $y$ is $\ln \frac{x(q)-x(o)}{-x(o)}=\ln \left(1-\frac{x(q)}{x(o)}\right)=\ln \left(1-z_\alpha^{-1}\right)$.
\end{proof}

\sloppy{\begin{remark}$du_\alpha(q)$ is divergent at $q=o$ because $ydx$ is regular at $q=o$ but $s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)$ is divergent.
\end{remark}}

Similarly to the terminology of the standard topological recursion \cite{EO07}, we shall call the coefficients $(t_{\alpha,k})_{k\geq 1}$ the \textit{irregular times} at the singular point $\alpha$, while $t_{\alpha,0}$ is called the \textit{monodromy} or \textit{temperature} at the pole. The new coefficient $s_\alpha$ appearing when $y$ has a log-singularity shall be referred to as the \textit{log-time} at the singular point $\alpha$. 

\begin{remark}It is important to notice that there is only one additional time at a pole where $y$ has a logarithmic singularity. In particular, if one can make a  formal series expansion at $z_\alpha=0$ of $\ln \frac{z_\alpha-1}{z_\alpha}$ to obtain $\underset{i=0}{\overset{\infty}{\sum}} \beta_i z_\alpha^i\ln z_\alpha$, this series is mostly useless since it looses the ability to compute the discontinuity across the logarithmic cut (which is just $2i\pi$).
\end{remark}

The formula in \autoref{PropLocalCoord} is a general formula regrouping the four different setups in a single formula. However, some of the coefficients are necessarily vanishing depending on the situation. As we will see from \autoref{SectionDetailDecomposition}, it is convenient to split cases using the following definition.

\begin{definition}\label{DefSplitSingPointsydx}We shall denote $\mathcal{S}$ the set of singular points of $ydx$. Moreover, we shall denote $\mathcal{S}_{\text{mero}}$ the set of singular points $\alpha$ of $ydx$ such that $s_\alpha=0$ in \autoref{PropLocalCoord}:
\beq \mathcal{S}_{\text{mero}}:=\left\{\alpha \in \Sigma \text{ such that } ydx \text{ is singular and } s_\alpha=0\right\}\eeq
On the contrary, we shall denote $\mathcal{S}_{\text{log}}$ the set of singular points $\alpha$ of $ydx$ such that $s_\alpha\neq 0$ in \autoref{PropLocalCoord}:
\beq \mathcal{S}_{\text{mero}}:=\left\{\alpha \in \Sigma \text{ such that } ydx \text{ is singular and } s_\alpha\neq 0\right\}\eeq
\end{definition}

The previous definition is done so that the following proposition holds:

\begin{proposition}[Decomposition of singular points of $ydx$]\label{PropDecompositionSingPointsydx}We have
\beq \mathcal{S}=\mathcal{S}_{\text{mero}}\sqcup\mathcal{S}_{\text{log}}\eeq
and moreover,
\beq\forall \, \alpha \in \mathcal{S}_{\text{log}}:  t_{\alpha,k}=0 \,,\,\forall\, k\geq 0\eeq
\end{proposition}

\begin{proof}The proof is a direct consequence of \autoref{SectionDetailDecomposition} where all possible cases are studied.
\end{proof}


\subsection{Description of the local decomposition of $ydx$ in each case}\label{SectionDetailDecomposition}
\autoref{PropLocalCoord} is a generic formula covering all possibles cases. However, because of the relation between $(x,y)$ and $(X,Y)$ we may only face subcases in \autoref{PropLocalCoord} that we detail below.

\subsubsection{Case when $(x,y)=(X,Y)$}
This is the setting of the standard TR and $(X,Y)$ are two meromorphic maps from $\Sigma$ to $\mathbb{P}^1$. In this case $ydx$ is meromorphic on $\Sigma$ and $dx$ cannot have poles with non-vanishing residues. Thus, only the first two cases of \autoref{DefLocalCoord} happen and the local coordinates are
 \begin{itemize}
 \item If $\alpha$ is a pole of $dY$ but $X$ is regular at $\alpha$, we shall define:
    \beq z_\alpha(q)=\frac{x(q)-x(\alpha)}{x(o)-x(\alpha)}=\frac{X(q)-X(\alpha)}{X(o)-X(\alpha)}\eeq
    \item If $\alpha$ is a pole of $X$ of order $d_\alpha\geq 1$, we shall define
    \beq z_\alpha(q)=\left(\frac{x(o)}{x(q)}\right)^{\frac{1}{d_\alpha}}=\left(\frac{X(o)}{X(q)}\right)^{\frac{1}{d_\alpha}}\eeq
    where the $d_\alpha$-branch is defined locally around $\infty=X(\alpha)$ and is analytically continued along a neighborhood of the cut from $\alpha$ to $o$. 
\end{itemize}
Moreover, $ydx$ does not have any log-singularities because it is meromorphic. In this case, the local decomposition reduces to 
\bea ydx(q)&=&-\sum_{k=2}^{R_\alpha+1} (k-1)t_{\alpha,k-1}z_\alpha(q)^{-k}dz_\alpha(q)+t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q) \cr
&=&dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eea
and the only possible singular points $\alpha$ correspond to poles of $dy=dY$ and/or poles of $dx=dX$. This recover the standard results of \cite{EO07}.

\subsubsection{Case when $(x,y)=(\ln X,Y)$} In this case we have $ydx=Y\frac{dX}{X}$. Thus, $ydx$ is a meromorphic one-form on $\Sigma$ with poles at either poles of $Y$, poles of $X$ but also zeros of $X$. We shall study these cases more precisely.
\begin{itemize}
    \item  If $\alpha$ is a pole of $Y$ but $x$ is regular at $\alpha$ (i.e. $\alpha$ is neither a pole of $X$ nor a zero of $X$), we shall define:
    \beq z_\alpha(q)=\frac{x(q)-x(\alpha)}{x(o)-x(\alpha)}=\frac{\ln (X(q)) -\ln (X(\alpha))}{\ln (X(o)) -\ln (X(\alpha))}
    \eeq
In this case, the local decomposition has the usual form
\bea ydx(q)&=&-\sum_{k=2}^{R_\alpha+1} (k-1)t_{\alpha,k-1}z_\alpha(q)^{-k}dz_\alpha(q)+t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q) \cr
&=&dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eea
where $du_\alpha$ is holomorphic in a neighborhood of $\alpha$ including a neighborhood of the cut from $o$ to $\alpha$.
\item If $\alpha$ is a pole of $X$ of order $d_\alpha=-n_\alpha\geq 1$ or $\alpha$ is a zero of $X$ of order $n_\alpha\geq 1$. Then $dx=\frac{dX}{X}$ has a simple pole with residue equal to $n_\alpha$. This creates a log-singularity for $x$ and so the local coordinate is
\beq z_\alpha(q)=\exp\left(\frac{x(q)-x(o)}{n_{\alpha}}\right)=\left(\frac{X(q)}{X(o)}\right)^{\frac{1}{ n_\alpha}}\eeq
The local decomposition is then
\bea ydx(q)&=&-\sum_{k=2}^{R_\alpha+1} (k-1)t_{\alpha,k-1}z_\alpha(q)^{-k}dz_\alpha+t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q) \cr
&=&dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eea
where $du_\alpha$ is holomorphic in a neighborhood of $\alpha$ including a neighborhood of the cut from $o$ to $\alpha$.
\end{itemize}

\subsubsection{Case when $(x,y)=(X, \ln Y)$}    
In this case we have $ydx=\ln Y dX$ so it is not a meromorphic form on $\Sigma$. More precisely, it is defined only outside cuts connecting any pole or zero or $Y$ to the basepoint $o$. There are several possible cases:
\begin{itemize} \item If $\alpha$ is a pole of $X$ of order $d_\alpha\geq 1$ but is not a pole of $Y$ nor a zero of $Y$. In that case $\ln Y$ is regular in a neighborhood of $\alpha$ and the local coordinate is
 \beq z_\alpha(q)=\left(\frac{x(o)}{x(q)}\right)^{\frac{1}{d_\alpha}}=\left(\frac{X(o)}{X(q)}\right)^{\frac{1}{d_\alpha}}\eeq
The local decomposition is the standard one
\bea ydx(q)&=&-\sum_{k=2}^{R_\alpha+1} (k-1)t_{\alpha,k-1}z_\alpha(q)^{-k}dz_\alpha(q)+t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)}+ du_\alpha(q) \cr
&=&dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eea 
where $du_\alpha$ is holomorphic in a neighborhood of $\alpha$ including a neighborhood of the cut from $o$ to $\alpha$.
\item If $\alpha$ is a regular point of $X$ but either a zero of $Y$ of order $n_\alpha$ or a pole of $Y$ of order $d_\alpha=-n_\alpha$. In that case, the local coordinate is
\beq z_\alpha(q)=\frac{x(q)-x(\alpha)}{x(o)-x(\alpha)}=\frac{X(q)-X(\alpha)}{X(o)-X(\alpha)}\eeq
$y$ has a logarithmic behavior at $\alpha$: $Y(q)=n_\alpha \ln (q-\alpha)+O(1)$ and the local decomposition is 
\beq ydx(q)=s_\alpha \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q) \eeq
with $s_\alpha\neq 0$ (because $\alpha$ is not a ramification point) and where $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured  neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$. 
\item If $\alpha$ if a pole of $X$ of order $d_\alpha\geq 1$ and either a zero of $Y$ of order $n_\alpha$ or a pole of $Y$ of order $d_\alpha=-n_\alpha$. In that case, the local coordinate is
 \beq z_\alpha(q)=\left(\frac{x(o)}{x(q)}\right)^{\frac{1}{d_\alpha}}=\left(\frac{X(o)}{X(q)}\right)^{\frac{1}{d_\alpha}} \eeq
where the $d_\alpha$-branch is defined locally around $\infty=X(\alpha)$ and is analytically continued along a neighborhood of the cut from $\alpha$ to $o$. In that case, the local decomposition is
\beq ydx(q)=s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q) \eeq
where $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured  neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$. 
\end{itemize}

\subsubsection{Case when $(x,y)=(\ln X, \ln Y)$}
In this case we have $ydx=\ln Y \frac{dX}{X}$ so it is not a meromorphic form on $\Sigma$. More precisely, it is defined only outside cuts connecting any pole or zero or $Y$ to the basepoint $o$. There are several possible cases:
\begin{itemize}
    \item If $\alpha$ is a pole of $X$ of order $d_\alpha=-n_\alpha\geq 1$ or a zero of $X$ of order $n_\alpha\geq 1$ but is not a pole of $Y$ nor a zero of $Y$. Then the local coordinate is 
   \beq z_\alpha(q)=\exp\left(\frac{x(q)-x(o)}{n_{\alpha}}\right)=\left(\frac{X(q)}{X(o)}\right)^{\frac{1}{ n_\alpha}}\eeq
   because $\frac{dX}{X}$ has a simple pole with residue $n_\alpha\neq 0$. $y=\ln Y$ is regular at $\alpha$ so the local decomposition is
   \beq ydx(q)=t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q) 
    \eeq
    where $du_\alpha$ is holomorphic in a neighborhood of $\alpha$ including a neighborhood of the cut from $o$ to $\alpha$.
    \item If $\alpha$ is a pole of $Y$ of order $d_\alpha=-n_\alpha\geq 1$ or a zero of $Y$ of order $n_\alpha\geq 1$ but is not a pole of $X$ nor a zero of $X$. Then the local coordinate is  
    \beq z_\alpha(q)=\frac{x(q)-x(\alpha)}{x(o)-x(\alpha)}=\frac{\ln (X(q)) -\ln (X(\alpha))}{\ln (X(o)) -\ln (X(\alpha))}
    \eeq
    and the local decomposition is 
  \beq ydx(q)=s_\alpha  \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q) \eeq
  where $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured  neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$. 
  \item If $\alpha$ is a pole of $Y$ of order $r_\alpha=-m_\alpha\geq 1$ or a zero of $Y$ of order $m_\alpha\geq 1$ and also either a zero of $X$ of order $n_\alpha\geq 1$ or a pole of $X$ of order $k_\alpha=-n_\alpha\geq 1$. In that case, the local coordinate is
  \beq z_\alpha(q)=\exp\left(\frac{x(q)-x(o)}{n_{\alpha}}\right)=\left(\frac{X(q)}{X(o)}\right)^{\frac{1}{ n_\alpha}}\eeq
  since $\frac{dX}{X}$ has a simple pole with residue $m_\alpha\neq 0$. The local decomposition is    
\beq ydx(q)=s_\alpha \ln\left( \frac{z_\alpha(q)-1}{z_\alpha(q)}\right) \frac{dz_\alpha(q)}{z_\alpha(q)}+ du_\alpha(q)
\eeq
 where $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured  neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$.
\end{itemize}



\subsection{Coefficients of the local decomposition as integrals}
Let us first starts with a technical lemma:
\begin{lemma}[Logarithmic integrals]\label{LemmaLogIntegrals}Let $0<r<1$ and let $\mathcal{C}_r$ be the counterclockwise circle of radius $r$ centered at $0$ parametrized by $z_0=re^{i\theta}$ with $\theta\in [0,2\pi]$. Let $\td \ln z_0$ be the logarithm with a branch taken on the positive real axis and such that $\td{\ln}(t+i\epsilon)=\td{\ln}(t-i\epsilon)+2i\pi$ for any $t\in \mathbb{R}_+^*$. In other words: $\td{\ln}(z_0)=-\ln(-z_0)$ where $\ln$ stands for the usual logarithm with its usual branch on the negative real axis. We have for any $z\in \mathbb{Z}$:
\beq \frac{1}{2i\pi}\oint_{\mathcal{C}_r} z_0^k \,\td{\ln}\, z_0\, dz_0=\left\{
    \begin{array}{ll}
        -\frac{r^{k+1}}{k+1} & \mbox{if } k\neq -1 \\
        -\ln r & \mbox{if } k=-1
    \end{array}
\right.
\eeq    
\end{lemma}

\begin{proof}The proof is done in \autoref{AppendixTechnicalIntegrals}.
\end{proof}



Let us now define $\mathcal{C}_\alpha$ as the contour starting from $o$ above the log-cut connecting $o$ to $\alpha$ and then circling around $\alpha$ counterclockwise and ending at $o$ below the log-cut connecting $o$ to $\alpha$. This definition implicitly assume that the contour only circles the log-cut connecting $o$ to $\alpha$ and $\alpha$ without  circling any other singular point or crossing holonomy cycles. Moreover, it is taken in a immediate neighborhood of the cut and $\alpha$ where the coordinate $z_\alpha$ is well-defined.
This contour can be split into two parts:
\begin{itemize}
    \item Let $q_\alpha$ be a point on the log-cut connecting $o$ to $\alpha$ such that $z_\alpha(q_\alpha):=r_\alpha$ satisfies $|r_\alpha|<1$ in the $z_\alpha$-plane. Then, the first part of the contour corresponds to the discontinuity across the log-cut from $o$ to $q_\alpha$.
    \item The second part corresponds to a circle integral starting at $q_\alpha$ and circling once around $\alpha$ counterclockwise and ending at $q_\alpha$. 
\end{itemize}

\textcolor{blue}{Insert a picture}


We may use \autoref{LemmaLogIntegrals} to obtain the coefficients of the singular part of $ydx$ at $\alpha$. Indeed, let us consider  for any $k\in \mathbb{N}$: \beq I_{\alpha,k}:=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha} z_\alpha(q)^k ydx\eeq
Following the previous decomposition of $\mathcal{C}_\alpha$, the discontinuity across the log-cut can be evaluated  from \autoref{PropLocalCoord}.

\begin{proposition}[Local coefficients as integrals]\label{PropCoeffIntegrals} For any singular point $\alpha$ of $ydx$, coefficients of \autoref{PropLocalCoord} are given by:
\beq \forall \, k\in \mathbb{N}\,:\, I_{\alpha,k}=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha}z_\alpha(q)^kydx= -k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+\frac{s_\alpha}{k-d_\alpha} \delta_{k\neq d_\alpha}.\eeq
where $d_\alpha$, local coordinates $z_\alpha$ and the coefficients $(t_{\alpha,k})_{k\geq 1}$ and $s_\alpha$ are defined from \autoref{DefLocalCoord} and \autoref{PropLocalCoord}. 
\end{proposition}

\begin{proof}The discontinuity (from above to below the cut) of $ydx$ is $-2i\pi s_\alpha z_\alpha^{-d_\alpha-1} dz_\alpha$. Thus the first contribution of $I_{\alpha,k}$ is 
\beq -s_\alpha\int_{\text{Cut } o\to q_\alpha} z_\alpha(q)^{k-d_\alpha-1} dz_\alpha(q)=-s_\alpha\int_{1}^{r_\alpha} z_\alpha^{k-d_\alpha-1} dz_\alpha
= \left\{
    \begin{array}{ll}
        s_\alpha\frac{1-r_\alpha^{k-d_\alpha}}{k-d_\alpha} & \mbox{if } k\neq d_\alpha\\
        -s_\alpha\ln r & \mbox{ if } k=d_\alpha
    \end{array}
\right.
\eeq
The second contribution of $I_{\alpha,k}$ corresponds to the circle integral which is given by \autoref{LemmaLogIntegrals}. For any $k\in \mathbb{N}$:
\bea \oint_{\mathcal{C}_{q_\alpha}} z_\alpha(q)^{k-d_\alpha-1} ydx&=&\oint_{\mathcal{C}_{q_\alpha}} \left(z_\alpha(q)^{k} ydx(q)-s_\alpha z_\alpha(q)^{k-d_\alpha-1} \ln (1-z_\alpha(q)^{-1}) \right)dz_\alpha(q) \cr&&+ s_\alpha\oint_{\mathcal{C}_{r_\alpha}} z_\alpha(q)^{k-d_\alpha-1} \ln (1-z_\alpha^{-1}) dz_\alpha\cr
&=& -k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+ \left\{
\begin{array}{ll}
        s_\alpha\frac{r_\alpha^{k-d_\alpha}}{k-d_\alpha}  & \mbox{if } k\neq d_\alpha\\
        s_\alpha\ln r & \mbox{ if } k=d_\alpha
    \end{array}
    \right.
\eea
Thus, we get that
\beq I_{\alpha,k}=\frac{1}{2i\pi}\oint_{\mathcal{C}_\alpha}z_\alpha(q)^kydx=-k\,t_{\alpha,k}\delta_{0<k\leq R_\alpha}+ t_{\alpha,0}\delta_{k=0}+\frac{s_\alpha}{k-d_\alpha} \delta_{k\neq d_\alpha}
\eeq
ending the proof.
\end{proof}

\autoref{PropCoeffIntegrals} is a general formula that can be used in all cases. However, as mentioned above, we may only face subcases of this formula depending on the situation. In particular we cannot have a non-trivial coefficient $s_\alpha$ with a non-trivial potential $V_\alpha$ or a non-trivial monodromy $t_{\alpha,0}$ so it is easy to invert the previous relation.

\begin{corollary}[Local coefficients as integrals]\label{CorollaryLocalCoeffsAsIntegrals}We have:
\begin{itemize}
    \item If $s_\alpha=0$, then $ydx$ and $z_\alpha$ are meromorphic in a neighborhood of $\alpha$ and thus 
    \bea \forall \,k>0\,:\,  t_{\alpha,k}&=&-\frac{I_{\alpha,k}}{k}=-\frac{1}{k} \Res_{q\to \alpha} z_\alpha(q)^k ydx(q)\cr
    t_{\alpha,0}&=&I_{\alpha,0}=\Res_{q\to \alpha} ydx(q).
    \eea
    \item If $s_\alpha\neq 0$, then all $t_{\alpha,k}$ are vanishing for $k\geq 0$. Thus we get
    \beq s_\alpha =(k-d_\alpha)I_{\alpha,k}\delta_{k\neq d_\alpha}\eeq
\end{itemize}
\end{corollary}


\subsection{Log forms and moduli space for $ydx$}
The next step is to rewrite $ydx$ using one-forms that are globally defined and that reproduces the singular behavior of $ydx$ at one of its singularities. From \autoref{PropDecompositionSingPointsydx}, we may study $\mathcal{S}_{\text{mero}}$ and $\mathcal{S}_{\text{log}}$ separately.

\subsubsection{One forms for $\mathcal{S}_{\text{mero}}$}
Let us consider $\alpha\in \mathcal{S}_{\text{mero}}$, then the local decomposition of $ydx$ at $\alpha$ only involves irregular times and monodromies and $ydx$ is locally meromorphic in a punctured neighborhood of $\alpha$. Following \cite{EO07}, we shall define the following one-form.

\begin{definition}[One-form for $\alpha\in \mathcal{S}_{\text{mero}}$]\label{DefOneFormSmero}Let $\alpha\in \mathcal{S}_{\text{mero}}$. From \autoref{PropLocalCoord}, the local expansion of $ydx$ is 
\beq ydx(q)=dV_\alpha(q) +t_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)} + du_\alpha(q)
\eeq
where the local potential is $V_\alpha(q)=\underset{k=1}{\overset{R_\alpha}{\sum}} t_{\alpha,k}z_\alpha(q)^{-k}$ and $du_\alpha(q)$ is holomorphic around $\alpha$. We define the one form $B_{\alpha,o'}(q)$ on $\Sigma$ by
\beq B_{\alpha,o'}(q):=\sum_{k=1}^{R_\alpha} t_{\alpha,k} B_{\alpha,k}(q) + t_{\alpha,0}\int_{o'}^\alpha B(.,q)\eeq
where $o'$ is a fixed basepoint and
\beq \forall \, k\in \llbracket 1,R_\alpha\rrbracket\,:\, B_{\alpha,k}(q):=-\Res_{s\to \alpha} B(q,s) z_\alpha(s)^{-k}\eeq
\end{definition}

The main interest of this definition is that $B_{\alpha,o'}$ is a meromorphic one form on $\Sigma$ with only poles at $\alpha$ and a simple pole at $o'$ such that
\beq \forall\, \alpha\in \mathcal{S}_{\text{mero}}: ydx(q)-B_{\alpha,o'}(q) \text{ is holomorphic around } \alpha\eeq

\subsubsection{One forms for $\mathcal{S}_{\text{log}}$}
Let us now adapt the definition in the case of a log-singularity.

\begin{definition}[One-form for $\alpha\in \mathcal{S}_{\text{log}}$]\label{DefOneFormSlog}Let $\alpha\in \mathcal{S}_{\text{log}}$. From \autoref{PropLocalCoord}, the local expansion of $ydx$ is 
\beq ydx(q)=s_\alpha z_\alpha(q)^{-d_\alpha-1} \ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)+ du_\alpha(q)
\eeq
 where $du_\alpha(q)$ stands for a one-form such that it is holomorphic in a $\alpha$-punctured  neighborhood of the log-cut connecting $\alpha$ to $o$ but excluding $o$.  We shall define
\bea B_{\alpha,o'}(q)&:=&-\oint_{s\in\mathcal{C}_{\alpha}} \left(\int_{o'}^s B(q,.)\right)ydx(s)\cr
&:=&-\frac{1}{2i\pi}\underset{s \in \mathcal{C}_{o\to q_\alpha}}{\text{Disc}} \left(\int_{o'}^s B(q,.)\right)ydx(s) -\oint_{s\in\mathcal{C}_{\alpha, q_\alpha}} \left(\int_{o'}^s B(q,.)\right)ydx(s)\cr
&=& -\int_o^{q_\alpha} \left(\int_{o'}^s B(q,.)\right)ds -s_\alpha \oint_{s\in\mathcal{C}_{\alpha, q_\alpha}} \left(\int_{o'}^s B(q,.)\right)z_\alpha(s)^{-d_\alpha-1}\ln \frac{z_\alpha(s)-1}{z_\alpha(s)} dz_\alpha(s) \cr
&=& -\int_o^{q_\alpha} \left(\int_{o'}^s B(q,.)\right)ds +s_\alpha \oint_{s\in\mathcal{C}_{\alpha, q_\alpha}} \left(\int_{o'}^s B(q,.)\right)z_\alpha(s)^{-d_\alpha-1}\ln z_\alpha(s) dz_\alpha(s) \cr
\eea
\end{definition}

\textcolor{red}{\begin{remark}Note that if we change the basepoint $o'$ in the previous definition, it simply adds a term $\left(\int_{o'}^{o''}B(q,.)\right)\oint_{s\in\mathcal{C}_{\alpha}} z_\alpha(d)^{-d_\alpha-1}\ln \frac{z_\alpha(d)-1}{z_\alpha(d)} dz_\alpha(d)=0$ so that the definition of $B_\alpha(q)$ does not depend on the choice of basepoint $o'$.
\end{remark}}

\textcolor{red}{What are the properties of $B_{\alpha,o'}(q)$?}



\subsubsection{Decomposition of $ydx$ using the Bergmann kernel}
Let us now rewrite the singular part of $ydx$ at each pole using the Bergmann kernel. We define
\bea B_{\alpha}(p)&:=& \oint_{q\in\mathcal{C}_{\alpha}} B(p,q)\left( \int_{o'}^qz_\alpha(s)^{-d_\alpha-1}\ln \frac{z_\alpha(s)-1}{z_\alpha(s)} dz_\alpha(s)\right)\cr
&=&-\oint_{q\in\mathcal{C}_{\alpha}} \left(\int_{o'}^qB(p,.)\right)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)\eea
Using the notation of \cite{EO07}:
\beq dS_{q_1,q_2}(p):=\int_{q_1}^{q_2} B(p,.)\eeq
it is equivalent to
\beq B_{\alpha}(p)=-\oint_{q\in\mathcal{C}_{\alpha}} dS_{o',q}(p)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)\eeq
If we change the basepoint $o'$, it adds a term $\left(\int_{o'}^{o''}B(p,.)\right)\oint_{q\in\mathcal{C}_{\alpha}} z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q)=0$ so that the definition of $B_\alpha(p)$ does not depend on the choice of basepoint $o'$.

Let us now analyze the properties of the one form $B_\alpha(p)$. First it is normalized on the $\mathcal{A}$-cycles similarly to the Bergmann kernel (because the contour $\mathcal{C}_\alpha$ is disjoint from the holonomy cycles). Then, it is holomorphic except when $p$ belongs to $\mathcal{C}_\alpha$. Indeed, $dS_{o',q}(p)$ has a simple pole when $q$ is closed to $p$: $dS_{o',q}(p)=\frac{dp dq}{p-q} +O(1)$. This provides a jump contribution which is given by $z_\alpha(p)^{-d_\alpha-1}\ln \frac{z_\alpha(p)-1}{z_\alpha(p)} dz_\alpha(p)$. In the end, we have

\begin{proposition}[Log-forms]\label{PropLogForms}Let $\alpha$ be a singular point of $ydx$. The one-form
\beq B_\alpha(p):=-\oint_{q\in\mathcal{C}_{\alpha}} \left(\int_{o'}^qB(p,.)\right)z_\alpha(q)^{-d_\alpha-1}\ln \frac{z_\alpha(q)-1}{z_\alpha(q)} dz_\alpha(q) \eeq
has the following properties:
\begin{itemize}
    \item It is holomorphic except on the contour $\mathcal{C}_\alpha$.
    \item On the contour $\mathcal{C}_\alpha$ it has a jump given by
    $z_\alpha(p)^{-d_\alpha-1}\ln \frac{z_\alpha(p)-1}{z_\alpha(p)} dz_\alpha(p)$ for all $p\in \mathcal{C}_\alpha$.
    \item It is normalized on the $\mathcal{A}$-cycles:
    \beq \oint_{\mathcal{A}_i} B_\alpha(p) =0 \,\,,\,\, \forall\,i\in \llbracket 1,g \rrbracket.\eeq
\end{itemize}
\end{proposition}

The one-form $B_\alpha$ encodes the logarithmic singularities at $\alpha$ of $ydx$. Using \autoref{PropLocalCoord} we get the following theorem.

\begin{theorem}[Decomposition of $ydx$]\label{TheoydxDecomposition}The one-form $ydx$ can be rewritten as
\beq ydx(p)= \sum_{\alpha} s_\alpha B_\alpha(p)+ \sum_{\alpha,k\geq 1} t_{\alpha,k} B_{\alpha,k}(p) +\sum_{\alpha} t_{\alpha,0}\int_{o'}^\alpha B(.,p) +\sum_{i=1}^g \epsilon_i du_i(p)  \eeq
where 
\beq \forall \, k\geq 1\,:\, B_{\alpha,k}(p):=-\Res_{q\to \alpha} B(p,q) z_\alpha(q)^{-k}\eeq
\end{theorem}
\begin{proof}The one-form
\beq ydx(p)- \left(\sum_{\alpha} s_\alpha B_\alpha(p)+ \sum_{\alpha,k\geq 1} t_{\alpha,k} B_{\alpha,k}(p) +\sum_{\alpha} t_{\alpha,0}\int_{o'}^\alpha B(.,p)\right)\eeq
 is regular at each pole $\alpha$ and has no jumps across each of the log-cuts. Therefore it is holomorphic on $\Sigma$. Moreover, its integral on $\mathcal{A}_i$ is $\epsilon_i$ and thus it is necessarily $\underset{i=1}{\overset{g}{\sum}} \epsilon_i du_i$.   
\end{proof}

%However, as mentioned above, we may only face subcases of this formula depending on the situation. In particular we cannot have a non-trivial coefficient $s_\alpha$ with a non-trivial potential $V_\alpha$ or a non-trivial monodromy $t_{\alpha,0}$ so it is easy to invert the previous relation.

%\begin{corollary}[Local coefficients as integrals]\label{CorollaryLocalCoeffsAsIntegrals}We have:
%\begin{itemize}
%    \item If $s_\alpha=0$, then $ydx$ and $z_\alpha$ are meromorphic in a neighborhood of $\alpha$ and thus 
%    \bea \forall \,k>0\,:\,  t_{\alpha,k}&=&-\frac{I_{\alpha,k}}{k}=-\frac{1}{k} \Res_{q\to \alpha} z_\alpha(q)^k ydx(q)\cr
%    t_{\alpha,0}&=&I_{\alpha,0}=\Res_{q\to \alpha} ydx(q).
%    \eea
%    \item If $s_\alpha\neq 0$, then all $t_{\alpha,k}$ are vanishing for $k\geq 0$. Thus we get
%    \beq s_\alpha =(k-d_\alpha)I_{\alpha,k}\delta_{k\neq d_\alpha}\eeq
%\end{itemize}
%\end{corollary}



%\textcolor{blue}{Do we have 
%\beq \Res_{z\to a_r} \,B(z,z_1)\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}\right)=-\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_r}?
\eeq
%for all $h\geq 1$? It is correct for $h=1$ but then I do not know. I think it is correct by integration by part.
%}

%\textcolor{green}{
%\begin{align*}
%    &\Res_{z\to a_r} \,B(z,z_1)\left(\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}\right)\\
%=&-\Res_{z\to a_r} \,d_z\frac{\omega_{0,2}(z,z_1)}{dx(z)}\left(\frac{\partial^{2h-2}}{\partial x(z)^{2h-1}}\frac{1}{z-a_r}\right)\\
%=&(-1)^{2h-1}\Res_{z\to a_r} \,dx(z)\frac{\partial^{2h-1}}{\partial x(z)^{2h-1}}\frac{\omega_{0,2}(z,z_1)}{dx(z)}\frac{1}{z-a_r}\\
%=&(-1)^{2h-1}\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\omega_{0,2}(z_1,q)}{dx(q)}\right)_{|\, q=a_r}
%\end{align*} 
%Since we have meromorphic function we can integrate by parts locally $2h-1$ times (first dividing by $dx(z) $ then integrating wrt to $z$) and this $2h-1$ times). In the last step we just evaluate the residue, where the left term is regular at $z=a_r$ which gives the desired formula.
%}


\begin{proposition}[Local integration by parts]\label{PropLocalIntegrationParts} Let $\omega_1$ and $\omega_2$ be two meromorphic one-form on $\Sigma$. Let $\beta$ be a point in $\Sigma$ and $o$ a basepoint in $\Sigma$ (i.e. a point where $\omega_1$ and $\omega_2$ are regular). Assume that $\omega_2$ is regular at $\beta$ then
\beq \Res_{q\to \beta} \left(\int_o^q \omega_1\right)\omega_2(q)= -\Res_{q\to \beta} \left(\int_\beta^q \omega_2\right)\omega_1(q) +\omega_2(\beta) \Res_{q\to\beta} \omega_1 \eeq
or equivalently
\beq \Res_{q\to \beta} \left(\int_o^q \omega_1\right)\omega_2(q)= -\Res_{q\to \beta} \left(\int_o^q \omega_2\right)\omega_1(q)  + \left(\omega_2(\beta) +\int_o^{\beta} \omega_2\right) \Res_{q\to\beta} \omega_1 \eeq
\end{proposition}
Note in particular $\omega_1$ may have a pole at $\beta$ with non-vanishing residue in the previous proposition

\begin{proof}The statement is purely local, hence we may write a local expansion around $\beta$:
\beq \omega_1(q)\overset{q\to\beta}{=}\sum_{k=-R_1}^{\infty} \alpha_k (q-\beta)^k dq \,\,,\,\, \omega_2(q)\overset{q\to\beta}{=}\sum_{j=0}^{\infty} \gamma_k (q-\beta)^k dq\eeq
where $\alpha_{-1}=\underset{q\to \beta}{\Res}\, \omega_1$ and $\gamma_0=\omega_2(\beta)$. Then
\bea \int_o^q \omega_1&\overset{q\to \beta}{=}& \sum_{k=-R_1,k\neq -1}^{\infty} \frac{\alpha_k}{k+1} (q-\beta)^{k+1} + \alpha_{-1}\ln(q-\beta) +A_0\cr
\int_{\beta}^q \omega_2&\overset{q\to \beta}{=}&\sum_{j=0}^{\infty} \frac{\gamma_j}{j+1} (q-\beta)^{j+1} 
\eea
From the fact that the residue is a local circle integral around $\beta$, we get that :
\beq  \forall\, j\in \mathbb{N}\,:\, \Res_{q\to \beta} (q-\beta)^j\ln(q-\beta) dq \overset{q=\beta + re^{i\theta}}{=}\frac{1}{2i\pi}\int_{-\pi}^{\pi} r^{j+1} e^{(j+1)\theta}(\ln r+i\theta)d\theta=\delta_{j,0}
\eeq
Thus we get:
\beq\Res_{q\to \beta} \left(\int_o^q \omega_1\right)\omega_2(q) =\sum_{k=-R_1}^{-2}\frac{\alpha_k}{k+1}\gamma_{-2-k}+ \alpha_{-1}\gamma_0  \eeq
while
\beq \Res_{q\to \beta}\left(\int_{\beta}^q \omega_2\right)\omega_1(q) =
\sum_{k=-R_1}^{-2} \alpha_k  \frac{\gamma_{-2-k}}{-1-k}
\eeq
ending the proof.
\end{proof}

Note that if both $\omega_1$ and $\omega_2$ have poles at $\beta$ with non-vanishing residues, it is unclear how to generalize this identity.

\textcolor{red}{Olivier: This proposition should be checked. Moreover, in the file, we should check at each step that I did not forget th extra term is $\omega_1$ has non-vanishing residues.}


\begin{proof}
Take the right hand side of the equation and compute
    \begin{align*}
        &\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) \partial_z\left(\frac{x(z)-x(a_r)}{dx(z)}\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\right)_{|z=q}\\
        =&\Res_{q\to a_r}dx(a_r)\omega_{h_1,1}(q) \frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}\\
        &+\Res_{q\to a_r}dx(a_r)(x(q)-x(a_r))\omega_{h_1,1}(q) \partial_{x(q)}\left(\frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}\right)\\
        =&\Res_{q\to a_r}dx(a_r)\omega_{h_1,1}(q) \frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}\\
        &-\Res_{q\to a_r}dx(a_r)\left(\frac{\partial}{\partial x(q)}(x(q)-x(a_r))\omega_{h_1,1}(q) \right)\frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}.
    \end{align*}
    Now applying  \autoref{LemmaRegularityComb} where we recognize in \autoref{LemmaRegularityComb} the singular part of $\omega_{h_1,1}(z)$ which is the only necessary part of $\omega_{h_1,1}$ needed in the last equation to compute the residue (because $\frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}$ is regular at $q=a_r$) we get that
\bea &&\Res_{q\to a_r}\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) \partial_z\left(\frac{x(z)-x(a_r)}{dx(z)}\omega_{h-h_1,k+1} (z,z_1,\dots,z_k)\right)_{|z=q}\cr
&&=\Res_{q\to a_r}dx(a_r)\omega_{h_1,1}(q) \frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}+(2h_1-1) \Res_{q\to a_r}dx(a_r)\omega_{h_1,1}(q)    \frac{\omega_{h-h_1,k+1} (q,z_1,\dots,z_k)}{dx(q)}\cr
&&= 2h_1 \Res_{q\to a_r}dx(a_r)\frac{dx(a_r)}{dx(q)}\omega_{h_1,1}(q) \omega_{h-h_1,k+1} (q,z_1,\dots,z_k)
\eea
\end{proof}




\section{Variations of the free energies with respect to the position of logTR vital singularities}
\begin{lemma}\label{Lem:trick2}
    Let $\omega(q)$ be a smooth 1-form at $a$ and $x(q)$ a smooth function at $a$.
    We have the following relations (for any $k\in \mathbb{N}$):
    \begin{align}
        &dx(a)\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^k \log(q-a)\\\nonumber
        =&-\Res_{q\to a} \left(\int^q_oF(q)\right)dx(q)\left(\frac{\partial}{\partial x(q)}\right)^k \frac{1}{q-a}\\\nonumber
        =&\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^{k-1} \frac{1}{q-a}
    \end{align}
    and 
    \begin{align}
        \Res_{q\to a} (x(q)-x(a))F(q)\left(\frac{\partial}{\partial x(q)}\right)^k \frac{1}{q-a}=-k\Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^{k-1} \frac{1}{q-a}.
    \end{align}
    \begin{proof}
        The first relation follows from the fact $dx(a)\frac{\partial}{\partial x(q)}\log(q-a)-\frac{1}{q-a}$ is regular at $q\to a$. Acting on this with $k-1$ derivative wrt $x(q)$ and multiplying it with $F(q)$ gives a 1-form which is regular at $q\to a$ and has therefore a vanishing residue:
        \begin{align*}
            \Res_{q\to a} F(q)\frac{\partial^{k-1}}{\partial x(q)^{k-1}}\left(dx(a)\frac{\partial}{\partial x(q)}\log(q-a)-\frac{1}{q-a}\right)=0.
        \end{align*}
        This is equivalent to the first and third line of the first equation. The second line is achieved by integration by parts of the third line.

        The second equation comes from the fact that $\frac{x(q)-x(a)}{q-a}$ is regular at $q\to a$. Acting with $k$ derivatives wrt $x(q)$ on it and multiplying with $F(q)$ gives a regular 1-form at $q\to a$, thus vanishing residue.
        \begin{align*}
            \Res_{q\to a} F(q)\left(\frac{\partial}{\partial x(q)}\right)^k\frac{x(q)-x(a)}{q-a}=0,
        \end{align*}
        where one can perform the $x(q)$ derivative $\left(\frac{\partial}{\partial x(q)}\right)^k\frac{x(q)-x(a)}{q-a}=(x(q)-x(a))\left(\frac{\partial}{\partial x(q)}\right)^k\frac{1}{q-a}+k\left(\frac{\partial}{\partial x(q)}\right)^{k-1}\frac{1}{q-a}$. After inserting this, one finds the desired formula.
    \end{proof}
\end{lemma}
\textcolor{blue}{Could you reformulate this lemma using the omega as you used it for \autoref{ReformulationVar}. }



By definition, we have
\bea (2-2h)\omega_{h,0}&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,1}(z)
\cr&&
-\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\left(\frac{1}{2}
        \overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1}(z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right)\cr&&
\eea
where $\Phi(z)=\int_o^z ydx$. Since $x$ is not varied and $d_{a_r}[ydx(z)]=y_{a_r}dS_{o,z}(a_r) dx(z) $, we get that
\bea (2-2h)d_{a_r}[\omega_{h,0}]&=&(A)+(B)+(C)+ (D)+ (E)+ (F)\text{ with}\cr
(A)&:=&y_{a_r}\sum_{i=1}^N\Res_{z\to p_i} \left(\int_{s=o}^{s=z} dS_{o,s}(a_r) dx(s)\right)\omega_{h,1}(z)\cr 
(B)&:=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)d_{a_r}[\omega_{h,1}(z)]\cr
(C)&:=&dx(a_r)\Res_{z\to a_r} \left(\frac{1}{2}\overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right)\cr
(D)&:=&-\frac{1}{2}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)\left(\overset{h-1}{\underset{h_1=1}{\sum}}\frac{d_{a_r}[\omega_{h_1,1} (z)]\omega_{h-h_1,1}(z) +\omega_{h_1,1} (z)d_{a_r}[\omega_{h-h_1,1}(z)]}{dx(z)}\right)\cr
(E)&:=&y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)B(z,a_r)\int_o^z\omega_{h,1} \cr
(F)&:=& \sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z)\int_o^zd_{a_r}[\omega_{h,1}]
\eea
From \autoref{TheoVariationsLogTRpoles} we have:
\bea d_{a_r}[\omega_{h,1}(z)]%= 
&=& y_{a_r}\sum_{i=1}^N \Res_{q\to p_i} \left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \omega_{h,2}(z,q)\cr
&&+ da_r\sum_{k=1}^h \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\cr
&=& y_{a_r}\sum_{i=1}^N \Res_{q\to p_i} \left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \omega_{h,2}(z,q)\cr
&&+da_r\sum_{k=1}^h \Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea
Note that $d_{a_r}[\omega_{h,1}(z)]$ has only pole at the ramification points and at $z=a_r$ but not at the other logTR vital singularities. Thus we get:
\bea (F)&=&(F_1)+(F_2) \text{ with }\cr
(F_1)&:=&y_{a_r}\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\sum_{i=1}^N \Res_{q\to p_i} \left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \int_{o}^{z}\omega_{h,2}(.,q)\cr
(F_2)&:=&da_r\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)\sum_{k=1}^h \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\int_o^z\omega_{h-k,2}(.,q)}{dx(q)} \right)_{|\, q=a_r}\cr
&=&da_r\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z) \sum_{k=1}^h  dx(q)\left(\int_{v=o}^{v=z}\int_{u=o}^{u=q} \omega_{h-k,2}(u,v)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea
Since the ramification points are away from $a_r$, we can swap the residues in $(F_1)$. But since $x(z)-x(a_r)$ has a simple zero, $dy(z)$ has a simple pole at $z=a_r$ and $\omega_{h,2}(z,q)$ is regular at $z=a_r$, we get that the integrand is regular at $z=a_r$ so that the residue is vanishing: $(F_1)=0$. A similar argument holds for $(F_2)$: $\big(x(z)-x(a_r)\big)dy(z)$ is regular at $z=a_r$ and for $h-k\neq 0$, $\omega_{h-k,2}(z,a_r)$ is regular at $z=a_r$ and $dx(a_r)\neq 0$. Thus the integrand is regular at $z=a_r$ and hence the residue is vanishing. Thus, we get from \eqref{ResidueExchange}:
\bea (F)&=&da_r\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z) \Res_{q\to a_r} dx(q)\left(\int_{v=o}^{v=z}\int_{u=o}^{u=q} \omega_{0,2}(u,v)\right)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr
&=&da_r\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z) \left([\hbar^{2h}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\int_o^z\omega_{0,2}(.,q)}{dx(q)} \right)_{|\, q=a_r}\cr&&
\eea

%Note that for $k=h$, we involve the Bergmann kernel and its derivative evaluated at $(z,a_r)$ that provides poles at $z=a_r$ so that the residue is a priori non-vanishing. In the end, we get:
%\beq (F)=\Res_{z\to a_r}\big(x(z)-x(a_r)\big)dy(z)da_r \left([\hbar^{2h}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\int_o^z\omega_{0,2}(.,q)}{dx(q)} \right)_{|\, q=a_r}\eeq
Let us now deal with $(B)$:
\bea (B)&:=&(B_1)+(B_2) \text{ with }\cr
(B_1)&:=&y_{a_r}\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right) \omega_{h,2}(z,q)\cr
(B_2)&:=&da_r\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{k=1}^h \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\cr
&=&da_r\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{k=1}^h \Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea
For $k=h$, we get that the integrand is regular at $z=p_i$ and hence: 
\bea (B_2)&=&da_r\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{k=1}^{h-1} \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\cr
&=&da_r\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{k=1}^{h-1} \Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea
In $(B_1)$ we swap the residue using \eqref{ResidueExchange}:
\bea (B_1)&=&y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right)\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)  \omega_{h,2}(z,q)\cr
&&-y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j}dS_{o,s}(a_r)dx(s)\right) \Res_{z\to q,\sigma_j(q)} \Phi(z)  \omega_{h,2}(z,q)\cr&&
\eea 
Since $h\geq 2$, $\omega_{h,2}(z,q)$ is regular at $z=q$ so that the last term is vanishing. Thus, we get:
\beq (B_1)=y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right)\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)  \omega_{h,2}(z,q)\eeq
Let us now deal with $(D)$ that immediately simplifies into (perform $h_1\to h-h_1$ in one of the sum):
\beq (D)=-\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}d_{a_r}[\omega_{h_1,1} (z)]\omega_{h-h_1,1}(z)\eeq
Inserting the expression of $d_{a_r}[\omega_{h_1,1}(z)]$ for $h_1\geq 1$, we find:
\small{\bea (D)&:=&(D_1) +(D_2)\text{ with}\cr
(D_1)&:=&- y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\sum_{i=1}^N \Res_{q\to p_i}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \omega_{h_1,2}(z,q)\omega_{h-h_1,1}(z)\cr
(D_2)&:=&-da_r\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\sum_{k=1}^{h_1} \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_1-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\omega_{h-h_1,1}(z)
\cr
&=&-da_r\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\sum_{k=1}^{h_1} \omega_{h-h_1,1}(z)\Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h_1-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea}
\normalsize{Let us} now write the dilaton equation for $\omega_{h,1}(z_1)$ from \autoref{TheoremDilatonEquation}:
\beq \label{DilatonReduced} -(2h-1)\omega_{h,1}(z_1)=\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h,2}(z,z_1) -\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-h_1,2} (z,z_1) \eeq
Thus we get that (being careful that the case $h_1=h$ in \eqref{DilatonReduced} is not included in $(B_1)+(D_1)$):
\bea (B_1)+(D_1)&=&y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right) \Big[\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)  \omega_{h,2}(z,q)  \cr
&&-\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\left(\int^{s=q}_{s=p_i} dS_{o,s}(a_r)dx(s)\right) \omega_{h_1,2}(z,q)\omega_{h-h_1,1}(z) \Big]\cr
&=&-(2h-1)y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right) \omega_{h,1}(q)\cr
&&+y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right)\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\omega_{h,1} (z)\omega_{0,2} (z,q)\cr&&
\eea
In the last term, we may swap the residue that are located at different points and the residue at $q=p_j$ is vanishing because all the terms in the integrand are regular at $q=p_j$. Thus, we get:
\beq (B_1)+(D_1)=-(2h-1)y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right) \omega_{h,1}(q) \eeq
Combining with $(A)$, we get
\beq \label{FirstPartTheorem} (A)+(B_1)+(D_1)= (2-2h)y_{a_r}\sum_{j=1}^N \Res_{q\to p_j} \left(\int^{s=q}_{s=p_j} dS_{o,s}(a_r)dx(s)\right) \omega_{h,1}(q)\eeq
This provides the first part of the theorem. We are left with $(B_2)$, $(C)$, $(D_2)$, $(E)$ and $(F)$ that are given by
\small{\bea (B_2)&=&da_r\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{k=1}^{h-1} \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\cr
(B_2)&=&da_r\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\sum_{k=1}^{h-1} \Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr
(C)&=&dx(a_r)\Res_{z\to a_r} \left(\frac{1}{2}\overset{h-1}{\underset{h_1=1}{\sum}}\frac{\omega_{h_1,1} (z)\omega_{h-h_1,1} (z) }{dx(z)} -dy(z)\int_o^z\omega_{h,1}\right)\cr
(D_2)&=&-da_r\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\sum_{k=1}^{h_1} \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_1-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\omega_{h-h_1,1}(z)
\cr
(D_2)&=&-da_r\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\overset{h-1}{\underset{h_1=1}{\sum}}\sum_{k=1}^{h_1} \omega_{h-h_1,1}(z)\Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h_1-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr
(E)&=&y_{a_r}\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)B(z,a_r)\int_o^z\omega_{h,1} \cr
(F)&=&da_r\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z) \left([\hbar^{2h}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2h-1}}{\partial x(q)^{2h-1}}\frac{\int_o^z\omega_{0,2}(.,q)}{dx(q)} \right)_{|\, q=a_r}\cr
(F)&=&da_r\sum_{j=1}^M\Res_{z\to a_j}\big(x(z)-x(a_j)\big)dy(z) \Res_{q\to a_r} dx(q)\left(\int_{v=o}^{v=z}\int_{u=o}^{u=q} \omega_{0,2}(u,v)\right)[\hbar^{2h}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea}
\normalsize{We} can transform the double sum in $(D_2)$ to get:
\small{\bea (D_2)&=&-da_r\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{k=1}^{h-1}\sum_{h_1=k}^{h-1} \left([\hbar^{2k}]\frac{y_{a_r}}{\mathcal{S}\left(y_{a_r}^{-1}\hbar\right)}\right)\left(dx(q)\frac{\partial^{2k-1}}{\partial x(q)^{2k-1}}\frac{\omega_{h_1-k,2}(z,q)}{dx(q)} \right)_{|\, q=a_r}\omega_{h-h_1,1}(z)\cr
&=&-da_r\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{k=1}^{h-1}\sum_{h_1=k}^{h-1} \omega_{h-h_1,1}(z)\Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h_1-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea}
\normalsize{We} need to swap the residues in $(B_2)$ and $(D_2)$. This can be done for $(B_2)$ but for $(D_2)$, it provides an additional term. This term is non-zero when $h_1-k=0$ because of the Bergmann kernel. From \eqref{ResidueExchange}, we get:
\small{\bea (D_2)&=&-da_r\Res_{q\to a_r}\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{k=1}^{h-1}\sum_{h_1=k}^{h-1} \omega_{h-h_1,1}(z) dx(q)\left(\int_o^q \omega_{h_1-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
-da_r\Res_{q\to a_r}\Res_{z\to q}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{k=1}^{h-1} \omega_{h-k,1}(z) dx(q)\left(\int_o^q \omega_{0,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr
&=&-da_r\Res_{q\to a_r}\sum_{j=1}^M\Res_{z\to a_j}\frac{\big(x(z)-x(a_j)\big)}{dx(z)}\sum_{k=1}^{h-1}\sum_{h_1=k}^{h-1} \omega_{h-h_1,1}(z) dx(q)\left(\int_o^q \omega_{h_1-k,2}(.,z)\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
-da_r\Res_{q\to a_r}\frac{\big(x(q)-x(a_j)\big)}{dx(q)}\sum_{k=1}^{h-1} \omega_{h-k,1}(q) dx(q)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea
}


\normalsize{We} now use the dilaton equation \autoref{TheoremDilatonEquation} for $\omega_{h-k,2}$ with $h-k\geq 1$:
\small{\bea \label{Dilatwhk} (1-2h+2k)\omega_{h-k,1}(q)&=&\sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h-k,2}(z,q) -\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h-k}{\underset{h_1=1}{\sum}}\omega_{h_1,1} (z)\omega_{h-k-h_1,2} (z,q)\cr
&\overset{\td{h}_1=h-h_1}{=}& \sum_{i=1}^N\Res_{z\to p_i} \Phi(z)\omega_{h-k,2}(z,q) -\sum_{j=1}^M\Res_{z\to a_j}\frac{x(z)-x(a_j)}{dx(z)}\overset{h-1}{\underset{\td{h}_1=k}{\sum}}\omega_{h-\td{h}_1,1} (z)\omega_{\td{h}_1-k,2} (z,q)\cr&&
\eea}
\normalsize{Thus,} combining $(B_2)$ and $(D_2)$ provides
\bea \label{B2PlusD2} (B_2)+(D_2)
&=&da_r \sum_{k=1}^{h-1} (1-2h+2k)\Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h-k,1}\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
-da_r\Res_{q\to a_r}\sum_{k=1}^{h-1}\big(x(q)-x(a_j)\big) \omega_{h-k,1}(q)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
\eea

\textcolor{blue}{Up to the case $k=h$, this corresponds to the second part of the theorem but the factor in front is not good, we miss $(2-2h-(1-2h+2k)=1-2k$ times this term to complete the proof. This should come from the other terms? We should apply \autoref{LemmaRegularityComb} to $(F)$ and \autoref{LemmaIntW02Wg1} to something. }

We can try to rewrite:
\bea &&-da_r\Res_{q\to a_r}\sum_{k=1}^{h-1}\big(x(q)-x(a_j)\big) \omega_{h-k,1}(q)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\cr&&
=da_r\Res_{q\to a_r}\sum_{k=1}^{h-1} \left(\int_o^q\omega_{h-k,1}\right)[\hbar^{2k}] dq\partial_q\left[\big(x(q)-x(a_j)\big)\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\right]\cr&&
=da_r\Res_{q\to a_r}\sum_{k=1}^{h-1} \left(\int_o^q\omega_{h-k,1}\right)dx(q)[\hbar^{2k}] \partial_x\left[\big(x(q)-x(a_j)\big)\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}\right]\cr&&
\eea
\textcolor{blue}{Is there a way to generalize \autoref{LemmaIntW02Wg1} and get that it is equal to
\beq \sum_{k=1}^{h-1}(2k-1) \Res_{q\to a_r} dx(q)\left(\int_o^q \omega_{h-k,1}\right)[\hbar^{2k}]\left(\frac{y_{a_r}}{\mathcal{S}(y_{a_r}^{-1}\hbar \partial_x)}\right)\frac{1}{q-a_r}?\eeq 
}


\subsection{What is $\Omega_{a_r}(q)$?}
\textcolor{red}{What I do not like is the following. The global decomposition gives that for only logTR vital singularities:
\beq  ydx(q)=\sum_{a_s} y_{a_s}\ln \frac{E(q,a_s)}{E(q,o)} dx(q) + \td{y}dx(q)\eeq
Thus, 
\beq d_{a_r}[ydx(q)]= y_{a_r}\frac{d_{a_r}[E(q,a_r)]}{E(q,a_r)}dx(q)\eeq
Now, the definition of the prime form is given in \autoref{DefPrimeForm}: The prime form $E(p,q)$ associated to $\Sigma$ is the unique $\left(\frac{1}{2},\frac{1}{2}\right)$ form such that it has no pole and simple zeros on the diagonal $p=q$. In any local coordinates:
\beq E(p,q)=\frac{z(p)-z(q)}{\sqrt{dz(p)}\sqrt{dz(q)}}\eeq
It is related to the modified third kind differential by
\beq dS_{z_1,z_2}(q)=d_q\ln \frac{E(q,z_1)}{E(q,z_2)}= \frac{d_q[E(q,z_1)]}{E(q,z_1)} - \frac{d_q[E(q,z_2)]}{E(q,z_2)}\eeq
The prime form is antisymmetric $E(q,p)=-E(p,q)$ so
\beq d_{a_r}[ydx(q)]= y_{a_r}\frac{d_{a_r}[E(a_r,q)]}{E(a_r,q)}dx(q)= y_{a_r}d_{a_r}\ln (E(a_r,q)) dx(q) \eeq
but this is not the third kind differential. Technically, this is not a globally well defined differential because it has only one simple pole and nothing else. Fay identities provide:
\beq d_{p}\ln E(p,q)= \int_q^{p}B(.,p)= \frac{d\xi(p)}{\xi(p)-\xi(q)}- \sum_{i=1}^g du_i(p)\int_q^p du_i\eeq
so that
\beq d_{a_r}[ydx(q)]=y_{a_r}dx(q)\left(\frac{d\xi(a_r)}{\xi(a_r)-\xi(q)}+ \sum_{i=1}^g du_i(a_r)\int_{a_r}^{q} du_i\right)
\eeq
In genus $0$, there is no problem because the second part is not there and we recover $\frac{dp}{p-q}=dS_{\infty,q}(p)$ (and note that we do not have the choice of an arbitrary point $o$). But this is not the case in arbitrary genus.
}






The variation of $ydx$ with respect to a logTR-vital singularity at fixed $x$ is given by
\beq \forall\, s\in \llbracket1,M\rrbracket\,:\, \partial_{a_s}[ydx(q)]=y_{a_s}\partial_{a_s}\left[\ln \frac{E(q,a_s)}{E(q,o)} \right]dx(q)
\eeq
Let us now express the last term in terms of differential by studying its properties. By definition, $y_{a_s}\partial_{a_s}\left[\ln \frac{E(q,a_s)}{E(q,o)} \right]dx(q)$ is a meromorphic one form on $\Sigma$ (the logarithmic cut disappear). It has a simple pole at $q=a_s$ with residue $-y_{a_s}x'(a_s)$. It also has poles at the poles of $dx$

\subsubsection{Genus $0$ case}
Let us consider a genus $0$ case:
\beq x(z) \text{ rational, } \,\, y(z)=\sum_{i} y_{a_i} \ln\left(\frac{z-a_i}{z-o}\right) +\td{y}(z) \,,\, \td{y} \text{ rational} \eeq
We assume for simplicity that $\td{y}$ does not depend on $a_i$ (otherwise the variations have already been covered). Moreover, we recall that we may only variate poles where $dx$ is regular. We have
\beq \partial_{a_i}[ydx(z)]=-y_{a_i} \frac{dx(z)}{z-a_i}=-y_{a_i}x'(z)\frac{dz}{z-a_i}=y_{a_i}x'(z)dS_{\infty,a_i}(z)=-y_{a_i}dx(z)\frac{dS_{\infty,z}(a_i)}{da_i}\eeq
where
\beq B(s,z)=\frac{1}{(z-s)^2} \,\,,\,\, dS_{a,b}(z)=\int_a^b B(s,z)=-\frac{dz}{z-b} +\frac{dz}{z-a}\eeq
so that 
\beq dS_{\infty,a_i}(z)=-\frac{dz}{z-a_i} \,\text{ and }\, dS_{\infty,z}(a_i)= -\frac{da_i}{a_i-z}=\frac{d a_i}{z-a_i}\eeq
Hence we have
\beq \Omega_{a_i}(q)= y_{a_i}x'(q)dS_{\infty,a_i}(q)=y_{a_i}dx(q)\frac{dS_{\infty,q}(a_i)}{da_i}\eeq
It is a meromorphic one-form with a simple pole at $q=a_i$ with residue $y_{a_i}x'(a_i)$ and poles at the poles of $dx$. Note that if $q=\infty$ is a regular point of $x$, there is no pole at infinity. Indeed, $x$ regular at infinity implies that $x(q)=x_{\infty,0}+x_{\infty,1}q^{-1}+ O(q^{-2})$ so that $x'(q)=- x_{\infty,1}\frac{1}{q^2}+O\left(q^{-3}\right)$ and thus $x'(q)dS_{\infty,a_i}(q)=O(q^{-3}dq)$.
Let us now observe that
\beq \Omega_{a_i}(z)=-\Res_{q\to z} \Omega_{a_i}(q)dS_{o,q}(z)\eeq
Note that the last identity is independent of the choice of $o$. We now use Riemann bilinear identity in genus $0$ for the meromorphic one form $\Omega_{a_i}(q)dS_{o,q}(z)$ in $q$. In genus $0$, it is equivalent to say that the sum of residues is vanishing. Thus we have
\beq  \Omega_{a_i}(z)=\Res_{q\to a_i}\Omega_{a_i}(q)dS_{o,q}(z)+ %\Res_{q\to \infty} \Omega_{a_i}(q)dS_{o,q}(z)
\sum_{\beta \text{ pole of } dx }\Res_{q\to \beta} \Omega_{a_i}(q)dS_{o,q}(z)\eeq
The first residue is just $y_{a_i}x'(a_i) dS_{o,a_i}(z)=y_{a_i}x'(a_i)\int_o^{a_i} B(s,z)$. For the other residues we have:
\beq \Res_{q\to \beta}\Omega_{a_i}(q)dS_{o,q}(z)=\Res_{q\to \beta}\Omega_{a_i}(q) \int_o^q B(s,z)= -\Res_{q\to \beta} B(q,z) \left(\int_o^q \Omega_{a_i}\right)\eeq
where  used the fact that the circle integral around $\beta$ of $\left(\int_o^q \Omega_{a_i}\right)\left(\int_o^q B(s,z)\right)dq$ is vanishing because it is a well defined function in a small neighborhood of $q=\beta$. 
Thus we get:
\beq \Omega_{a_i}(z)= y_{a_i}x'(a_i) \int_{[o,a_i]} B(s,z) - \sum_{\beta \text{ pole of } dx }\Res_{q\to \beta} B(q,z) \left(\int_o^q \Omega_{a_i}\right)\eeq
Thus we can write $\Omega_{a_i}$ using the Bergmann kernel with several parts: $\Lambda_{a_i,1}(q)= y_{a_i}x'(a_i)$ and $\partial_{a_i,1}=[o,a_i]$ and $\Lambda_{a_i,\beta}(q)=\frac{1}{2i\pi}\int_o^q \Omega_{a_i}$ and $\partial_{a_i,\beta}=\mathcal{C}_\beta$ a small loop around $\beta$, where $\beta$ is either a pole of $x$ or $\infty$. This enters into the general framework and we get\todo{I don't understand the formula, the first term still has a $q$. Do you want to have $a_i$ as upper integration limit or taking residue at $q=a_i$?}
\beq \delta_{a_i}[\omega_{n,g}(z_1,\dots,z_n)]= y_{a_i}x'(a_i)\int_o^q\omega_{g,n+1}(z_1,\dots,z_n,.) + \sum_{\beta \text{  pole of } dx} \Res_{q\to \beta} \left(\int_o^q \Omega_{a_i}\right)\omega_{g,n+1}(z_1,\dots,z_n,q)\eeq\todo{Is there a reason why the sign in front of the second term is different in (7-29) and (7-28)?}
To avoid the integral of $\Omega_{a_i}$, we may replace
\beq   \delta_{a_i}[\omega_{n,g}(z_1,\dots,z_n)]= y_{a_i}x'(a_i)\int_o^q\omega_{g,n+1}(z_1,\dots,z_n,.) - \sum_{\beta \text{  pole of } dx} \Res_{q\to \beta}  \Omega_{a_i}(q) \left(\int_o^q\omega_{g,n+1}(z_1,\dots,z_n,.)\right)\eeq
where the last integral is well-defined because the $\omega_{g,n+1}$ do not have residues at their poles.

\subsubsection{The arbitrary genus case}
The first difficulty in the arbitrary genus case is to compute $\partial_{a_i}[ydx(z)]$. In fact since $a_i$ is a point in $\Sigma$, it is more natural to consider the one-form $d_{a_i}[ydx]= \partial_{a_i}[ydx(z)] da_i$ which is independent of the coordinates chosen to express $a_i$. Since
\beq dy(z)=y_{a_i}dS_{o,a_i}(z)+\dots\eeq
we have 
\beq d_{a_i}[dy(z)]= y_{a_i}B(a_i,z)\eeq
Thus from $y(z)=\int_o^z dy$ (the lower bound correspond to fixing the logarithmic cut), we have
\beq d_{a_i}[y(z)]=y_{a_i}\int_o^z B(.,a_i)=y_{a_i}dS_{o,z}(a_i)\eeq
In the end:
\beq \Omega_{a_i}(z)da_i:= d_{a_i}[ydx(z)]=y_{a_i}dS_{o,z}(a_i) dx(z)\eeq
This gives that $\Omega_{a_i}(z)$ is a meromorphic one-form in $z$ with poles at $z=a_i$ (simple with residue $y_{a_i}x'(a_i)$) and poles at the poles of $dx$. But it is not clear if $dS_{o,z}(a_i)=\int_o^z B(.,a_i)$ may have other poles in $z$ \textcolor{blue}{(I would say ther are none because $B(z,a_i)$ has only one double pole without residue at $z=a_i$ so its anti-derivative is regular everywhere except at $z=a_i$.). In genus $0$, we get lucky, because we have
\beq dx(z)\frac{dS_{o,z}(a_i) }{da_i}=x'(z)\left(-\frac{dz}{a_i-z}+\frac{dz}{a_i-o}\right)\eeq
and it is obvious that the dependence in $z$ has no other pole.}

The next step is to write
\beq \Omega_{a_i}(z)=-\Res_{q\to z} \Omega_{a_i}(q)dS_{o,q}(z)\eeq
which is independent of $o$. We need to use Riemann bilinear identity with $\omega_1(q)= B(q,z)$ and $\omega_2(q)=\Omega_{a_i}(q)$ to go to the other poles of the integrand \eqref{CorollaryRiemannBilinearIdentity}: 
\bea \Omega_{a_i}(z)&=& \sum_{\beta \text{ poles of }\Omega_{a_i}} \Res_{q\to \beta} dS_{o,q}(z)\Omega_{a_i}(q) +\sum_{i=1}^g du_j(z) \oint_{\mathcal{A}_j} \Omega_{a_i}\cr
&=& \Res_{q\to a_i} dS_{o,q}(z)\Omega_{a_i}(q)+\sum_{\beta \text{ poles of }dx}\Res_{q\to \beta} dS_{o,q}(z)\Omega_{a_i}(q)+\sum_{j=1}^g du_i(z) \oint_{\mathcal{A}_j} \Omega_{a_i}\cr
&=& y_{a_i}x'(a_i)dS_{o,a_i}(z)+\sum_{\beta \text{ poles of }dx}\Res_{q\to \beta} dS_{o,q}(z)\Omega_{a_i}(q)+\sum_{j=1}^g du_j(z) \oint_{\mathcal{A}_j} \Omega_{a_i}\eea
We now use \autoref{PropLocalIntegrationParts} with $\omega_1(q)=\Omega_{a_i}(q)$ and $\omega_2(q)=B(q,z)$ which is regular at the poles of $dx$. We get
\bea \Omega_{a_i}(z)
&=& y_{a_i}x'(a_i)\int_{[o,a_i]}B(.,z)+\sum_{j=1}^g \frac{1}{2i\pi} \left(\oint_{\mathcal{A}_j} \Omega_{a_i}\right) \left(\oint_{B_j} B(.,z)\right)\cr
&&-\sum_{\beta \text{ poles of }dx}\Res_{q\to \beta}B(q,z)\left(\int_o^q\Omega_{a_i}\right)- \sum_{\beta \text{ poles of }dx}\left(\omega_2(\beta)+\int_o^\beta \omega_2\right) \Res_{q\to \beta} \Omega_{a_i}\cr
&=& y_{a_i}x'(a_i)\int_{[o,a_i]}B(.,z)+\sum_{j=1}^g \frac{1}{2i\pi} \left(\oint_{\mathcal{A}_j} \Omega_{a_i}\right) \left(\oint_{B_j} B(.,z)\right)\cr
&&-\sum_{\beta \text{ poles of }dx}\Res_{q\to \beta}B(q,z)\left(\int_o^q\Omega_{a_i}\right)- \sum_{\beta \text{ poles of }dx}\left(B(\beta,z)+dS_{o,\beta}(z) \right) \Res_{q\to \beta} \Omega_{a_i}\cr
&=& y_{a_i}x'(a_i)\int_{[o,a_i]}B(.,z)+\sum_{j=1}^g \frac{1}{2i\pi} \left(\oint_{\mathcal{A}_j} \Omega_{a_i}\right) \left(\oint_{B_j} B(.,z)\right)\cr
&&-\sum_{\beta \text{ poles of }dx}\Res_{q\to \beta}B(q,z)\left(\int_o^q\Omega_{a_i}\right)- \sum_{\beta \text{ poles of }dx}\left(B(q,z) \delta^{\text{Dirac}}_{\beta}(q)+\int_{q=o}^{q=\beta} B(q,z) \right) \Res_{s\to \beta} \Omega_{a_i}(s)\cr&&
\eea 
i.e. since $\Omega_{a_i}(q)da_i=y_{a_i}dS_{o,q}(a_i) dx(q) $:
\bea \Omega_{a_i}(z)da_i&=& y_{a_i}\Big[x'(a_i)\int_{[o,a_i]}B(.,z)-\sum_{\beta \text{ poles of }dx}\Res_{q\to \beta}B(q,z)\left(\int_{s=o}^{s=q}dS_{o,s}(a_i) dx(s)\right)\cr&&
+\sum_{j=1}^g \frac{1}{2i\pi} \left(\oint_{s\in\mathcal{A}_j} dS_{o,s}(a_i) dx(s)\right) \left(\oint_{B_j} B(.,z)\right)\cr
&& - \sum_{\beta \text{ poles of }dx}\left(B(q,z) \delta^{\text{Dirac}}_{\beta}(q)+\int_{q=o}^{q=\beta} B(q,z) \right) \Res_{s\to \beta} dS_{o,s}(a_i) dx(s)
\Big]\cr&&
\eea

In the end, we find four contributions but they can be expressed using the Bergmann kernel and thus we have 

\bea &&d_{a_i}[\omega_{0,n}(z_1,\dots,z_n)]=y_{a_i}\Big[dx(a_i)\int_o^{a_i} \omega_{0,n+1}(z_1,\dots,z_n,.) \cr&&
+ \frac{1}{2i\pi}\sum_{j=1}^g\left(\oint_{s\in\mathcal{A}_j} dS_{o,s}(a_i) dx(s)\right)\left(\oint_{B_j} \omega_{0,n+1}(z_1,\dots,z_n,.)\right)\cr&&
-\sum_{\beta \text{ poles of } dx} \Res_{q\to \beta} \left(\int_{s=o}^{s=q}dS_{o,s}(a_i) dx(s)\right)\omega_{0,n+1}(z_1,\dots,z_n,q)\cr&&
- \sum_{\beta \text{ poles of }dx}\left(\omega_{0,n+1}(z_1,\dots,z_n,\beta)+\int_{q=o}^{q=\beta} \omega_{0,n+1}(z_1,\dots,z_n,q) \right) \Res_{s\to \beta} dS_{o,s}(a_i) dx(s)\Big]\cr&&
\eea
or equivalently using \autoref{PropLocalIntegrationParts} for $\omega_2(q)=\omega_{0,n+1}(z_1,\dots,z_n,q)$ and $\omega_1(q)=\Omega_{a_i}(q)$:
\bea &&d_{a_i}[\omega_{0,n}(z_1,\dots,z_n)]= y_{a_i}\Big[dx(a_i)\int_o^{a_i} \omega_{0,n+1}(z_1,\dots,z_n,.) \cr&&
+ \frac{1}{2i\pi}\sum_{j=1}^g\left(\oint_{s\in\mathcal{A}_j} dS_{o,s}(a_i) dx(s)\right)\left(\oint_{B_j} \omega_{0,n+1}(z_1,\dots,z_n,.)\right)\Big]\cr&&
+\sum_{\beta \text{ poles of } dx} \Res_{q\to \beta} dS_{o,q}(a_i) dx(q)\left(\int_o^q\omega_{0,n+1}(z_1,\dots,z_n,.)\right)
\eea
with the last formula independent of the point $o$ chosen. Indeed, in the logTR procedure, the induction is the same as in TR for $h=0$. \textcolor{red}{For $\omega_{h,n}$ with $h\geq 1$ we have to be careful because in the former proof, I did not get any derivative of the $\ln(z-a_i)$ terms but only of the third kind differential. This will add terms in the formula.}

\textcolor{blue}{\subsubsection{Variations of the special logTR terms with respect to the position of logTR-vital singularities}}
We need to compute the variations with respect to $a_s$ of the special terms involving $\ln(z-a_s)$ in the logTR recursion (the variation of the $dS_{a_s,z}(z_1)$ term is already included in the current proof of the variational formula):
\beq A_h(z_1):=\Res_{z\to a_s}dS_{a_s,z}(z_1) dx(z)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}(\delta_{a_s})_{|x}[\ln(z-a_s)] \right)=?\eeq
and include them later in the proof of the variational formula by induction. Remember that variations are done at fixed $x$. We have $\partial_z= x'(z) \partial_x$.
\bea A_h(z_1))&=& -\Res_{z\to a_s}dS_{a_s,z}(z_1) dx(z)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}\frac{1}{z-a_s} \right)\cr
&=&-\Res_{z\to a_s}dS_{a_s,z}(z_1) dx(z)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}\partial_z[\ln(z-a_s)]\right)\cr
&=&-\Res_{z\to a_s}dS_{a_s,z}(z_1) dx(z)[\hbar^{2h}]\left(\frac{1}{\alpha_s\mathcal{S}(\alpha_s\hbar \partial_x)}x'(z)\partial_x[\ln(z-a_s)] \right)\cr&&
\eea




\subsection{Variations of $\omega_{0,0}$}
Recall that $\omega_{0,0}$ is defined by
Finally we define:
\beq \omega_{0,0}:=\frac{1}{2}\sum_{\alpha \in \mathcal{P}}\Res_{q\to \alpha}\td{V}_\alpha(q) \td{y}dx(q) +\frac{1}{2}\sum_{\alpha\in \mathcal{P}}\td{t}_{\alpha,0}\mu_{\alpha,0}+\frac{1}{4i\pi}\sum_{i=1}^g\td{\epsilon}_i\left(\oint_{\mathcal{B}_i}\td{y}dx\right)\label{definitionF0TR}
\eeq
where the potential at each pole of $\td{y}dx$ is defined in \autoref{PropLocalCoord} and we have defined:
\beq \forall \,\alpha\in \mathcal{P}\,:\, \mu_{\alpha,0}:=\int_{\alpha}^o \left(\td{y}dx(q) -d\td{V}_\alpha(q)-\td{t}_{\alpha,0}\frac{dz_\alpha(q)}{z_\alpha(q)}\right)
 +\td{V}_\alpha(o)-\td{t}_{\alpha,0} \ln z_\alpha(o)
\eeq
For a logTR vital singularity $a_r$, there are no associated irregular times nor monodromies ($x$ is regular at $a_r$ and $a_r$ is a simple pole of $dy$).Thus $\omega_{0,0}$ is independent of $a_r$:
\beq \forall \, r\in \llbracket 1,M\rrbracket\,:\, d_{a_r}[\omega_{0,0}]=0\eeq

So we need to add something, which behaves under deformation as 
\bea \label{RHSF0Proof}&&\Res_{z\to \{p_i\}\cup \{a_j\}} d_{a_r}[\Phi(z)]\omega_{0,1}(z) +{\color{red}2}\frac{1}{2}\Res_{z\to a_r}dx(a_r)y(z)\omega_{0,1} (z),
\eea
if it makes sense. There is no residue at the ramification points $p_i$. For the residue at $a_j\neq a_r$, one can integrate $d_{a_r}[\Phi(z)]dx(z)$ once more and take the derivative of $y(z)$ (integration by parts). This, however, yields also a constant term 
\bea &&\Res_{z\to a_j\neq a_t} d_{a_r}[\Phi(z)]\omega_{0,1}(z) \cr
&=&-\Res_{z\to a_j\neq a_r} \int^{t=z} d_{a_r}[\Phi(t)]dx(t) dy(z)\cr
&=&-y_{a_j} \int^{t=a_j} d_{a_r}[\Phi(t)]dx(t) +C(a_r,o).
\eea
Here, $C(a_r,o)$ comes from the lower bound $o$ of the integration. The constant depends on $a_r$. 

For the residue at $z\to a_r$, we have to take into account that $d_{a_r}[\Phi(z)]+dx(a_r)y(z)$ is regular at $z=a_r$. With the same consideration as above we find
\bea &&\Res_{z\to a_t} (d_{a_r}[\Phi(z)]+dx(a_r)y(z))\omega_{0,1}(z) \cr
&=&-\Res_{z\to  a_r}  \int^{t=z}(d_{a_r}[\Phi(t)]+dx(a_r)y(t))dx(t)dy(z)\cr
&=&-y_{a_r}\int^{t=a_r}(d_{a_r}[\Phi(t)]+dx(a_r)y(t))dx(t) +\tilde{C}(a_r,o).
\eea

Following the definition of the original paper, we have to adapt it to the situation of a log-vital singular point. At a log-vital singular point $\alpha=a_r$, we have the local coordinate:
\begin{align*}
    z_\alpha(p)=x(z)-x(\alpha),
\end{align*}
see also \cite{EO07} or Section \ref{Sec:localcorrdinate}. Since $y$ has a log-singularity (which means $dy$ has a residue) and $x$ is regular, we don't have a potential $V_\alpha$ and also no $t_{\alpha,0}$ at this point. Let us adapt the definition of $\mu_\alpha$ to the situation of log-vital singular points. In the definition, the local coordinate is used subtracting from $ydx$ the singular part. We define
\beq\label{defmualphalogvital}
\mu_\alpha:=\int_{\alpha}^o(y(q)dx(q)-y_{\alpha}\log(z_\alpha(q))dz_\alpha(q)+y_{\alpha}z_\alpha(o)(\log(z_\alpha(o))-1).
\eeq
The subtraction of the constant part at $o$ is made to make it more or less independent of $o$ (or think of an integration constant). Let us write locally $y(q)=y_{\alpha}\log(q-\alpha)+y^{reg}(q)$, then the definition of $\mu_{\alpha}$ is equivalent to 
\beq
\mu_\alpha:=\int_{\alpha}^o\big(y_\alpha \log\frac{q-\alpha}{x(q)-x(\alpha)}
dx(q)+y^{reg}(q)dx(q)\big)+\underbrace{y_{\alpha}z_\alpha(o)(\log(z_\alpha(o))-1)}_{C_{\alpha}(o)}.
\eeq
{\color{blue} Exactly the same structure appeared in the definition of $F_1$.}

This integral is actually finite due to its regularisation.

Let us compute the variation of $\mu_\alpha$ write to $\alpha=a_r$ {\color{blue}Note that $\mu_\alpha$ plays a slightly different role for the log-vital singular points than $\mu_{\alpha,0}$ for the other times. In \eqref{definitionF0TR}, $\mu_{\alpha,0}$ is multiplied by the time, which is variate, however, our $\mu_{\alpha}$ from \eqref{defmualphalogvital} corresponds directly to the product of the time and $\mu_{\alpha,0}$.}
\bea
d_{\alpha}\mu_{\alpha}&=&\log(x'(\alpha))dx(\alpha)+\int_{\alpha}^o\big(y_\alpha \big(\frac{d\alpha}{\alpha-q}-\frac{dx(\alpha)}{x(\alpha)-x(q)}\big)
dx(q)+d_{\alpha}y^{reg}(q)dx(q)\big)+d_{\alpha}C_{\alpha}(o)\cr
&=&y_\alpha\log(x'(\alpha))dx(\alpha)+\int_{\alpha}^oy_\alpha \big(\frac{d\alpha}{\alpha-q}-\frac{dx(\alpha)}{x(\alpha)-x(q)}\big)
dx(q)+d_{\alpha}C_{\alpha}(o).
\eea


\section{Free energies}


\subsection{Variational formulas for the free energies}
\begin{theorem}[Variational formulas for the free energies]\label{TheoVarFormulasFreeEnergies} For any $h\geq 2$ and any variation $\delta_\Omega$ with respect to $(\td{t}_{\alpha,k})_{\alpha \in \mathcal{P},k\geq 0}$ and $(\td{\epsilon}_i)_{1\leq i\leq g}$ (i.e. fixed log-times) we have:
\beq (2-2h)\delta_{\Omega}[\omega_{h,0}]=\int_{\partial_{\Omega}}\Lambda_{\Omega}(s)\omega_{h,1}(s)\eeq
\end{theorem}

\begin{proof}The proof is given in Appendix \ref{AppendixCompatibilityDilatonVarFreEnergies}.
\end{proof}

We also have:
\begin{theorem}[Variational formula for $\omega_{1,0}$]\label{theoVarF1}
For any variation $\delta_\Omega$ with respect to $(\td{t}_{\alpha,k})_{\alpha \in \mathcal{P},k\geq 0}$ and $(\td{\epsilon}_i)_{1\leq i\leq g}$ (i.e. fixed log-times), we have:
\beq \delta_\Omega[\omega_{1,0}]=\int_{\partial_{\Omega}} \Lambda_\Omega(q) \omega_{1,1}(q)\eeq
\end{theorem}

\begin{proof}The proof is given in Appendix \ref{AppendixVarF1}.
\end{proof}

Finally we also have
\begin{theorem}[Variational formula for $\omega_{0,0}$]\label{theoVarF0}
For any variation $\delta_\Omega$ with respect to $(\td{t}_{\alpha,k})_{\alpha \in \mathcal{P},k\geq 0}$ and $(\td{\epsilon}_i)_{1\leq i\leq g}$ (i.e. fixed log-times), we have:
\beq \delta_\Omega[\omega_{0,0}]=\int_{\partial_{\Omega}} \Lambda_\Omega(q) \td{y}dx\eeq
\end{theorem}

\begin{proof}$\td{y}dx$ and its associated irregular times, monodromies and filling fractions are described by the standard TR of \cite{EO07} and since our definition of $\omega_{0,0}$ is the same as in \cite{EO07}, the variational formula for $\omega_{0,0}$ proved in \cite{EO07} holds in our setup with the replacement $ydx\to \td{y}dx$.
\end{proof}

%\begin{theorem}[Variational formula for $\omega_{0,0}$]\label{theoVarF0}We have
%\beq \forall\,i\in \llbracket 1,g\rrbracket\,: \partial_{\epsilon_i}\omega_{0,0}=\frac{1}{4i\pi}\oint_{\mathcal{B}_i}ydx=\frac{1}{2}\oint_{\partial_{\epsilon_i}}\Lambda_{\partial_{\epsilon_i}}(s) \omega_{0,1}(s)
%\eeq
%\end{theorem}

%\begin{proof}Let $i\in \llbracket 1,g\rrbracket$ then we have from the definition:
%\beq \partial_{\epsilon_i}\omega_{0,0}=\frac{1}{2}\sum_{\alpha\in \mathcal{P}} \Res_{q\to \alpha} V_\alpha(q) du_i(q) +\frac{1}{2}\sum_{\alpha\in \mathcal{P}}t_{\alpha,0}\int_\alpha^o du_i(q)+\frac{1}{4i\pi}\oint_{\mathcal{B}_i} ydx\eeq
%However, we have
%\beq V_\alpha(q)=\Res_{p\to q} dS_{o,q}(p)V_\alpha(p)\eeq   
%\end{proof}



