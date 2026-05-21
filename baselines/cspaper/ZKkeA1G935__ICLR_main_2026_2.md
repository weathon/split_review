---
job_id: 8bff859d-ac69-4cdc-82ff-ec7b77756ed3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ZKkeA1G935.pdf
paper: Can LLMs Alleviate Catastrophic Forgetting in Graph Continual Learning? A Systematic Study
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly in scope for ICLR, it studies continual learning, learning on graphs, pretrained/LLM-based methods, and introduces a benchmark for graph continual learning.

## Minimum Quality
Pass ✅ The paper contains the necessary components for an ICLR submission, including abstract, introduction, methodological description, experiments/results, related work, and conclusion. While I have substantial concerns about experimental framing and methodological clarity, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence of hidden prompts, reviewer-targeted instructions, invisible text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies whether LLMs can mitigate catastrophic forgetting in graph continual learning, focusing on node-level class-incremental learning and few-shot NCIL on text-attributed graphs. The paper argues that a commonly used local-testing protocol suffers from task-ID leakage, introduces the LLM4GCL benchmark under a global-testing setup, evaluates a range of GNN-, LLM-, and GLM-based baselines, and proposes SimGCL, which combines first-session LoRA instruction tuning with a training-free prototype classifier for later sessions.

## Strengths
The strongest part of the paper is the attempt to scrutinize the evaluation protocol itself rather than just adding another method on top of a possibly flawed setup. The discussion around local testing versus global testing is meaningful, and the intuition is well conveyed in **Figure 1** on **Page 3**. In particular, the lower-right panel gives a concrete visual explanation of how task-specific graph statistics can leak task identity, which makes the criticism of prior local-testing practice easy to follow.

The empirical scope is reasonably broad for a benchmark-style paper. The paper evaluates multiple method families, 7 datasets, and two continual-learning scenarios, with main results summarized in **Table 2** and **Table 3** on **Pages 6-7**. This breadth is useful for the community, especially because the comparison is not restricted to GNN baselines but also includes LLM-only and graph-enhanced LLM methods.

The main empirical trend is interesting: prototype-based approaches appear consistently stronger than repeated fine-tuning baselines. This is visible in **Table 2** and **Table 3**, where SimpleCIL and SimGCL are generally much stronger than standard GNN CL methods and than several GLM baselines. Even if one is skeptical about some causal interpretations, the result itself is valuable and suggests that freezing representations after initial adaptation may indeed be a promising recipe for rehearsal-free GCL.

The proposed SimGCL is simple and operationally attractive. The architecture in **Figure 2** on **Page 5** is easy to understand, and the design choice, first-session instruction tuning followed by prototype classification, is computationally cleaner than methods that keep adapting a heavy LLM across all sessions. The simplicity is a plus here; the paper is not trying to hide behind excessive machinery.

I also appreciate that the paper does not oversell graph-enhanced LLMs as automatically better. The results in **Table 2** and **Table 3** are actually somewhat humbling for current GLM designs, and that negative finding is useful. A benchmark paper that reports inconvenient outcomes is more credible than one that only arranges wins.

## Weaknesses
1. **The core claim about "task ID leakage" is plausible, but the paper does not establish it with the level of rigor needed for such a strong indictment of prior evaluation practice.**  
   The argument is introduced in **Section 3.1** on **Pages 3-4**, and visually summarized in **Figure 1**. However, the empirical evidence in **Table 1** on **Page 4** is not really an apples-to-apples test of the claimed leakage mechanism. The table reports performance for TPP, mean pooling, and an MLP under local testing, but it does not explicitly report the task-ID prediction accuracy for each method, despite the text emphasizing "100% task ID prediction accuracy". It also does not compare against a controlled variant where local testing is modified to remove graph-identity cues while keeping other factors fixed. As written, the paper shows that local subgraphs can make task separation easy, but it falls short of proving that the benchmark is fundamentally invalid in all its current uses. That matters because a major contribution of the paper is a critique of existing setups, and such a critique needs to be demonstrated more carefully than a single proxy table.

2. **The evaluation protocol may overcorrect by removing inter-task edges and rebalancing classes, which weakens the claim of being "more realistic".**  
   On **Page 4**, the paper states that to avoid previous knowledge leakage and class imbalance, it excludes inter-task edges and removes classes with insufficient samples. I understand the motivation, but this is a substantial intervention on the data-generating process. In many real streaming graphs, inter-session edges are not noise, they are the graph. Removing them may make the benchmark cleaner, but it also changes the problem and potentially suppresses the exact structural transfer that graph methods are supposed to exploit. Likewise, filtering classes and enforcing unified sample sizes improves comparability but reduces ecological validity. The paper repeatedly frames global testing as "more realistic", yet the benchmark construction itself is heavily sanitized. This mismatch matters because the paper is not just proposing a method, it is trying to redefine what proper GCL evaluation should look like.

