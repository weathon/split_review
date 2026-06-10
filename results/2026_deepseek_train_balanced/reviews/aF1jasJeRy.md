Now I have all the verification I need. Let me write the final consolidated review.

## Summary

This paper proposes Torque-Aware Momentum (TAM), which modifies classical momentum by scaling the gradient contribution with a damping factor based on the cosine similarity between the gradient and the previous momentum vector. The intuition — dampening misaligned gradients to stabilize exploration — is clear and physically motivated. The paper evaluates TAM (and an underspecified adaptive variant, AdaTAM) on image classification, LLM fine-tuning, online learning with label-flipping shifts, and warm-up ablations.

## Strengths

- **Robustness to severe distribution shifts is convincingly demonstrated.** In the online learning experiments (Section 4.3), under 80% and 100% label flipping, TAM maintains accuracy and stability across 40+ tasks while SGDM and SGD degrade. This is a clean, non-obvious result and the strongest evidence in the paper.

- **TAM warm-up delays gradient-norm spikes and improves convergence.** Section 4.4 shows that TAM used as a warm-up phase (25–50 steps) defers oscillatory behavior by 5–10 epochs compared to SGDM, and the mode connectivity analysis (though confusingly described) suggests TAM leads to better generalization basins.

- **Fixed hyperparameters with sensible defaults.** The two new hyperparameters $\gamma=0.9$ and $\epsilon=10^{-8}$ require no tuning (line 79), making TAM a practical drop-in replacement for SGDM.

- **Honest reporting of mixed results.** The paper acknowledges that AdaTAMW results on RoBERTa-large are inconsistent and that improvements over AdamW are often modest ("similar or better" in 28/42 configurations). This transparency is appreciated.

## Weaknesses

### Major

**1. AdaTAM is never defined — the adaptive variant used in ~half of experiments lacks any specification.** 
The abstract claims TAM "can be combined with both SGD and Adam." The contributions promise an "adaptive variant, AdaTAM." The experiments compare AdaTAM (and AdaTAMW) against Adam, AdamW, and AngularGrad across image classification and LLM fine-tuning. Yet **Section 3 (Methodology) gives equations only for the non-adaptive TAM applied to SGD** — it simply ends at Eq. 3 ($d_t$, $m_t$ update) with no explanation of how the damping factor integrates with Adam's bias correction, second-moment estimate, or any other component. There is no equation, no algorithm pseudocode, and no prose for AdaTAM. Since roughly half the experimental evidence depends on this variant, the paper's central empirical claims around adaptive optimizers are unverifiable from the description given. This is not a minor omission for a methods paper at a top venue.

**2. The Learning Rate Transfer derivation is incomplete — Equation 6 is referenced but never appears.**
Lines 81–84 begin a derivation: *"For SGDM, the idea is that momentum changes the update magnitude in a way that can be approximated as $t$ gets large as"* — and then the section ends. Equation 6 is subsequently invoked to justify learning rate search ranges (line 92, *"choose the ranges of these grid searches to be consistent with the learning rate transfer heuristic rule in Equation 6"*), but the formula never appears. This leaves the experimental protocol only partially specified and prevents reproducibility of the hyperparameter selection.

**3. The warm-up experiment contains contradictory and incoherent descriptions.**
The setup described in lines 146–147 states: train with TAM, then *"switch to SGDM"*. However, the reported results (line 153) compare *"TAM warmup"* against *"naive Adam and SGDM warmup $^+$ Adam"* (implying the switch was to Adam, not SGDM). Additionally, line 148 mentions training *"with different order non-adaptive momentum-based methods for the GNN architecture"* in a section about ResNet18 on CIFAR-10. The reader cannot determine which optimizer the method switches to, nor whether the GNN mention is an error or refers to a different experiment.

**4. No variance or statistical significance reporting.**
All experimental results are reported as single numbers — no error bars, standard deviations, number of trials, or random seeds. Given the well-known variance of deep learning training outcomes (especially on CIFAR-10/100 and in LLM fine-tuning), single-run comparisons are insufficient evidence to support claims that one optimizer "improves generalization" over another. This is especially acute for ImageNet results where margins are typically small.

