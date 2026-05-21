---
job_id: 9ec53d34-9701-441c-8b35-1d92b6e6c262
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: qSak1Hjfdq.pdf
paper: All-Day Multi-Scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies lifelong learning, parameter-efficient adaptation, representation learning with tensor factorization, and embodied vision-and-language navigation in robotics.

## Minimum Quality
Pass ✅. The submission contains the core components expected of a research paper, including abstract, introduction, related work in the appendix, methodology, experiments, quantitative results, and conclusion; while there are notable technical and clarity issues, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence of hidden prompts, manipulative instructions to reviewers, or suspicious embedded text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper introduces the all-day multi-scenes lifelong vision-and-language navigation (AML-VLN) setting, where a VLN agent must learn sequentially across combinations of scenes and environmental conditions such as low-light, overexposure, and scattering. To address this, the authors propose Tucker Adaptation (TuKA), a tensor-based parameter-efficient adapter that factorizes adaptation weights into shared components and scene/environment-specific experts, together with a decoupled knowledge incremental learning strategy (DKIL) using EWC-style regularization, expert consistency, and orthogonality constraints. The paper also builds an Allday-Habitat benchmark with 24 sequential tasks and reports improvements over several LoRA-style continual learning baselines in both simulated and limited real-world settings.

## Strengths
1. The paper tackles a practically motivated problem. Continual adaptation for VLN across scene and environmental shifts is a real deployment bottleneck, and the AML-VLN formulation is a reasonable and useful benchmark direction for embodied learning.

2. The core idea is interesting. Representing adaptation parameters as a higher-order tensor with separate modes for scene and environment, then instantiating a task-specific adapter via Tucker contraction as in **Equation (3)**, is a sensible way to encode multi-factor structure that matrix LoRA variants do not expose explicitly.

3. The architecture diagrams are helpful overall. In particular, **Figure 3** gives a clear visual comparison between vanilla LoRA, HydraLoRA, and TuKA, and it makes the intended distinction concrete: LoRA and shared-A variants expose only matrix-factor hierarchies, while TuKA introduces explicit scene and environment modes. Even though the paper overclaims this distinction in places, the figure itself helps readers understand what is actually changing architecturally.

4. The empirical comparison is fairly broad within the paper’s chosen setting. **Table 1** shows sizeable average SR gains of AlldayWalker over strong baselines such as SD-LoRA and O-LoRA, and **Table 2** suggests that these gains are accompanied by lower forgetting rather than just better plasticity on later tasks. That combination is the right thing to test for a lifelong learning claim.

5. I appreciate that the paper does not stop at one headline metric. The inclusion of SR, SPL, OSR, and corresponding forgetting rates, with additional curves in **Figure 7**, is directionally good experimental practice for VLN.

6. There are several targeted ablations that at least try to probe the proposed design choices. **Table 3** studies which Tucker factors are shared, **Table 4** explores scaling to more tasks, and **Table 5** examines generalization to unseen scenarios. These analyses strengthen the paper relative to a submission that would only provide one main benchmark table.

7. The benchmark construction has some value by itself. **Figure 5** clearly illustrates the intended environmental degradations, and the attempt to move beyond a single “normal” visual condition is useful for embodied navigation evaluation.

## Weaknesses
1. The paper’s central novelty claim is overstated relative to what is actually demonstrated. The manuscript repeatedly argues that LoRA-style methods are fundamentally limited because they use “two-dimensional matrices” whereas TuKA learns in a “high-order tensor” space, see the framing around **Figure 1**, **Figure 3**, and Section 3.1. That rhetoric is too strong. A tensor factorization here is still just a structured parameterization of a matrix update that is ultimately reconstructed into $\Delta W_t \in \mathbb{R}^{a_l \times b_l}$. The practical distinction is not “matrix methods cannot represent multi-hierarchical knowledge, tensor methods can,” but rather that TuKA imposes a particular multiplicative sharing structure across scene and environment indices. That is a more modest and more defensible claim. Why this matters: the current framing risks making the contribution look deeper than it is, and it also weakens the scientific positioning because the real question is whether this specific factorization is better than other structured sharing schemes, not whether tensors are magically higher-capacity in the abstract.