3. **The proposed method is effective, but the novelty is fairly modest and the paper does not convincingly separate method contribution from benchmark/protocol contribution.**  
   SimGCL, described in **Section 3.3** on **Page 5**, is essentially a combination of graph-text prompting, first-session LoRA tuning, and prototype-based classification. Each ingredient is standard on its own, and even the high-level recipe, adapt a pretrained model once, then use prototypes to avoid forgetting, is already central to methods like SimpleCIL. The main novelty seems to be adapting this recipe to graph-text prompts. That can still be publishable in a benchmark paper, but then the paper needs to be careful not to frame SimGCL as a large algorithmic advance. Right now the narrative oscillates between benchmark paper, protocol critique, and new method paper, and I am not convinced all three parts are equally strong.

4. **The mathematical specification of the prototype classifier is incomplete/inconsistent.**  
   In **Equation (1)** on **Page 5**, the prototype for class \(i\) is defined as
   \[
   \mathbf{c}_i = \frac{1}{K}\sum_{j=1}^{|\mathcal{Y}_b|}\mathbb{I}(y_j=i)\mathbf{h}_j,
   \]
   where \(K = \sum_{j=1}^{|\mathcal{Y}_b|}\mathbb{I}(y_j=i)\). This is fine as a per-session prototype, but the text says SimGCL "progressively generates class prototypes across sessions". It is unclear whether, when an old class reappears, the prototype is recomputed from all historical labeled samples, updated via a running average, or stored once and never revisited. For a continual-learning method, this distinction is not cosmetic, it defines the memory assumptions.  

   More importantly, **Equation (2)** is written as
   \[
   \hat{y}_{i,j} = \frac{\mathbf{h}_i \cdot \mathbf{c}_j}{\|\mathbf{h}_i\|\cdot\|\mathbf{c}_j\|}\cdot \tau.
   \]
   This is a scaled cosine similarity, not a probability, despite the surrounding sentence saying "its probability of belonging to class \(j\) is formulated as follows". If the authors intend logits, say logits. If they intend probabilities, a normalization such as
   \[
   p(y=j\mid \mathbf{h}_i)=\frac{\exp(\tau \,\cos(\mathbf{h}_i,\mathbf{c}_j))}{\sum_{k}\exp(\tau \,\cos(\mathbf{h}_i,\mathbf{c}_k))}
   \]
   is needed. This matters because the classifier description is otherwise mathematically inaccurate, and the role of \(\tau\) is underspecified.

5. **There are several notation and formulation problems that reduce confidence in the technical precision.**  
   In the FSNCIL formulation on **Page 3**, the paper writes \(\mathcal{G}_{s_i}\cap \mathcal{G}_{s_i} = \mathcal{C}_{s_i}\cap \mathcal{C}_{s_j} = \emptyset\) for all \(i\neq j\), which is clearly malformed, the first term should presumably involve \(\mathcal{G}_{s_j}\). In **Section 3.1**, the notation for the global class set is also awkward: \((\mathcal{C}_{q_j} = \bigcup_{j = 1}^j \mathcal{C}_{s_j})\), where the index is reused in a confusing way. These are not just typography nits. In a paper whose main contribution partly rests on precise benchmark definitions, notation sloppiness directly hurts reproducibility and confidence.

6. **The empirical comparison is broad but not always fair or sufficiently transparent.**  
   **Table 2** and **Table 3** compare many baselines, which is good, but the methods operate with different backbones and capacities. According to **Table 7** on **Page 21**, BERT is 110M, RoBERTa is 355M, and LLaMA is 8B, while several graph baselines use shallow GCNs. Unsurprisingly, pretrained language models can dominate text-rich node classification. The paper does include this fact, but then some conclusions about "LLMs alleviate catastrophic forgetting" blur together the benefits of pretraining, model scale, and the actual continual-learning strategy. A cleaner comparison would isolate whether the gain comes from the continual-learning design rather than simply replacing a small GNN with a much larger pretrained backbone. This is especially important because **Figure 3** on **Page 8** explicitly shows that larger LLMs perform better. That figure is useful, but it also undercuts causal claims that the method, rather than scale, is doing most of the work.

7. **Some of the strongest claims in the discussion are too causal relative to the evidence provided.**  
   For example, on **Pages 6-8**, the paper attributes GLM underperformance to "inter-modal misalignment", "overfitting tendencies", or sparse structural information. These are plausible hypotheses, but the presented results are largely observational. **Table 2**, **Table 3**, and **Table 4** do show patterns, yet they do not isolate these mechanisms. The same issue appears in the interpretation of Arxiv-23 and long-session settings. The paper often jumps from correlation to explanation. For a benchmark paper, that is risky, because readers may take these interpretations as established findings when they are really post hoc stories.

