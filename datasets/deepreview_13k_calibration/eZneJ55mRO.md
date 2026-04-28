# G$^2$N$^2$ : Weisfeiler and Lehman go grammatical

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
This paper introduces a framework for formally establishing a connection between a portion of an algebraic language and a Graph Neural Network (GNN). The framework leverages Context-Free Grammars (CFG) to organize algebraic operations into generative rules that can be translated into a GNN layer model. As CFGs derived directly from a language tend to contain redundancies in their rules and variables, we present a grammar reduction scheme. By applying this strategy, we define a CFG that conforms to the third-order Weisfeiler-Lehman (3-WL) test using the matricial language MATLANG. From this 3-WL CFG, we derive a GNN model, named G$^2$N$^2$, which is provably 3-WL compliant. Through various experiments, we demonstrate the superior efficiency of G$^2$N$^2$ compared to other 3-WL GNNs across numerous downstream tasks. Specifically, one experiment highlights the benefits of grammar reduction within our framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the expressive power of 3-WL from the aspect of formal language. The authors show that 3-WL is equivalent to a context-free grammar (CFG), and propose a reduced CFG that preserves the same expressiveness. Based on the reduced CFG, the authors develop a new WL algorithm and GNN model that match the expressiveness of 3-WL. The new GNN model achieves competitive performance and efficiency on downstream tasks.

### Strengths
There are some positive points of this paper. 
* The paper is well-written and easy to follow.
* The paper exploits the formal language equivalence to investigate the GNN model and design a new GNN model, which I think is a promising direction for future research.

### Weaknesses
I have some concerns about the paper as follows:
* I am not convinced by the novelty and the contribution of the paper, as the CFG $G_\mathcal{L_3}$​​ seems to be a straightforward derivation of the MATLANG.
* The validation and discussion of the reduced CFG and the corresponding GNN may be insufficient, both empirically and theoretically. I have some questions for the authors below.

### Questions
* In the theoretical aspect, although the two CFGs r-$G_{\mathcal{L}_3}$ and $G_{\mathcal{L}_3}$ have the same expressive power, it may take more steps for r-$G_{\mathcal{L}_3}$ than $G_{\mathcal{L}_3}$ to generate the same string. Therefore, how can $G^2N^2$ match the expressiveness of the ordinary 3-WL GNN with a fixed number of layers?
* I would also like to see how the new GNN model performs on the ZINC-12k and ZINC-full datasets, which are widely used benchmarks for molecular property prediction.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a framework to convert context-free rules over an algebraic matrix language into a GNN architecture. Using this framework, they produce a WL-3 GNN as follows: (1) they write down a set of context-free rules producing a language that is just as expressive as 3-WL, (2) they reduce this set of rules into a smaller set of rules, and (3) they translate these rules directly into a GNN architecture. The resulting architecture performs competitively in practice, outperforming various existing GNNs on a variety of tasks.

### Strengths
(1) While this is not my area, the contribution of the paper seems strong in that it presents a framework for designing GNN architectures that implement a given CFG.

(2) The experiments seem strong, and the proposed GNN is both provably expressive and performs competitively compared to existing architectures.

(3) The paper is well-written, clear, and well-organized.

### Weaknesses
Some minor weaknesses are discussed in the questions section.

### Questions
(1) While many CFGs are equally expressive if we can apply their rules an arbitrary number of times, it seems like what we actually care about is the expressiveness of the grammar after L rule applications, given that in practice our GNNs are finite depth. In light of this intuition, the paper might benefit from some discussion of which CFGs are preferable, given that they have the same expressive power.

(2) From my understanding, it seems that this architecture outperforms other architectures in some datasets but not others (table 6), but has the advantage of being the strongest GNN out of those with provable expressivity (since it dominates PPGN). Is this understanding correct? If so, what is the utility of having provable expressivity, beyond the model's performance on the datasets?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new architecture for GNNs that captures precisely the expressive power of 3WL. This architecture is based on a grammatical representation of a language over graphs that has the same expressive power as 3WL. The idea is that this new architecture permits a more efficient implementation than the 3WL-based GNNs, which are known not to scale well in practical scenarios.

### Strengths
- The paper is very polished and easy to follow
- The topic is timely and the problem practically relevant
- Experiments confirm the suitability if the approach

### Weaknesses
 There is only one criticism I make to the paper and it is the lack of search for a principled explanation of why the GNNs based on MATLANG are more efficient than the ones based on 3WL.

### Questions
Could you please comment further on the main criticism I posed above: what do you think is the main reason the MATLANG-based GNNs are more practically suitable than the standard ones based on 3WL? This came as a big surprise to me, and it is a bit dissatisfying to stay with an explanation based on experiments only. I feel that a more principled, perhaps theoretical explanation, is lacking.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