2. The mathematical presentation has several inconsistencies and underspecified points, enough that I had to reverse-engineer the intended objective.  
   - In **Equation (2)**, the tensor shape is written as $\mathcal{X}^l \in \mathbb{R}^{a_l \times b_l \times M \times N}$, but the notation in the text uses malformed dimensions “$\mathbb{R}^{d_1 \times d_2, \dots, \times d_N}$” just before it, which is sloppy.  
   - In **Equation (3)**, the contraction result should be carefully dimension-checked. Given $\mathcal{G}\in\mathbb{R}^{r_1\times r_2\times r_3\times r_4}$ and row experts $U^3[s,:]\in\mathbb{R}^{r_3}$, $U^4[e,:]\in\mathbb{R}^{r_4}$, the inner contracted tensor becomes an $r_1\times r_2$ matrix, then left-multiplied by $U^1\in\mathbb{R}^{a_l\times r_1}$ and right-multiplied by $(U^2)^T\in\mathbb{R}^{r_2\times b_l}$. That part is plausible, but the paper should state this explicitly because it is the core adapter construction.  
   - In **Equation (6)**, the update is written as $F_{\theta,t} = \omega F_{\theta,t-1} + (1-\omega)F_{\theta,t}$, which is circular as written. Presumably the second $F_{\theta,t}$ on the right-hand side is meant to denote a newly estimated Fisher for task $t$, say $\widehat{F}_{\theta,t}$. In the current form, the equation is formally wrong.  
   - In **Equation (8)**, $Norm(\mathbf{U}) = \mathbf{U}[i,:]/\|\mathbf{U}[i,:]\|_F^2$ is not unit-norm normalization. If the intention is row-wise unit Euclidean norm, it should be $\mathbf{U}[i,:]/\|\mathbf{U}[i,:]\|_2$, not division by the squared norm.  
   - In **Equation (9)**, the loss references $\mathcal{L}_{sk}$, but the earlier shared-knowledge term is named $\mathcal{L}_{ewc,t}$ in **Equation (4)**. This is likely a naming mismatch, but again it affects the readability of the core training objective.  
   These are not tiny typos, because they appear exactly in the equations that define the method. At minimum, the authors need to clean this up carefully.

3. The continual-learning evaluation protocol is not fully convincing, especially because task identity assumptions and inference-time retrieval are mixed in a somewhat confusing way. In the problem definition on **Page 3**, the paper says “task-id $t$ is seen during the testing phase,” but later in Section 5.1 it says the task-id is “agnostic during the testing phase,” and Section 3.4 introduces a CLIP-based retrieval mechanism to select scene and environment experts under unknown scenarios. These are materially different settings. If task identity is known, expert selection is trivial. If it is unknown, retrieval accuracy becomes part of the method and should be evaluated explicitly. Why this matters: a lifelong learning method can look substantially better if oracle task identity is available, and the current paper does not clearly isolate which results use oracle information versus retrieval.

4. The retrieval mechanism in Section 3.4 is underspecified and empirically under-analyzed. The method stores CLIP features for each scene and environment, then does nearest-neighbor matching by cosine similarity. But the paper does not tell the reader what exact features are stored, whether a single prototype or multiple observations per class are used, how temporal variation is handled, or how retrieval errors affect downstream navigation. There is also an indexing typo in Section 3.4, where environment matching is written against $\{Fe_{e1},\dots,Fe_{eM}\}$ instead of $N$. More importantly, **Table 5** reports generalization on unseen scenarios using this expert selection mechanism, but there is no direct retrieval-accuracy analysis, no confusion matrix across scenes/environments, and no ablation comparing oracle expert selection versus retrieved expert selection. That omission matters because some of the reported generalization gain may come from CLIP retrieval quality rather than the adaptation method itself.

5. The experimental comparisons are broad but not always cleanly fair or well controlled. The main comparison in **Table 1** and **Table 2** mixes several categories: continual LoRA methods, methods that store multiple adapters, and test-time adaptation methods such as FSTTA and FeedTTA that are designed for a somewhat different use case. I understand why the authors include them, but the comparison would be more persuasive if the paper more carefully separated “continual adaptation with persistent memory” from “episodic test-time adaptation.” Also, several baselines appear to use the paper’s own expert-selection procedure at inference according to the appendix algorithm descriptions, which may advantage methods that naturally fit that selection pipeline and disadvantage others. If a baseline did not originally rely on this retrieval mechanism, then this should be acknowledged as a modified baseline setup rather than silently treated as standard.

6. The paper gives strong empirical wins, but it does not sufficiently disentangle which ingredient is doing the work. TuKA bundles at least three changes:  
   - Tucker-structured factorization of the adapter,  
   - explicit scene/environment decomposition,  
   - DKIL regularization with EWC-style shared constraints plus consistency plus orthogonality.  
   **Table 3** studies shared components, and the appendix compares 3rd-order and 4th-order versions, but the main paper still lacks a clean decomposition such as: TuKA without DKIL, DKIL with a non-tensor hierarchical baseline, TuKA with only EWC, TuKA with only consistency, etc. The ABC-LoRA comparison lives only in the appendix and should really be elevated, because it addresses the obvious counterargument that the gains come from hierarchical factorization rather than specifically from Tucker structure. Right now, the paper asks the reader to accept a fairly bundled story.

7. The benchmark itself is useful, but its scientific interpretation is narrower than the paper suggests. The “all-day” environments are synthetic degradations generated by imaging models, see **Equations (10)-(12)** and **Figure 5**, plus a small amount of real-world data. That is reasonable as a first step, but the paper sometimes writes as if it has established robust all-day multi-scene navigation broadly. It has not. It has shown robustness to a specific set of photometric degradations in Habitat-like settings, with limited real-world validation. This matters because the language of the paper drifts from “benchmark under several degradations” to “enabling all-day multi-scenes VLN,” which is a stronger claim than the evidence supports.

