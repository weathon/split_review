Now I have all the information needed. Let me produce the final review.

---

## Final Review

### Summary
PromptArmor revisits the idea of using an off-the-shelf LLM as a guardrail to detect and remove prompt injections from data before it reaches a backend LLM. Prior work found prompting-based detection ineffective, but those studies used older, weaker LLMs. The paper shows that modern LLMs (GPT-4o, GPT-4.1) achieve FPR and FNR below 1% on AgentDojo and below 5% on two other benchmarks, with attack success rates near zero. The method is a system prompt plus fuzzy matching for removal. Ablations with Qwen3 models across sizes and reasoning modes confirm that larger models perform better, and a memorization test rules out data contamination. The paper argues that prompting a strong off-the-shelf LLM should now be a standard baseline for prompt injection defense evaluation.

### Strengths
- **Strong empirical demonstration on AgentDojo**: GPT-4.1 achieves 0.56% FPR, 0.13% FNR, and 0.00% ASR on AgentDojo (Table 2), outperforming all seven baseline defenses on both security and utility metrics. This convincingly overturns the prior finding that prompting-based defenses are ineffective.
- **Well-controlled ablation of model size vs. reasoning capability**: The Qwen3 experiments (Section 4.4, Figure 3 data table) test 0.6B, 8B, and 32B models in both reasoning and non-reasoning modes. The results reveal a clear threshold: tiny models show a fundamental utility-security trade-off that reasoning cannot resolve, mid-sized models benefit from reasoning (FNR drops from 26.50% to 15.78%), and sufficiently large models (32B) achieve near-perfect performance regardless of reasoning mode. This provides actionable insight for practitioners deploying with resource constraints.
- **Memorization test ruling out data contamination**: Section 4.5 applies the prefix-suffix methodology from Carlini et al. / Staab et al. to test whether GPT-4.1 memorized AgentDojo samples. Average similarity is 0.34 with only 3.5% exceeding the 0.6 threshold, directly addressing the concern that benchmark leakage inflates the near-zero error rates.
- **Comprehensive baseline comparison spanning multiple defense paradigms**: Table 2 compares against seven baselines from detection-based, prompt augmentation, system-level, and tool-filtering approaches, with clear evidence that PromptArmor achieves Pareto improvement on ASR while maintaining high UA.
- **Prompting strategy analysis that explains prior negative results**: Section 4.3 shows that GPT-3.5 fails badly without a definition of "prompt injection" (FNR 60.24%) but drops to 15.74% when a definition is added, providing a concrete explanation for why prior work using older models found prompting ineffective.

### Weaknesses

#### Fatal
None.

#### Major
- **Thin contribution for a top venue**: The method is a single system prompt (Figure 2) plus fuzzy matching. The core empirical finding — that GPT-4o/4.1 are much better than GPT-3.5 at detecting prompt injections — is directionally correct but unsurprising given the known capability gap between these model generations. While the paper is candid about its "baseline" framing, an empirical revisit paper needs particularly rigorous evaluation to carry weight, and the evaluation has notable gaps (see next point and minor weaknesses).
- **Adaptive attack evaluation does not support claims of robustness**: In Table 4, AgentVigil-Adaptive achieves only 21.46% ASR against the *undefended* agent — less than half the 54.53% ASR of the original AgentDojo attacks. This means the adaptive attacks are substantially weaker than the static benchmark attacks they are meant to improve upon. Showing PromptArmor stops these weaker attacks (0.16% ASR) provides little evidence of robustness against a genuinely adaptive adversary. The paper's claim that "PromptArmor is robust against adaptive attacks" (Section 4.6, line 288) is not supported by this evidence.

