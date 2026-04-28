# REVISITING MULTI-PERMUTATION EQUIVARIANCE THROUGH THE LENS OF IRREDUCIBLE REPRESENTATIONS

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
This paper explores the characterization of equivariant linear layers for representations of permutations and related groups.
Unlike traditional approaches, which address these problems using parameter-sharing, we consider an alternative methodology based on irreducible representations and Schur's lemma. Using this methodology, we obtain an alternative derivation for existing models like DeepSets, 2-IGN graph equivariant networks, and Deep Weight Space (DWS) networks. The derivation for DWS networks is significantly simpler than that of previous results.

Next, we extend our approach to unaligned symmetric sets, where equivariance to the wreath product of groups is required. Previous works have addressed this problem in a rather restrictive setting, in which almost all wreath equivariant layers are Siamese. In contrast, we give a full characterization of layers in this case and show that there is a vast number of additional non-Siamese layers in some settings. We also show empirically that these additional non-Siamese layers can improve performance in tasks like graph anomaly detection, weight space alignment, and learning Wasserstein distances.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces an alternative approach for characterizing equivariant linear layers in neural networks that process permutation and related group representations. The paper derives a simpler method for obtaining existing models such as DeepSets, 2-IGN, and Deep Weight Space networks, based on irreducible representations and Schur’s lemma. The proposed framework also considers unaligned symmetric sets, that build upon equivariance to the wreath product of groups.

### Strengths
1. The paper introduces a fresh perspective on equivariant layer characterization by applying irreducible representations and Schur’s lemma to obtain simplified derivations of established models, such as DeepSets, 2-IGN, and Deep Weight Space (DWS) networks.

2. The theoretical foundations are well-developed. The work provides a complete characterization of equivariant layers in the context of unaligned symmetric sets, which is an interesting theoretical contribution.

### Weaknesses
1. The presentation and flow of the paper could be improved. The claims and results are challenging to follow, which may limit the broader audience’s ability to appreciate the work.

2. The paper’s contributions lack clarity. The paper offers an irreducible-based derivation for existing results and characterizes equivariant functions on unaligned symmetric elements, but the impact and relevance of these contributions remain unclear. It is not evident how these results benefit the design of novel architectures or enhance our understanding of current ones. This limits the significance of the work and may fall short of ICLR’s standards.

3. The empirical evaluation is limited, and the results are not compelling. Using synthetic data for anomaly detection does not sufficiently demonstrate the method’s practical applicability, as the task is relatively unchallenging and does not show the strengths of the proposed approach.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies equivariant linear layers for representations of permutations and related groups from a novel irreducible representations perspective. The authors provide an alternative derivation for models including DeepSets, 2-IGN, and Deep Weight Space (DWS) networks. The theory is then extended to unaligned symmetric sets, showing that there is a vast number of additional non-Siamese layers in certain settings. Experiments show that additional non-Siamese layers improve the performance in tasks like graph anomaly detection, weight space alignment, and learning Wasserstein distances.

### Strengths
The paper offers the irreducible representations perspective for deriving classical models like DeepSets, 2-IGN and DWS networks. Some derivations are simpler than the original ones. The writing is clear and easy to follow. I check with the details and they are sound.

### Weaknesses
 * While the new derivations align with original methods, the resulting models are not new. The concept of ``irreducible representation'' is also well studied, so the contribution of the paper lies mainly in bridging two topics, which is interesting but natural. In particular for equivariant graph layers, the authors only provide derivations for 2-IGN. As admitted in the limitation section, the paper does not involve higher-order $k$-IGN. The author should explain whether their method is broadly applicable for these networks based on tensor representations, or need case-by-case derivations.

* Although this is a theoretical paper, the experiments could be improved. More baselines and more real-world tasks are strongly encouraged.

### Questions
* Can the method be generalized to higher-order $k$-IGN in a principled manner? Can you briefly describe the claim that ``using irreducibles could lead to new equivariant models with intermediate irreducible features of lower dimensions''?

* Can you conduct more experiments on real-world and large-scale datasets, and include more baseline? In addition, can you intuitively explain why non-Siamese layers help in these tasks?

### Soundness
3

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
3

### Summary
The paper introduces a novel methodology for characterizing equivariant linear layers for permutation representations, utilizing classical results from representation theory. Specifically, it provides an alternative characterization of equivariant linear layers for DeepSets, $2$-IGNs, and DWSNets, as well as the first comprehensive characterization of equivariant linear layers for unaligned symmetric elements. Importantly, the authors identify novel non-Siamese layers and empirically assess their impact.

### Strengths
- Clear presentation and notation, supported by rigorous proofs.
- The methodology is both valuable and simple, with potential to generalize beyond the examples presented.
- A novel and complete characterization of representations for unaligned symmetric elements.

### Weaknesses
 - Lacks discussion on extending the approach to groups and representations beyond the few presented.
