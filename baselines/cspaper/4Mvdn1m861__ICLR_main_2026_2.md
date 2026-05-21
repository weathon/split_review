---
job_id: c1c7c4a0-aae0-4d28-b013-804f2f77978a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4Mvdn1m861.pdf
paper: TokenCount: A Training-Free Framework for Object Counting by Interpreting Output Tokens
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies a training-free vision method built on SAM for class-agnostic object counting, with emphasis on representations, prompting, and token interpretation.

## Minimum Quality
Pass ✅. The submission contains the necessary scientific structure, including abstract, introduction, related work, method, experiments, quantitative and qualitative results, discussion, and conclusion. While there are notable weaknesses in novelty, methodological specification, and exposition, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious formatting, or content targeting automated reviewers in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes **TokenCount**, a training-free class-agnostic object counting framework built on SAM. The method combines: (i) a probabilistic prompt generation mechanism that samples prompts from a similarity-derived spatial distribution and updates that distribution iteratively, and (ii) an output token-based verification stage that uses SAM decoder output tokens, compared via the TS-SS similarity metric, to determine whether prompted regions correspond to target instances.

The paper evaluates the approach on FSC-147 and CARPK, compares against both supervised and training-free baselines, and includes ablations on verification metrics, iteration/prompt budgets, and a comparison between output-token and image-embedding verification spaces.

## Strengths
1. **The paper targets a relevant and timely problem setting**. Training-free counting with foundation models is an active area, and the goal of obtaining competitive counting performance using only SAM, without extra learned modules or auxiliary encoders, is meaningful for the ICLR audience.

2. **The high-level idea is reasonably intuitive and practically motivated.** The separation into prompt exploration and candidate verification is sensible. In particular, the motivation that image-embedding similarity can be ambiguous, while decoder output tokens may contain more prompt-conditioned information, is plausible and well aligned with how SAM is architected.

3. **The empirical results are competitive in parts.** In **Table 1 (Page 6)**, the method improves substantially over plain SAM and prior SAM-only baselines such as TFOC on both datasets. On CARPK, the reported **MAE 4.68 / RMSE 6.13** is strong for a training-free SAM-only method and substantially better than TFOC. Even on FSC-147, the reported MAE improves over OmniCount and TFCounter, though not over TFCAC.

4. **The ablations are directionally useful.**  
   - In **Table 3 (Page 8)**, the comparison among dot product, cosine, L2, and TS-SS at least attempts to isolate the effect of the chosen verification metric.  
   - In **Table 4 (Page 8)**, the trade-off between iteration count, prompts per iteration, and mean prompt count provides some visibility into the accuracy-efficiency frontier, which is important for a sampling-heavy training-free method.  
   - In **Table 5 (Page 8)**, the output-token versus image-embedding comparison is directly tied to the central claim of the paper.

5. **Some figures help communicate the intuition of the method.**  
   - **Figure 2 (Page 4)** is helpful in showing the overall workflow, especially the interaction between probabilistic prompt generation, verification, and probability-distribution updates across iterations.  
   - **Figure 3 (Pages 4-5)** is a useful visual aid for understanding the intended update rule on the sampling distribution after positive and negative verification.  
   - **Figure 5 (Page 9)**, while not definitive evidence, provides an intuitive illustration of why output-token space may be more separable than raw image-embedding space for the prompted candidates considered by the method.

6. **The paper does make an effort to discuss limitations.** The discussion section acknowledges failure modes in dense small-object scenes where SAM itself struggles to segment boundaries, which is an honest and relevant limitation for a SAM-based counting pipeline.

## Weaknesses
1. **The core methodological contribution feels narrower than the paper’s framing suggests, and the novelty is not convincingly differentiated from closely related training-free SAM-based counting work.**  
   The paper positions itself as directly repurposing SAM via output-token verification and probabilistic prompting, but much of the pipeline is still built from familiar ingredients: exemplar-conditioned similarity maps, iterative prompt sampling, NMS, and a hand-chosen distance metric. The paper does not make a sufficiently sharp case for why using decoder output tokens constitutes a qualitatively new counting formulation rather than a different feature choice inside an existing prompt-and-verify pipeline. This matters because the empirical gains over the most relevant baselines are mixed: in **Table 1**, the method beats TFOC and several other methods, but still trails TFCAC on both FSC-147 and CARPK. So the paper is not in a position where very strong results compensate for a somewhat incremental conceptual step.

