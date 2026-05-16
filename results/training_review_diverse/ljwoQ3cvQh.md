Now I have a thorough understanding of the paper and can verify each claim. Let me write the consolidated review.

## Summary

This paper identifies and provides evidence for a phenomenon: neural network predictions on high-dimensional OOD inputs tend to revert toward the optimal constant solution (OCS)—the best input-independent prediction under the training loss. The authors propose a mechanism (feature norm decay → bias domination → OCS approximation), study aspects of it empirically on small-scale models and theoretically on simplified homogeneous networks, and demonstrate an application to risk-sensitive selective classification.

## Strengths

- **Well-supported core empirical claim**: The "reversion to the OCS" phenomenon is demonstrated across 8 datasets (CIFAR10, ImageNet, ImageNet-R/S, OfficeHome, BREEDS, WILDS Amazon, etc.), 3 loss functions (cross-entropy, MSE, Gaussian NLL), and multiple architectures (ResNet, VGG, DistilBERT), as shown in Figure 3. This systematic evidence is the paper's strongest contribution and is not undermined by any of the weaknesses below.

- **Extends prior observations to a general principle**: While prior work noted softmax confidence drops for OOD inputs (Hendrycks & Gimpel 2016), this paper generalizes the observation to arbitrary loss functions and continuous outputs, and identifies the specific constant (OCS) to which predictions revert. This reframes a well-known phenomenon under a unified, testable hypothesis.

- **Clear and testable mechanistic hypothesis**: The proposed explanation—OOD features have smaller norms and align less with weight subspaces, causing outputs to be dominated by accumulated biases that approximate the OCS—is intuitive, grounded in empirical measurements (Figure 4), and independently verifiable.

- **Demonstrates the practical relevance of OCS alignment**: The selective classification example (Section 5) illustrates a conceptually important point: the loss function's OCS determines the model's "default behavior" on OOD inputs, and this can be aligned with cautious actions. This insight is valuable regardless of whether the specific implementation is state-of-the-art.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical analysis does not match the claimed mechanism of multi-layer bias accumulation.** The paper's mechanism (Section 4 intro, line 119) describes "accumulation of model constants (e.g. bias terms)" across layers. However, the theory in Section 4.2 studies homogeneous ReLU networks that have *no bias terms in intermediate layers* (line 143–144). Bias is only introduced as a final-layer additive term (line 168: $\mathcal{\tilde{F}} = \{f(W; \cdot) + b\}$). The theory therefore cannot explain the *accumulation* of biases across multiple layers that the mechanism posits. The theory instead shows something narrower: with only a final bias, under certain margin-point conditions, the bias approximates the OCS. This is a structural gap between the claimed mechanism and what is formally supported. The authors should either extend the theory to include per-layer biases or clearly delineate what the theory does and does not cover.

- **The selective classification comparison is against an unrealistically weak baseline.** The paper compares a reward-prediction (MSE) agent to a "standard classification" agent that *never abstains* (Figure 6–7). In selective classification, standard practice involves thresholding on a confidence measure (e.g., maximum softmax score) to decide when to abstain. The paper does not include this natural baseline. The claim that "appropriately leveraging reversion to the OCS can substantially improve an agent's performance on OOD inputs" is weakened by this omission—a thresholded classifier, even with a threshold tuned only on in-distribution data, would likely also increase abstention on OOD inputs and could achieve competitive rewards. The oracle baseline (temperature-scaled on OOD labels) is not a substitute for a practical baseline. The paper's conceptual point about OCS alignment is valid, but the empirical comparison overstates the practical advantage.

### Minor

- **The mechanism analysis (Section 4.1) is conducted only on small-scale models and datasets (MNIST with a 4-layer net, CIFAR10 with ResNet20).** The main phenomenon experiments (Figure 3) include ImageNet-scale models and DistilBERT, but the mechanism analysis is not replicated at this scale. It is unclear whether the feature-norm drop and bias-approximation patterns hold for ResNet50 on ImageNet-R or DistilBERT on WILDS Amazon. This limits the generality of the mechanistic explanation relative to the broader empirical claim.

- **The paper does not specify which layer $k$ is used for the "accumulation of model constants" computation** (line 136: "at one of the final layers $k$"). The approximation quality of the accumulated constants may vary across layers; specifying the choice is important for reproducibility and for assessing robustness of the finding.

- **No causal intervention test of the mechanism.** The paper shows correlations (OOD features have smaller norms; biases approximate the OCS) but does not demonstrate that the norm drop *causes* the output to revert to the OCS. An intervention such as zeroing out biases at test time would test whether the bias accumulation is causal. Without this, the mechanism remains a plausible correlation rather than a validated explanation.

### Trivial
None (the email truncation noted by the reviewer is a parser artifact, not a paper flaw).

## Nice-to-Haves
- Include a thresholded softmax classifier baseline in the selective classification experiments to show the practical value of OCS-aligned methods versus a standard alternative.
- Replicate the mechanism analysis (Figure 4) on at least one larger-scale model/dataset (e.g., ResNet50 on ImageNet-R).
- Perform a causal intervention test (e.g., zeroing biases at test time) to strengthen the mechanism claim.
- Discuss known failure modes or OOD shifts where reversion to the OCS is weak or absent.
- Commit to releasing code for reproducibility.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *"The propositions and theorem are stated informally and without proof"* and *"Consider relegating it to the appendix"* — Removed because the proofs almost certainly exist in the appendix (appendix sections are stripped by the PDF parser). Criticizing absent appendix content that exists in the original submission is not valid.
- *"The blfootnote contact email appears truncated"* — Removed as a PDF parsing artifact, not an error in the original paper.
- *"Code release: Not mentioned"* — Removed as this is a standard suggestion, not a weakness of the paper content.

## Novel Insights
None beyond the paper's own contributions. The reviews confirm the value of the core empirical finding while narrowing the scope of what is actually proven about the mechanism and the application.

## Suggestions
1. **Disambiguate the theory's scope.** Either extend the theory to model per-layer biases, or explicitly state in the main text that the theory covers only the final-bias component of the mechanism and that the multi-layer accumulation remains an empirical finding. This would prevent readers from over-interpreting what is formally supported.
2. **Add a thresholded classifier baseline** to the selective classification experiments. Tune a softmax threshold on in-distribution validation data (without OOD labels) and compare rewards. This would directly test whether the OCS-alignment insight provides genuine practical value beyond a simple heuristic.
3. **Specify the chosen layer $k$** for the accumulation-of-constants computation, and ideally show results for multiple choices of $k$ to demonstrate robustness.

## Score and Decision

The paper makes a genuine contribution: it identifies, names, and systematically validates a general pattern in how neural networks extrapolate on OOD inputs. This core observation is well-supported and likely to influence how researchers think about OOD behavior and uncertainty. The weaknesses—the theory not matching the full mechanism, the weak baseline in the application, and the limited scale of the mechanism analysis—are real but do not invalidate the central claim. They primarily affect the secondary contributions (mechanism explanation and practical demonstration). These issues are addressable in revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>