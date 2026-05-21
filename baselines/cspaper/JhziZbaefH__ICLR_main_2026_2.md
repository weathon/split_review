---
job_id: df7b53f2-d8bb-4fbe-b018-65ebdb91d77c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: JhziZbaefH.pdf
paper: Online Multimodal Learning With Human-in-the-Loop
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on online multimodal learning, continual/lifelong learning, representation learning across vision, audio, and taste, with a human-in-the-loop learning setting.

## Minimum Quality
Pass ✅. The paper contains the expected core sections, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results tables, and Conclusion. While there are serious issues in clarity, methodological justification, and evaluation, they do not rise to the level of an immediate desk rejection based solely on the manuscript text.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies online multimodal learning with human-in-the-loop interaction, aiming to learn new multimodal concepts and associations incrementally without forgetting previous ones. The authors propose a hierarchical modular architecture with feature neurons, unimodal association neurons, and multimodal association neurons, together with ascending, descending, and lateral pathways, a conflict-checking mechanism that can query the user, and a reference extraction procedure intended to identify which part of a multimodal signal a word refers to. Experiments on fruit and household-object datasets evaluate cross-modal recall, continual extension with color words, and extension to a new taste modality.

## Strengths
The paper tackles a worthwhile problem. Online multimodal learning with user interaction is underexplored compared with standard offline multimodal retrieval/classification, and the goal of combining continual adaptation, conflict detection, and interactive clarification is interesting.

The method is ambitious in scope. It does not just propose another cross-modal retrieval model, but tries to integrate several capabilities in one framework: incremental concept acquisition, multimodal association, conflict checking, modality extension, and a notion of reference disambiguation. Even though I have substantial concerns about execution, the target functionality is broader than in many standard multimodal papers.

Figure 1 is useful for motivating the setting. It makes clear the intended use case, namely that a learner encounters a new word that partially conflicts with prior knowledge and resolves the discrepancy by asking a question. This grounding helps the reader understand why the authors care about conflict detection rather than only top-1 retrieval accuracy.

Figure 2 also helps communicate the high-level architecture. In particular, the separation into feature, unimodal association, and multimodal association layers, and the distinction between ascending, descending, and lateral pathways, makes the architectural intent more concrete than the text alone. The diagram at least gives an interpretable picture of how information is supposed to propagate across modalities.

The experiments are broader than a single benchmark table. The authors include baseline multimodal recall in Table 1, a continual-learning-style extension with color-referring words in Table 2, and modality extension to taste in Table 3. This at least attempts to test different aspects of the claimed system behavior.

In the reported results, the method is consistently the strongest among the online baselines in Tables 1 to 3. For example, in Table 1 OML outperforms ART and AEN across both datasets and both environments, and in Table 3 it also outperforms AEN under modality extension. If the protocol is sound, this would support the claim that the proposed architecture is better suited than prior online baselines for incremental multimodal association.

## Weaknesses
1. **The mathematical formulation is often underspecified, and in several places internally inconsistent.**  
   This is a central issue because the paper is method-heavy and asks the reader to trust a custom neuron/signal formalism. In **Equation (1)** on Page 3, the ascending activation of a feature neuron is written as
   \[
   \boldsymbol{y}^{\alpha_k}=\sum_{i=1}^{n}\sum_{t=1}^{T} w_{j,i}\cos\lambda_i^{\alpha_k}2\pi\frac{t-1}{T},
   \]
   conditioned on \(d(\boldsymbol{x},\boldsymbol{w}_j)\le \theta\). But the signal does not actually depend on the current input \(\boldsymbol{x}\) except through the threshold gate. Once the gate passes, the output seems determined only by the neuron's stored weights and frequencies. That is a strange design choice and should be justified explicitly, because it means two distinct inputs within threshold induce the same output signal. If that is intended, it has serious consequences for discriminability and memorization capacity. If it is not intended, then Eq. (1) is mis-specified.

   There are also notation problems. In **Eq. (4)** on Page 4, the descending activation of a UAN outputs \(\boldsymbol{a}^{\alpha_k}\), yet the text around it uses \(\boldsymbol{a}^{\beta}\) as the descending signal and later says \(A^{\alpha_k}\) is transmitted to feature area \(\alpha_k\). The mapping from a MAN output to multiple feature-area-specific descending signals is not formally defined. Likewise, in **Eq. (6)** on Page 5, \(\mathcal{F}(\boldsymbol{z}^{\beta})\) yields \([\boldsymbol{a},\boldsymbol{\lambda}]\), but it is unclear how dimensional consistency is maintained across channels, especially when different feature areas have different sizes and frequencies.

