---
job_id: aa8329ad-c676-4c36-b5ac-3717bd02a6a9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 3V559xWIWc.pdf
paper: SALF & TALF: Optimized Loss Function and Drafting for Tree-Based Speculative Decoding
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies LLM inference acceleration through speculative decoding, draft-model training objectives, and tree-structured decoding algorithms, all of which fall under general machine learning, language modeling, optimization, and ML systems.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, including abstract, introduction, method, related work, experiments, quantitative results, and conclusion. While I have substantial concerns about the rigor and completeness of several claims, especially around the algorithmic objective and empirical isolation of SALF versus TALF, these are review-time weaknesses rather than desk-reject-level failures.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious embedded text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies tree-based speculative decoding for LLM inference and argues that prior draft-model training objectives are mismatched with tree-structured inference. It proposes a tree-aware loss function, TALF, that aggregates distillation losses over nodes in a target-generated draft tree, and a drafting strategy, SALF, that stops tree expansion when estimated further gains become too small. Experiments on three target models and several tasks report consistent end-to-end speedups over EAGLE-2 and HASS.

## Strengths
The paper tackles a real and important bottleneck in speculative decoding. The central motivation, namely that sequence-style training is misaligned with tree-based inference, is sensible and well articulated in Section 3.1.

The empirical gains in **Table 1 (Page 7)** are non-trivial and consistent across all tested models, tasks, and both greedy and non-greedy decoding. In particular, the paper does not rely on a single cherry-picked benchmark; the improvements over EAGLE-2 and HASS appear across MT-bench, HumanEval, GSM8K, Alpaca, and CNN/DM. That breadth is a genuine strength.

The decomposition in **Table 2 (Page 8)** is useful. It gives at least some attempt to separate the effects of the training loss from the tree-construction strategy, instead of only reporting the combined SALF&TALF system. This is important because otherwise the paper would be much harder to interpret.

**Figure 1 (Page 3)** is one of the clearer parts of the paper. It makes the distinction among EAGLE, HASS, and TALF training more concrete, especially the fact that TALF supervises multiple tree nodes rather than a single sequence rollout. For a paper with several moving parts, that diagram materially helps the reader.

**Figure 2 (Page 4)** also supports the motivation reasonably well. Figure 2(a) shows that lower-ranked tokens are not negligible in the final tree, and Figure 2(b) provides evidence that prior objectives degrade on such branches. Even if I have reservations about the exact experimental framing, the figure does substantiate the paper’s core intuition better than a purely verbal argument would.

The SALF idea is practically motivated. The paper correctly notes that maximizing the probability mass of the candidate tree is not the same as minimizing wall-clock latency, and this systems-oriented perspective is valuable for deployed decoding.

The method is relatively lightweight from an architectural standpoint. The authors improve training and tree construction without changing the draft model architecture, which is a pragmatic contribution if the reported gains hold broadly.

## Weaknesses
1. **The paper bundles two contributions, SALF and TALF, but the causal attribution remains weaker than the headline presentation suggests.**  
   The title and abstract sell a paired system, and the strongest numbers are for the combination. However, the evidence that each component independently advances the state of the art is still somewhat incomplete in the main paper. **Table 2 (Page 8)** is a helpful start, but it only reports one target model, Deepseek-R1-Distill-Llama-8B. Since **Table 1 (Page 7)** shows large variation by model family, especially much larger relative gains on Llama3-8B and DeepSeek than on Llama2-7B, it is hard to know whether the SALF-versus-TALF story generalizes similarly across models. This matters because the central scientific claim is not merely that one tuned system works, but that tree-aware training and gain-aware stopping are both principled improvements. Right now, the isolation is suggestive rather than fully convincing.

2. **The mathematical formulation of TALF is underspecified relative to the actual EAGLE/HASS draft model described earlier, especially with respect to feature inputs and self-conditioning.**  
   In Section 2.2, the draft model input is explicitly \((x_{2:s}, f_{1:s-1})\), and HASS’s whole point is to train with self-generated \(f^{(d)}\) features. But in **Algorithm 1 (Page 5)**, line 6 simply writes \(p^{(d)}_{\mathrm{child}(n)} \leftarrow D(x[n])\) with “input features omitted for brevity.” That omission is not cosmetic, it hides a key part of the training distribution. TALF’s claimed benefit depends on how the model is rolled out along each branch while feeding back speculated features. Without a precise definition of the computational graph, the objective is not fully specified.  
   More concretely, if a node \(n\) corresponds to a path \(x[n]\), then the actual draft-state computation should distinguish between target-derived features on the prefix and autoregressively predicted features on the path suffix. A more faithful notation would be something like
   \[
   (p^{(d)}_{\mathrm{child}(n)}, f^{(d)}_{n}) = D\!\left(x_{2:|x[n]|}, \hat f_{1:|x[n]|-1}\right),
   \]
   where \(\hat f\) mixes target features before the root and self-generated draft features along the branch. As written, the algorithm obscures exactly the mechanism that allegedly resolves training-inference mismatch. This is not a pedantic issue, it affects reproducibility and conceptual correctness.

