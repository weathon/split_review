Here is the final consolidated review.

---

## Summary

LANE extends the Area Under the Margin (AUM) framework for learning under label noise in fine-grained text classification. It makes two main changes: (1) it rescales the AUM margin by class-similarity weights learned through a weighting network Π trained via a label-aware supervised contrastive loss (LSCL), and (2) it replaces AUM's hard threshold removal with a soft reweighting scheme that fits a truncated Gaussian to the negative ALM distribution and down-weights (rather than discards) likely mislabeled samples. The method is evaluated on 10 fine-grained classification datasets against several baselines.

## Strengths

- **Concrete demonstration of the label-aware margin's differentiating behavior (Table 1).** The paper shows two samples with identical vanilla margins (−0.6) that receive different label-aware margins because one mislabel is semantically close (fear→anger, LM = −0.5) and the other is distant (fear→trust, LM = −0.3). This is a direct, reproducible illustration of a genuine limitation in the vanilla AUM formulation.

- **Consistent empirical gains across 10 diverse datasets under original and 20% symmetric-noise conditions (Tables 2, 3).** LANE outperforms all baselines (DISC, UNICON, AUM, PLF, LCL, SCL, noise layer, data cartography) on every dataset in both conditions. The improvement over AUM on SST5 at 20% noise is 2.7% accuracy; over DISC it is 1.4%; and over UNICON it is 2.3%. The breadth of datasets (7 to 105 classes; emotion, sentiment, topic domains) rules out task-specific artifacts.

- **Ablation confirms both components contribute (Table 4).** On RCV1 (105 classes), LANE achieves 49.4% micro F1 versus 45.2% for LANE^{−sim} (removing the semantic similarity component, a 4.2-point drop) and 46.2% for LANE^{−alm} (removing the ALM weighting, a 3.2-point drop). Both components are shown to be empirically necessary, and the gap is largest on the dataset with the most classes, where inter-class distinctions matter most.

- **Principled soft reweighting replaces AUM's hard removal (Section 3.2, Eqs. 5–8).** The truncated Gaussian fit to the negative-ALM distribution is a conceptually cleaner and more practical approach than AUM's fixed threshold elimination: the model retains all training data but adaptively down-weights samples whose ALM falls below the dynamically estimated mean, avoiding information loss from discarding difficult but valuable examples.

## Weaknesses

### Fatal
None.

### Major

- **The 40% noise results described in the experimental design are absent.** Section 4.1 (line 129) explicitly lists "40% noise, where we perform the same process for 40% of the training examples" as one of three evaluation setups. No results for this condition appear anywhere in the paper — not in the tables, analysis, or conclusion. The abstract claims testing on "various amounts of label noise," but only two amounts (original and 20%) are reported. This is a basic completeness failure: the reader cannot assess how LANE behaves as noise increases toward 40%, and whether gains are maintained, diminish, or collapse.

- **The injected-noise experiments use only symmetric (random) label flips, which do not directly test the paper's core claim about inter-class semantic similarity.** The paper's central motivation is that semantically similar class confusions (e.g., fear↔anger) are less harmful than distant ones (fear↔joy). Yet the 20% injected-noise experiments flip labels uniformly at random — all class pairs are equally likely, regardless of semantic distance. Under this noise model, the label-aware margin's theoretical advantage is not probed. The original dataset results partially mitigate this (natural annotation noise tends to be class-conditional), but the paper does not acknowledge the gap or run asymmetric-noise experiments (e.g., constructing confusion matrices concentrated among similar classes) where the label-aware mechanism would be directly tested. Without this, it is unclear whether gains come from the label-awareness or from the weighting/contrastive components.

- **Training details essential for reproducibility are omitted.** The experimental setup (Section 4.2) specifies only the batch size (32), number of augmentations (7), and the α=0.5 loss weight. No learning rate, optimizer, number of epochs, warm-up schedule, or ALM initialization/warm-up strategy is provided. The ALM accumulates from "the beginning up until the current iteration" (line 91), but early, unreliable ALM estimates could harm training, and no handling mechanism is described. These omissions make the experiments difficult to reproduce.

### Minor

- **The LLM comparison (Table 5) does not inform the paper's research question.** Comparing LANE (fine-tuned BERT on the full training set, up to 600K examples) against ChatGPT and Llama-2 in a few-shot setting (100 examples, 10 for SciHTC) confounds multiple factors — dataset size, model scale, training paradigm — and does not isolate label noise robustness. The finding that a fine-tuned BERT model outperforms few-shot LLMs on most datasets is expected and does not speak to whether LANE is effective against label noise. This comparison should either be removed or replaced with a more controlled setup (e.g., fine-tuning the LLMs on the same noisy data).

