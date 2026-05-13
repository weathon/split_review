# The "Law'' of the Unconscious Contrastive Learner: Probabilistic Alignment of Unpaired Modalities

- Decision: Accept
- Scores: 5, 8, 5, 5

## Abstract
While internet-scale data often come in pairs (e.g., audio+image, image+text), we often want to perform inferences over modalities unseen together in the training data (e.g., audio+text). Prior work has addressed this issue by learning multiple contrastive embedding spaces between existing modality pairs, implicitly hoping that unseen modality pairs will end up being aligned. This theoretical paper proves that this hope is well founded, under certain assumptions. Starting with the proper Bayesian approach of integrating out intermediate modalities, we show that directly comparing the representations of data from unpaired modalities can recover the same likelihood ratio. Our analysis builds on prior work on the geometry and probabilistic interpretation of contrastive representations, showing how these representations can answer many of the same inferences as probabilistic graphical models. Our analysis suggests two new ways of using contrastive representations: in settings with pre-trained contrastive models, and for handling language ambiguity in reinforcement learning. Our numerical experiments study the importance of our assumptions and demonstrate these new applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
A common belief in contrastive multimodal learning is that the embedding spaces of seen modality pairs (A&B and B&C) naturally align with those of unseen modality pairs (A&C). This paper introduces the "Law of the Unconscious Contrastive Learner", showing that under specific assumptions about the geometric and probabilistic properties of contrastive embeddings, it is possible to establish relationships between unseen modality pairs. The law relies on three key assumptions: the first two allow for evaluating the connection between two unpaired modalities (A&C) via a Bayesian approach that integrates over an intermediate modality (B), while the third enables the use of the intermediate representation marginal distribution to derive a closed-form solution. The law is then formalized into a practical algorithm using Monte Carlo approximations. It is validated through experiments on synthetic and real datasets, including CLIP and CLAP. Results show the alignment of unpaired modalities, though some assumptions may not be strictly necessary in practice.

### Strengths
1. The idea of aligning representations of the same concept or sense, regardless of modality, is valid and taps into a widely-held belief. Although this is commonly accepted, it has not been well grounded in theory. This paper makes strides by validating this belief under certain assumptions. It provides a foundation that may guide further theoretical development in contrastive embedding alignments.
2. Although not checking line-by-line, the proposed theory assumes probabilistic contrastive learning, allowing connections between unpaired modalities (A&C) to be established across a shared intermediate modality (B) using Bayes Rule. Its algorithm using Monte Carlo approximations is backed by empirical evidence, which is interesting compared to the Oracle methods, where modality pairs (A&C) can be seen.
3. The paper is well-presented, especially the first half theoretical sections. This clarity makes the framework and assumptions easy to follow. Results shown in Figure 2 are helpful for a good understanding.

### Weaknesses
1. The experimental setup in Section 6 lacks standard organization, making it difficult to immediately grasp the task, input, output, and evaluation metrics. A clearer presentation of each experiment would improve readability and understanding.
2. There appears to be a gap between the Monte Carlo approximation method and the main theoretical framework. For example, Assumption 3 is noted as not strictly necessary, introducing ambiguity in the experiments and leaving some uncertainty about the necessity of all three proposed assumptions given the results.
3. Of the three main experiments, both the first (6.1) and third (6.3) are conducted on in-house datasets, and only the second experiment applies the algorithm to an external dataset (AudioSet) by comparing CLIP and CLAP, but its scope, datasets, model types, and modality pairings are limited.

### Questions
An easy way to strengthen the experimental findings could be to swap the modalities within the same setup. Theoretically, there is no strict assignment of text, image, or audio to roles A, B, or C, so these modalities could be switched to test the robustness of results.

(There appears to be a formatting issue in the proof of Lemma 2 on page 5.)

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proves under certain assumption that the “hope” of unseen modality pairs will be aligned when the embedding space of models between existing modality pairs are trained contrastively. Using Bayesian approach, the paper shows that directly comparing the representation of data from unpaired modalities can recover the same likelihood ratio. The analysis shows that contrastive representations can answer many of the same inferences as probabilistic graphical models. The result of the paper suggests that the contrastive representations can be used in settings with pre-trained contrastive models, and for handling language ambiguity. Experiments are done to verify the theoretical results over synthetic datasets and more realistic setting.

