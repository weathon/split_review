Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper addresses label privacy during API-based fine-tuning of large language models. It proposes P³EFT, a two-party split learning protocol that combines (1) a privacy-preserving backpropagation that exploits the linearity of backprop in output gradients to split the true gradient across multiple servers, and (2) an adversarial mixture of multiple adapter sets whose outputs are combined with randomized mixing weights to prevent label leakage from activations. Experiments on DeBERTa-v2-XXLarge and Flan-T5-Large with LoRA adapters on SST-2 and MRPC show that P³EFT achieves accuracy close to non-private fine-tuning while resisting several label-inference attacks.

## Strengths

1. **Principled gradient privacy via linearity of backprop (Section 3.2).** The observation that backprop is linear in output gradients for fixed inputs and parameters is correctly derived. This allows the client to decompose the true gradient into noise vectors sent to different servers and recover the exact gradient — not a noisy approximation — by recombination. This is a genuine advance over prior gradient-noise defenses that degrade accuracy.

2. **Leveraging PEFT compactness for multi-adapter mixing (Section 3.3).** Using the fact that LoRA adapters are compact enough to maintain multiple sets, the paper mixes adapter outputs with randomized weights whose gradients w.r.t. individual adapters are obfuscated, while the combined model retains utility. This is a clever use of PEFT's properties that would be prohibitive for full parameter training.

3. **Systematic attack surface analysis (Section 3.1, Figure 1).** The paper identifies that both gradients w.r.t. activations *and* trained activations leak labels via simple k-means clustering, and correctly notes that protecting only one source is insufficient. This motivates the two-pronged defense and is more thorough than prior split-learning studies that focus on gradients alone.

4. **Empirical validation on large modern models.** The paper evaluates on DeBERTa-v2-XXLarge (1.5B) and Flan-T5-Large with LoRA, which is larger-scale than prior split-learning work tested on smaller models (e.g., CIFAR-10). The results show P³EFT outperforms the Distance Correlation baseline at matched privacy levels.

## Weaknesses

### Major

1. **Server non-collusion assumption mismatched with motivating use cases.** The gradient privacy protocol (Section 3.2) requires multiple independent, non-colluding servers — if two servers share information, the true gradient is recovered by summing components. The paper acknowledges this in passing (line 119–128) and suggests decentralized systems (Petals) or TEEs, but its primary motivation (Section 1) explicitly cites commercial APIs like OpenAI, Hugging Face AutoTrain, and OctoAI — none of which offer multiple independent servers to a single client. The paper does not provide a credible path for deploying the protocol under the commercial-API scenario that motivates it. This is not fatal (the protocol is valid for decentralized systems, and TEEs are mentioned as an alternative), but it is a significant gap between problem framing and solution that limits practical applicability.

2. **Overclaimed guarantee for adversarial activation regularization.** Section 3.3 states that the adversarial regularizer "ensures that it is impossible to predict labels from individual adapters" — this is too strong. The adversarial update (fitting linear heads, then updating adapters to prevent prediction) is a heuristic inspired by gradient reversal (Ganin & Lempitsky 2015); it provides no formal bound on information leakage. The empirical attack AUCs only show that *simple* classifiers fail under *specific* experimental conditions. An adaptive attacker with a more powerful model or combining information across time steps may still recover labels. The paper would benefit from tempering this language ("reduces leakage against the attacks considered") or providing a formal analysis.

### Minor

3. **Input privacy scoped out but not adequately addressed.** The paper correctly identifies that it focuses on label privacy (Section 1, line 25), noting inputs "can often be anonymized or obfuscated by other means (see Section 2.1)." However, Section 2.1 is a general background on federated/split learning and does not actually discuss input obfuscation methods. For many sensitive domains (medical records, proprietary text), the raw input itself is private and cannot be shared with an untrusted server. This limitation deserves a clearer statement; as it stands, the scope is narrower than the phrase "client data privacy" may imply.

4. **Missing computational overhead analysis.** The paper claims the adversarial update takes "negligible time" (line 169) but provides no runtime or communication cost measurements. Given that the protocol requires \( m \times n \) forward/backward calls per step (for \( m \) gradient splits and \( n \) adapter sets), understanding the practical overhead is essential for a method positioned as practical.

5. **No adaptive attack evaluation.** The privacy metrics rely on three attack methods (spectral attack, norm attack, logistic regression) applied to the obfuscated data as-is. These are not adaptive attacks that account for the defense mechanism. A stronger evaluation would include attackers who know the defense and train more expressive models on the obfuscated activations/gradients.

### Trivial

- Line 207: "P³FT" appears to be a typo for "P³EFT".

## Nice-to-Haves

- A comparison to a calibrated-noise baseline (e.g., adding Gaussian noise to gradients before sending, with privacy level matched via the same attack metrics) would help justify the complexity of P³EFT's gradient splitting over simpler noise-based approaches.
- Evaluating on a generative task (e.g., summarization with Flan-T5) would broaden the contribution, though this is scope expansion beyond the paper's current focus.
- A sensitivity analysis showing how privacy degrades when the adversarial regularizer is weakened or omitted would be informative.

## Removed Points

The following reviewer criticisms were removed per the review guidelines:

- *"Algorithm 2 is referenced but not fully presented in the main text"* — The parser strips appendices; Algorithm 2 exists in the original submission.
- *"Comparison to DP baselines"* — The paper already explains why DP is not applicable in this setting (line 53); the critic acknowledges this but asks for "more thorough discussion."
- *Request for evaluation on generative tasks* — Scope expansion beyond the paper's stated focus on classification.
- *"The 'Training w/o LoRA adapters' baseline is expected to have very low accuracy"* — This baseline serves as a lower-bound (max privacy, minimal accuracy), which is a standard and informative baseline choice.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses largely corroborate the paper's stated claims and limitations without surfacing new cross-cutting patterns.

## Suggestions

1. **Address the server-assumption gap head-on.** Either propose a concrete mechanism (e.g., using cryptographic commitments, auditable TEEs, or horizontal client-side splitting) to make the protocol work with single-entity API providers, or pivot the motivation toward decentralized systems where the assumption holds naturally. A clear limitations paragraph acknowledging this gap would substantially improve the paper's honesty.

2. **Temper the activation privacy claims.** Replace "ensures that it is impossible to predict labels" with a more measured statement like "reduces label leakage against the considered attacks" and discuss what stronger adaptive attacks might look like.

3. **Report runtime and communication cost.** Even a single table showing wall-clock time per step and total communication volume for the tested configurations would help readers assess the practical tradeoffs.

4. **Clarify the input privacy limitation.** Either add a brief discussion of what "obfuscation by other means" entails concretely, or explicitly scope the paper to label privacy under the assumption that inputs are not sensitive.

## Score and Decision

**Overall assessment:** The paper identifies a real problem and proposes a clever combination of techniques that is well-aligned with PEFT's properties. The gradient-splitting protocol is principled, and the multi-adapter mixing is an interesting idea. However, the core gradient privacy mechanism requires a server non-collusion assumption that does not match the commercial API scenarios motivating the work, and the activation privacy claims are overstated. The paper has genuine contributions but needs substantial revision — particularly to address the server-assumption gap and temper claims — before it is ready for acceptance. The experimental evaluation is a reasonable start but limited in scope.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>