- **The ablation does not isolate the contribution of the LSCL loss independently.** LANE^{−alm} removes the ALM weighting (sets λ=1) but retains the LSCL loss. An ablation that removes LSCL entirely (i.e., BERT + weighted CE based on ALM, without any contrastive component) is needed to determine how much of the gain comes from the contrastive loss versus the ALM weighting. Additionally, an ablation using standard AUM margins with LANE's Gaussian weighting (without the label-aware rescaling) would isolate whether the reweighting scheme alone drives the gains.

- **The joint training of θ and Π is described without addressing potential optimization challenges.** The paper states that the weighting network Π and classifier θ are "learned jointly" (line 69), creating a loop where Π's outputs affect the weights λ that train θ, whose representations h_x in turn feed Π. The LSCL loss (Eq. 2) also uses Π's own outputs w to modulate the contrastive learning. No gradient stopping, alternating optimization, or warm-up mechanism is described to prevent degenerate solutions (e.g., Π collapsing to near-uniform weights). This does not invalidate the method — joint training often works in practice — but the paper should at minimum acknowledge this concern and describe how it is managed.

### Trivial

- **Minor imprecision in describing AUM's thresholding.** Section 1 (line 12) says AUM uses a "fixed rigid AUM threshold (i.e., the 95 percentile)," while Section 3.1 (line 60) correctly describes Pleiss et al.'s two-stage procedure using an artificial holdout class to learn the threshold. The characterization in Section 1 is an oversimplification.

## Nice-to-Haves

- Running asymmetric-noise experiments (e.g., constructing confusion matrices from semantic similarity graphs of emotion labels) would directly validate the paper's central claim about label-awareness providing value.
- Adding significance testing (e.g., paired bootstrap over the 5 runs) would clarify whether the modest margins (1.3–1.6%) on some datasets are reliable.
- A hyperparameter sensitivity analysis for α (currently fixed at 0.5 with no exploration) would strengthen the paper.
- Reporting the 40% noise results would complete the evaluation and address the most obvious gap.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "Outperforms large language models on 9/10 noisy datasets."** Removed because this conflicts with a verified weakness — the LLM comparison is uninformative due to mismatched settings (full-dataset finetuning vs. few-shot). Per the merging rules, when a strength and weakness conflict, the weakness prevails.
- **Weakness: "Foundational circular dependency" (framed as fatal).** Demoted to Minor. The reviewer characterized this as a "structural/methodological" fatal flaw, but the joint training of Π and θ through two separate loss functions (LSCL and weighted CE) is a standard optimization setup, not a guaranteed degeneracy. The concern is reasonable as a discussion point but not a fatal error.
- **Weakness: "Label-aware margin conflates example-specific and class-pair information."** Demoted from the main weakness list. The reviewer's point is technically correct — w_{x,j} is an example-specific softmax output, not a direct measure of a priori class similarity — but this is already implicit in the design: Π is trained via LSCL to encode inter-class relationships, so its per-example outputs reflect semantic similarities. The paper's framing is somewhat imprecise but not misleading enough to warrant inclusion as a standalone weakness.
- **Weakness: "Inconsistency in AUM description."** This is a minor imprecision between the introduction and Section 3.1, but Section 3.1 gives the correct description. Demoted from the main list to a trivial note.
- **Weakness: "Statistical significance not reported."** This is a reasonable suggestion but not a weakness unique to this paper, and the paper does report means and standard deviations over 5 runs. Demoted to a nice-to-have.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension between the paper's motivating claim (label-awareness matters because of inter-class semantic similarity) and the evaluation design (symmetric noise does not test this), but this observation follows directly from reading the paper. The missing 40% results and incomplete training details are verification failures rather than novel insights.

## Suggestions

- Report the 40% noise results or explicitly remove the claim from the experimental setup and abstract. This is the single most actionable fix.
- Add asymmetric-noise experiments (e.g., flips concentrated among semantically similar classes using a confusion matrix derived from class embeddings or a similarity graph) to directly test whether the label-aware margin provides value in the setting it was designed for.
- Add an ablation that removes the LSCL loss entirely (simple BERT + weighted CE) to quantify the contrastive component's contribution.
- Add a standard AUM + Gaussian weighting ablation (without the label-aware margin rescaling) to isolate the benefit of reweighting from the benefit of label-awareness.
- Provide full training hyperparameters (learning rate, optimizer with settings, number of epochs, warm-up strategy) and describe how the ALM is initialized and when weighting begins.

## Score and Decision

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**