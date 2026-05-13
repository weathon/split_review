# Entropy Coding of Unordered Data Structures

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
We present shuffle coding, a general method for optimal compression of
  sequences of unordered objects using bits-back coding. Data structures that
  can be compressed using shuffle coding include multisets, graphs,
  hypergraphs, and others. We release an implementation that can easily be
  adapted to different data types and statistical models, and demonstrate that
  our implementation achieves state-of-the-art compression rates on a range of
  graph datasets including molecular data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the problem of compressing unordered objects. It presents a general approach called “shuffle coding” to compress different data structures with bits-back coding. After introducing the background in Section2, including data structures and the problem definition of compressing unordered objects, the authors derive Lemma3.2 and then provide the pseudo algorithm for the proposed method. The key idea is to decode an ordering as part of an encode function. The experimental results demonstrate that the proposed shuffle coding could compress different data structures with better lossless compression performance, compared with ordered ER.

### Strengths
It seems to be meaningful to reduce compression cost by removing the order information in data structure. The proposed shuffle coding can get a discount in lossless compression of such data structures, as illustrated by Equation 14.

### Weaknesses
My major concern is about the significance of the problem studied in this paper: considering the complexity, will the proposed method have wide/potential applications in practice? For my side, it seems slightly intuitive to remove the order information so that we can reduce the coding cost when we compressing graph data. Is bits-back coding necessary in this scheme? These my concern may partially be attributed to my lack of expertise in the field of compressing graphs. In addition,  Appendix C describes the modifications compared with Daniel et al., 2023b, which is also an important baseline in this paper. But for a reader that is not very familiar with the area, appendix C may be hard to understand.

### Questions
As I am not entirely familiar with this field, the authors are welcome to direct my attention and address my concerns with more details provided. And I’ll gladly consider increasing my initial rating.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors introduce _shuffle coding_, a method for compressing sequences of unordered objects based on bits-back coding. They provide an exposition of the group-theoretic fundamentals relevant for shuffle coding (Section 2 and Appendix A), define the desiderata required for an optimal-rate codec for unordered sequences (Section 3) and present shuffle coding, an algorithm that fulfils these desiderata (Section 3.1). They apply shuffle coding to unordered data structures (specifically graphs), showing strong performance compared to PnC and SZIP (Section 5).

### Strengths
This paper presents a few key strengths which, in my view, are as follows:

__Elegant unified framework:__
This paper provides an unified theoretical framework for compressing unordered objects, such as multisets and graphs.
This approach is based on the elegant idea that the order of the parts of an object does not matter, one can reduce the cost of communicating the object by getting a certain number of bits, i.e. the bits corresponding to a particular ordering of the parts, back.
This generality is appealing because one does not have to devise specialised method for each different type of unstructured object.
However, it should be noted that this framework assumes access to a "canonicalisation" function, which determines a canonical representation  as well as the automorphism group of the object (e.g. graph) in question (also see weaknesses section below).

__Strong compression performance:__
The authors demonstrate that shuffle coding achieves strong compression rates in practice.
In particular, shuffle coding outperforms SZIP and PnC on a range of graph datasets.
This is an encouraging result because, while the proposed method is asymptotically optimal, it also involves a non-trivial overhead (which is amortised as more data are compressed).
Therefore it is good that despite this cost, shuffle coding seems to perform well in practice.

__Well written paper:__
The paper is generally clearly written and well motivated.
The authors have made an effort to discuss the limitations of their work, specifically about the time complexity and initial rate overheads induced by their method.
I appreciated the illustrations and pseudocode listings in the main text, which helped understand their method.

### Weaknesses
 The paper's main weaknesses, in my view, revolve around the practical applicability of shuffle coding:

__Large runtime complexity:__
As the authors note, applying shuffle coding to a graph requires solving a graph isomorphism problem, for which no polynomial-time algorithm is known. This can be a significant hurdle when coding larger graphs. The authors brought up this issue in the paper, and suggested that approximately solving the isomorphism problem is a promising way to scale the method. However, in its current form, the method does not scale to larger graphs. Further, it is unclear what the tradeoff between the communication rate and computational complexity of the method would be, if one were to use an approximate scheme instead. The computational cost of finding the canonical form is a critical bottleneck, and while approximation may alleviate this, the practical implications of this trade-off need to be thoroughly investigated. Specifically, the authors should provide a more detailed analysis of how the approximation error in the canonicalization affects the final compression rate, and whether there are specific graph structures where the approximation is more or less effective.

