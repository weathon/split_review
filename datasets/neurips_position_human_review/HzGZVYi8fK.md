# Position: Biology is the Challenge Physics-Informed ML Needs to Evolve

- Decision: Accept
- Scores: 7, 5, 7

## Abstract
Physics-Informed Machine Learning (PIML) has successfully integrated mechanistic understanding into machine learning, particularly in domains governed by well-known physical laws.
This success has motivated efforts to apply PIML to biology, a field rich in dynamical systems but shaped by different constraints.
Biological modeling, however, presents unique challenges: multi-faceted and uncertain prior knowledge, heterogeneous and noisy data, partial observability, and complex, high-dimensional networks.
\textbf{In this position paper, we argue that these challenges should not be seen as obstacles to PIML, but as catalysts for its evolution. We propose Biology-Informed Machine Learning (BIML): a principled extension of PIML that retains its structural grounding while adapting to the practical realities of biology.}
Rather than replacing PIML, BIML retools its methods to operate under softer, probabilistic forms of prior knowledge.
We outline four foundational pillars as a roadmap for this transition: uncertainty quantification, contextualization, constrained latent structure inference, and scalability.
Foundation Models and Large Language Models will be key enablers, bridging human expertise with computational modeling.
We conclude with concrete recommendations to build the BIML ecosystem and channel PIML-inspired innovation toward challenges of high scientific and societal relevance.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
Physics-informed Machine Learning (PIML) is an established research line, which is characterized by the integration of Physics laws into Machine Learning models.
This paper puts forward the position that a promising evolution of PIML is Biology-informed Machine Learning (BIML), which has a similar scope to PIML while presenting unique challenges. 
After laying out such challenges, the position is articulated around four main pillars that should form the basis for future research in BIML, including: uncertainty quantification, contextualization, constrained latent structure inference, and scalability.
The paper discusses the possible role played by foundation models in this evolution to BIML, and it provides a short illustrative example on gene regulatory network inference. 
The paper then concludes with some alternative views.

### Strengths
- I enjoyed reading this paper. I think it is well-written and well-structured.

- The position is clearly stated and backed up by a significant number of appropriate references.

- I believe that the topics discussed in this position paper are timely; foundation models are becoming very popular and I expect that they will play a major role in future Machine Learning approches. I found the discussion on foundation models within BIML informative.

### Weaknesses
I cannot find any major weaknesses in this paper.

A minor point is about Physics informed Gaussian processes and Deep Gaussian Processes, which were developed way earlier than when PIML became a thing. A few examples: Calderhead et al., NeurIPS 2008, Dondelinger et al., AISTATS 2013, Lorenzi and Filippone, ICML 2018. -- and references therein.

### Questions
Maybe it would have been nice to see a couple of use-cases developed to a greater extent, but I'm well aware of space limitations. Maybe something to think about for the appendix?

Would it be possible to think of other fields where PIML could evolve to similar to BIML? In other words, are there any other fields characterized by the sort of challenges specific to Biology? Maybe this could be a nice way to expand on the paragraph about "Why biology should be the next frontier for PIML". Maybe something to elaborate on in the conclusions?

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper argues that the successes of physics-informed ML (PIML) do not translate directly to biology, a domain characterised by noisy, heterogeneous, partially observed, multi-scale systems. Rather than viewing these difficulties as roadblocks, the authors frame them as an opportunity to evolve PIML into Biology-Informed ML (BIML). They identify four structural mismatches (uncertain priors, data heterogeneity, hidden variables and network complexity) and propose four corresponding pillars (uncertainty quantification, contextualization, constrained latent structure inference and scalability). Concrete recommendations include biology-centric benchmarks and incentive structures. The position is that tackling biology’s challenges will catalyse methodological advances benefitting scientific ML broadly.

### Strengths
- I found the presentation to be clear and accessible to both ML and computational biology audiences. 
- The paper tries to make a diagnosis of why direct PIML to biology transfer fails and provides classification of four mismatches.
- Proposes actionable pillars and provides recommendations for benchmarking, incentives, interdisciplinary workshops, etc
- The paper takes a relevant position since biology is a major domain for for applying ML and the paper highlights risks of ignoring domain idiosyncrasies.
- Includes a dedicated alternative views section that tries to rebut opposing stances.

### Weaknesses
- The authors state "PIML ...near-complete observability" (lines 98-99) but ignores extensive work on state estimation in partially observed physical systems.
- The paper claims biology has 4 unique challenges but there might be oversimplifications. Example: climate models face uncertainty about cloud formation, aerosol interactions, and tipping points. They also involve complex networks of ocean-atmosphere-land interactions. (Social networks also exhibit similar complexity). 
- The paper does not explain why biological uncertainty is fundamentally different from uncertainty in PIML. Example: cosmological simulations must handle heterogeneity across galaxies, dark matter halos and cosmic environments. Materials science also deals with heterogeneous alloys and composites. We also cannot observe dark matter directly, only its gravitational effects. The paper's claim that "only sparse glimpses" are available uniquely in biology seems to be simplistic.
- The authors claim (lines 237-238): "These...are not speculative add-ons...components." and they admit (lines 240-241) "simple baselines...outperform LLMs". This inclusion of FMs / LLMs seem to dilute the core PIML or BIML argument since LLMs have their share of issues and concerns.

### Questions
- How would uncertainty quantification scale to the "dozens or hundreds of interacting species" (lines 111-112)?
- Can you provide specific examples where current PIML methods have failed on biological problems due to the four challenges?
- How would you validate BIML methods when biological ground truth is often unavailable?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This position paper argues that modern biology should be understood as a direct outgrowth of physics, both in conceptual foundations and methodological approaches. The authors contend that many breakthroughs in biology—particularly in molecular biology, biophysics, and systems biology—derive from physical principles and tools originally developed in physics. They advocate for a deeper integration of physics-based thinking into biological research, especially in the era of large-scale data, complex systems modeling, and AI-driven discovery. The paper reviews historical examples, outlines conceptual parallels between the disciplines, and identifies opportunities for cross-disciplinary training and research frameworks. The authors propose that embracing physics-style modeling and inference can accelerate biological discovery and improve the rigor of biological sciences.

### Strengths
- The central thesis is clearly articulated, with multiple historical and contemporary examples supporting the link between physics and biology.
- The paper is well-structured, progressing logically from conceptual framing to historical context and forward-looking recommendations.
- The emphasis on training, methodology transfer, and the potential for AI to strengthen cross-disciplinary research is timely.
- The writing style is clear and accessible, making it approachable for a broad NeurIPS audience.

### Weaknesses
- The paper’s examples, while compelling, are weighted toward molecular and systems biology; broader coverage of other biological subfields could improve generality.
- Although the argument is persuasive, quantitative evidence showing the direct impact of physics-derived approaches in recent biological breakthroughs is limited.
- The discussion of AI integration is relatively brief and could be expanded with specific scenarios or case studies.
- The call to action could be made more actionable, e.g., outlining concrete steps for the NeurIPS community to engage with biological research.

### Questions
1. Can the authors provide quantitative or bibliometric evidence showing trends in the adoption of physics-inspired methods in biological research?
2 How do the authors envision AI acting as a bridge between physics and biology in practical collaborative projects?
3. Are there specific subfields in biology where the physics-based approach has met resistance, and if so, how might these challenges be addressed?

### Presentation
3