2. **The probabilistic descending activation model is not well justified and appears ad hoc.**  
   On Page 4, each dimension \(A_i^{\alpha_k}\) is modeled as Gaussian, and the activation checks whether
   \[
   p_i^{\alpha_k}=\exp\left(-\frac{(a_i^{\alpha_k}-\mu_i)^2}{2\sigma_i^2}\right)\ge \vartheta
   \]
   for all \(i\). This quantity is called a “relative probability density,” but it is not a normalized density, and the thresholding rule requires *every* dimension to pass. In high dimensions, such an all-coordinate conjunction is extremely brittle. The paper gives no explanation of why this should work robustly, no sensitivity analysis for \(\vartheta\), and no derivation connecting this criterion to recognition accuracy or false positive/false negative tradeoffs. Since descending activation is essential for recall, conflict detection, and cross-modal routing, this matters a lot.

   There is also a practical concern: if \(\sigma_i\) becomes small, the criterion becomes numerically sharp and highly unstable; if \(\sigma_i=0\), the formula is undefined. The text does not discuss these cases.

3. **The reference extraction mechanism is too weakly justified for the claims made about “precise referring.”**  
   The core idea in **Section 3.4** is to identify the referred feature type by low coefficient of variation, using
   \[
   \boldsymbol{r}=\boldsymbol{\sigma}\oslash \boldsymbol{\mu},
   \]
   then taking per-feature-type maxima and thresholding them in **Eq. (7)**. There are several problems here. First, if any component of \(\mu\) is near zero, the coefficient of variation becomes unstable or undefined. Second, taking the maximum within each feature type is a very pessimistic aggregation; one noisy dimension can make an entire feature type fail. Third, the argument assumes the referred dimensions are stable across examples while irrelevant dimensions vary more, but that assumption is not generally true, especially for realistic visual features. It might hold in the toy setting of color words paired with simple fruit images, but the paper presents it as a more general mechanism.

   Figure 3(a) illustrates the intended behavior, namely that the word “hóng sè” should lock onto color rather than shape. However, the figure is only a schematic cartoon. It does not provide quantitative evidence that the proposed criterion reliably separates referred versus non-referred feature groups, nor does the paper provide precision/recall or error analysis of the reference extraction itself. Given that Table 2 is presented as validation of this component, the paper should directly measure whether the extracted reference mask is correct, not only downstream retrieval accuracy.

4. **The conflict-checking and question-asking logic is described informally and leaves important algorithmic choices unspecified.**  
   Section 3.5 gives four cases for online learning, but many details that strongly affect behavior are omitted. For example, when multiple recalled concepts exist, how exactly is the system selecting the candidate word \({}^{V}N_i^A\) to ask about? The text says it “picks out a name” or “selects a neuron” with the same referring pattern, but no tie-breaking rule, score, or confidence measure is defined. Similarly, conflicts are based on set intersections such as \({}^{A}N^b\cap G_p^b\neq\varnothing\), yet the construction of these activated sets depends on thresholds, descending routing, and lateral propagation that are themselves only partially specified.

   This matters because the claimed human-in-the-loop capability is one of the main advertised contributions. Figure 3(b) sketches ascending/descending activations, but it does not resolve the procedural ambiguity. As currently written, the “interactive” part feels more like a hand-written case analysis than a fully specified learning algorithm.

