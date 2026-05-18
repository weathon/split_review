- Decision: Reject
- Scores: 6, 3, 6

## Merged Review

### Summary
This paper proposes a geometric parameterization (GmP) for ReLU networks, building on an analysis of characteristic activation values of individual ReLU units and their connection to learned features. The parameterization uses radial-angular decomposition in hyperspherical coordinates, decoupling radial and angular parameters. Input mean normalization (IMN) is also introduced. The authors claim improved optimization stability, convergence speed, and generalization, and provide some experimental results.

### Strengths
1. Novel concept of characteristic activation sets of individual neurons and their geometric connection to learned features; offers fresh perspective on ReLU network understanding (Reviewers 1, 3).
2. Geometric parameterization (GmP) based on radial-angular decomposition, with a proof that the change in angular direction under perturbation ε is bounded by ε—a property not held for standard parameterization or weight normalization (Reviewer 1).
3. Some experimental results showing advantages of the proposed GmP (Reviewers 1, 2).
4. Unique and innovative approach to ReLU network analysis (Reviewer 3).
5. Writing is clear and comprehensible (Reviewer 3).

### Weaknesses
1. **Insufficient comparison to existing normalization methods**: 
   - The GmP (Eq.16) appears equivalent to weight normalization (WN) via Eq.9 (u(θ) = w/‖w‖₂). The specific benefits of optimizing in angular space over direct WN, especially regarding stability and optimization behavior, are not clearly articulated (Reviewer 1).
   - The proposed input mean normalization (IMN) is very similar to mean-only batch normalization (Salimans & Kingma, 2016); no advantage of the former over the latter is discussed (Reviewer 2).
   - The paper does not consider how the analysis applies to advanced batch normalization improvements like IEBN, SwitchNorm, or LayerNorm; these should be added to related work or analysis (Reviewer 3).

2. **Weak theoretical justification for generalization**: The proof only shows a bound on angular change Δφ, but the connection between this bound and generalization performance is not sufficiently established. Supporting evidence using loss function values or additional theoretical arguments is needed (Reviewer 1).

3. **Experimental evaluation is not fully convincing**:
   - The ResNet-50 training settings deviate from standard protocols (no standard learning rate decay schedule of first 30 epochs 0.1, 30-60 epochs 0.01, 60-90 epochs 0.001). Under standard settings, Batch Normalization achieves ~76.1% top-1 accuracy on ImageNet. The paper should either compare under standard settings or provide a convincing explanation for the deviation (Reviewer 1).
   - Comparison is limited to a few settings; the paper should evaluate on more models and datasets to be convincing (Reviewer 2). One reviewer (score 3) found the experimental results insufficient overall, contrasting with the two other reviewers (score 6) who found them supportive but also noted limitations.

4. **Missing input variance normalization**: The paper uses IMN but does not further normalize input features by their variance; the reason for this omission is not explained (Reviewer 1, question becomes weakness).

5. **Presentation issues**: The English language and equations in the paper need improvement for clarity (Reviewer 2).