2. **The mathematical formulation in Section 3.1 is underspecified and somewhat inconsistent, which makes the method hard to verify or reproduce from the main paper.**  
   On **Page 4**, the sequence
   \[
   \mathbf{F}^I = f(\mathbf{l}),\quad \mathbf{M}=g(\mathbf{F}^I,e),\quad \mathbf{F}^E=\operatorname{nonzero}(\mathbf{F}^I\odot \mathbf{M}^R),\quad \boldsymbol{S}=\cos(\mathbf{F}^I,\operatorname{mean}(\mathbf{F}^E))
   \]
   leaves several important details unspecified:
   - What exactly is the tensor shape of \(\boldsymbol{S}\)? The text calls it a “similarity matrix”, but given the inputs it appears to be a per-location similarity map over the \(64\times 64\) grid. That should be stated explicitly.
   - The operator \(\operatorname{nonzero}(\cdot)\) is not a mathematically standard way to define masked feature extraction. Does it return all spatial vectors whose resized mask entry is nonzero? If the resized mask is soft-valued, what threshold is used?
   - The cosine similarity \(\cos(\mathbf{F}^I,\operatorname{mean}(\mathbf{F}^E))\) is ambiguous because \(\mathbf{F}^I\in\mathbb{R}^{64\times 64\times 256}\), while \(\operatorname{mean}(\mathbf{F}^E)\in\mathbb{R}^{256}\). Presumably the cosine is computed independently at each spatial location:
     \[
     S_{ij} = \frac{\langle \mathbf{F}^I_{ij,:}, \bar{\mathbf{f}}^E \rangle}{\|\mathbf{F}^I_{ij,:}\|\,\|\bar{\mathbf{f}}^E\|},
     \]
     but that is never written.
   - The paper says prompts are sampled from a multinomial distribution based on \(P(\mathbf{l};\mathbf{e})\), but does not specify whether sampling is with or without replacement within an iteration, how duplicate sampled coordinates are handled, or whether any top-\(k\) truncation is applied before sampling.  
   These omissions are not cosmetic. They directly affect the produced prompt sets and therefore the reported counting performance.

3. **The verification stage is not rigorously justified, and the choice of TS-SS is only weakly supported.**  
   The central claim in Section 3.2 is that output tokens encode “semantic (angular) and positional (magnitudinous)” information and therefore dot product, cosine, and Euclidean distance are inadequate, while TS-SS is more appropriate. This argument is asserted rather than demonstrated. There is no formal analysis of why token norm should correspond to positional content, why angular information should correspond to semantic content, or why the particular hybrid
   \[
   \text{TS-SS}(\mathbf{a},\mathbf{b})=\text{TS}(\mathbf{a},\mathbf{b})\cdot \text{SS}(\mathbf{a},\mathbf{b})
   \]
   is the right functional form for SAM decoder tokens. In fact, **Table 3 (Page 8)** shows only a very small MAE gap between cosine similarity (16.48), L2 distance (16.53), and TS-SS (16.25). That is a marginal gain relative to the paper’s strong narrative that standard metrics are fundamentally inadequate. If the main conceptual selling point is “token geometry requires a new metric”, the empirical support here is thinner than advertised.

4. **The paper repeatedly makes efficiency claims without a sufficiently fair or complete efficiency evaluation.**  
   The method is described as computationally efficient because it avoids auxiliary encoders and costly post-processing, yet the proposed pipeline is still iterative and prompt-heavy. **Table 4 (Page 8)** reports mean prompt counts up to **1438.22** on FSC-147 for the best setting, which is not obviously cheap. The main text states an average processing time of **1.69 seconds per image on FSC-147** (**Page 6**), but there is no apples-to-apples timing comparison against TFOC, OmniCount, TFCAC, or any other baseline under similar hardware and implementation conditions. Saying the method is “more than twice as fast” than TFCAC on CARPK, without presenting an explicit comparison table with hardware, image size, prompt count, and implementation details, is not enough. Since computational efficiency is one of the headline claims, the evidence should be much stronger.

