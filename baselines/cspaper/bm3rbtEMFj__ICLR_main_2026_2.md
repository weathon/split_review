---
job_id: b5217055-60ce-4f05-8812-f4b9d4ace547
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: bm3rbtEMFj.pdf
paper: ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL Problems
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in scope for ICLR, it studies reinforcement learning / imitation learning under partial observability with a memory-augmented transformer architecture and evaluates it on long-horizon decision-making and robotics tasks.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, method, related work, experiments/results, and conclusion, and it presents a concrete method with nontrivial empirical evidence. While I found several issues in novelty positioning, exposition, and rigor, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions aimed at automated reviewers, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes ELMUR, a decoder-only transformer augmented with layer-local external memory, bidirectional token-memory cross-attention, and an LRU-style update rule that either replaces empty slots or convexly blends into the least recently used slot. The method is evaluated on synthetic long-horizon T-Maze, POPGym, and MIKASA-Robo manipulation tasks, with the paper also providing a simple analysis of memory retention under the convex blending update.

## Strengths
The empirical picture is the strongest part of the paper. The method is tested across three fairly different settings, namely synthetic long-horizon memory tasks, POPGym, and visually grounded robotic manipulation, which is a better breadth of evaluation than many memory papers manage in the main text. The main claims are reflected in the presented results rather than being purely architectural intuition.

The T-Maze results are striking and easy to interpret. In **Figure 3** on Page 8, ELMUR maintains essentially perfect success while corridor length grows far beyond the training horizon and far beyond the local context length. Whatever one thinks about the realism of T-Maze, this figure does support the narrow claim that the architecture can carry information much longer than its self-attention window. **Figure 4** is also useful because it does not just show one extrapolation point, it shows the train/test length grid and suggests robust transfer across sequence lengths rather than memorization of one horizon.

The MIKASA-Robo results in **Table 1** on Pages 8-9 are meaningful because they include difficult sparse-reward visual tasks where memory should matter. The gains on tasks like RememberColor3-v0 and TakeItBack-v0 are large enough to be hard to dismiss as noise. The broader benchmark summary in **Table 2** also suggests that ELMUR is not only good on one cherry-picked domain, it improves the overall POPGym aggregate and the puzzle subset where long-term memory is plausibly most relevant.

The architecture itself is reasonably intuitive. **Figure 1** on Page 2 does a good job of showing the two-track structure, token track and memory track, and how mem2tok, tok2mem, and LRU fit together. This makes the high-level idea accessible: memory is not just cached activations tacked on at the end, it is integrated per layer.

I also appreciated that the paper includes ablations in the main text. **Figure 6** and the associated discussion on Page 9 suggest that memory size and the update rule matter materially, which is important because otherwise the paper could be accused of simply winning by scale or extra parameters. The observation that under-provisioned memory collapses when \(M < N\) is useful and gives some mechanistic insight.

## Weaknesses
1. **The novelty claim is somewhat overstated relative to existing memory-augmented transformers, and the paper does not sharpen the distinction enough.**  
   The core ingredients, segment recurrence, explicit memory slots, cross-attention between sequence and memory, and a bounded update mechanism, are all familiar design patterns. The paper does cite several related directions in Section 6, including Transformer-XL, Memformer, RATE, and block-recurrent variants, but the actual methodological delta is not crisply isolated. For example, on Page 4 the paper contrasts itself with architectures that cache hidden states, and on Page 10 it says “Unlike prior methods, ELMUR integrates explicit memory into every layer,” but the paper does not make a careful apples-to-apples argument for why per-layer memory plus LRU blending is qualitatively different from prior slot-based or recurrent memory modules rather than an incremental combination of known ideas. This matters because the bar for ICLR is not just “works well,” it is also whether the conceptual advance is clearly articulated and positioned.

