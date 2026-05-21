---
job_id: 48414302-d9b1-49b0-91f5-2614aa721712
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: eu3PwSle8J.pdf
paper: Enforcing Instruction Hierarchy via Augmented Intermediate Representations
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on LNN security, representation learning inside transformers, and robustness to prompt injection via architectural modifications to intermediate representations.

## Minimum Quality
Pass ✅. The paper contains the required components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion, and it presents a concrete method with nontrivial empirical evaluation. While there are important weaknesses in evaluation breadth and methodological clarity, they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, concealed instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies instruction-hierarchy-based defenses against indirect prompt injection in LLMs. The main idea is AIR, which augments hidden states at every decoder layer with trainable privilege-level embeddings, instead of injecting instruction hierarchy signals only at the input layer via delimiters or segment embeddings. The paper evaluates AIR across three base models, two adversarial training schemes (SFT and DPO), and several prompt-injection benchmarks/attacks, reporting substantially lower attack success rates on gradient-based attacks with only small utility degradation.

## Strengths
The paper addresses an important and timely problem. Prompt injection is a real weakness of LLM systems, and the paper targets a concrete failure mode of current instruction-hierarchy defenses rather than proposing another attack-specific patch.

The proposed architectural change is simple, easy to understand, and reasonably lightweight. The mechanism in **Equation (1)** is straightforward, and the parameter overhead analysis on **Page 5** suggests that the additional parameters are modest relative to model size. From an engineering perspective, this is a clean intervention.

The empirical comparison is broader than a single-model case study. The authors test three model families/sizes, two adversarial training schemes, several static attacks, two gradient-based attacks, and the SEP benchmark. This gives the paper more substance than many security papers that hinge on one model and one attack.

There is a useful qualitative narrative linking the hypothesis to empirical observations. In particular, **Figure 3** is one of the more convincing pieces of evidence in the paper: it shows that cosine similarity between representations from different privilege levels increases with depth for delimiter- and input-embedding-based approaches, while AIR preserves lower similarity across layers. Whether cosine similarity is the right proxy can be debated, but the figure does support the paper’s core motivation that input-only hierarchy signals may wash out through the network.

The architecture illustrations are helpful. **Figure 2** clearly contrasts delimiter-based injection, input segment embedding, and the proposed layer-wise injection; **Figure 4** then makes the decoder-block modification concrete. These figures substantially improve readability, especially since the proposed change is conceptually simple but easy to underspecify in text.

The main empirical tables do show substantial gains on the hardest attacks considered. In **Table 1**, AIR is often dramatically better than delimiter and ISE baselines under GCG, especially for Llama-3.2-3B SFT (4.1 vs 38.0/48.1) and Qwen-2.5-7B DPO (1.6 vs 32.0/7.7). Even when AIR is not uniformly best on Astra, the gradient-attack results overall are strong enough to support the narrower claim that AIR materially improves robustness to strong white-box optimization-based attacks.

The paper also makes a fair attempt to discuss the utility-robustness tradeoff rather than reporting robustness only. **Figure 6** suggests the utility drop on AlpacaFarm is usually small, and **Figure 8** provides a more nuanced utility-vs-separation view on SEP, where AIR with DPO appears to sit on a favorable frontier.

## Weaknesses
1. **The central mechanistic claim is plausible, but the evidence for “IH signal degradation” is still weaker than the paper’s rhetoric suggests.**  
   The paper repeatedly frames input-only IH injection as suffering from a “critical limitation” because the signal degrades through the network, but in the main paper this claim is supported mainly by **Figure 3**, which plots average cosine similarity between hidden states of tokens encoded with different privilege levels. This is a fairly indirect proxy. Increased cosine similarity across layers does not by itself establish that the model can no longer use privilege information, nor that this is the causal reason for downstream attack vulnerability. Hidden states may become more similar for many reasons unrelated to privilege signal loss, including task-conditioned compression or attention mixing. The paper would be much stronger if it either toned down the causal language or provided a more direct analysis in the main paper, for example privilege-label probing, attention-pattern analysis, or ablations connecting representational separation quantitatively to attack success rate. As written, the interpretation of **Figure 3** is suggestive, not decisive.