5. **The evaluation setup leaves important ambiguities, especially around hyperparameter tuning and threshold selection.**  
   On **Page 6**, the paper says, “Based on validation experiments, we set the token verification threshold to 300.” But the validation protocol is not described. FSC-147 and CARPK evaluation conventions matter a lot here. What validation split is used, was the threshold tuned per dataset, is \(\tau\) also tuned, and how sensitive is performance to these values? For CARPK, the paper says it “randomly selected 12 objects from the training set to use as exemplars,” but does not explain whether this sampling is fixed across runs, whether performance is averaged over multiple random selections, or how much variance arises from exemplar choice. This is particularly important for a few-shot or exemplar-based counting paper, where exemplar selection can materially change outcomes.

6. **Some of the empirical claims are overstated relative to what the tables actually show.**  
   The abstract claims “superior accuracy” and says the method “outperform[s] existing training-based and training-free counting methods,” but **Table 1 (Page 6)** does not support that statement globally. On FSC-147, LOCA, PseCo, SAFECount, BMNet+, and TFCAC all have better MAE than the proposed method. On CARPK, TFCAC is still better. A more accurate claim would be that the method is competitive and strong among SAM-only, training-free approaches. This distinction matters. Overselling can mislead readers about the actual contribution level.

7. **The quantitative evidence is incomplete for the strongest claim that output-token space is better than image-embedding space.**  
   **Table 5 (Page 8)** compares output token space and image embedding space only for the authors’ own method, showing MAE **16.25 vs 16.94** on FSC-147. That is a modest gain. The paper then makes a broad claim that output-token verification “clearly distinguish[es] similarities between objects” better than image embeddings. But there is no broader study across multiple thresholds, multiple metrics, or multiple datasets to show robustness of this conclusion. **Figure 5 (Page 9)** presents PCA plots with apparently cleaner separation in token space, but PCA visualizations can be highly selective and are not quantitative evidence by themselves. At minimum, I would have liked to see a more systematic comparison, for example precision/recall of positive-vs-negative verification under the different spaces, or sensitivity curves over the verification threshold.

8. **Presentation quality is uneven, and several parts of the paper are harder to parse than they should be.**  
   There are many grammatical issues and awkward phrasings throughout the paper, such as “a output token-based verification stage,” “used for criterion,” “works correctly” as a conclusion from a trend in Table 4, and several claims that read more like intuition than analysis. Section 3.2 in particular is verbose but still imprecise about the actual procedure. For example, it never clearly states the decision rule for positive verification in notation, something as simple as whether a candidate token \(\mathbf{t}\) is accepted when
   \[
   \min_{r\in \mathcal{R}} d_{\text{TS-SS}}(\mathbf{t}, \mathbf{r}) < \delta
   \]
   or via nearest-neighbor ranking, averaging over exemplars, or some other criterion. Given that this is the heart of the method, the omission is serious.

9. **The paper’s own figures reveal limitations that deserve more analysis than they receive.**  
   - **Figure 4 (Page 7)** shows nice success cases, especially for CARPK, but it is almost entirely celebratory. It would be more convincing if the main paper also showed representative near-failure or ambiguous cases rather than only clean examples.  
   - The appendix **Figure 8 (Page 12)** does show failure cases in dense overlapping scenes and with atypical object sizes, but the main paper reduces these to a short discussion. These failures are not peripheral, they are central to SAM-based counting. The paper should have analyzed whether the bottleneck is the mask generator, the prompt sampling process, or the token-verification metric. Right now, the reader is left with “SAM fails” as a catch-all explanation, which is too shallow.

10. **The one-shot results in Table 2 are not especially strong, which weakens the broader claim of general effectiveness.**  
   In **Table 2 (Page 7)**, the method is clearly behind TFCAC and LOCA on FSC-147 one-shot, and its RMSE is particularly poor (**135.86**). This does not invalidate the paper, but it suggests the approach is less robust when exemplar information is more limited. Since the method’s premise is exemplar-guided training-free counting, this deserves more discussion than the brief “results are promising.” A more candid analysis would help readers understand where the method is actually useful.