### Minor

- **Initialization corner case is unaddressed.** At $t=0$, $m_{t-1}=0$, making the cosine similarity $S_t$ in Eq. 3 undefined (division by zero). The paper does not discuss how $\hat{s}_t$ or this first step is handled.

- **The LLM fine-tuning claims are modest.** The headline result is "similar or better in 28/42 configurations." "Similar" is not threshold-defined, and the paper admits results on RoBERTa-large are inconsistent. This is a fair but underwhelming finding.

### Trivial

None.

## Nice-to-Haves

- Providing error bars for at least the core classification results (even 3 runs with std devs) would significantly strengthen the paper.
- Clarifying the symmetry: TAM stores one extra scalar ($\hat{s}_t$) beyond SGDM's momentum buffer; the paper's claim of "same memory footprint" is approximately correct but slightly imprecise.

## Removed Points

*These points were flagged by the reviewers but are removed after cross-checking against the paper. Treat them with caution.*

- **"Asymmetric hyperparameter comparison"** (Harsh Critic, Critical Issue 5): The paper explicitly states a learning rate grid search with fixed compute budget per optimizer (line 92). Tuning momentum coefficients is not standard practice in optimizer comparisons (0.9 is universally used). The critic's complaint is generic and unsupported by evidence in the paper.
- **Memory footprint criticism** (Harsh Critic, Section-by-Section Notes): The critic argues TAM does not have "the same memory footprint as SGDM" because it stores an additional scalar $\hat{s}_t$. A single scalar is negligible; the comparison with AggMo (which stores multiple full momentum vectors) remains valid. This is an overly pedantic point.
- **"Normalize" mischaracterization** (Harsh Critic, methodology notes): The critic claims calling $d_t = (1+\hat{s}_t)/2$ a "normalization" is a mischaracterization. Affine rescaling from $[-1,1]$ to $[0,1]$ is a standard normalization. This is a semantic nitpick.
- **Citation "oddities"** (Harsh Critic, missing parts section): Critic points to "Zhuang et al., 2021" for RoBERTa and "Kingma & Ba, 2015" for momentum as incorrect citations. Hard rules prohibit flagging missing related works or references; I cannot verify these claims with external knowledge.
- **Learning rate transfer heuristic as a strength** (Strength Finder): The paper claims a heuristic but the derivation cuts off and Equation 6 is missing. This strength is undermined by the incomplete specification, so it is moved here.

## Novel Insights

None beyond the paper's own contributions. The reviewers' main observations validate the paper's self-reported findings (online learning strength, mixed LLM results) but do not uncover a fundamentally new insight about the method.

## Suggestions

1. **Define AdaTAM explicitly.** Add a subsection in Methodology with the full update equations for the Adam variant — show how the damping factor $d_t$ interacts with Adam's momentum, bias correction, and RMS normalization. Without this, the adaptive experiments are not reproducible.
2. **Complete the learning rate transfer derivation** and supply Equation 6. If the derivation space is limited, at minimum state the heuristic formula and cite the source.
3. **Resolve the warm-up experiment confusion.** Clarify which optimizer is switched to (SGDM or Adam) and remove the incongruent GNN reference. Report a single coherent experiment.
4. **Add variance estimates** for the core classification results. Even 3 runs with standard deviations would substantially increase credibility.

## Score and Decision

This paper identifies a genuine weakness in classical momentum (vulnerability to misaligned gradients) and proposes a sensible, physically motivated fix. The online learning experiment provides the strongest and most convincing evidence that TAM has value beyond what existing methods offer. However, the paper has three major specification gaps that prevent acceptance in its current form: (a) AdaTAM — the variant used in roughly half of all experiments — is never defined; (b) the learning rate transfer derivation is incomplete, with a critical equation referenced but absent; and (c) the warm-up experiment description is internally contradictory. These are not minor presentation issues but gaps that prevent the reader from understanding or reproducing the claimed results. The core idea is promising and salvageable with significant revisions, but as submitted, the paper does not meet the completeness bar for a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>