# Position: Require Frontier AI Labs To Release Small "Analog" Models

- Decision: Accept
- Scores: 4, 6, 6

## Abstract
Recent proposals for regulating frontier AI models have sparked concerns about the cost of safety regulation, and most such regulations have been shelved due to the safety-innovation tradeoff. This paper argues for an alternative regulatory approach that ensures AI safety while actively \textit{promoting} innovation: mandating that large AI laboratories release small, openly accessible "analog models"—scaled-down versions trained similarly to and distilled from their largest proprietary models.

Analog models serve as public proxies, allowing broad participation in safety verification, interpretability research, and algorithmic transparency without forcing labs to disclose their full-scale models. Recent research demonstrates that safety and interpretability methods developed using these smaller models generalize effectively to frontier-scale systems. By enabling the wider research community to directly investigate and innovate upon accessible analogs, our policy substantially reduces the regulatory burden and accelerates safety advancements.

This mandate promises minimal additional costs, leveraging reusable resources like data and infrastructure, while significantly contributing to the public good. Our hope is not only that this policy be adopted, but that it illustrates a broader principle supporting fundamental research in machine learning: deeper understanding of models relaxes the safety-innovation tradeoff and lets us have more of both.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
This work argues organizations that develop "frontier" AI models ought to release smaller distilled "analogue" models with very similar architecture, trained on the same dataset and optimization objectives but with only a small fraction of the number of parameters. Such analogue models would supposedly facilitate interpretability research, since distilled models can likely still enable intervention studies given certain observed universality in LLM circuit. Additional benefits include promoting open source science and encouraging AI innovation which would bring societal benefits. At the same time, there are also risks associated with requiring to release analogue models, such as intellectual property loss and

### Strengths
- The work is easy to follow. Positions and counterpoints are clear presented and well argued for.
- The topic is very important in that it could potentially accelerate generative AI safety research.

### Weaknesses
- The main premise of the paper is that distilled models has "reliable transferability of insights" (L 46), i.e. (enough of) the "safety and interpretability interventions discovered" (L 61) in the analogue can be transferred to the base/teacher model which is commercially released. But this ignores [recent](https://arxiv.org/abs/2505.11837) [examples](https://aclanthology.org/2025.acl-short.61/) of distilled models having distinct behaviours (e.g. [amplifying harms](https://arxiv.org/pdf/2505.24842)) than the base model: for example, the distilled model may only capture part of the mechanisms of the base model, and so interventions found on it should not be expected to necessarily work on the base model. *In sum, the distilled -> base model transfer is not straightforward and claims need to be assessed empirically.*
- The analogy drawn on generic vs brand-name drug is not entirely accurate. In that case, the differences lie primarily in formulation, including inactive ingredients with potential side effects. For drugs needing precise dosage to function properly, this could make a large difference.

### Questions
- How would the proposed approach apply to closed-source models such as ChatGPT?
- Are there other ways to "democratize access to advanced AI research" (L256-257)? For example, grant better cloud GPU/TPU access to researchers who would otherwise have difficulty getting access to those machines?
- The discussion has mostly focussed on LLMs. Would it generalize to other kinds of generative AI models especially multimodal models?

### Presentation
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This position paper proposes a regulatory mandate that any lab releasing a frontier AI model must also release a small-scale, openly accessible “analog model” trained on the same data and objectives, typically via distillation. The analog would be capped at 0.5–5% of the parameter count of the frontier model, released within 1–3 months of deployment, and licensed permissively for research. The authors argue that safety interventions and interpretability findings discovered in these smaller models reliably transfer to the larger systems, citing empirical studies, representational similarity research, and scaling laws. They present detailed policy mechanisms, compliance timelines, enforcement pathways, and cost estimates showing minimal burden. The paper also anticipates and addresses objections (IP, dual-use, substitution risk), drawing analogies from pharmaceuticals and telecom standards to illustrate that regulated openness can coexist with innovation incentives. The core claim is that such a mandate would relax the perceived safety–innovation tradeoff, providing substantial public benefit at low cost.

### Strengths
Presents a clear, concrete, and implementable policy proposal, backed by both technical research and policy precedent.

Effectively synthesizes empirical results on cross-scale transferability, representational similarity, and scaling laws to support the central claim.

Anticipates major objections (IP, competitive risk, security) and offers detailed mitigation strategies.

Uses compelling analogies from other regulated sectors to illustrate feasibility and precedent for openness without undermining innovation incentives.

Includes a cost analysis that convincingly argues for minimal compliance burden, enhancing the proposal’s practical appeal.

### Weaknesses
The discussion of cross-scale transfer largely assumes that smaller analogs capture the key behaviors of frontier models, without deeply engaging with cases where emergent or scale-specific behaviors may not manifest in the smaller version.

The empirical foundation for reliable safety transfer is still relatively early-stage; potential policy downsides if this assumption fails could be explored more fully.

The paper could give more attention to challenges of enforcing such a mandate globally and ensuring consistent compliance across jurisdictions.

### Questions
How would you ensure that analog models are representative enough when certain capabilities or behaviors only emerge at larger scales? Some concrete discussion of this is necessary for the arguments to land well.

Would you propose formal benchmarks or fidelity metrics to verify that analog models are suitable for meaningful safety and interpretability research?

What adaptations would be necessary for applying this mandate to multi-modal or non-text-based frontier models, where scaling patterns and representational alignment may differ?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a regulatory policy requiring AI labs to release an “analog model”—defined as a small, openly accessible proxy for a proprietary model crossing established frontier thresholds—shortly after each major model deployment. Drawing on empirical evidence, the paper argues that safety and interpretability interventions developed on these smaller models reliably transfer to larger ones, as capability and representations scale predictably with model size in identical or closely matching architecture families. The authors conclude that their analog-model mandate could shift the safety–innovation frontier outward, reconciling public oversight with rapid private-sector AI progress.

### Strengths
This position paper is a thoughtful and timely contribution to AI safety research. The authors convincingly argue that the benefits associated with their proposed policy include accelerated safety research, improved transparency and public trust, and wider innovation participation at low cost (≈0.1–0.2% of training expenses), while risks such as intellectual property leakage or dual-use/misuse are addressed through size caps, delayed releases, and security assessments.

### Weaknesses
The potential limits to the transferability of safety and interpretability mechanisms from smaller analog models to larger frontier models could be explored more rigorously.

### Questions
Do capability and safety scale predictably for vision/audio/multi-modal models?

### Presentation
3