11. **Some implementation details with direct impact on results are relegated to vague prose rather than specified algorithmically.**  
   The probability update rule after positive and negative verification is verbally described around **Figure 3 (Pages 4-5)**, but the exact update is missing. If a region is negative, by how much is the probability reduced? Is it set to zero, multiplied by a constant \(\gamma<1\), or decremented additively? Is the map renormalized after each update? Similar issues apply to the NMS procedure on **Page 6**: the IoU threshold is not given. These details are not optional, because iterative sampling procedures can be highly sensitive to them.

## Questions
1. **Please specify the verification rule mathematically.**  
   Given a sampled prompt and its output token, how exactly is the positive/negative decision made against the current exemplar list? Is it nearest-neighbor TS-SS similarity, average similarity, minimum distance to any exemplar token, or something else? What is the exact role of the threshold 300 in this decision?

2. **Please clarify the probability update equations after each iteration.**  
   The text and **Figure 3** suggest that positive regions are zeroed out and negative regions are down-weighted, but the exact update rule is missing. Writing this explicitly would greatly improve reproducibility. For example, is the update something like
   \[
   P_{m+1}(u)\propto P_m(u)\cdot \mathbf{1}[u\notin \mathcal{M}^{+}] \cdot \gamma^{\mathbf{1}[u\in \mathcal{M}^{-}]},
   \]
   with renormalization afterwards? If not, what is the actual rule?

3. **How sensitive is performance to the token threshold and temperature \(\tau\)?**  
   Since the token verification threshold is chosen based on “validation experiments” (**Page 6**), a sensitivity plot or small ablation over threshold and \(\tau\) would materially increase confidence. Right now, it is hard to know whether the method is robust or fairly brittle.

4. **How stable are the CARPK results with respect to exemplar selection?**  
   Because the paper uses 12 randomly selected exemplars from the training set, please report whether the CARPK numbers are from a single draw or averaged over multiple draws. If they are from a single draw, variance could be substantial.

5. **Can the authors provide a fair efficiency comparison against the closest baselines?**  
   Since efficiency is repeatedly emphasized, a table reporting runtime, number of prompts, and hardware for TFOC / OmniCount / TFCAC / Ours would be very helpful. This could change my view if it shows a substantial and robust practical advantage.

6. **Can the authors better justify why output-token magnitude should be interpreted as positional information?**  
   This point is central to the TS-SS motivation in Section 3.2, but currently it reads as intuition. Even a modest empirical analysis, for instance correlations between token norms and prompt displacement or localization consistency, would make the argument more convincing.

7. **Could the authors analyze failure modes more granularly?**  
   In the failure cases shown later in the paper, is the dominant source of error poor SAM masks, poor prompt coverage, or incorrect token verification among visually similar instances? A breakdown would help determine whether the proposed token verification is truly the limiting factor.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns stood out from the submission. The work is a computer vision counting method evaluated on standard benchmark datasets, and the paper does not introduce a new dataset, human-subject collection procedure, or explicitly high-risk deployment claim.

## Soundness Rating
2: fair. The method is plausible and supported by some experiments, but several key algorithmic details are underspecified, the central metric choice is only weakly justified, and some empirical claims are stronger than what the tables substantiate.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures help, but important notation and decision rules are missing or ambiguous, and the writing often overstates conclusions.

## Contribution Rating
2: fair. There is a useful empirical idea here, especially the use of SAM output tokens for verification in a training-free counting pipeline, but the novelty relative to nearby SAM-based counting work is not sharply established and the gains are not decisive.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is relevant and has some promising ingredients, especially the attempt to exploit decoder output tokens directly and the decent empirical performance on CARPK. However, I do not think the current version clears the bar for ICLR main track. The main reasons are: incomplete specification of the algorithm, limited justification for the TS-SS verification metric, insufficiently supported efficiency claims, and a contribution story that feels somewhat narrower than the paper presents. With a cleaner mathematical specification, stronger efficiency comparisons, and a more rigorous analysis of why output-token verification really matters, this could become a more convincing paper.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the method description, equations, figures, and tables, but some ambiguity in the paper itself limits how much can be verified from the main text alone.