#### Minor
- **Unexplained utility gap**: Clean utility (no attacks, no defense) is 94.27% (visible only in Figure 3's legend), while PromptArmor-GPT-4.1 achieves 72.02% UA in Table 2. With FPR and FNR both near zero, the origin of this ~22-point gap relative to clean operation is not discussed or analyzed. The paper also does not report clean utility alongside the defense comparison in Table 2, making it harder for readers to calibrate the utility numbers.
- **0.00% ASR reported without qualitative scrutiny**: Achieving literally zero successful attacks across 629 adversarial scenarios warrants examination. The paper provides no qualitative examples of what PromptArmor extracts, no edge-case discussion, and no analysis of detection failures that happen to not result in attack success.
- **Proprietary model reliance undercuts the "baseline" framing**: The headline results use GPT-4o and GPT-4.1, whose behavior can change and whose reproducibility is limited. The Qwen3-32B results (0.00% ASR non-reasoning) partially address this and should be elevated.

#### Trivial
- The memorization test uses a prefix-continuation methodology that cannot detect structural or pattern-level memorization of injection attacks — a known limitation worth acknowledging.
- The paper claims computational efficiency (Section 3.2) but provides no latency or cost measurements for the additional LLM inference call.

### Nice-to-Haves
- Report clean utility (no attacks, no defense) alongside all UA numbers so readers can see the full picture of utility sacrifice.
- Include qualitative examples of what PromptArmor extracts and removes, especially for edge cases.
- Either strengthen the adaptive attack evaluation (run AgentVigil until it achieves comparable ASR to static attacks against the undefended agent) or acknowledge the current evaluation as preliminary.
- Elevate the Qwen3-32B results to co-equal status with the GPT results for reproducibility.

### Removed Points
These points are flagged to be removed, treat them with caution.

- *"Per-dataset prompt adjustments are mentioned but not shown"* — REMOVED. The prompts are in Appendix C, which the parser strips from all submissions. The original submission includes them.
- *"No error bars or variance estimates"* — REMOVED. With temperature=0 and deterministic outputs, variance is minimal, and demanding confidence intervals for large-scale benchmark evaluations is not standard practice in this subfield.
- *"SecAlign excluded from baselines, creating favorable comparison"* — DEMOTED to not included. The paper explicitly justifies excluding SecAlign because it "exhibits poor utility on AgentDojo even in the absence of attacks, largely due to degraded instruction-following capability." Including a defense that cannot complete user tasks would not add meaningful comparison. Seven other baselines spanning multiple categories are included.
- *"Tool Filter configuration not explored"* — REMOVED. Evaluating hyperparameter-tuned versions of every baseline is beyond reasonable scope.
- *"The prompt design is not the active ingredient; model capability is"* — REMOVED. The paper already acknowledges this in Section 4.3: "GPT-4o and GPT-4.1 perform equally well across different prompting strategies." The paper's thesis is precisely that model capability is what changed.
- *"The fuzzy matching mechanism described in one sentence could easily fail"* — REMOVED. The paper describes the regex approach and the motivation (whitespace/punctuation differences). No evidence suggests it fails in practice.
- *"Baseline selection is uneven; Deberta and Llama Prompt Guard 2 perform poorly"* — REMOVED. The paper includes the standard baselines from the literature and the baselines' poor performance is a finding, not a selection bias. The paper also includes Tool Filter which achieves comparable ASR (0.79%).
- *"The paper's contribution is almost entirely the empirical observation that stronger LLMs are better at this task — which is unsurprising"* — partially retained as a Major weakness but the "unsurprising" framing is weakened; the paper is candid about this being a baseline revisit, and the value is in the systematic empirical demonstration, not in the surprise factor.

### Novel Insights
The Qwen3 scaling analysis (Section 4.4) provides a genuinely novel and actionable insight: there appears to be a critical model size threshold (~8B-32B parameters) where prompting-based prompt injection detection transitions from unreliable to near-perfect, and reasoning capability provides measurable benefit specifically in the mid-sized regime (8B) but is unnecessary once sufficient scale is reached (32B). This finding has practical implications for deploying such defenses with resource-constrained open models, and the interaction between model scale and reasoning mode is not obvious a priori.

### Suggestions
- Elevate the Qwen3-32B results to co-equal status with the GPT results. The finding that an open 32B model achieves 0.00% ASR is arguably more important for the "baseline" thesis than the GPT results, since it ensures reproducibility.
- Move the actual system prompt(s) from the appendix into the main paper body — they are the method.
- Analyze and report where the ~22-point utility gap (94.27% clean vs. 72.02% defended) comes from. If FPR is truly 0.56%, what accounts for the remaining user task failures under defense?
- Fix or reframe the adaptive attack evaluation: either run AgentVigil until it achieves ASR comparable to static attacks against the undefended agent, or acknowledge the current evaluation as preliminary and avoid claiming robustness against adaptive attacks.

### Score and Decision

**Bracketing (Round 1):** Compared PromptArmor against weak anchors (3.00 guardrail pipeline papers), middle anchors (5.25 benchmark/evaluation papers), and strong anchors (8.00 novel-method papers). PromptArmor landed clearly above the 5.25 tier and clearly below the 8.00 tier. Initial bracket: **5.5 – 7.0**.

**Narrowing (Round 2):** Retrieved papers in the 5.0-7.5 range including ASB (6.25), Robustness Over Time (6.75), Prompt Infection (5.20), and Jailbreaking with Simple Adaptive Attacks (6.14). PromptArmor is comparable to ASB in evaluation quality but with a thinner method; similar to Robustness Over Time in being an empirical observation paper but asking a less novel question. It is clearly stronger than Prompt Infection (5.20).

**Anchor comparison:**
| Anchor | Score | Round | Comparison |
|---|---|---|---|
| Wildflare GuardRail (`KjxZ4BdUdN`) | 3.00 | R1 | PromptArmor far stronger — rigorous multi-benchmark evaluation |
| FSPIB (`MsRdq0ePTR`) | 5.25 | R1/R2 | PromptArmor stronger — deeper empirical story, better ablations |
| Baseline Defenses (`0VZP2Dr9KX`) | 5.25 | R1/R2 | PromptArmor stronger — uses modern models, comprehensive ablations |
| Prompt Infection (`NAbqM2cMjD`) | 5.20 | R2 | PromptArmor stronger — more systematic evaluation |
| Jailbreaking w/ Adaptive Attacks (`hXA8wqRdyV`) | 6.14 | R2 | Comparable quality; JA has more methodological novelty |
| AutoAdvExBench (`leSbzBtofH`) | 6.17 | R2 | PromptArmor comparable in evaluation rigor |
| ASB (`V4y0CpX4hK`) | 6.25 | R2 | Comparable evaluation scope; ASB contributed more artifacts |
| Robustness Over Time (`eC4WlSZc4H`) | 6.75 | R2 | PromptArmor slightly below — RoT asks a more novel question |
| Catastrophic Jailbreak (`r42tSSCHPh`) | 7.00 | R2 | PromptArmor below — genuine methodological novelty |
| Booster (`tTPHgb0EtV`) | 8.00 | R1 | PromptArmor far below — novel method with theory |

**Final score: 6.0** — A well-executed empirical paper with systematic ablations and a practically useful finding, but held back by a thin contribution (a single prompt), a weak adaptive attack evaluation that does not support its robustness claims, and an insufficiently analyzed utility gap. At ICLR, this sits below the acceptance threshold given the combination of thin methodology and evaluation gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>