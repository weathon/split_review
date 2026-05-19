- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have thoroughly read the paper and verified all claims. Let me produce the consolidated review.

## Summary

This paper proposes FPTT, a transformer-based architecture for world modeling that adopts the corrector-predictor structure from slot-attention methods (STEVE/SAVi) but replaces all components with pure transformer modules. The corrector uses unmasked cross-attention to align internal representations with observed frames, the predictor advances the representation forward in time, and the loss is computed on the predicted frame (not the corrected representation). Evaluated on the PHYRE benchmark via an auxiliary classification task, the method shows comparable performance to STEVE with somewhat narrower variance and a ~35% improvement in steps-to-threshold for reaching 0.95 F1 (5,500 vs. 8,500 training steps).

## Strengths

- **Measurable sample-efficiency improvement over STEVE**: Table 1 reports FPTT reaches the 0.95 F1 threshold in 5,500 training steps (mean) versus 8,500 for STEVE, a 35% reduction, with a smaller standard error (758 vs. 1,483). This directly supports the sample-efficiency claim.

- **Narrower performance variance across runs**: Figures 5(b) (F1) and 5(d) (recall) show consistently tighter error bands for FPTT compared to STEVE across most of training, supporting the claim of improved training stability.

- **Loss-on-prediction design**: Computing the loss on the predictor output \(\hat{z}_{t+1}\) rather than on the corrected representation (as in prior slot-attention work) directly biases the model toward future prediction — a principled design choice that ties the architecture to the world-modeling objective rather than representation fidelity alone.

## Weaknesses

### Fatal
None.

### Major

- **Title and framing overclaim "slot encoding"**: The title promises "slot encoding" and the abstract claims a combination with "the slot-attention paradigm," but the architecture does not implement slot attention, learn slot-based object representations, or perform object-centric binding. The paper's own limitations (Sec. 5.1) honestly state that "attempts at replicating the object segmentation displayed by slot-attention architectures have not yet yielded positive results." While the method borrows the corrector-predictor *structure* from STEVE/SAVi and is transparent about this in the body, the central framing implicitly promises an object-centric capability that is not delivered. This is a significant gap between the paper's marketing and its actual contribution.

- **No ablation justifies the core architectural split**: The paper's key design choice — separating the corrector and predictor into two smaller transformers rather than using a single transformer for both functions — is never tested. Without an ablation comparing the proposed two-transformer setup against a single-transformer alternative (or against SlotFormer's single-transformer approach), there is no evidence that this specific architectural decision is responsible for the observed improvements. The contribution therefore remains a combination of existing ideas without demonstrated insight into which component drives the gains.

- **Evaluation limited to a single simple dataset**: Experiments are conducted only on PHYRE (50K synthetic 2D Newtonian physics videos). The paper acknowledges plans to test on more complex datasets (MOVi-E, Physion) but presents no such results. This sharply limits the generality of the findings — the claimed advantages in stability and sample efficiency have not been shown to transfer to more realistic scenes with more objects, occlusions, or visual complexity.

### Minor

- **Missing architectural details for reproducibility**: The paper does not provide key hyperparameters: the dimensionality of \(\Lambda_t\), the number of tokens it contains, the number of layers and heads for each transformer (corrector, predictor, decoder), the learning rate, optimizer, batch size, VQVAE codebook size, or latent dimension. These details are essential for reproduction and fair comparison.

- **Sample-efficiency metric is informative but has limited statistical support**: The 0.95 F1 threshold for 4 consecutive epochs is taken from prior work but is ultimately arbitrary. The decoder-only baseline's 29,000-step mean is de facto a single datapoint (1 of 5 runs cleared the threshold), making that comparison uninterpretable. The paper does not report whether the difference between FPTT and STEVE is statistically significant (e.g., via a permutation test or confidence intervals on the difference), and does not verify that a "training step" costs the same compute across models.

- **Auxiliary evaluation is indirect**: The world model is evaluated through a downstream classifier's accuracy on a success/failure prediction task rather than through direct metrics on predicted frames, reconstruction quality, or rollout fidelity. While the same protocol is used in related work, direct evaluation would strengthen the claims about world model quality.