__Initial bit overhead:__
Due to the requirement of initial bits, shuffle coding introduces a communication overhead to the transmitted message. This can be significant in the one-shot or few-shot case, making the method from compressing small sequences of messages. I think the authors should specify the amount of extra bits used in the experiments (see Table 3) in the main text. While the authors mention a maximum overhead of 64 bits, the actual overhead observed in practice, and how it scales with the size of the input, is not clear. A more detailed analysis of this overhead, perhaps as a function of the number of vertices or edges in the graph, would be beneficial. This would allow practitioners to better assess the practical applicability of the method for different use cases.

__Contribution as a general solution seems somewhat exaggerated:__
While the shuffle coding approach is general from a theoretical point of view, it requires access to a "canonicalisation" function. The authors focus on graphs, for which existing libraries offering this functionality exist. For other permutable classes, the authors argue that one can "embed objects into graphs in such a way that the structure is preserved and the canonization remains valid." However, it is unclear whether, for example, this embedding might affect the compression rate, or how difficult it is to construct such an embedding. In light of this latter point, the statement that the authors' "implementation can easily be adapted to different data types" in the abstract may be regarded as exaggerated (if for example coming up with an algorithm that constructs such graph embeddings is challenging, or if the computational / memory complexity of such an algorithm is large). A more measured statement in the appendix and / or positioning of the main text might be beneficial in this regard. The practicality of this embedding approach for arbitrary permutable classes needs further justification. The authors should provide examples of how such embeddings can be constructed for different types of data, and discuss the potential impact on both computational complexity and compression rate.

### Questions
Below are some questions for the authors and suggestions that I think could improve the paper.

## Questions

__Clarification on the discount factors for Table 3:__
The ER and PU models are specific probabilistic models for graphs and, as the authors explain, they can be swapped in with any other exchangeable model of graphs.
Therefore, while it is important to report the overall communication cost in the experiments, an equally important (in my view) quantity to report is the rate discount afforded by shuffle coding.
What are the discounts corresponding to the results in table 3?
Perhaps the authors can report these as an extra column, since the discount is a function of the graph alone and not the modelling distribution $P.$


__Extending the framework with approximate isomorphism solutions:__
The authors claim that while no known polynomial-time solution for solving the exact graph isomorphism problem is known

> this limitation can be overcome by approximating an object’s canonical ordering, instead of calculating it exactly. This introduces a trade-off between speed and compression rate in the method, and lowers runtime complexity to polynomial time.

Can the authors comment on the tradeoff between the speed and compression rate of this modified method, here and / or the main text?


## Suggestions

__Definition 2.5:__
I think that definition 2.5 is not totally accurate and / or could be improved.
Presumably, what the authors mean by "inverse functions" is that $\texttt{decode}$ is the inverse function of $\texttt{encode}.$
In that case the $\texttt{decode}$ function isn't really needed and / or can be defined as $\texttt{decode} = \texttt{encode}^{-1}.$
Also, the statement "with respect to $P$" does not seem to make sense on its own.
I think clearer statement is to say that 

> an optimal codec for $P$ is an invertible function $\texttt{encode} : M \times X \to M$, which is optimal with respect to $P,$ in the sense that for any [...].

More importantly however, in shuffle coding, the $\texttt{encode}$ function is _not invertible_, because for $f \in \mathcal{F},$ applying $\texttt{decode}(\texttt{encode}(M, f))$ returns the message $M$ together with the canonical representation $\bar{f}$ rather than $f$ itself (see for example the function signature and return statements in the code listing in Section 3.1).
While this is a technicality that does not seem affect the validity of the algorithm, I think the authors should modify their definition and / or exposition to account for this.

__Framing of definition 2.5:__
I think definition 2.5 and the paragraph under it could be framed better.
In particular, the authors define optimal codecs and explain that "definition 2.5 captures the abstract properties of codecs based on the range variant of asymmetric numeral systems."
I think a clearer approach would be to say up-front that their plan is to set up a method that gets those bits which correspond to permutations of the graph in question back.
This in turn necessitates using a last-in-first-out codec, such as (r)ANS, and that definition 2.5 specifies "Optimal last-in-first-out codecs", rather than "Optimal codecs".

__Initial bit overhead statement:__
The authors argue that the constant bit overhead incurred by bits-back "exists for all entropy coding methods."
While all entropy coding methods have a constant overhead that is amortised as more and more data are compressed, typical methods such as Arithmetic Coding (AC), have constant overheads of the order of a couple of bits.
This is far smaller than the claimed overhead of "at most 64 bits" of bits-back for shuffle coding.
I think the authors' phrasing somewhat misrepresents the overhead of other entropy coding methods.
A more accurate statement would be welcome here, such as: "As in other entropy coding methods, which invariably have similar (though typically smaller) constant overheads, the constant 'initial bit cost' of bits-back is amortised as more data are compressed."