2. **The paper does not sufficiently disentangle the effect of architectural placement from the effect of simply adding more trainable parameters and repeated perturbations.**  
   AIR adds a fresh embedding table at every layer plus one after the final decoder layer. The baselines do not have this same repeated degree of freedom. The paper argues the added parameter count is small, but that is not the right control. A stronger ablation would compare against parameter-matched alternatives, such as repeated injection of a shared embedding across layers, random frozen per-layer embeddings, or extra trainable vectors added at all layers without privilege semantics. Without such controls, it remains unclear how much of the gain comes from “enforcing hierarchy at all layers” versus “giving the model more trainable knobs distributed throughout the stack.” This matters scientifically because the paper’s claimed contribution is architectural insight, not just a slightly larger defense model.

3. **The attack evaluation is narrower than the paper’s framing implies, and the conclusions should be correspondingly narrower.**  
   The title and abstract make the work sound like a more general method for enforcing instruction hierarchy, but the main evaluation is concentrated on a particular adversarial setting: single-turn indirect prompt injection, mostly on Alpaca-style data, with attacks targeted to produce the literal string “hacked!” on AlpacaFarm or witness extraction on SEP. This is useful, but it is a constrained setup. There is no evaluation on multi-turn interactions, tool use, retrieval-augmented pipelines, role-rich chat settings, or more realistic agentic contexts, even though the introduction explicitly motivates those settings. This gap matters because instruction hierarchy is arguably most relevant in those more complex workflows, where privilege must be maintained across turns and sources. The limitation is acknowledged in Appendix A, but in the main paper the claims are still somewhat broader than the evidence supports.

4. **The static attack results are close to saturated, which reduces their diagnostic value, while the stronger gradient-based results expose some instability that is not sufficiently discussed.**  
   In **Table 1**, nearly all defended models achieve near-zero ASR on Naive, Ignore, Completion, and Escape Separation. That suggests these attacks are too easy to meaningfully distinguish methods after adversarial training. The important part of the table is really GCG, Astra, and SEP. On those harder settings, the story is more mixed than the prose suggests. For example, under Astra with DPO on Llama-3.2-3B, AIR is substantially worse than Delim, 23.8 vs 34.5 helps AIR, but AIR is not remotely close to the striking near-zero result seen for SFT; on Llama-3.1-8B DPO, ISE slightly beats AIR, 1.2 vs 1.0, and on Qwen SFT, AIR is better but the gap to ISE is modest for GCG relative to other cases. These are not fatal contradictions, but they show the method is not uniformly dominant across all strong attacks/model/training combinations. The discussion on **Page 8** emphasizes the best reductions, but the paper should more explicitly discuss the failure cases and variability.

5. **The comparison against prior work is somewhat incomplete in the sense of defense scope, even if the cited IH baselines are appropriate.**  
   The paper compares only three IH injection mechanisms, None, Delim, ISE, and AIR, under SFT/DPO training. That is a reasonable ablation space for the claimed contribution, but the paper’s broader security pitch would benefit from at least some comparison or discussion against non-IH defense families, such as detection/filtering approaches, structured prompting/runtime separation, or stronger architectural compartmentalization. The appendix mentions detection-based defenses, but the main experimental story is effectively “among IH injection mechanisms, AIR is best on these attacks.” That is a narrower claim than the framing suggests, and the paper should be clearer about that distinction.

6. **The training data and attack distributions are tightly coupled, raising concerns about overfitting to a particular notion of prompt injection.**  
   On **Page 12**, the adversarial SFT and DPO datasets are built by corrupting Alpaca examples with Naive or Ignore prefixes and swapping in instructions from other Alpaca examples. This means robustness training is anchored to a rather stylized synthetic distribution. The models are then evaluated on related attack families, including the same in-distribution static attacks and optimization-based attacks targeting a fixed output phrase. It is encouraging that AIR does well on GCG/Astra, but it remains unclear how much of the robustness comes from genuinely improved privilege reasoning versus adaptation to the training corruption template. This matters because a defense that mostly internalizes the training distribution can look strong on benchmark attacks while remaining fragile to semantically different prompt injections.

