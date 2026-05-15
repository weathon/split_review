Now I have thoroughly verified all claims against the paper text. Here is my consolidated review.

---

## Summary

This paper proposes FedBiOT, a federated learning method for fine-tuning LLMs where clients never access the full model (protecting the LLM owner's IP). The approach splits the model into a compressed emulator (distributed to clients, held frozen) and a small adapter (fine-tuned locally and aggregated via FL). Its key claimed novelty is a bi-level optimization that continuously re-aligns the emulator with the full model during training, rather than relying on one-shot static distillation as in the prior FedOT work. Experiments on LLaMA-7B across math, code, and QA tasks report improvements of >4% over the baselines.

## Strengths

- **Clear problem diagnosis:** The paper correctly identifies that FedOT's one-shot distillation on a public dataset fails when the public data distribution drifts from clients' private data (Section 2.2). This is a genuine limitation, and the idea of continuously updating the emulator during FL is a natural and reasonable direction.

- **Improved adapter placement grounded in transfer learning:** The choice of bottom-only layers as the adapter (rather than top+bottom as in prior work) is principled, motivated by computation constraints and the established finding that earlier layers encode general features while later layers specialize (Yosinski et al., 2014). This design choice is internally consistent and well-reasoned.

- **Multiple tasks and non-i.i.d. settings:** The evaluation spans three diverse tasks (math problem-solving, code generation, question answering) with both i.i.d. and non-i.i.d. data partitions. This demonstrates generality and is more thorough than evaluating on a single task.

- **Ablation study targeting the proposed components:** The ablation examines the regularization term (ε), the KL distillation term (λ), and the number of emulator update steps. The finding that λ benefits AdapEmu performance and ε benefits both AdapEmu and AdapFu provides some evidence that the introduced loss terms have tangible effects.

## Weaknesses

### Fatal

- **The reported improvements cannot be attributed to the bi-level optimization because the experimental design confounds the bi-level component with a different adapter selection.** The paper explicitly states (Section 4.1) that FedBiOT uses the *last two / last four decoders* as the adapter, while both baselines (Offsite-tuning, FedOT) use the *first two and last two decoders*. This means FedBiOT and the baselines differ in **two** ways: (1) the bi-level optimization vs. static distillation, and (2) which layers constitute the adapter. The ablation study (Section 4.4) tests the components of the bi-level formulation (λ, ε, number of emulator steps) but never includes the crucial control of running FedOT with the same bottom-layer adapter selection. Without this control, the reported gains of "more than 4% accuracy improvement" could be entirely due to the better adapter placement rather than the bi-level optimization — the paper's central claimed contribution. This is a fundamental experimental omission that makes the core claim unsupported by the presented evidence. *(Verified: Section 4.1 confirms the different adapter selections; no control experiment isolating the bi-level component is present anywhere in the paper.)*

### Major

- **IP protection claims are substantially overblown relative to what the method actually provides.** The paper motivates the problem by stating that LLM owners "may not be willing to disclose the LLMs' details, including their architectures and parameters" (Section 1). Yet the method distributes a compressed emulator composed of actual layers from the original model with exact weights. At a 20% dropout rate, this emulator contains 80% of the transformer layers. The paper provides no obfuscation, no differential privacy, no mechanism limiting what clients can infer about the held-out layers or architecture. The abstract's claim that the method "guarantees the clients' data privacy and avoids the disclosure of an LLM" is inaccurate — it discloses a large portion of the LLM and offers no formal privacy guarantee for client data either. The method offers *partial* model disclosure, which is a reasonable trade-off, but the paper should be candid about what "protection" means rather than implying full protection.

- **Efficiency claims are unsubstantiated.** The paper claims the method is "eco-efficient" and "friendly to computation-limited clients" but provides **zero measurements** of GPU memory, FLOPs, training time per round, or communication volume. Section 2.1 cites costs for full-parameter fine-tuning (112GB GPU memory, 28GB communication) as motivation, but never reports the corresponding numbers for FedBiOT. If a central selling point is computational efficiency, the paper must measure and report it.

### Minor

- **The bi-level optimization is overclaimed.** The paper formulates a formal bi-level problem in Equations (1)–(2) but implements a simple alternating scheme: server-side emulator updates (E gradient steps on public data) → broadcast → client-side adapter updates (K gradient steps) → aggregation. There is no inner-loop convergence check, no hypergradient computation, and no mechanism ensuring the lower-level argmin is reached before the upper-level update. The paper's claim that the algorithm "can optimize the bi-level problems to an equilibrium point" (Section 3) is not supported by any analysis. This should be described as alternating minimization with auxiliary losses, which is reasonable but not novel as a bilevel solution. *(Verified: Section 3 algorithm description confirms simple alternating updates with no bilevel-specific machinery.)*

- **Ablation results are stated without supporting data in the main text.** Section 4.4 presents four bullet-point findings (e.g., "layerwise alignment is not necessary," "regularization benefits training") without showing the actual numerical results. The reader cannot quantitatively verify these claims from the main paper. Even if details are deferred to an appendix, the main text should display key ablation data.

- **Best-checkpoint reporting may inflate results.** The paper reports "the best results at every 100 rounds" rather than final-round performance or a consistent reporting methodology. This risks cherry-picking the best snapshot and is not standard practice for FL evaluation.

### Trivial

None.

## Nice-to-Haves

- A comparison to FL + LoRA or similar PEFT methods (even with the caveat that they require full model access) would help calibrate how much performance is sacrificed for the IP-protection constraint. This is not a required baseline but would strengthen the empirical picture.
- A convergence curve (test accuracy vs. communication rounds) for FedBiOT and baselines would be more informative than reporting only best checkpoints.
- A privacy analysis quantifying what a client could infer about the full model from the distributed emulator would address the IP protection overclaim noted above.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Missing comparison to split learning, differential privacy, API-based distillation"* — These address fundamentally different problem settings and are outside the paper's stated scope of extending the offsite-tuning framework to FL. The baselines used (Offsite-tuning, FedOT) are the directly comparable methods in this line of work. This criticism is scope creep.
- *"Missing related works"* — Per standard review policy, this cannot be confirmed without external literature access and is not raised as a verified omission.
- *"The 0% AdapEmu at dropout 0.5 is a critical failure"* — The paper reports this result honestly (Table 3). It is a limitation of the approach, not a flaw in the paper's reporting or claims. The paper never asserts that AdapEmu works at high compression.
- *"Missing appendix / proofs in appendix"* — These are parser artifacts; the original submission likely contained them.
- *Formatting or typographical criticisms* — Parser artifacts, not author errors.
- Strength Finder's claim that empirical improvements are "over strong baselines" — This conflicts with the fatal weakness (the improvements may be due to different adapter selection rather than the bi-level component). Since the weakness prevails, this over-generous characterization is removed. The improvements themselves are real, but their attribution is confounded.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run the missing control experiment**: Compare FedBiOT against FedOT using the **same** adapter selection (bottom layers only). If the bi-level optimization provides additional value, FedBiOT should outperform FedOT even when both use the same adapter choice. If performance is similar, the claimed contribution of the bi-level formulation is not supported.

2. **Reframe the IP protection claim honestly**: Describe the method as providing *partial* model disclosure (the server shares a compressed subset of layers) rather than claiming it "avoids disclosure of an LLM." Clarify what an adversary could and could not learn from the emulator.

3. **Report computational costs**: Measure and report GPU memory, training time per round, and communication volume for FedBiOT and baselines to support (or qualify) the efficiency claims.

4. **Remove the "bi-level optimization" overclaim**: Describe the algorithm as alternating minimization with auxiliary losses, which is what it actually is. A formal bi-level treatment would require inner-loop convergence or hypergradient computation.

5. **Include ablation numbers in the main text**: Add a table summarizing the effect of λ and ε on performance rather than stating findings without evidence.

## Score and Decision

This paper addresses a timely and important problem, and the intuition behind continuously adapting the emulator during FL is sensible. However, the experimental design contains a fatal confound that makes it impossible to attribute the reported improvements to the paper's central claimed contribution (the bi-level optimization). The adapter selection differs between FedBiOT and the baselines, and no control experiment isolates the effect of the bi-level component. Additionally, the IP protection claims are substantially overstated relative to what the method actually provides. These issues cannot be fixed in a rebuttal; they require re-running experiments with proper controls.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>