- In particular, an appropriate discussion on characterizing the more expressive layers of $k$-IGNs for $k>2$ is missing.



### Questions
1. I find the methodology presented in L135-155 valuable to the research community due to its generalizability beyond the provided examples, most of which are already characterized. For this reason, would it be possible to add a *brief* discussion on the generalization of this methodology to strengthen the impact of this contribution and broaden its relevance to a wider community? See the following for more specific questions.
2. Computing a basis compatible with the irreducible representation decomposition can be challenging. Does this difficulty limit the methodology’s generalization? Are there similar technical challenges for characterizing $k$-IGN layers for $k > 2$?
3. Can this methodology be applied to other groups beyond $S_n$ and wreath products? If so, could you briefly provide a few examples?
4. Representations of the symmetric group are relevant in machine learning and its irreducible representation are absolutely irreducible. In contrast, other relevant groups, such as finite cyclic groups, have real irreducible representations that are not absolutely irreducible. Could the framework presented here be extend to these cases? What potential challenges do you envision in extending to non-absolutely irreducible representations?
5. Could you elaborate on the future directions for $k$-IGNs presented in the conclusions (L537-539)?

**Minor Issues (No Impact on Recommendation):**
- L073: I recommend specifying "$2$-IGNs" for transparency.
- L183: Is the presentation of $P_\tau$ unnecessary?
- L340: The wreath product of groups is introduced but not defined in detail; as this operation is uncommon in machine learning literature, additional explanation would benefit Section 5. Also, consider demonstrating that equation 7 forms a linear representation of this group, perhaps in the appendix.
- L420: Typo, “is prove”.
- L379 and L1030: I cannot understand why $\mathcal{V}^k$ is an irreducible representation of $\mathcal{G}^k$; is it instead irreducible for $\mathcal{G} \wr S_n$?
- L1040: The closing curly bracket is missing.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the problem of constructing linear equivariant layers for groups acting (linearly) on input and output spaces. Specifically, it proposes to exploit the decomposition into irreducible group representations and then appealing to Schur’s Lemma, which reduces the problem to choosing coefficients for pairs of isomorphic representations. Several specific instances are analyzed, such as permutation groups in the context of graph neural networks, groups acting on weights of deep networks, and wreath products acting on products of representations.

### Strengths
-The paper is exceptionally well written. The language is clear and concise, the sections are structured, and the mathematical formalism/notation is elegant. 

-The problem considered is a fundamental one in machine learning literature. Constructing (linear) equivariant maps lies at the heart of geometric deep learning, which has been successful in several applications. 

-The proposed solution is general, as it applies, in principle, to any input/output group representation. Several existing frameworks are phrased under the same paradigm, contributing with structure and clarity to the geometric deep learning literature.

### Weaknesses
I believe that the proposed approach via Schur’s Lemma comes with disadvantages. To begin with, using Schur’s Lemma to construct equivariant linear maps is not novel in the geometric deep learning community. It is a rather well-known technique – see, for example, Behboodi et al., Section 3.2. This is a major concern, since Schur’s Lemma represents a core point of this work; the other contributions amount to rephrasings of known frameworks from the literature under the lenses of Schur’s Lemma. Moreover, Schur’s Lemma has some restrictions. First, it requires the decomposition into irreducible representations to be known a priori, which is not always the case. Such decomposition is challenging to compute algorithmically for general groups and representations.  Second, Schur’s Lemma applies naively only to complex representations (i.e., over $\mathbb{C}$). As the authors mention, this is not an issue for permutation groups (appendix B), but it can be for other groups. It is still possible to apply Schur’s Lemma to arbitrary real representations of arbitrary groups, but this involves subtleties – see Behboodi et al., Section 8. 

I also find the experimental section rather weak. The experiments reported only consider ideal equivariant tasks, i.e., scenarios where the ground-truth function is equivariant. The experimental results show that adding equivariant layers to the network improves (generalization) performance, as compared to non-equivariant architectures. This is not surprising, since in these cases the inductive bias given by equivariance aligns perfectly with the structure of the task. In typical real-world scenarios (e.g., image classification), the (highly-noisy) ground-truth function is instead not exactly equivariant, or it is not equivariant on all the input data. In my opinion, it would be more informative and less trivial to test the models on these types of real-world tasks. The equivariance bias is often still beneficial in terms of generalization – as works in geometric deep learning have extensively shown – but empirical investigations are required to assess this carefully. 

Minor typos: 

-The paragraph title on line 86 is not capitalized, while the one on line 100 is. 

-The tables in section 6 exceed the margins of the paper.

### Questions
I would like the authors to comment on the above points regarding novelty and significance of experiments. 

My current opinion is that the work is exceptionally well-written, and bears several contributions to the geometric deep learning literature. However, I am concerned with the novelty and significance, as outlined above. Still, I am leaning towards accepting the paper, but would like to hear from the authors about my points of criticism.

### Soundness
3

### Presentation
4

### Contribution
2