3. **The loss definition for TALF is surprisingly narrow given the paper’s earlier discussion of EAGLE and HASS, and the ablation around removing feature regression is not sufficient.**  
   On **Page 5**, the authors state that TALF does not use feature regression at all and that “training solely on the token probability distributions across multiple nodes was sufficient.” This is potentially interesting, but it is also a fairly strong claim because EAGLE and HASS explicitly use both \(\mathcal{L}_{\mathrm{reg}}\) and \(\mathcal{L}_{\mathrm{cls}}\). The paper does not present a direct ablation of TALF-with-regression versus TALF-without-regression, nor EAGLE/HASS without regression under matched settings. Therefore it is hard to tell whether the gain comes from tree supervision, from removing a harmful regression term, or from both. Since the proposed loss is one of the paper’s main contributions, this missing ablation matters.

4. **The main experimental evidence focuses almost entirely on speedup and \(\tau\), but the claim of “without any generation quality degradation” in the conclusion is not really established in the main paper.**  
   The paper reports latency speedups and mean generation length. Those are necessary metrics for speculative decoding, but they are not the same as output quality or exactness. For standard speculative decoding, one normally wants either a proof of distributional equivalence to the target model under the chosen acceptance rule, or explicit quality metrics showing that the served outputs are unchanged. Here the paper benchmarks on HumanEval, GSM8K, MT-bench, Alpaca, and CNN/DM, yet the reported tables show only speedup and \(\tau\), not task accuracy/pass@k/ROUGE/judge score. Since the conclusion on **Page 9** states “without any generation quality degradation,” I expected at least some direct evidence in the main paper. The omission is particularly noticeable because the tree construction changes can affect the candidate set and thus practical decoding behavior.

5. **SALF’s stopping rule is heuristic with respect to the actual objective of wall-clock speedup, even though the paper frames it as a principled gain estimate.**  
   In Section 3.3, the stopping criterion is based on the probability sum of nodes in \(\mathcal{D}\). Theorem 1 then shows this sum decreases monotonically. But monotonic decrease of
   \[
   S_i = \sum_{(pr,n)\in \mathcal D_i} pr
   \]
   is not, by itself, a guarantee that stopping at threshold \(th\) is near-optimal for latency. The actual optimization target should involve at least a trade-off between added drafting cost and expected increase in accepted tokens, perhaps something resembling expected benefit per unit time. The current paper does not derive such an objective; instead, it uses a monotonic surrogate and tunes \(th\) empirically. That is fine as an engineering heuristic, but the prose sometimes oversells it as a more direct measure of “further gains” than is justified. This gap between the optimization proxy and the true latency objective should be stated more candidly.

6. **The theorem/proof discussion is a bit too neat for the actual algorithmic setting, and some assumptions are buried or idealized.**  
   The main text on **Page 6** presents Theorem 1 under the condition \(B < |\mathrm{Vocab}|\), while Appendix B and C introduce monotonic-tree assumptions and implementation caveats about not pushing all vocabulary children. The proof may be acceptable under the stated abstraction, but the practical algorithm used in LLM systems almost certainly truncates candidate children aggressively. Once this happens, the equivalence between the abstract queue dynamics and the practical implementation deserves more careful justification than the brief Appendix-C statement that the implementation “does not affect correctness.” That is a strong claim.  
   Relatedly, **Algorithm 2 (Page 6)** says “Ensure: Tree \(\mathcal{G}\) containing the top-\(N\) high-probability nodes,” but the algorithm with SALF clearly does not ensure top-\(N\) nodes in general, because it may stop early. The “Ensure” statement is therefore misleading unless it explicitly refers to the no-early-stopping variant. This is a mathematical-specification issue, not just wording.

7. **There are presentation-level inconsistencies and ambiguities in Algorithm 2 that make the method harder to trust than it should be.**  
   In **Algorithm 2 (Page 6)**, \(\mathcal{G}\) is initialized with the root node on line 1, and then nodes popped from \(\mathcal{Q}\) are pushed into \(\mathcal{G}\) again on line 8. It is unclear whether the root is double-counted, whether \(\mathcal{G}\) is intended to include expanded nodes only, or whether the initialization is schematic. Also, line 5 says “for \(b\) in 0..B do,” which conventionally means \(B+1\) iterations rather than \(B\). These are fixable issues, but in an algorithm-heavy paper they matter because they blur the exact semantics.

8. **The “misalignment” evidence in Figure 2 is informative but not fully controlled, and the interpretation is a bit stronger than what the experiment actually establishes.**  
   In **Figure 2(b) (Page 4)**, TALF appears better on lower-ranked branch conditioning than EAGLE/HASS in both accuracy and ECE. That supports the narrative. But the setup probes the draft model under self-conditioning on the \(n\)-th ranked token from its own previous prediction, then compares to a target-generated next token \(\tilde x_{s+2}\). This is one proxy for branch robustness, not a direct measure of full tree alignment or acceptance probability in the actual verification pipeline. In other words, the figure motivates TALF, but it does not by itself prove that the training objective matches the inference objective better in the exact operational sense. I would prefer more caution in how this figure is used rhetorically.

