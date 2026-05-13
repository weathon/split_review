# DEPfold: RNA Secondary Structure Prediction as Dependency Parsing.

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
RNA secondary structure prediction is critical for understanding RNA function but remains challenging due to complex structural elements like pseudoknots and limited training data. We introduce DEPfold, a novel deep learning approach that reframes RNA secondary structure prediction as a dependency parsing problem. DEPfold presents three key innovations: (1) a biologically motivated transformation of RNA structures into labeled dependency trees, (2) a biaffine attention mechanism for joint prediction of base pairings and their types, and (3) an optimal tree decoding algorithm that enforces valid RNA structural constraints. Unlike traditional energy-based methods, DEPfold learns directly from annotated data and leverages pretrained language models to capture intricate RNA patterns. We evaluate DEPfold on both within-family and cross-family RNA datasets, demonstrating significant performance improvements over existing methods. On the RNAStrAlign dataset, DEPfold achieves an F$_1$ score of 0.985, predicting pseudoknots and long-range interactions. Notably, DEPfold shows strong performance in cross-family generalization when trained on data augmented by traditional energy-based models, outperforming existing methods on the bpRNA-new dataset. This demonstrates DEPfold's ability to effectively learn structural information beyond what traditional methods capture. Our approach bridges natural language processing (NLP) with RNA biology, providing a computationally efficient and adaptable tool for advancing RNA structure prediction and analysis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
After the author response, I appreciate the efforts that the authors made to make the paper more readable. I especially found the more explicit inclusion of pseudoknots and the workflow in Figure B1 quite helpful. I thus adjusted my score from a 5 to a 6.

----

The paper presents a novel and interesting approach for RNA secondary structure prediction. The authors frame this problem as dependency parsing in NLP. This first involves mapping the RNA structure to a dependency tree (this can be challenging because of pseudo-knots that result in non-projectivity).

