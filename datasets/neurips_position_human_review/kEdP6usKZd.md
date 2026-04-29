# Beyond Equilibrium: Non‑Equilibrium Foundations Should Underpin Generative Processes in Complex Systems

- Decision: Reject
- Scores: 6, 7, 6

## Abstract
This position paper argues that next-generation non-equilibrium-inspired generative models will provide the essential foundation for better modeling real-world complex dynamical systems. While many classical generative algorithms draw inspiration from equilibrium physics, they are fundamentally limited in representing systems with transient, irreversible, or far-from-equilibrium behavior. We show that non-equilibrium frameworks naturally capture non-equilibrium processes and evolving distributions. Through empirical experiments on a dynamic Printz potential system, we demonstrate that non-equilibrium generative models better track temporal evolution and adapt to non-stationary landscapes. We further highlight future directions such as integrating non-equilibrium principles with generative AI to simulate rare events, inferring underlying mechanisms, and representing multi-scale dynamics across scientific domains. Our position is that embracing non-equilibrium physics is not merely beneficial—but necessary—for generative AI to serve as a scientific modeling tool, offering new capabilities for simulating, understanding, and controlling complex systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper argues that in many physical systems, the equilibrium assumption fails, requiring tools from non-equilibrium statistical mechanics for accurate modeling. For example, the Boltzmann distribution—a cornerstone of equilibrium statistical mechanics—only holds when a system is in equilibrium. If we naively apply such assumptions to non-equilibrium systems (e.g., driven or time-varying systems), the results will be physically inaccurate.
	
	The paper advocates for non-equilibrium generative models (like diffusion processes) that better capture real-world dynamics, where systems are often far from equilibrium, irreversible, or subject to external forcing.

### Strengths
This paper clearly arguing that non-equilibrium physics should underpin generative models for complex dynamical systems, presenting a compelling case through both theoretical reasoning (connecting statistical mechanics to modern ML) and empirical evidence (demonstrating superior performance on time-evolving systems like the Printz potential). It addresses core challenges in generative AI—simulating non-stationary processes and rare events—while offering principled solutions grounded in physics.

### Weaknesses
- The paper argues that equilibrium-based EBMs are theoretically better suited for static data (like images), since they directly model the Boltzmann distribution without time-dependent dynamics. However, the empirical reality contradicts this: diffusion models—which are fundamentally non-equilibrium—consistently produce higher-quality images in practice.
How do you reconcile this gap between your theoretical framework (favoring EBMs for static systems) and the overwhelming empirical success of diffusion models? Is this a fundamental limitation of equilibrium approaches?

- The analysis shows EBMs need only learn a scalar potential while non-equilibrium methods must model vector fields. Could you elaborate on the computational implications of this fundamental difference? Specifically, does modeling velocity fields become more demanding due to (1) the higher-dimensional output space requiring more complex architectures, (2) the need for iterative sampling processes that scale poorly with dimensionality, or (3) inherent challenges in training dynamics like gradient instability? Understanding whether these costs stem from theoretical necessities or just current implementation limitations.

### Questions
- The Equivalence between Eq.~7 and Eq.~8 is not clear. Especially this sentence:\\
``Compared with Equation 7 with 8, the ELBO parallels variational free energy, with its likelihood and KL terms corresponding to expected energy and entropy, thereby linking VAEs to both equilibrium and non-equilibrium statistical mechanics."

-  Ref 153 is not correct. 
- In Eq.~2 it is not clear what is $\<ij\>$, Please clarify.

- The authors mentioned fluctuation theorem (Jarzynski-Crooks) in the paper multiple times, but doesn't clearly articulate their practical implications.  While these theorems provide elegant theoretical frameworks, their practical application often faces significant challenges. For instance, the Jarzynski equality is known to suffer from high variance in estimation, requiring extensive trajectory sampling between states to obtain meaningful results. What specific advantages these fluctuation theorems offer for the proposed non-equilibrium generative framework?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The paper argues that many real systems are far from equilibrium, so generative models for scientific/temporal phenomena should be grounded in non-equilibrium statistical mechanics rather than equilibrium analogies. After situating diffusion/Schrödinger-bridge–style methods historically, it presents a time-varying potential case study where a non-equilibrium approach tracks the evolving distribution better than an equilibrium sampler. It lays out research directions (rare events, multi-scale dynamics, entropy production control) and contends that non-equilibrium principles are necessary for faithful generative modeling of dynamical systems.

### Strengths
- Takes a timely stance with relevance to AI-for-Science and time-dependent generative modeling.
- Effective historical and contextual bridge from statistical physics to modern ML with clear articulation of gaps in equilibrium framing.
- Includes an illustrative experiment showing advantages of non-equilibrium modeling for dynamic distributions.
- Provides thoughtful Alternative Views section with counterarguments.
- Strong discussion potential and useful research agenda (rare events, multiscale, flux/entropy constraints).

### Weaknesses
- At times "non-equilibrium foundations" read as "use diffusion-like training", which is already mainstream. Authors could clarify what is beyond DDPM / SB.
- Non-equilibrium methods can raise computation and gradient variance. The paper could include a discussion about runtime / variance table versus equilibrium surrogates and discuss where the cost pays off. Computational costs seemed to be downplayed.
-The single synthetic dynamic-potential example seems too narrow.

### Questions
- For which task classes would you not recommend non-equilibrium foundations?
- How sensitive are results to time-discretization and stiffness?
- For which task classes would you not recommend non-equilibrium foundations?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Although current generative AI models mainly focus on tasks over images, texts, videos, etc, their working mechanism actually resembles the statistical physics processes, therefore can be analyzed from the perspective of statistical physics. This paper analyze the generative models for modelling real-world complex dynamical systems, and proposes the position that non-equilibrium is essential for better modelling real-world dynamical systems, while the existing models relies on the equilibrium assumption.

In additional to conceptual analysis, the paper also provides empirical results demonstrating that non-equilibrium based models can better capture the temporal evolution and making models adaptable to non-stationary cases.

### Strengths
1. This paper provides a new and insightful perspective to analyze the generative AI models, with theoretical and empirical justification for supporting the new position on the importance of non-equilibrium based generative AI models.

2. The background of the target problem is well introduced with clear history timeline. The new analysis and results are also well presented with proper figures.

3. In addition to the position, preliminary experiments are also provided to support the claim,

### Weaknesses
1. Although briefly mentioned in the alternative positions part, it would still be better if more analysis and experiments can be provided to analyze why the existing equilibrium based methods can actually perform very well, given that they don't follow the non-equilibrium assumption.

2. The experiments are conducted on abstract systems without touching real-world systems, which may provide more insights and make the claim more convincing.

3. Are diffusion models based on equilibrium or not, could they be included in the analysis in Section 2.3?

### Questions
Please refer to the weakness part.

### Presentation
3
