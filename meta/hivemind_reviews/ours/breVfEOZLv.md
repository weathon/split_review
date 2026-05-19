## Summary
The paper proposes AdaptConf, an adaptive confidence loss for weak-to-strong knowledge distillation in vision models. The method dynamically weights a weak teacher's soft supervision against the strong student's self-supervision via a per-sample weighting function β(x). Experiments span image classification, few-shot learning, transfer learning, and noisy-label learning, showing consistent improvements over fixed-weight baselines (AugConf) and standard KD methods.

## Strengths
1. **Consistent empirical improvements across diverse and challenging tasks.** AdaptConf outperforms AugConf and prior KD methods in nearly all teacher-student pairings on CIFAR-100 (Tables 2, 4), with gains of 0.5%–2%. These gains extend to few-shot learning (Table 5, 6), transfer learning (Table 7: +0.33% with GT, +2.15% without GT on ImageNet), and noisy-label settings (Table 8: +0.81% on CIFAR-100 asymmetric noise).

2. **Only method succeeds when the teacher is substantially weaker.** In the MobileNetV2→ResNet50 pair (Table 4), no KD-based method except AugConf and AdaptConf improves the student — confirming that the self-training component is essential when the teacher's signal is poor.

3. **Robust to hyperparameter choice.** The ablation (Figure 2) shows that AdaptConf's temperature T produces smaller performance variance than AugConf's α, making the method easier to deploy without extensive tuning.

4. **Quantitative validation of dynamic weighting.** Figure 3 tracks β(x) over training, showing that as the student improves, β shifts toward 0.5, confirming the loss adaptively rebalances supervision.

## Weaknesses
### Fatal

None.

### Major

1. **β(x) function contradicts the claimed motivation for adaptive weighting (verified from Eq. 2 and surrounding text).**  
   The paper states (line 52) that when the student's soft output is close to its hard label — i.e., the student is confident — the loss should increase the weight on self-supervision. However, β(x) = exp(CE(f, ˆf)) / (exp(CE(f, ˆf)) + exp(CE(f, ˆf_w))) does the *opposite* in the critical case. When the student is confident (small CE(f, ˆf)) and disagrees with a weak teacher (large CE(f, ˆf_w)), β becomes *very small*, decreasing the self-supervision weight rather than increasing it. This is not a minor ambiguity: the paper's core claimed mechanism (dynamically trusting the confident student) is not what the formula implements. The positive empirical results may still hold, but they cannot be attributed to the mechanism claimed. The paper would need to either (a) correct the formula to match the motivation, or (b) revise the motivation and provide a correct explanation for why the current formula works.

2. **Unsupported claim of surpassing "strong-to-strong distillation."**  
   The abstract asserts that AdaptConf "surpasses benchmarks set by strong-to-strong distillation." Strong-to-strong methods such as Born-Again Networks (Furlanello et al., 2018) and Noisy Student (Xie et al., 2020) are mentioned in the related work but never compared against in any experiment. The baselines used are standard KD methods designed for strong-to-weak settings and AugConf. The claim of superiority over strong-to-strong distillation is unsubstantiated by the evidence presented.

### Minor

1. **Overclaiming in the abstract: "exceeds the performance of fine-tuning strong models on full datasets."**  
   The evidence for this claim is a +0.33% gain on ImageNet (Table 7, from 83.53% to 83.86%) — a marginal improvement on an already strong MAE-pretrained ViT-B baseline. While technically positive, the phrasing implies a qualitative breakthrough far beyond what the data supports. The +2.15% gain without ground truth is more notable, but the abstract makes a blanket statement.

2. **The β(x) function uses hard teacher labels (ˆf_w(x)) while the loss itself uses soft teacher labels (f_w(x)) in the first CE term.** This soft/hard inconsistency is never acknowledged or justified in the paper. It may not be a fatal flaw, but it makes the formulation appear ad hoc and harms reproducibility.

3. **No error bars or standard deviations reported.** Results are averaged over 3 trials (stated in table captions) but no variance is reported. Given the small margins (e.g., 0.33%), this information is important for assessing significance.

4. **AGI framing in the introduction** (lines 23–24: "To advance towards super-human AGI models…") is grandiose and disconnected from the actual scope — ImageNet-pretrained backbones for image classification. This weakens the impact of an otherwise solid empirical paper.

### Trivial

- The temperature T used in the ablation (Figure 2) is introduced only in Section 4.3 without being defined in Eq. 2. The paper does explain that T is applied within the CE computation (following standard KD practice), but stating this earlier would improve clarity.

## Suggestions
1. **Fix the β(x) formulation or correct the motivation.** If the intended behavior is "trust the confident student," then β should be *decreasing* in CE(f, ˆf) rather than increasing. For example, β(x) = exp(−CE(f, ˆf)) / (exp(−CE(f, ˆf)) + exp(−CE(f, ˆf_w))) would make β large when the student is confident. Alternatively, provide a new correct explanation for why the current formula works.
2. **Provide explicit comparisons to strong-to-strong distillation methods** (Born-Again Networks, Noisy Student) if the abstract claim is to be maintained.
3. **Report standard deviations** for all main results.
4. **Address the soft/hard label inconsistency** — either justify it or switch to a consistent formulation.
5. **Tone down the AGI framing** in the introduction to match the paper's actual scope.

## Score and Decision

**Originality:** Moderate — adaptive weighting is a known idea (AugConf), but the specific β(x) formulation is novel. **Importance:** The weak-to-strong distillation problem is timely and relevant. **Claims support:** The empirical claims are supported by extensive experiments, but the central claimed mechanism (adaptive confidence weighting) is undermined by a verifiable inconsistency between the motivation and the formula. **Soundness:** The experimental design is reasonable, but the core formulation's behavior is at odds with the paper's explanation. **Clarity:** Generally clear, though the motivation-formula mismatch creates confusion. **Value:** The empirical results suggest the method works, but without a correct explanation of why, the scientific contribution is weakened.

The paper's core claimed contribution is the adaptive confidence weighting mechanism. The β(x) function does not implement the claimed behavior in the critical case (confident student disagreeing with weak teacher). This is a Major weakness that must be resolved. The empirical results remain potentially useful, but the paper as a scientific explanation of why the method works is flawed. I recommend rejection in the current form, but the paper could be substantially improved by correcting the formulation or the claimed mechanism.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