7. **The mathematical specification of the method is minimal, and some implementation details that affect interpretation are left underspecified in the main paper.**  
   **Equation (1)** defines
   \[
   \mathbf{x}'_{ij} = \mathbf{x}_{ij} + \mathbf{s}_j^k,\quad \mathbf{s}_j^k = S_j[k_i].
   \]
   This captures the core operation, but the surrounding specification is not fully precise. For example, the text says AIR modifies the decoder block and also augments the representation after the last decoder layer before logits, yet it does not precisely state whether the addition occurs before or after the block’s input normalization in pre-norm architectures, nor whether the augmentation is applied identically in all layers across different base architectures. **Figure 4** suggests one insertion point, but the exact placement relative to residual streams and normalization is important because it directly affects optimization and interpretation. Given that the proposed method is an architectural intervention inside transformer blocks, these details should be explicit in the main paper rather than left to a schematic figure.

8. **The optimization setup for the white-box attacks is not fully symmetric across methods, which complicates robustness interpretation.**  
   On **Page 7**, the authors state that GCG/Astra optimize a 100-token random prefix for 200 steps on DPO models and 50 steps on SFT models. This already makes cross-training-method comparisons somewhat awkward. More importantly, there is not much detail on whether all attack hyperparameters were tuned equally for each defense/model pair, whether early stopping or restarts were used, or whether attack budgets were chosen because stronger runs ceased to improve. Since the paper’s headline contribution is robustness against gradient-based white-box attacks, attack strength calibration is not a side issue. A security paper needs to be especially careful not to make defenses look better because the attack is under-tuned on the harder target.

9. **The utility evaluation is serviceable but not especially convincing as a broad claim of “minimal utility degradation.”**  
   **Figure 6** reports AlpacaEval win rates against text-davinci-003 references judged by Llama-3-70B-Instruct, and the reported deltas are usually small. Still, this is one automatic preference-style metric on 805 AlpacaFarm test instances. On **Figure 8**, AIR-SFT sometimes has noticeably worse utility than the none baseline, especially for Qwen-2.5-7B and Llama-3.1-8B. The paper ultimately qualifies the claim to “when trained with DPO” on SEP, but the abstract and conclusion read more generally. I would prefer the authors to state more carefully that utility preservation is strongest with DPO and somewhat less reliable with SFT. Also, the main paper does not report broader general-language or reasoning evaluations, so “utility” here mainly means instruction-following under the chosen benchmark setup.

10. **The Qwen-specific initialization adjustment is a nontrivial fairness wrinkle, even though the authors disclose it.**  
    Appendix B.2 states that the default AIR embedding initialization worked poorly on Qwen, so the authors increased the standard deviation from \(0.02\) to \(0.1\), and applied the same adjustment to ISE for fairness. I appreciate the transparency, but this also highlights that AIR may be somewhat sensitive to activation scale and model-specific tuning. Since the main contribution is presented as a broadly applicable architectural defense, the method’s dependence on such tuning deserves more attention in the main paper. At minimum, the paper should discuss whether this sensitivity affects portability to other architectures and whether the gains persist under a common untuned initialization regime.

11. **The paper’s positioning relative to evaluation of instruction hierarchy following is weaker than it could be.**  
    The paper uses SEP and AlpacaFarm, which are useful, but neither directly isolates hierarchical instruction adherence in the richer sense implied by the paper’s motivation. Given that the paper argues AIR better enforces privilege ordering, a benchmark more directly measuring whether higher-priority instructions override lower-priority ones across varied conflict structures would strengthen the claim. As it stands, the results show improved robustness on chosen attack setups, but they do not fully establish that AIR improves instruction-hierarchy reasoning in a more general sense.