__All units in bits?__
Are all reported rates, including for example Table 1, in bits?
If so, it would be good to add a statement up front, early in the paper, that specifies this.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
## Summary
* This paper propose shuffle coding, a BB-ANS approach towards lossless compression of unordered sets. The scenario described by the paper seems to related to the Birkhoff Polytope in variational inference of permutation [Linderman 2017, Reparameterizing the Birkhoff Polytope for Variational Permutation Inference], where each permutation's likelihood is the same. The authors demonstrate the effectiveness of their approach on various datasets.

### Strengths
## Strength
* The unordered set / graph compression problem is of good practical value. The proposed approach is a neat extension of bits-back coding. It is simple, novel and works well.

### Weaknesses
## Weakness
* As the authors have discussed, the current initial bits required is quite large. This hinders the practical application of the proposed approach to one-shot object coding. Though it is still possible to apply this approach to a dataset to amortize the initial bits. An alternative to the bit-swap approach mentioned by authors is correlation communication [Harsha 2010, The Communication Complexity of Correlation] [Li 2018, Strong Functional Representation Lemma and Applications to Coding Theorems] [Theis 2021, Algorithms for the Communication of Samples], which has extra overhead of approximately $\log \log N!$, but does not require any initial bits. The practicality of correlation communication methods is questionable due to their computational complexity, which scales exponentially with the entropy of the source, making them unsuitable for large datasets. Furthermore, the paper does not fully explore the trade-offs between the initial bit overhead and the computational cost of the proposed method, especially for very large unordered sets. The current approach requires an initial bit cost that scales with the size of the set, which may be prohibitive for large sets, even with amortization across a dataset. The paper should include a more detailed analysis of the initial bit cost and its impact on the overall compression performance for different set sizes.


### Questions
## Questions
* For practically large structure, what is the computational cost for finding and sampling from the isomorphism class $\hat{f}$? For practical codec, the metrics such as latency and throughput should also be discussed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a general method called shuffle coding for compressing sequences of unordered objects using bits-back coding.    
The proposed shuffle coding is applicable to multisets, graphs, hypergraphs etc.    
SOTA compression rate is achieved on several graph datasets including molecular data.

### Strengths
The problem of compressing unordered data optimally by considering the storing order as redundancy is novel to me.    
The paper is a solid contribution with solid theoretical foundations. The mathematical structures from group theory are closely connected with the target unordered data.      
The idea of decoding the ordering as part of an encode function in the spirits of bits-back coding is very interesting.    
The background and proposed methods are clearly explained and relatively easy to follow.    
Experiments are conducted on server different datasets, and achieve sota compression rate.   
Limitations of the proposed method is properly discussed.

### Weaknesses
One major concern is the practical value of compressing those unordered data. Compared with images or videos, it seems to me the data volume of those unordered date is very limited. However, I still appreciate the technical contribution of this paper.

Currently the numbers in Table 4 is relatively not easy to understand. It would be better to report speed as GB/s or MB/s and compare this with previous methods, so that readers can better feel the efficiency.

Definition 2.5 is described in a very concise way. It is not clear why the definition is specifically connected with rANS. I think is also applies to arithmetic coding.

It is not clear how eq9 is related to the real bitrate. In this definition, the data is compressed in an instance-wise manner and l(m) is the initial bit cost which can be amortized later if we compress more instances. However, log(1/p(x)), which is defined as the rate of the codec, is an averaged value averaging over the input symbol number. I do not understand why l(m) can be added with log(1\p(x)).

Definition 2.3 (Automorphism group) is actually the difinition of stabilizer. If I remember correctly, the concept of Automorphism in group theory is connected with operation by conjugation. Did I miss anything?

### Questions
Definition 2.5 is described in a very concise way. It is not clear why the definition is specifically connected with rANS. I think is also applies to arithmetic coding.    

It is not clear how eq9 is related to the real bitrate. In this definition, the data is compressed in an instance-wise manner and l(m) is the initial bit cost which can be amortized later if we compress more instances. However, log(1/p(x)), which is defined as the rate of the codec, is an averaged value averaging over the input symbol number. I do not understand why l(m) can be added with log(1\p(x)).  

Definition 2.3 (Automorphism group) is actually the difinition of stabilizer. If I remember correctly, the concept of Automorphism in group theory is connected with operation by conjugation. Did I miss anything?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
