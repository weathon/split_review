# AI Progress Should Be Measured by Capability-Per-Resource, Not Scale Alone: A Framework for Gradient-Guided Resource Allocation in LLMs

- Decision: Accept
- Scores: 3, 5, 6

## Abstract
This position paper challenges the "scaling fundamentalism" dominating AI research, where unbounded growth in model size and computation has led to unsustainable environmental impacts and widening resource inequality. We argue that LLM development should be fundamentally reoriented toward capability-per-resource rather than capability alone. We present a theoretical framework demonstrating that resource-allocation decisions guided by gradient influence patterns can dramatically improve efficiency throughout the AI lifecycle. Our analysis shows that in transformer-based models, where a small fraction of parameters exert outsized influence (following heavy-tailed distributions), three critical insights emerge: (1) updating only high-influence parameters strictly outperforms full-parameter tuning on a performance-per-resource basis; (2) simple gradient norms provide computationally efficient proxies for identifying these high-influence components; and (3) coordinated parameter and data selection yields multiplicative efficiency gains, potentially reducing resource requirements by orders of magnitude. Building on these theoretical foundations, we propose a two-stage paradigm—marginal-return pretraining for foundation developers and influence-guided adaptation for downstream users—bridged by gradient blueprints, metadata describing which parameters matter most for various tasks. This capability-per-resource perspective transforms what were once considered pragmatic hardware workarounds into theoretically optimal strategies, democratizing access to cutting-edge AI capabilities while significantly reducing environmental impact. By embedding resource consciousness into how we develop, adapt, and evaluate models, we can reshape AI progress toward a more sustainable and equitable future.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the concept of "Capability-Per-Resource," defined as the ratio of performance improvement to the required resource investment, challenging the conventional focus on solely scaling model capabilities. The authors present an analysis of Transformer-based models, revealing that only a small fraction of parameters have a large gradient norm and a similarly small subset of data wields high influence on the gradient. Consequently, they argue that selective training of these key parameters and data points can yield significant efficiency gains. Building on these findings, the paper proposes two novel strategies: "marginal-return pretraining" for foundation model developers and "influence-guided adaptation" for end developers, both designed to optimize the trade-off between performance and computational cost.

### Strengths
The arguments in the introduction (lines 69-87) serve as a crucial alert regarding current foundation model development. The authors rightly emphasize the significant environmental impact, a point that large-model practitioners should be more aware of. Furthermore, the concentration of AI capabilities is a timely and important issue for the tech industry. The paper itself is well-structured and easy to follow.

### Weaknesses
This paper's central argument—that AI progress should be measured by capability-per-resource—is not adequately justified. The majority of the paper is dedicated to demonstrating methods for resource-conscious LLM development (e.g., parameter and data selection), rather than arguing for the fundamental importance of the capability-per-resource metric itself. A more compelling justification would involve discussing the environmental impact of massive resource allocation or how optimizing for capability-per-resource can foster high-performing models even under resource constraints. As it stands, the paper presupposes the reader's acceptance of this metric as a primary objective and then explains how to achieve it.

Additionally, the paper rests on several strong, yet unsupported, assumptions. For instance, the claim that the rate of improvement, ΔΨ/ΔΓ, smoothly diminishes to zero (as depicted in Figure 1) is questionable. This model fails to account for empirical phenomena such as grokking, where performance can stagnate for extended periods before a sudden improvement.

Finally, the proposed gradient-based selection methods are not novel (discussion to related work needed), and their effectiveness is not sufficiently justified.

### Questions
1.How valid is the power-law assumption in practice? Furthermore, what is the rationale for proposing it?
2 .Even if many parameters have a small gradient norm, how significantly do they affect downstream performance? Intuitively, a minor change to a parameter in an early layer—even one with a small gradient—could create a butterfly effect that substantially alters the final layer's output.

### Presentation
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This position paper contends that “scaling fundamentalism” overlooks sustainability and equity; it proposes measuring progress by capability-per-resource and optimizing training/adaptation via gradient influence. Concretely, it recommends (i) a marginal-return stopping rule for pretraining; (ii) influence-guided adaptation for downstream users using gradient blueprints—released metadata that identify high-influence submodules; and (iii) multiplicative gains by jointly selecting parameters and data. Theory argues partial updates can strictly beat full tuning on performance-per-resource under heavy-tailed gradients, with gradient norms as practical proxies; a cross-influence tensor motivates joint selection. The paper surveys related work and outlines a JSON blueprint schema.

### Strengths
1. Clear, actionable north-star metric (capability-per-resource) and stopping rule. 

2. Practical two-stage lifecycle and gradient blueprints to guide selective tuning. 

3. Formal insight that partial updates can strictly beat full tuning under heavy-tailed gradients. 

4. Justification for gradient-norm proxies instead of costly second-order influence. 

5. Articulates cross-influence idea for multiplicative savings; offers schema/implementation notes.

### Weaknesses
1. Empirical grounding is minimal; key claims (e.g., heavy-tailed gradients, blueprint utility) would benefit from targeted experiments/ablations. 

2. Assumptions (heavy tails; block-diagonal Fisher; local short-step regime) may break under large distribution shifts; guidance on when they fail is limited. 

3. Blueprint generalization and update drift over time are acknowledged but under-specified (e.g., refresh cadence, domain-shift detection). 

4. Limited discussion of privacy/security risks of releasing gradient maps (e.g., leakage or attack surface).

5. Cost model abstracts hardware parallelism

### Questions
1. Can you provide a small empirical study validating stopping on a public checkpoint (compute saved vs. loss/accuracy)? 

2. How stable are gradient blueprints across domains/time—what refresh protocol or confidence intervals do you recommend? 

3. Any privacy/safety analysis for releasing submodule-level gradient norms (e.g., data-leak risks, attack mitigation)?

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
This paper advocates for measuring AI progress in terms of capability-per-resource instead of only “scale” (or capability along).

The paper tries to make a normative argument that it is not the case that “ever larger models and more computation will inevitably lead to better AI.” This argument seems woven into sections rather than bracketed out explicitly; for example, the related work reads somewhat argumentative, it brings out specific pieces of work like stochastic parrots, critical of the dominant AI paradigm.

### Strengths
This argument of the paper is given sort of wrapped around a pretty meaty set of theoretical foundations and proposals related to model quantization, efficient training, selective data, and other proposals. These proposals and foundations seem to be the most useful bit of this paper, and they are tied together in a framework for a new paradigm for measuring ML performance.

The paper has a clear position. It also sets out to provide a theoretical foundation for achieving its proposal. It provides some analysis within the framework.

I am pretty borderline but would recommend accept.

### Weaknesses
Overall, I like this paper, but I wished there were real experiments and demonstrations where the proposals were actually implemented, so there’s a sense that efficiency and performance gains are possible. Some kind of Pareto understanding between these could be interesting, too, although I understand if this come up frequently in the literature.

However, absent those more empirical bits, it is a bit hard to tell whether the proposals work, and so the reader is left with a) firmly technical foundational proposals for measuring and reducing performance-per-resource and b) broad-strokes claims that this is how these things should be measured.

### Questions
One question:
How does the proposed selective data usage influence considerations like overfitting and generalization? Is there reason to believe that selective data use would harm these attributes of model performance?

### Presentation
3