12. **Some presentation and notation issues reduce precision.**  
    A few examples: on **Page 4**, the statement that similarity increases “indicating that the representations may fail to adequately preserve the IH signals” is stronger than the evidence warrants; on **Page 7**, ASR for gradient attacks is measured using likelihood from logits rather than actual generation containing the target phrase, which is not directly comparable to the static attack ASR definition in the preceding bullet; and the table formatting in **Table 1** is somewhat awkward, making it harder than necessary to parse the SFT/DPO structure. These are not huge issues, but in a paper making security claims, metric definitions and comparisons need to be especially crisp.

## Questions
1. The main causal claim is that AIR works because hierarchy information is re-injected at every layer, preventing degradation. Can the authors provide a stronger ablation that controls for parameter count and repeated additive perturbations, for example a shared-across-layers hierarchy embedding, random frozen layer-wise embeddings, or parameter-matched non-hierarchy vectors added at each layer? This would materially increase my confidence that the gain comes from the proposed mechanism rather than extra capacity.

2. Can the authors clarify the exact insertion point of AIR relative to the transformer block internals? **Figure 4** suggests addition to the residual stream before a sub-layer, but the model-specific implementation details are important. Is the augmentation applied before the first LayerNorm in a pre-norm block, after attention, or at the block input? Is the placement identical across Llama and Qwen?

3. For the white-box attacks on **Page 7**, how were the budgets, restarts, and hyperparameters selected? Were they tuned separately for each defense/model combination, or fixed globally? Since AIR may alter the optimization landscape, stronger or differently tuned attacks could change the conclusions. A more explicit attack-strength validation would help.

4. The paper reports robustness on attacks targeted to produce the exact string “hacked!”. How well do the conclusions hold if the target instruction is semantically richer, more open-ended, or less lexically constrained? Even a small experiment with multiple target behaviors would make the robustness claim less benchmark-specific.

5. Can the authors quantify how much AIR’s benefits persist under a strictly identical initialization regime across models, especially given the Qwen-specific change in Appendix B.2? If AIR requires model-dependent scaling to work well, that should be surfaced as part of the method’s practical limitations.

6. The utility story appears strongest for DPO and less stable for SFT, particularly in **Figure 8**. Can the authors provide a clearer explanation for why AIR-SFT sometimes loses utility, and whether this tradeoff is intrinsic or a consequence of training hyperparameters?

7. The representational evidence in **Figure 3** is interesting, but cosine similarity is only one proxy. Could the authors add a direct privilege-prediction probe or another quantitative layer-wise analysis in the main paper? That would make the “signal preservation” story much more convincing.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper is about prompt injection defenses, which is squarely a security topic. While the intent is defensive, the work also operationalizes a white-box attack setup, including gradient-based optimization procedures and benchmark protocols for eliciting malicious outputs. I do not view this as disqualifying, but it does merit ethics-aware handling because such evaluations can be repurposed to improve attacks. The concern is tied mainly to **Sections 3.1, 5.4, and 6.1**, where attack construction and optimization settings are described. A balanced framing is important, and the paper generally does that.

## Soundness Rating
2: fair. The core method is sensible and the empirical results are substantial, but the causal claims are only partially supported, key ablations are missing, and the robustness evidence is narrower and less airtight than the paper’s strongest claims suggest.

## Presentation Rating
3: good. The paper is generally readable and the figures, especially **Figures 2, 3, 4, 6, 7, and 8**, help communicate the idea and results. However, some implementation details, metric choices, and the interpretation of representation analyses need sharper presentation.

## Contribution Rating
2: fair. The idea of injecting hierarchy signals into intermediate layers is interesting and practically relevant, but the current paper does not yet fully establish the breadth, mechanism, and generality of the claimed contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a real idea here, and the gradient-attack results are genuinely interesting. Still, the paper overstates what is established. Right now the evidence supports a narrower claim, AIR is a promising architecture tweak that improves robustness to the specific white-box prompt-injection benchmarks tested here, especially under DPO. That is not yet the same as showing robust enforcement of instruction hierarchy in a broader sense. The missing mechanism-focused ablations, limited evaluation breadth, and some ambiguity in the attack-strength calibration push me to a slightly negative score.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant security/LLM robustness setting, though stronger implementation details and additional ablations from the authors could still shift my opinion somewhat.