8. Some quantitative patterns in the results deserve more discussion than they receive. For example, in **Table 1**, AlldayWalker improves average SR from 56 to 65 over SD-LoRA, which is solid, but some tasks still remain weak, such as T2, T5, T6, T8, and T19. Likewise, **Table 2** contains negative forgetting values for some methods and tasks, including AlldayWalker, which indicates performance after sequential learning exceeds the reference single-prefix performance. That is not impossible, but it should be explained explicitly. Without that explanation, the forgetting metric is slightly awkward to interpret. A spicy version of this point is: if your forgetting score can go negative and the paper does not discuss why, then the metric is not doing as much explanatory work as the table formatting suggests.

9. Presentation quality is mixed. There are many grammatical issues, notation inconsistencies, and naming slips, for example “Tucker-Adaption” versus “Tucker Adaptation”, “InIncrementAL”, “the 3-order tensor are”, “the matrices are maintained at a consistent order of magnitude”, and several symbol overloads for $S$, $T$, and $E$. **Figure 1** is visually appealing and communicates the application story, but it also packages a lot of assertions into the graphic, especially the claim that prior LoRA variants only learn “single-dimensional task knowledge,” which is not a careful characterization of those baselines. This does not kill the paper, but it keeps the work from feeling fully polished.

10. The memory/computation story is incomplete. The paper emphasizes parameter efficiency, and Appendix Table 17 reports parameter counts, but the central appeal of TuKA is not just parameter count, it is also continual deployment practicality. Yet the paper does not report training or inference overhead of Tucker reconstruction, retrieval cost, or memory growth from storing scene/environment features and task-related Fisher information. For a robotics-facing lifelong learning paper, omitting these costs weakens the practical case.

## Questions
1. Please clarify the test-time setting unambiguously. Are the main results in **Table 1**, **Table 2**, and **Figure 7** obtained with oracle task/scene/environment identity, or via the retrieval mechanism in Section 3.4? The statements on **Page 3** and **Page 7** appear inconsistent. A precise statement of the evaluation protocol would significantly increase my confidence.

2. Can the authors provide a corrected and fully dimension-annotated derivation around **Equations (2)-(3)** and fix the apparent formal mistakes in **Equations (6)** and **(8)**? If these are merely notation issues, the rebuttal should state the corrected formulas clearly.

3. How much of the gain comes from Tucker factorization itself versus DKIL? A rebuttal table including at least:  
   - TuKA without $\mathcal{L}_{ewc}$,  
   - TuKA without $\mathcal{L}_{co}$,  
   - TuKA without $\mathcal{L}_{es}$,  
   - hierarchical non-tensor baseline with the same DKIL losses,  
   would make the causal story much stronger.

4. What is the retrieval accuracy for scene and environment expert selection in Section 3.4? Please report expert-selection accuracy, or at least compare oracle expert selection against CLIP-retrieved expert selection. This would help separate “representation quality” from “retrieval quality.”

5. In **Table 5**, the unseen-scenario generalization gains are meaningful, but can the authors clarify whether the unseen scenes share degradation-generation parameters, instruction style, or other benchmark artifacts with training? A more careful statement of what is truly unseen would help.

6. For the forgetting metrics in **Equation (13)** and **Table 2**, why do some values become negative? Is this due to transfer from later tasks, variance from finite evaluation episodes, or something else? A short explanation would improve interpretability.

7. Could the authors comment on runtime and memory overhead relative to SD-LoRA and O-LoRA, not just parameter count? This seems especially relevant for embodied deployment.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The work studies embodied navigation and includes real-world robotic deployment discussion, see Appendix Section F and the societal impact note on **Page 32**. Systems that navigate homes or real environments using onboard cameras raise standard privacy and safety concerns, especially if deployed in sensitive indoor settings or used for surveillance-like purposes. I do not see an ethical violation in the paper itself, but these deployment risks are real enough that I would flag them for routine ethics consideration.

## Soundness Rating
3: good. The core idea is plausible and the empirical evidence is substantial, but the paper has several equation-level mistakes, protocol ambiguities, and missing controls that prevent a higher soundness score.

## Presentation Rating
2: fair. The high-level story is understandable and some figures are helpful, but the paper has too many notation inconsistencies, grammatical issues, and objective-definition slips for a “good” presentation score.

## Contribution Rating
3: good. The AML-VLN setting and Tucker-style adapter formulation are useful contributions, and the empirical gains are meaningful, though the paper overstates novelty and does not fully isolate why the method works.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The problem is relevant, the tensorized adapter idea is interesting, and the empirical results are strong enough to make the paper worth discussing at ICLR. That said, the paper needs a firmer and less hype-driven positioning, cleaner math, and better isolation of the retrieval and DKIL components.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main technical and empirical details carefully, though some implementation specifics remain underspecified in the paper.