5. **The experimental protocol is not strong enough to support the broad claims about catastrophic forgetting and continual online multimodal learning.**  
   The “open environment” on Page 8 divides the dataset into four equal parts with different classes and feeds them sequentially. This is a very limited form of non-stationarity. There is no comparison to standard continual-learning metrics such as average accuracy over time, forgetting, backward transfer, forward transfer, or memory footprint. The paper repeatedly states that offline methods suffer from catastrophic forgetting, but in fact the offline baselines appear simply ill-matched to a sequential protocol, and the paper does not describe any reasonable adaptation strategy for them. That comparison risks being stacked.

   More importantly, no replay-based or regularization-based continual learning baselines are included, even though the paper's core claim is about online continual learning. The baselines are mostly older multimodal retrieval methods or a small number of architecture-growing systems. This weakens the empirical case considerably.

6. **The comparison to offline methods is not obviously fair.**  
   Tables 1 and 2 compare OML, an explicitly online expandable architecture that learns one sample once, against offline methods such as DAE, DBM, DISRH/DJSRH, NRCH, and FUME. But the evaluation setup is not carefully matched. The paper says these offline methods can be iteratively optimized multiple times and are frozen after training, while OML, ART, and AEN learn each sample only once. In the open environment, the offline methods show large drops, and the authors attribute this to catastrophic forgetting. However, it is unclear whether those methods were retrained from scratch on accumulated data, fine-tuned only on new chunks, or evaluated under some other procedure. Those choices completely determine whether “forgetting” is expected.

   Without a rigorously controlled protocol, the strong headline in **Table 1**, namely that OML becomes best in open environments while offline methods drop sharply, is hard to interpret scientifically. This is not a minor experimental detail; it directly affects the paper's main conclusion.

7. **Some reported evaluation choices are overly favorable to the proposed method and muddy interpretation of the numbers.**  
   On Page 9, the paper explicitly states that when AEN returns both visual and taste concepts for a word, “we count this as a correct result for AEN in Table 3,” and similarly ART/AEN are counted correct in Table 2 even when they return all features rather than the precise referred subset. This is already a lenient metric for baselines, but the deeper issue is that the target task itself is vaguely defined. Is success exact retrieval of the referred concept only, or is any superset acceptable? Different sections imply different answers.

   Even more concerning, the paper states that if a question posed to the user remains unanswered for some time, “we set the answer to be positive” (Page 8). That effectively injects positive confirmation by default into the learning loop. Since the method is built around querying the user in conflict situations, this assumption could materially inflate performance. The paper does not report how often this happened, nor provide ablations with negative or missing feedback.

8. **The datasets and tasks are too simple to substantiate the broader claims.**  
   The experiments are conducted on Fruits, HomeF-derived fruit subsets, enhanced versions with color words, and taste-augmented variants. These are narrow and relatively low-complexity settings with handcrafted features such as Fourier descriptors for shape, mean color, and MFCCs for audio. This does not match the paper's ambitious framing around general online multimodal learning. It is much closer to incremental concept association in a toy symbol grounding setup.

   That narrow scope would be acceptable if the paper positioned itself accordingly, but instead the framing is broad and human-brain-inspired. The gap between ambition and evidence is large.

9. **The method relies on hand-engineered feature decomposition, which limits generality and weakens the representation-learning contribution.**  
   On Page 8, the visual pipeline uses SAM for object extraction, then handcrafted normalized Fourier descriptors for shape and mean color inside the boundary; the auditory pipeline uses syllable segmentation via short-time energy and zero-crossing rate, followed by MFCCs. So the proposed “learning” system largely operates on manually separated factors such as shape, color, and syllable sequence. This is very different from modern multimodal representation learning, where the challenge is to learn robust representations from high-dimensional raw or pretrained embeddings without assuming such a clean decomposition.

   The paper's central reference extraction story, especially in Figure 3(a), depends heavily on this separation. In more entangled representations, the coefficient-of-variation heuristic may not work at all. This significantly narrows the scientific contribution.

10. **Presentation quality is below the level needed for a complex new framework.**  
   The exposition is frequently difficult to follow. There are notation inconsistencies, undefined or weakly defined variables, and grammatical problems throughout. One concrete example is the naming mismatch on Page 8, where the text says “We compare our method OML with ... DJSRH ...” but Table 1 lists “DISRH,” and later the paper says “ART, AEN, and OLM learn multimodal representations in an online manner,” apparently switching from OML to OLM. These are not fatal by themselves, but in a paper with many custom symbols and routing matrices, such inconsistencies seriously hurt readability.

   Figures 2 and 3 are also dense and require substantial cross-referencing to decode. Figure 2, in particular, includes many arrows, layer labels, and pathway annotations, but the mapping between symbols in the figure and the equations is not cleanly explained. A reader should not have to reverse-engineer the paper's notation from the diagram.