### Trivial

- The paper uses \acronym{} and \fullname{} macros whose expansions are not visible in the extracted text, making the acronym "FPTT" appear only in a table caption without being defined.

## Nice-to-Haves

- A more natural baseline would be a single transformer of comparable total capacity that performs both correction and prediction, to isolate the benefit of the architectural split.
- Reporting wall-clock time or FLOPs would contextualize the sample-efficiency comparison, since the paper notes the decoder-only baseline takes roughly twice as long per experiment.
- Visualizing attention patterns or performing probing tasks on the learned representation \(\Lambda_t\) would help interpret what the model has learned, especially given the slot-centric framing.

## Removed Points

- **"Evaluation is stacked" (decoder-only baseline stripped-down)**: The harsh critic claimed the decoder-only baseline is an unfair comparison because it removes action/reward inputs. *Reason for removal*: The paper clearly explains (Sec. 4.2) that this adaptation is necessary because PHYRE is a pre-rendered video dataset with no agent actions or rewards — removing these inputs is standard practice, not a stacked comparison. The primary baseline is STEVE, not the decoder-only model.

- **"Overlapping error bands undermine the contribution"**: *Reason for removal*: The paper's own text acknowledges FPTT and STEVE are "comparable in terms of performance" — the claimed advantages are specifically in stability (narrower error bands, visible in the figures) and sample efficiency (Table 1), not in raw accuracy. The overlapping bands on one metric do not contradict the paper's actual claims.

- **"Precision is worse for FPTT — selective emphasis"**: *Reason for removal*: The paper explicitly discusses this (lines 286-287): "The only exception to the above is the precision metric... where STEVE achieves 1... However, its performance on recall is significantly more erratic and lower on average, resulting in an overall lower F1 score." The paper is transparent about precision, not selectively hiding it.

- **"VQVAE frozen — can't adapt tokenization"**: *Reason for removal*: This is standard practice in this line of work (Micheli et al., STEVE, SlotFormer all do this). It is not a weakness specific to this paper.

- **Strength Finder items 3, 4, 5 (architectural separation, loss-on-prediction, transformer-only pipeline)**: *Reason for removal*: These are descriptions of design choices, not demonstrated strengths supported by evidence. They are retained as architectural descriptions in the Strengths/Summary where appropriate.

## Novel Insights

The harsh critic and strength finder both observed the same structural tension: the paper occupies an awkward middle ground between slot-attention methods and transformer world models. It adopts the *form* of slot encoding (corrector-predictor architecture) without the *function* (object binding), which means the paper's experimental contributions (modest stability and sample-efficiency gains on PHYRE) could potentially be explained by architectural factors entirely unrelated to object-centric representation — such as the inductive bias of the corrector-predictor separation, the unmasked cross-attention, or simply having more parameters focused on temporal dynamics. Neither reviewer identified which of these mechanisms drives the improvement, which underscores the need for the missing ablation. Beyond the paper's own contributions, the key meta-observation is that the community currently lacks a clean way to disentangle *architectural structure inspired by slot methods* from *actual object-centric learning* — a distinction this paper inadvertently highlights by borrowing one without achieving the other.

## Suggestions

1. **Retitle the paper** to remove the "slot encoding" language (e.g., "Transformer corrector-predictor architecture for sample-efficient world modeling") to match what the method actually does.
2. **Add an ablation** comparing the two-transformer corrector–predictor split against a single transformer of equivalent total capacity performing both correction and prediction — this is the single most important missing experiment for establishing the contribution.
3. **Provide full architectural hyperparameters** (number of layers, heads, token dimensions, learning rate, optimizer, batch size) in a table.
4. **Add a statistical significance test** (e.g., bootstrap or permutation test) for the sample-efficiency comparison between FPTT and STEVE.
5. **Report at least one direct world-modeling metric** (e.g., per-frame prediction accuracy or rollout MSE on held-out videos) alongside the auxiliary classification results.