9. **The empirical study lacks variance estimates or repeated-run statistics for the headline speedups.**  
   All tables report single numbers. Since end-to-end latency can fluctuate with implementation details, prompt lengths, and GPU scheduling noise, confidence intervals or standard deviations would strengthen the claims. This is especially relevant when some improvements over HASS are modest, for example the **6.5% mean gain in Table 1 for Llama2-7B, greedy decoding (Page 7)**. Without run-to-run variability, it is hard to judge how robust those margins are.

10. **Hyperparameter tuning appears somewhat asymmetric and may advantage the proposed method.**  
   In Section 4.1, SALF uses \(th=0.6\) by default, and **Table 4 (Page 9)** shows threshold sensitivity. But comparable sensitivity studies for baseline tree-construction parameters are not shown in the main paper. Likewise, TALF uses \(k=4\) for training, supported by **Table 3 (Page 8)**, whereas HASS is essentially represented as top-1. If the training-tree width is a key degree of freedom, the comparison would be fairer if the paper more explicitly discussed whether HASS could also benefit from wider or alternative branch-aware supervision variants short of full TALF. The current setup is plausible, but not airtight.

11. **The literature positioning is reasonable for cited 2024-2025 work, but the novelty claim should still be phrased more carefully as an incremental systems-method improvement rather than a fundamental reframing.**  
   The paper is strongest when presented as a well-motivated refinement of EAGLE/HASS-style draft training and dynamic tree construction. It is less convincing when it suggests a broader methodological break. Tree-based speculative decoding, dynamic tree search, and distillation-based alignment are already well established in the cited prior work, and the paper’s contribution is to better match the training target and to stop search earlier. That is a useful contribution, but the framing should stay disciplined.

## Questions
1. Please make the TALF training objective fully explicit in the main paper. For a node \(n\), what exactly is the input to the draft model, including target-derived versus self-generated features along the branch? A precise equation for the rollout would substantially increase my confidence.

2. Can the authors provide a direct ablation for TALF with and without feature regression, and ideally HASS/EAGLE with matched removal of \(\mathcal{L}_{\mathrm{reg}}\)? Right now it is difficult to disentangle “tree-aware supervision” from “dropping a harmful auxiliary loss.”

3. Can the authors report at least one direct quality-preservation check in the main paper, for example task metrics before and after speculative decoding, or a brief argument connecting the specific verification procedure used here to exact target-model outputs? This would directly support the “no quality degradation” claim.

4. For **Table 2**, can the authors add the same SALF-versus-TALF decomposition on at least one additional target model, ideally Llama3-8B? This would help establish that the gains are not specific to DeepSeek-R1-Distill-Llama-8B.

5. How sensitive are the speedups in **Table 1** to repeated measurements? Please provide variance or confidence intervals across runs, or at least clarify whether each number is averaged over multiple timing runs.

6. In **Algorithm 2**, please clarify the semantics of \(\mathcal{G}\) and \(\mathcal{Q}\), especially whether nodes are duplicated in \(\mathcal{G}\), and whether the “Ensure: top-\(N\)” statement applies only to the no-SALF variant. As written, the pseudo-code is confusing.

7. Theorem 1 establishes monotonic decrease of \(S_i\), but can the authors connect this more directly to expected latency benefit? Even a heuristic derivation of a cost-benefit objective would strengthen the motivation for SALF.

8. Regarding **Figure 2**, can the authors report a more direct metric of tree alignment or verification acceptance on lower-ranked branches, rather than only next-step accuracy/ECE after forced self-conditioning?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper as written. The work focuses on inference efficiency for existing language models and does not introduce a new dataset, human-subject protocol, or clearly identifiable privacy/fairness risk beyond the standard concerns associated with LLM deployment.

## Soundness Rating
2: fair. The core ideas are plausible and the empirical results are substantial, but several central claims are supported more heuristically than rigorously, and the main algorithm/loss descriptions are not specified cleanly enough.

## Presentation Rating
3: good. The paper is generally readable, the motivation is clear, and **Figure 1**, **Figure 2**, and the main tables help. However, the algorithmic notation and some claims are imprecise enough that the presentation falls short of excellent.

## Contribution Rating
2: fair. The paper offers a useful improvement to existing tree-based speculative decoding pipelines, but the contribution feels more like a solid refinement than a clearly definitive advance, and the empirical isolation of the two proposed components is not yet strong enough for a higher score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and practically relevant, with real speedup gains and a sensible motivation, but too many pieces of the argument remain underspecified or only partially validated in the main paper. With clearer objective definitions, stronger ablations, and direct evidence for quality preservation, I could imagine this moving up.

## Reviewer Confidence
4: confident. I am familiar with speculative decoding and related draft/verify methods, and I checked the paper’s main mathematical and empirical claims carefully, though I did not independently verify every appendix proof in full detail.