### Strengths
- The three assumptions are clearly stated, and proofs as well as empirical tests for the assumptions are provided. The derivation of the conclusion that the relationship between the $\phi$ functions for both normalized and unnormalized representation closely resemble their critic functions.
- Empirical evaluations using the Monte Carlo approximation validates some assumptions’ validity, and also brings the possibility of only use intermediate modality data to align all the modalities’ representations. Experiments are done in both synthetic setup (section 6.1, 6.3) and real-world data (Section 6.2).

### Weaknesses
Section 6.1’s setup might be a bit artificial. Since modality A and C are only a projection of B, it does not quite suffice the general definition of “modality” that most of us agrees on.

### Questions
- In equation from 4.2, $\phi(A)^T\phi(B) + \phi(B)^T\phi(C) \geq \phi(A)^T\phi(C)$ is because the trained pairs are almost guaranteed to be closer than the unseen pair?
- Missing subscript $C$ for $\phi_C(C)$ in line 247?
- Apologize for not being familiar enough with the theory of the work, why is von-Mises-Fisher the distribution in Lemma 2? Is it just because the normalization constant or wanting to match assumption 3?
- The citation format in section 6.2.1 should be changed. E.g., AudioSet (Gemmeke et al., 2017).
- Monte Carlo approximation can be expensive. What is the cost in computation and time efficiency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Existing work often assumes alignment between different modality pairs without providing a theoretical basis. This paper, motivated by (1) isotropic representations and (2) a Bayesian probabilistic framework, introduces three assumptions that theoretically ensure alignment.

In a synthetic experiment, the authors first demonstrate that alignment fails when Assumption (iii)—that acquired representations have a marginal distribution following an isotropic Gaussian—is violated. They then show that retrieval accuracy remains high (indicating successful alignment) when Assumptions (i) and (ii), which involve Monte Carlo approximations, are satisfied, using an intermediate modality like language.

Finally, in a real-world application, the authors apply contrastive representations from pre-trained contrastive models within a probabilistic framework to manage language ambiguity in reinforcement learning.

### Strengths
1. This paper proposes theoretical assumption to guarantee the universally agreed alignment for multi-modalities.
2. The experiments on synthetic data verifies the correctness of the assumptions. 
3. The real application experiment show promise of the assumption in reinforcement learning for addressing handling language ambiguity.

### Weaknesses
It is not clear why the proposed framework is better at language ambiguity situation, is it because that the framework is based on a probabilistic framework, i.e., the uncertainty. 

The proposed assumptions seem to less contribute to the real-data application, i.e., language ambiguity in reinforcement learning framework, which limits its practical contribution.

### Questions
See weakness above.

1. Any practical implication based on the assumptions.
2. Detailed explanations of the reason why the framework can help language ambiguity, is that possible applied to other frameworks. The motivation of taking different multi-modality data into consideration in the RL settings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tries to provide a theoretical justification to the scenario of using the third modality to connect two modalities which are not explicitly trained during contrastive learning. A typical use case is to conduct image-audio retrieval tasks through CLIP and CLAP with language as the intermediate.

Authors prove that such heuristic is theoretically grounded, by making a conditional independence assumption (of the two modalities to be
connected), along with two ideas published in previous work.

Two numerical experiments with synthetic and real-world datasets are employed to validate the effectiveness of the proof.

### Strengths
- It is desired to have some theoretical justifications to the common
  use case or practice of connecting two modalities that are not
  explicitly trained during contrastive learning. There are published
  work, but not much theoretical justifications contained.

### Weaknesses
- The method derived from the proof, LogSumExp, seems not working well for
  LanguageBind, and it leads to performance drop (Figure4).

- Overall the proposed proof seems mostly effective on synthetic
  datasets. I am thus concerned about how strong are the assumptions,
  especially assumption 1 -- are modalities A (e.g., audio) and C
  (e.g., image) really independent conditioned on B (language)?

- Writing needs to be improved; Sec. 6.3 experiment is difficult to
  understand with the main text alone.

### Questions
Line457. LanguageBind is claimed to assume the proposed Law
implicitly. However, when applying the law explicitly, why the
performance actually drops? I was expecting no impacts on LanguageBind
if the Law is implicitly implemented already.

### Soundness
2

### Presentation
2

### Contribution
2
