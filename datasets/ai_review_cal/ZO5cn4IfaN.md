- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6, 6, 8
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

CO2 proposes a distributed data-parallel training method that achieves full overlap of communication with computation by combining local updating (τ inner steps) with one-step asynchronous all-reduce of model parameters. To maintain convergence under asynchrony, it introduces a staleness gap penalty and outer momentum clipping. The paper provides a convergence theorem and evaluates on CV and NLP tasks up to 128 A100 GPUs, including a 7B-parameter TransNormer-LLM.

---

## Strengths

1. **Impressive scalability on low-bandwidth TCP/IP clusters.** On 80Gbps TCP/IP with τ=48, CO2 achieves 304,736 words/sec at 128 GPUs (scalability ratio 1.06) vs. AdamW's 22,810 words/sec (ratio 0.82) — a >13× throughput improvement. This directly supports the paper's claim of democratizing training on limited-bandwidth clusters (Table 3, rows 3 vs. 5).

2. **Consistently outperforms prior communication-overlap methods (Local-SGD, Overlap-Local-SGD, SlowMo) by significant margins.** CO2 beats Local-SGD/Overlap-Local-SGD by 1–3% accuracy on CV tasks and 0.5–1.0 perplexity on NLP tasks (Tables 1 and 2). This demonstrates that the specific design (one-step async + local updating + staleness penalty) is empirically superior to existing approaches in this family.

3. **Ablation confirms the staleness gap penalty provides a clear benefit.** Removing the penalty increases validation perplexity from 7.39 to 7.56 on GPT-2 Small (Table 4), a consistent 0.17 PPL improvement.

4. **Demonstrated ZeRO-2 integration for 7B-scale models.** CO2 trains a 7B TransNormer-LLM with ZeRO-2 on 128 GPUs, showing practical compatibility with memory-saving distributed optimizers (Section 4.1).

---

## Weaknesses

### Fatal
None.

### Major

1. **Convergence improvements over standard optimizers (SGD/AdamW) are marginal or negative, yet the paper overstates them.** Across six tasks in Tables 1 and 2:
   - ViT (Base): AdamW 81.33±0.04 vs. CO2 80.95±0.08 — non-overlapping standard deviations, AdamW is clearly better. The paper dismisses this as "within expected random fluctuations" (line 246), but with σ=0.04 on AdamW this is not credible.
   - GPT-2 Small: CO2 7.37±0.73 ties with SlowMo 7.34±0.89 — essentially identical.
   - RoBERTa: all methods produce overlapping confidence intervals.
   - ResNet-50: CO2 77.14±0.09 vs. SGD 76.92±0.05 — the intervals do NOT overlap (CO2 is better by 0.22%). The paper's claim that CO2 "consistently outperforms" (line 246) or achieves "better generalization" across tasks is misleading when the ViT and RoBERTa results tell a different story.

2. **Convergence theorem excludes the clipping operation that the paper presents as critical for training stability.** The theorem statement (Section 3.4) says "ignore the clip operation." Clipping is not a trivial detail — it directly modifies the outer momentum update that controls training stability, especially for large models. A convergence guarantee for a different algorithm does not guarantee convergence of the actual method. The theorem's conditions (involving Tτ ≥ G L²(…), with dependencies on α, β, τ) are also not verified for the experimental setups, so their practical relevance is unclear.

### Minor

3. **No experimental comparison to the most relevant baselines: recent asynchronous SGD methods.** The paper cites Dutta et al. (2021) and Koloskova et al. (2022) in related work but does not compare against them experimentally. Since CO2's core idea is asynchronous communication with staleness handling, these are the natural baselines. Without this comparison, it is hard to assess whether CO2's specific one-step staleness + penalty design is genuinely better than existing async approaches.

4. **Critical hyperparameter τ not reported for Local-SGD and Overlap-Local-SGD baselines.** τ controls the communication frequency and directly affects both efficiency and convergence. Without knowing the τ values used for these baselines, it is impossible to tell whether the comparison is fair (e.g., did baselines use the same communication budget?).