11. **Related-work positioning is incomplete for the continual/online learning angle.**  
   The related work section mostly contrasts joint versus coordinated multimodal learning and then cites a small number of online multimodal approaches. Given the paper's emphasis on online continual learning, catastrophic forgetting, and user interaction, the positioning against broader online continual learning literature is thin. The manuscript would benefit from stronger contextualization relative to modern online continual learning methods and evaluation practices, not just multimodal retrieval papers and two architecture-growing multimodal baselines.

## Questions
1. For **Equation (1)**, is it really intended that the ascending output of a feature neuron depends only on \(\boldsymbol{w}_j\) and not on the input \(\boldsymbol{x}\), except through the gating condition \(d(\boldsymbol{x},\boldsymbol{w}_j)\le \theta\)? If not, please provide the corrected equation. If yes, please explain why this does not collapse all within-threshold inputs to the same signal.

2. In **Equations (2) and (4)**, how are \(\mu_i\) and \(\sigma_i\) initialized and updated for descending pathways, and how do you handle the cases \(\sigma_i=0\) or \(\mu_i\approx 0\)? This is especially important because both the Gaussian thresholding and the coefficient-of-variation criterion can become numerically unstable.

3. Please provide a fully specified algorithm for the interaction loop in **Section 3.5**. In particular, when several candidate recalled concepts exist, what exact rule chooses which question to ask, and what exact score determines a conflict?

4. Can you report a direct evaluation of the **reference extraction** component itself, beyond downstream retrieval accuracy? For example, for color words versus object-name words, what is the accuracy of selecting the correct referred feature type in **Eq. (7)**?

5. For the “open environment” results in **Tables 1 and 2**, what exactly is the training protocol for each offline baseline? Are they retrained from scratch on accumulated data, fine-tuned only on new chunks, or trained separately per chunk? A precise description is needed to interpret the comparison fairly.

6. Since the paper states that unanswered user queries are treated as positive responses, how often does this happen in practice? Please provide an ablation with: always answered, unanswered-as-positive, unanswered-as-negative, and unanswered-ignored. This could materially change the conclusions about the human-in-the-loop mechanism.

7. In **Table 2**, the paper says ART and AEN are counted correct even when they return all features rather than the precise referred subset. Could you also report a stricter metric where only exact referring is counted as correct? That would better isolate whether OML truly solves the intended problem rather than a relaxed version.

8. Please provide runtime, memory growth, and neuron growth statistics over time. Since the architecture expands online with new neurons and pathways, scalability is a practical and scientific concern.

9. Can you include stronger continual-learning baselines and metrics, such as forgetting measures and stream-wise performance over time, rather than only final recall accuracies?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper itself. The work uses standard object and speech-like multimodal data and proposes interactive querying, but there is no deployment claim involving sensitive populations or high-risk applications in the manuscript.

## Soundness Rating
1: poor. The paper has interesting goals, but the core mathematical formulation is underspecified, several equations are unclear or internally inconsistent, and the empirical protocol does not adequately support the strongest claims.

## Presentation Rating
2: fair. The high-level idea is understandable, and the figures help with intuition, but the notation, algorithmic details, and experimental descriptions are too unclear for a method of this complexity.

## Contribution Rating
2: fair. The problem setup is interesting and potentially relevant, but the current paper does not yet provide a sufficiently rigorous or convincing contribution for ICLR.

## Overall Rating
2: Reject, not good enough. The paper has an appealing high-level goal and some encouraging empirical trends, but the combination of unclear mathematics, weakly specified algorithmic details, and insufficiently convincing evaluation leaves me with low confidence in the central claims.

## Reviewer Confidence
4: confident. I am confident in the overall assessment, particularly regarding the clarity, methodological specification, and experimental evaluation issues, though some implementation details are hard to verify because the paper does not define them precisely.