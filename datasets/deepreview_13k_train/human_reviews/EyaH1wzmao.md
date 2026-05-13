# The Ramanujan Library - Automated Discovery on the Hypergraph of Integer Relations

- Decision: Accept
- Scores: 8, 3, 8

## Abstract
Fundamental mathematical constants appear in nearly every field of science, from physics to biology. 
Formulas that connect different constants often bring great insight by hinting at connections between previously disparate fields.
Discoveries of such relations, however, have remained scarce events, relying on sporadic strokes of creativity by human mathematicians.
Recent developments of algorithms for automated conjecture generation have accelerated the discovery of formulas for specific constants.
Yet, the discovery of connections between constants has not been addressed.
In this paper, we present the first library dedicated to mathematical constants and their interrelations. This library can serve as a central repository of knowledge for scientists from different areas, and as a collaborative platform for development of new algorithms.
The library is based on a new representation that we propose for organizing the formulas of mathematical constants: 
a hypergraph, with each node representing a constant and each edge representing a formula.
Using this representation, we propose and demonstrate a systematic approach for automatically enriching this library using PSLQ, an integer relation algorithm based on QR decomposition and lattice construction. During its development and testing, our strategy led to the discovery of 75 previously unknown connections between constants, including a new formula for the `first continued fraction' constant $C_1$, novel formulas for natural logarithms, and new formulas connecting $\pi$ and $e$.
The latter formulas generalize a century-old relation between $\pi$ and $e$ by Ramanujan, which until now was considered a singular formula and is now found to be part of a broader mathematical structure. 
The code supporting this library is a public, open-source API that can serve researchers in experimental mathematics and other fields of science.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduce a new search algorithm for integer polynomial relations between mathematical constants. The authors organize their algorithm into a library and use a hypergraph as data structure to store the relations. The library can interact with a relation finding machine to search for new relations.

### Strengths
Strengths:
- The paper claims to have discovered new integer relations between constants that have not been discovered before. This is an exciting and relevant direction for publication in ICLR since machine assisted mathematics has many unrevealed potentials.
- The methodology is sound and correct, since it is a combination of previously published and peer-reviewed systems. 
- The ROI scheme, while simple, may prove to be generalizable to other domains/applications.
- The resulting code seems to be available publicly. 
- The paper is mostly written in a clear and comprehensive way, with appropriate figures and tables for demonstration.

### Weaknesses
Some weaknesses include:
- There is almost no machine learning (emphasis on the 'learning' part) in the paper, as it seems to be an engineering/database product that interfaces with existing code base. This is, of course, not a weakness on the content of the paper, but on its fit for the venue of publication.
- The use of hypergraphs as data structure, while theoretically clean, is perhaps only practically useful if the code can make use of graph symmetries (for instance in a graph learning framework). Due to the lack of practical ways to distinguish sets vs sequence in hardware, I very much doubt storing relations as hypergraphs is much more practically advantageous than any naive data structure. Of course, some data structure is needed to store the relations, but the authors also claimed that this is an "effective representation" (line 72) and overall feature it as one of their main contributions. The practical advantage of using hypergraphs over other data structures for storing these relations is not well justified, especially given the computational overhead of maintaining such a structure.
- From my understanding, perhaps inherent to the problem the authors are trying to solve, until a proof is given, it is almost never guaranteed that any new relations found are actually correct. This makes the problem rather ill-defined since there are no performance metric attributed to the proposed methodology, making it hard, almost impossible, to judge its effectiveness, outside of engineering perspective.

### Questions
Some other minor comments and questions: 
- Line 42, I believe it is quite a stretch to claim that any computer assisted proof (which comprises of the majority of citations in this sentence are examples of "usage of AI as a scientific tool" 
- Line 101-104, it took me awhile to parse the sentences here. This can be solved by explicitly stating the definition of C-transform and how it differs from continued fraction since at first glance and without definition, it's not easy to distinguish. Alternatively, one can also just give an example of the difference. An example of why this is confusing is: it seems that C-transform, as stated on arbitrary function f_n, captures all continued fraction; yet some continue fractions cannot be converted to infinite sums when C-transforms can? 
- What is the question mark in table 2?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This proposes an improved method to discover equations

### Strengths
Automated equation discovery is interesting and providing a library with basic tools is certainly useful.
The text uses good english.

### Weaknesses
 The text only provides a high level explanation of a few ingredients of the proposed method.  While it may be understandable for a few specialists, the text isnt accessible to the general logic or reasoning expert. 
The text doesnt introduce the basics of the considered formalism, does not offer specifications nor examples of inputs or outputs of the system.



#### Supplementary material

The code contains a Readme file but it does not comprehensively explain how to install,or use the code.  Despite looking around to the several files i didnt succeed to use it nor understand it.

#### details

* when defining hypergraph, make clear whether you consider directed / ordered or undirected edges.
* Sec 2 mentions giving cnstants such as $\pi$ or $e$ explicitly but does not say how to give an irrational number explicitly.
* please specify how one can define a C teansform (as it contains an infinite number of parameters)
* while libe 108 talks about polynomial relations, line 111 only gives the form of a linear relation
* line 115 requires thar the absolute value of the linear expression equals exactly $\epsilon$.  I suppose you mean $\le$ instead.
* the precision is defined as $\log(\epsilon)$, i guess this can lead to problems if $\epsilon$ happens to be exactly 0 ?
* line 119: "we define its degree as the sum of all exponents in each monomial": does this imply you consider homogeneous polynomials, as else the different monomials may have a different sum of exponents?
* line 125: is an edge a hyperedge?
* line 127: please define transitivity in this context
* line 153: please define "type"
* line 155: the expression "product space on certain subtypes" is very unclear.
* line 159: it is unclear what is a combined constant, or what language or equations the user can use to define them.

Section 5 may have provided useful insight in capabilities of the proposed system,if the used notations would have been clear.

Making abstraction of that problem i observe the displayed equations are rather complicated and hence the search space of possible conjectures must be huge.  Given one searches only approximate equalities under bounded precision it seems likely one will discover many incorrect conjectures.

### Questions
It may help to answer questions in my detailed comments, even if that is not guaranteed to clarify everything.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a new library for automatically discovering functional relations between mathematical constants. The paper outlines the structure of the library as well as the numerical approaches to discovering (polynomial) functional dependencies between fundamental mathematical constants. The authors discuss the convergence properties of the selected approach as well as some limitations and future directions.

### Strengths
I am not an expert in the area but I enjoyed reading the paper. There are quite a few things I like about it:

- Fundamental mathematical constants are fascinating, they are often the cornerstones in many scientific disciplines. Discovering new complex relations between them can inspire interdisciplinary discoveries.
- The presented approach for the representation of organizing the relations in a hypergraph and searching for new relations using numerical methods is innovative.
- The implementation is publicly available and likely to benefit the broader scientific community.
- The most time-consuming algorithm is embarrassingly parallel, so it is likely scalable.

### Weaknesses
I think the presentation can be improved. The paper is interesting but at times it felt more like reading an article from Quanta magazine. Here are a few suggestions:
- Include a more thorough description of the setup. How was the hypergraph initially created, how many constants and relations were used, how much did the graph expand when new relations were discovered, etc? Some tables and figures can help.
- Include some explanation about operating the library. For example, how can one include new constants and start searching for relations? I think some high-level pseudocode will help.
- Add some formal results about the validity of results and rate of convergence. I think the discussion in section 3 can be organized in a more formal way using some lemmas. This will help the reader concentrate on the results and maybe think about improvements. 
- Maybe provide examples with a few more constants, I see only $\pi$, $e$ and $\zeta$.

### Questions
Would it be feasible and useful to create a knowledge graph that contains information about the constants and the relations between them? Initially, it will contain human/LLM written explanations, e.g. a short text with references to research papers that introduce the constant or relation and how it is used. When new relations are discovered, the graph will be automatically updated with a short description of the discovery process including computational statistics. The edges of the graph can be labeled with the different relation types (e.g. linear, polynomial, etc.) and/or the certainty of the discovered connection. Knowledge graphs are very popular and this would allow the usage of third-party software for a better visualization and understanding of the discovery process.

### Soundness
4

### Presentation
3

### Contribution
4