2. **The mathematical specification of the attention and update mechanisms is underspecified in several places, which makes the method harder to reproduce and assess than it should be.**  
   In **Equation (2)** on Page 4, the mem2tok cross-attention is written as  
   \[
   \mathbf{h}_{\mathrm{mem2tok}}=\mathrm{AddNorm}(\mathbf{h}_{\mathrm{sa}}+\mathrm{CrossAttention}(Q=\mathbf{h}_{\mathrm{sa}}, K, V=\mathbf{m})).
   \]
   Here \(K\) is left implicit, even though the text says memory embeddings act as keys and values. Presumably \(K=\mathbf{m}\), but the equation should say so explicitly. The same issue appears in **Equation (4)**, where tok2mem is written as \(\mathrm{CrossAttention}(Q=\mathbf{m}, K, V=\mathbf{h})\), again leaving \(K\) implicit. These are not cosmetic slips, they concern the central read/write operator of the paper.  
   There is also inconsistency between the notation in **Algorithm 1** and the prose. Algorithm 1 defines \(B_{\mathrm{rel}}\) in lines 3 and 8, but lines 4 and 9 pass \(B_{\mathrm{read}}\) and \(B_{\mathrm{write}}\) to cross-attention. This suggests either a notation mismatch or missing definitions.  
   More importantly, **Algorithm 2** updates only one slot \(j^\*\) using \(\hat{u}_{j^\*}\), but \(\hat{u}\) is produced in **Equation (5)** / Algorithm 1 as a full set of candidate updated memory embeddings. The paper never clearly explains how the index \(j^\*\) is selected jointly with these candidate vectors, or why taking the candidate at the least-recently-used slot is the right merge operation. If the write path computes a new vector for every slot, but the manager overwrites just one slot, the semantics of the other \(\hat{u}_j\) are unclear. This is a core methodological ambiguity, not a side detail.

3. **The theoretical section is correct as far as it goes, but it is quite weak relative to the claims it is used to support.**  
   Section 4 proves exponential decay under repeated convex updates and boundedness under bounded inputs. That is fine, but these are basically properties of the scalar recursion
   \[
   m^{i+1} = \lambda m_{\text{new}}^{i+1} + (1-\lambda)m^i.
   \]
   The analysis does not capture the learned attention, slot selection dynamics, multi-layer interactions, or retrieval quality. The “effective horizon” claim on Page 6, \(H(\epsilon)=M L \frac{\ln(\epsilon)}{\ln(1-\lambda)}\), is presented as if it characterizes practical retention, but it relies on the statement that a memory slot is overwritten once every \(M\) segments “in expectation.” Under strict LRU and task-dependent access/update dynamics, this is not really derived from the actual algorithm, it is a heuristic average-case approximation. The paper partially hedges by calling it a conservative lower bound, but then also uses it to support broad retention claims.  
   In short, the theory is not wrong, but it is analyzing a simplified blending recurrence, not the deployed model. That matters because the paper lists theoretical analysis as one of the main contributions in the Introduction.

4. **The experimental comparison set is strong in some respects, but still incomplete for the paper's specific claim about external memory.**  
   The baselines in Section 5.1 include DT, RATE, DMamba, BC, CQL, and Diffusion Policy. These are reasonable general baselines, but for a paper whose central story is explicit external memory for long-horizon sequence modeling, the comparison is missing some closer architectural competitors. The Related Work section itself cites Memformer, Block-Recurrent Transformers, memorizing transformers, and multiple external-memory approaches, but those do not appear in the main benchmark tables. That leaves a gap: the reader can conclude ELMUR beats several strong general baselines, but not whether the specific ELMUR design is better than the nearest external-memory alternatives. This matters a lot for judging contribution versus engineering.

5. **Some of the results are less decisive than the narrative suggests, and the paper occasionally leans on selective aggregation.**  
   The POPGym aggregate in **Table 2** is positive for ELMUR, but the margin over RATE is modest: 10.4 versus 9.5 overall, and 1.2 versus 0.45 on puzzles. This is good, but not a blowout. **Figure 5** usefully shows many per-task improvements over DT, yet DT is not the strongest POPGym baseline in Table 2, RATE and BC-LSTM are both more competitive in several settings. So comparing visually only against DT paints the rosiest picture rather than the most informative one.  
   Likewise, **Table 1** on MIKASA-Robo highlights four tasks and the gains are real, but even there ELMUR remains low on RememberColor5-v0 and RememberColor9-v0, so the statement that performance “remains stable as the number of distractors increases” on Page 9 is not really supported by the table. It decreases from \(0.89\) to \(0.19\) to \(0.23\). Yes, it stays ahead of baselines, but “stable” is the wrong word. This kind of phrasing matters because it overstates the empirical conclusion.