5. **ZeRO integration comparison is incomplete.** The TN-LLM 7B experiment uses CO2 with ZeRO-2 but does not report a ZeRO-2+AdamW baseline under identical conditions. The table shows only "Adamw" (perplexity 16.82), but it is unclear whether this baseline also used ZeRO-2. If not, the comparison conflates the effect of ZeRO memory reduction with the method.

6. **Scalability ratio definition inflates the reported ratio.** The ratio is computed from 16→128 GPUs, deliberately excluding the 8→16 GPU transition where the largest per-GPU throughput drop occurs (the paper acknowledges this on line 319: "Transitioning from 8 GPUs to 16 GPUs caused a notable drop"). Reporting the ratio from 2→16 nodes instead of from 1→16 nodes gives an inflated picture. For TCP/IP τ=12, the 0.86 ratio already shows non-perfect scaling; including the 8→16 drop would make it worse.

### Trivial
None.

---

## Nice-to-Haves

- **Full training wall-clock curves** (not just iterations 100–200) for the scalability experiments, showing total time to reach a target loss. This would strengthen the claimed end-to-end speedup.
- **Breakdown of compute time vs. communication time** in the scalability experiments (e.g., via PyTorch profiling). This would make the "full overlap" claim verifiable beyond throughput numbers.
- **Ablation on the clipping threshold φ**, which is introduced as important for stability but never varied experimentally.
- **Automatic τ selection guidance** — the paper treats τ as a configured hyperparameter but offers no practical advice for choosing it on a new cluster.

---

## Removed Points

These points from the inputs were removed with justification:

- **"Physically impossible" throughput drop (18,444→3,488).** The paper explicitly explains (line 319) that this is the transition from single-node (NVSwitch 600GB/s, no inter-node communication) to two-node (80Gbps TCP/IP). The severe drop is expected and acknowledged. Not impossible — the critic's characterization is incorrect.
- **ResNet-50 intervals "overlap almost completely."** Factually wrong. SGD interval [76.87, 76.97] and CO2 interval [77.05, 77.23] do NOT overlap.
- **Algorithm 1 execution order inconsistency.** The critic claimed x_{t,0} is not yet set where Λ_t is computed. In Algorithm 1, x_{t,0} was already set at the end of iteration t−1 (line 94: x_{t+1,0} = …). The pseudocode is correct.
- **Missing appendix content / proof not checkable.** The appendix was stripped by the PDF parser; it exists in the original submission.
- **No error bars on scalability ratio.** Raw throughput values have standard deviations; the ratio is a derived quantity. Standard practice in scaling studies.
- **"Cherry-picking" τ for scalability experiments.** τ is a configurable parameter of the method; reporting scaling at the optimal τ (τ=48 for TCP/IP) is standard. The paper also reports the less favorable τ=12 case (ratio 0.86) transparently.
- **Formatting/typo nitpicks.** These are parser artifacts, not author errors.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tensions in asynchronous distributed training (overlap vs. convergence, theory vs. practice) but do not reveal novel cross-cutting observations.

---

## Suggestions

1. **Tone down the claims.** Replace "100% scalability" with "near-perfect scalability under favorable configurations" (e.g., τ=48 on TCP/IP). Acknowledge that τ=12 gives 0.86 scaling and that results depend on choosing τ appropriately.

2. **Add asynchronous SGD baselines.** Compare against Dutta et al. (2021) or Koloskova et al. (2022) — even on a single task — to position CO2 within the async training literature.

3. **Report τ for all local-updating baselines (Local-SGD, Overlap-Local-SGD).** Without this, the comparison is not reproducible.

4. **Extend the theory or temper its claims.** Either add the clipping operation into the analysis, or be explicit that the theorem applies to a simplified version of the algorithm. Verify the theorem's conditions for at least one experimental setting.

5. **Report the 8→128 GPU scalability ratio alongside the 16→128 ratio** for full transparency.

---