8. **The headline gains should be contextualized more carefully.**  
   The abstract and introduction emphasize improvements of around 20%. In the main tables, SimGCL is indeed substantially stronger than GNN baselines, but a more relevant comparison is often against SimpleCIL, since both are prototype-based pretrained-model approaches. On some datasets the gap is large, but on others it is much smaller, and there are settings where SimGCL still struggles badly, especially on Arxiv-23 and the long-session cases in **Table 4** on **Page 8**. The claim is directionally true, but the framing is a bit selective. For the scientific value of the paper, it is more important to understand when graph prompting materially helps beyond SimpleCIL than to emphasize the largest win over weaker rehearsal-free GNN baselines.

9. **The presentation in the main paper is uneven, with too many grammatical and naming inconsistencies for a benchmark paper.**  
   Examples include "consists an ordered sequence" on **Page 2**, "overperform" on **Page 7**, inconsistent metric notation between \(A,\ A_N,\ \hat{A}\), and naming mismatches such as GCNLLMEmb / GCN\(_{Emb}\) / GCNsub in different places. These are individually small, but together they make the paper feel less polished than it should be for a benchmark submission. Benchmark papers are often used as references by others, so exactness in notation, dataset setup, and method naming really matters.

10. **The figure-based evidence is mixed: useful for intuition, weak for decisive support.**  
   **Figure 2** on **Page 5** explains the two-stage SimGCL pipeline clearly, which helps. By contrast, **Figure 3** on **Page 8** is used to support scaling claims, but it only shows Arxiv and only compares backbone size for SimpleCIL and SimGCL. That is suggestive, not systematic. Likewise, the qualitative embedding visualization in **Figure 4** in the appendix is visually favorable to SimGCL, but since it depends on dimensionality reduction choices and lacks quantitative cluster metrics in the main paper, it should not be leaned on too heavily. In short, the figures help readability, but they do not fully close the evidentiary gaps behind some of the paper's stronger conclusions.

## Questions
1. For the local-testing critique, can the authors provide a more direct demonstration of leakage in the main paper, for example explicit task-ID prediction accuracy for TPP, mean pooling, and additional controls, rather than relying mainly on downstream accuracy in **Table 1**? This would substantially strengthen the central benchmark claim.

2. Please clarify the exact memory assumptions of SimGCL. In **Equation (1)** and **Section 3.3**, are class prototypes computed from all labeled examples seen so far, only from the session in which the class first appears, or from a maintained running statistic? This is crucial for judging whether the method is truly rehearsal-free and what state must be stored.

3. In **Equation (2)**, is \(\hat y_{i,j}\) intended to be a logit/score or a probability? If it is a probability, please give the missing normalization. If it is a score, please correct the wording in the paper. A precise classifier definition would improve both soundness and reproducibility.

4. The paper removes inter-task edges to avoid knowledge leakage. Can the authors clarify whether SimGCL still retains its advantage when global testing is used but inter-session edges are preserved? This would help separate benchmark cleanliness from real-world applicability.

5. Since **Table 2** and **Table 3** suggest that SimpleCIL is already a very strong baseline, could the authors include a sharper ablation isolating the incremental value of graph prompts over plain text prompts, while keeping the same LLM, LoRA setup, and prototype classifier? Right now the paper demonstrates that SimGCL works, but not as cleanly why each component is necessary.

6. The paper attributes several trends to graph density, session length, and overfitting. Can the authors indicate which of these explanations are empirically tested versus speculative interpretation? Even a short caveat in the camera-ready version would make the conclusions more trustworthy.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are raised by the main paper. The study uses public graph datasets and focuses on benchmark evaluation and rehearsal-free continual learning methods. The broader-impact discussion does mention privacy, bias, and adversarial risks, which is appropriate, but nothing in the main paper appears to require formal ethics escalation.

## Soundness Rating
2: fair. The paper has substantial empirical value and the central observations are plausible, but the benchmark critique is not demonstrated as rigorously as claimed, and the method description contains mathematical and protocol ambiguities that should be cleaned up.

## Presentation Rating
2: fair. The overall structure is understandable and some figures, especially **Figure 1** and **Figure 2**, are helpful, but notation issues, wording imprecision, and inconsistent naming reduce clarity.

## Contribution Rating
3: good. The combination of protocol critique, broad benchmark construction, and a simple strong baseline/method is useful to the community, even though the algorithmic novelty of SimGCL itself is limited and several claims are overstated.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and has clear community value, especially in questioning existing GCL evaluation and benchmarking pretrained models. However, the main protocol critique needs more rigorous support, the method is simpler than the framing suggests, and the mathematical/presentation issues are serious enough that I do not think the current version is ready without revision.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with continual learning, graph ML, and pretrained-model evaluation, and I checked the main technical details and empirical evidence carefully.