6. **Statistical reporting and evaluation protocol are acceptable but not especially strong for the breadth of claims being made.**  
   The evaluation uses only three runs for most experiments, as stated on Page 7, and then aggregates over 100 episodes per run. For noisy RL/IL settings, three seeds is often too small to support confident claims about consistency, especially when some baselines have large variance, for instance RATE on TakeItBack-v0 in **Table 1** has \(0.42 \pm 0.24\). In **Figure 5**, confidence intervals over only three run means are shown for 48 tasks; visually this looks rigorous, but with \(n=3\) one should be cautious.  
   More importantly, the paper says hyperparameters “follow the task-specific configuration table in Appendix, Table 7” and that baselines are “faithfully re-implemented,” but the main paper gives little detail on whether tuning effort was symmetric across methods. Since ELMUR includes several additional knobs, \(M\), \(\lambda\), \(\sigma\), segment layout, MoE settings, relative bias, the fairness of tuning becomes important.

7. **Presentation quality is noticeably below the standard of the empirical contribution.**  
   There are repeated figure references like “Figure 2, Figure 2” on Page 5, inconsistent notation between equations and algorithms, and a visibly corrupted references section on Page 13 with many duplicate entries of Hausknecht & Stone. There are also minor but distracting errors, for example “Let fix a memory embedding” on Page 6, “a bounded new values” in Proposition 2, and “Theoretical re” cut off across Pages 10-11. None of these invalidate the work, but together they reduce confidence that the manuscript received the level of polish expected at this venue. The exposition is good at the intuition level, yet sloppy at the formal level.

## Questions
1. In **Equations (2) and (4)**, what exactly are the keys in the cross-attention, and can the authors provide the fully specified read/write equations with tensor shapes? I would like a precise mathematical definition of mem2tok and tok2mem, because the current notation leaves \(K\) unspecified in both cases.

2. In **Algorithm 2**, why is the selected slot updated with \(\hat{u}_{j^\*}\) specifically? Since tok2mem appears to produce a candidate updated memory representation for every slot, it is unclear how these candidates are interpreted before the LRU manager chooses a single destination. Please clarify the intended semantics and whether alternative merge rules were tried.

3. The theoretical “effective horizon” on Page 6 assumes a slot is overwritten once every \(M\) segments in expectation. Can the authors justify this assumption more carefully under the actual learned dynamics, or present it more explicitly as a heuristic estimate rather than a formal property of the full model?

4. Can the authors provide a tighter comparison to the closest external-memory or retrieval-based transformer baselines, not just general sequence-model baselines? This would significantly increase my confidence that the gains come from the specific ELMUR design rather than the general idea of adding any explicit memory.

5. For the POPGym analysis, could the authors add a figure analogous to **Figure 5** but comparing against the strongest baseline per task, or at least RATE as well as DT? Right now the visual story is anchored to DT, which is not always the most competitive comparator.

6. In **Table 1**, the text says performance on RememberColor[3,5,9]-v0 “remains stable” with more distractors, but the success rates drop sharply. Do the authors mean stable relative ranking rather than stable absolute performance? Please revise that claim or support it more carefully.

7. How sensitive are the MIKASA-Robo and POPGym results to backpropagation through memory across segments? Page 7 states the memory is detached between segments. Since this is a central design choice, I would like to know whether the gains persist if limited BPTT over a few segments is allowed.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work uses simulated benchmarks and standard policy-learning settings; no human subjects, privacy-sensitive data, or clearly harmful deployment claims are discussed in the main submission.

## Soundness Rating
3: good. The core empirical claims are supported reasonably well by the experiments, and the method is plausible, but some key mathematical and algorithmic details are underspecified, and the theoretical analysis is narrower than the presentation suggests.

## Presentation Rating
2: fair. The paper is readable at a high level and the central idea is illustrated well by **Figure 1** and **Figure 2**, but the manuscript contains too many notation inconsistencies, overstatements, and reference/polish problems for a higher score.

## Contribution Rating
3: good. The paper offers a useful and empirically strong memory-augmented architecture for long-horizon partially observable control, especially in the robotics benchmarks, even if the conceptual novelty over prior memory-augmented transformers is not as sharp as the paper claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real empirical contribution and a sensible architecture, and the results on T-Maze plus the gains in **Table 1** and **Table 2** make it relevant to the ICLR community. That said, the manuscript needs a cleaner mathematical specification, more careful novelty positioning, and less optimistic interpretation of some results.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main technical details and experimental evidence carefully, though some uncertainty remains because several implementation details of the read/write mechanism are not fully specified in the main paper.