The authors then use a neural network biaffine parser (based on Dozat and Manning - 2016) for this task which predicts the pairwise edges + labels. The authors then use either Eisener algorithm (for projective structures or Kirchoff's Matrix-Tree Theorem (for non-projective structure) to find the optimal tree.

Experiments show that the authors achieve strong performance on multiple datasets.

### Strengths
-The paper tackles an important problem.

-The method is interesting and novel. 

-Empirical results are strong.

### Weaknesses
Overall I found the description of the RNA secondary structure and how to transform it into a dependency tree to be confusing and non-rigorous.

-There is brief notation given in Section 2 and it states how a typical RNA secondary structure is composed of linear sequences (dots) and then different types of brackets. However, this is all quite vague and non-rigorous.

 It would be great to see an example of each type of label and how it is represented in this notation (e.g. stems, loops, pseudoknots etc.) I feel these concepts are not rigorously defined i.e. despite the importance of pseudo-knots I do not see a clear example/definition in the paper.

-The description of 3.1 (transformation of RNA structures to dependency) would be clearer with a running example that shows what happens at each step. Moreover, I am confused about whether the transformation is a 1:1 mapping. Is it provable the case that for any RNA secondary structure it maps to a unique dependency tree and vice versa? Or is this a heuristic.

### Questions
I have many questions about the RNA secondary structure and the transformation to dependency trees as described above in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new NLP dependency parsing-inspired algorithm for RNA secondary structure prediction, DEPfold. The paper's results suggest that DEPfold performs much better than other methods on within-family and cross-family RNA datasets, getting near perfect results on several datasets. 

As a "positionality statement" for this review, I'll mention that I'm expert in NLP dependency parsing, and assume that I was chosen to review for that reason, but I have little understanding of the biology and am generally not familiar with the test sets and performance of other methods in the RNA structure prediction domain.

### Strengths
- The approach to treating RNA secondary structure prediction via NLP dependency parsing, and largely using the biaffine dependency parsing algorithm of Dozat and Manning (2016) seems largely original.
- The results of the paper, as presented, are very strong. If this all checks out, the method provides a new much more accurate RNA secondary structure prediction and this would be quite significant

### Weaknesses
 - I feel that the presentation of the paper should have been clearer. It might have been better to move Fig. 1 to section 3 and to have referred to it when presenting the algorithm. The algorithm for conversion to dependency trees is presented somewhat informally. Something more precise would have been better. Among other things: (i) The algorithm is presented with reference to "bracket-dot notation" for RNA secondary structure (lines 126-136) but this is never rigorously defined. This notation may be well known in bioinformatics, but not to me. If this is the starting point of the algorithm, it would minimally be really useful to have shown the example sequence in Fig. 1 in bracket-dot notation. Indeed, it seems like the two subdiagrams in the top right of Figure 1 do not add much to understanding and at least one of them could have been deleted. Lines 165-187: While a projective dependency diagram is isomorphic to a certain kind of binary tree (a single-level X' CFG), a pure dependency grammar presentation would not normally evoke tree structure. Is it necessary? I would guess not and that the algorithm could be described directly in terms of creating dependency arcs. Things might even be clearer that way, given what is in Fig. 1. Tree completion (lines 210-215): AFAICS, g is never defined. Is it the root node, or the "grandparent" (parent of the head node)? Most importantly, I don't think the section 3.1 presentation of the algorithm even attempts to explain rigorously the treatment of pseudoknots. They're mentioned, as on line 223, but what is the details of their dependency grammar representation. Are they just treated as some kind of not fully labeled clump, as perhaps suggested by the notation introduced for P_i on line 159? I know vaguely that there is an older thread of work crossing from NLP to bioinformatics arguing that giving powerful enough grammars to describe pseudoknots requires more powerful "mildly context sensitive" grammars like tree-adjoining grammar, beyond the power of dependency grammars (e.g., https://academic.oup.com/bioinformatics/article/21/11/2611/294713 ). Is that still true? Is having a non-projective dependency tree grammar sufficient? This paper left me no wiser. Finally, I wondered whether the post-processing (line 291ff) couldn't have been incorporated into the decoding algorithm with some appropriate constraint.

 - Results: I'm not really the person to judge the appropriateness and completeness of all the results presented, but to the extent that I tried to look other things up on the web for a few minutes, I seemed to be left with more questions than answers. The algorithm referred to in this paper as "E2Efold" is referred to by the authors of the cited reference as E2Efold-3D. There is actually a different algorithm by different authors called E2Efold that appear at ICLR in 2020 (https://openreview.net/forum?id=S1eALyrYDH) and which itself used an algorithm "close to" biaffine dependency parsing. At least it is mentioned as related work. How does this paper refer to that paper. This paper is not in the references, and there is no explicit comparison in related work. But then the RNAStrAlign results in Table 2 seem to be the results of E2Efold not E2Efold-3D. They're identical to the ones in the E2Efold paper. Somehow this isn't giving me confidence.... I don't really know what are the best datasets or perceived best methods in this domain, but it then also seems like there are other recent methods claiming good results, such as RNAformer (https://icml-compbio.github.io/2023/papers/WCBICML2023_paper43.pdf) or DEBFold (https://pubs.acs.org/doi/10.1021/acs.jcim.4c00458) which aren't mentioned in the references here. Am I getting the best most up-to-date comparisons? It's not clear to me. The latest, best algorithm compared to is UFold from 2022, but there are clearly papers on this topic from 2023 and 2024, but it's not trivial for me to compare since there seem to be a lot of different datasets around, etc.

### Questions
This largely duplicates what I put in "weaknesses". 

- Lines 165-187: While a projective dependency diagram is isomorphic to a certain kind of binary tree (a single-level X' CFG), a pure dependency grammar presentation would not normally evoke tree structure. Is it necessary? I would guess not and that the algorithm could be described directly in terms of creating dependency arcs. Things might even be clearer that way, given what is in Fig. 1.

- Tree completion (lines 210-215): AFAICS, g is never defined. Is it the root node, or the "grandparent" (parent of the head node)?

- Most importantly, I don't think the section 3.1 presentation of the algorithm even attempts to explain rigorously the treatment of pseudoknots. They're mentioned, as on line 223, but what is the details of their dependency grammar representation. Are they just treated as some kind of not fully labeled clump, as perhaps suggested by the notation introduced for P_i on line 159? I know vaguely that there is an older thread of work crossing from NLP to bioinformatics arguing that giving powerful enough grammars to describe pseudoknots requires more powerful "mildly context sensitive" grammars like tree-adjoining grammar, beyond the power of dependency grammars (e.g., https://academic.oup.com/bioinformatics/article/21/11/2611/294713 ). Is that still true? Is having a non-projective dependency tree grammar sufficient?

- Can the post-processing (line 291ff) be incorporated into the decoding algorithm with some appropriate constraint?

- Clarify the relation between this algorithm and E2Efold (from ICLR 2020)

- Clarify the relation and what you're citing as results between E2Efold and E2Efold-3D

- Clarify whether there are results from 2023 or 2024 that should be included as comparisons and how the methods and results of algorithms from these years relate to yours.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes to use deep dependency parsing technique to predict RNA secondary structures. The paper shows how RNA structures can be mapped to dependency structures and via verse. Then now, the problem of predicting RNA structures is casted to dependency parsing, a classical task in NLP. The paper uses the Dozat & Manning 2016 parsing method, in which nucleotides are represented by RNA-fm or Roberta contextual embeddings. 

The paper shows experiments with popular datasets, RNAStrAlign, ArchiveII, and bpRNA-*. The proposed method substantially outperforms strong baselines (UFold, MXfold2, E2Efold). The paper also presents analyses showing a surprising result that Roberta contexutal embeddings actually are effective for this problem.

### Strengths
This paper showcases a very interesting application of NLP (more specifically, dependency parsing) to biology. The authors propose an effective way to translate the RNA structure prediction to dependency parsing, connecting the two challenges. The experiment results are evidence for the effectiveness of the proposed method.

### Weaknesses
The paper only mentions methods and work from 2022 backward, and only one published in 2024. However, I found several publications in 2023, such as [1,2,3]. I thus question about the up-to-date information in the paper.

(I'm willing to raise my overall score if the authors can provide comparison with the most up-to-date work in the literature).

### Questions
* Did the authors try "undirected" dependency structures? if yes, what are the performance?
* Because a RNA sequence can be very long (>1500), could the authors explain how to use Roberta effectively?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel method named DEPfold, which reframes the prediction of RNA secondary structures as a dependency parsing task. 

During training, given an RNA sequence, DEPfold constructs a dependency tree from the sequence using three types of arcs/labels: stem, pseudoknot, and connector. DEPfold then employs Biaffine parsers to learn these trees. 
During inference, DEPfold first predicts the tree from the raw sequence and subsequently recovers the internal secondary structures through several post-processing steps.

The authors have experimented with various base models, including RNAfm and RoBERTa, and different learning strategies such as fine-tuning and freezing pretrained models. They found that DEPfold outperforms existing models across multiple datasets in the field of RNA structure prediction.

### Strengths
This is a novel work, which, to my knowledge, is the first to frame RNA structure prediction as dependency parsing. 

I am excited to see that the wisdom from traditional NLP parsing tasks can still play important roles in a wider range of structured prediction tasks, such as RNA secondary structures.
DEPfold is built on the biaffine parser, a widely known neural-based dependency parser, and demonstrates very strong performance by leveraging the power of pretrained masked language models like RoBERTa.

I am very optimistic about further improving the performance of DEPfold by scaling it to larger model sizes and larger datasets.
Also, beyond the scope of this work, I believe DEPfold opens the door for utilizing some other parsing methods like stack-pointer [1] networks or modeling RNA structures via context-free grammars [2].

[1] Stack-Pointer Networks for Dependency Parsing  
[2] Strongly Incremental Constituency Parsing with Graph Neural Networks

### Weaknesses
* I suggest that the authors elaborate further on the definitions of RNA structures. For instance, a small figure illustrating the differences between stem and pseudoknot would be helpful. As someone who is not an expert in RNA structure prediction, I find it challenging to fully understand the details of the paper without resorting to external resources like Wikipedia or search engines.
* Line 284, Decoding: The Matrix-Tree Theorem is used for calculating the normalization term of the probabilities of non-projective trees. For decoding, one should use O(N^2) MST algorithms to decode non-projective trees.
* Lines 126-129: It would be beneficial if the authors could provide examples to demonstrate the bracketing structures.

### Questions
* > Pseudoknots, we find, are equivalent to adding a certain level of non-projectivity to the dependency parsing model.

I can't build the connection between the non-projectivity and Pseudoknots. Can the authors give me more details?

* There are some length limitatations for RoBETa that make it hard to extrapolate to longer sequences, how did you handle RNA sequence with thoundands of nucleotides?

* I'm very curious about the effectiveness of extending DEPfold to structured learning algorithms like TreeCRF, which has been proven very useful in the field of dependency Parsing [1,2,3]

* How about the speed of optimal tree decoding. Did you use any parallelized implementations of MST/Eisner in [torchstruct](https://github.com/harvardnlp/pytorch-struct) or [SuPar](https://github.com/yzhangcs/parser) for acceleration?

[1] Neural Probabilistic Model for Non-projective MST Parsing  
[2] Efficient Second-Order TreeCRF for Neural Dependency Parsing  
[3] Headed-Span-Based Projective Dependency Parsing

### Soundness
3

### Presentation
2

### Contribution
3
