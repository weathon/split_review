# SimXRD-4M: Big Simulated X-ray Diffraction Data and Crystalline Symmetry Classification Benchmark

- Decision: Accept
- Scores: 6, 6, 5, 8

## Abstract
Powder X-ray diffraction (XRD) patterns are highly effective for crystal identification and play a pivotal role in materials discovery. While machine learning (ML) has advanced the analysis of powder XRD patterns, progress has been constrained by the limited availability of training data and established benchmarks. To address this, we introduce SimXRD, the largest open-source simulated XRD pattern dataset to date, aimed at accelerating the development of crystallographic informatics. We developed a novel XRD simulation method that incorporates comprehensive physical interactions, resulting in a high-fidelity database. SimXRD comprises 4,065,346 simulated powder XRD patterns, representing 119,569 unique crystal structures under 33 simulated conditions that reflect real-world variations. We benchmark 21 sequence models in both in-library and out-of-library scenarios and analyze the impact of class imbalance in long-tailed crystal label distributions. Remarkably, we find that: (1) current neural networks struggle with classifying low-frequency crystals, particularly in out-of-library situations; (2) models trained on SimXRD can generalize to real experimental data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a benchmark dataset "SimXRD" which comprises 4,065,346 simulated powder XRD patterns that represent 119,569 unique crystal structures. This dataset aims to advance crystallographic informatics by providing high-quality training data for machine learning models. The authors evaluated 21 sequence models on their XRD dataset, testing both in-library and out-of-library classification scenarios. Their analysis revealed that current models struggle with rare crystal types and showed how different physical conditions affect model performance. The results demonstrate that models trained on simulated data can work with real XRD patterns.

### Strengths
This is essentially a benchmark paper that introduces a dataset that can be a useful resource for the community.

1. Creates the largest open-source XRD dataset (4M+ patterns) with validation against experimental data, enabling advancement in crystallographic machine learning research
2. Provides benchmarking across 21 models (CNNs, RNNs, Transformers) with detailed performance metrics 
3. Tests both in-library and out-of-library scenarios and also evaluates against real experimental data (RRUFF dataset)
4. Identifies key challenges like long-tail distribution in crystal structures, providing directions for future machine learning model development

### Weaknesses
1. The paper benchmarks existing approaches without introducing new architectures to address the identified challenges, particularly for low-frequency crystal classification. This limits its technical novelty from an architectural perspective.

2. While generating experimental data is challenging, the validation against real-world data is limited. The RRUFF dataset (~3K patterns) represents only 0.07% of the simulated dataset size (4M+ patterns), and the comparison between simulated and real-world patterns is demonstrated only for Li2MnO3. A more comprehensive analysis of sim and real world gaps would be helpful.

3. The paper lacks investigation of model failure modes and interpretability analysis. For example, analyzing what patterns CNNs learn and how they make decisions could reveal important insights and potentially guide future architectural improvements. Such analysis would provide valuable direction for developing more effective models.

### Questions
1. Model Interpretability: Could you provide analysis of what patterns your best performing models learn from XRD data, and what features differentiate successful classifications from failures, especially for low-frequency crystals?

2. While not very important, it would be helpful to understand systematic differences between simulated and real XRD patterns beyond the Li2MnO3 case study, and identify which simulation parameters most affect model performance on real data.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Introduces a new dataset of simulated X-ray diffraction dataset. It is generated with a novel technique based on known physical interactions. This dataset is the largest symmetric dataset to date. They train existing model architectures on their dataset, and show that some models have superior performance using their dataset. However, CNNs (one of the most commonly used architectures for this task) do not perform well. They also struggle to handle low-frequency class labels, even with re-weighting of sample importance.

### Strengths
The novel technique for generating samples of data is quite interesting; gathering experimental x-ray diffraction data on scale for large machine learning projects is difficult. This gives a strong motivation and need for this paper in the research community. The explanation for the techniques (in appendix B4) is very strong and extremely easy to read. Overall, the work and explanation provided in the appendix is one of the strongest parts of the paper, and is excellent in both content and writing quality. 

The testing and the results appear to have had a significant amount of effort put into them and cover a variety of models. This provides strong support for the claims made and the generalizability of the results.

### Weaknesses
Overall: I think that this submission is on a very good track. As someone who has worked with x-ray diffraction data before, I understand the need for this work. However, the limitations of the dataset are too severe for practical use, and so I do not think that it is ready for use. 

The two main weaknesses are: 

A - There is no validation of SimXRD to show that the patterns it creates match reality. The results from the machine learning models trained on the data show that to ML algorithms it seems close enough, but analytical results would be nice. The only justification provided is the technique used to create the data and the results from training with SimXRD then testing on other datasets.

B - The poor performance of the models on the long-tailed distribution. These results undercut the quality of the distribution; they show that the dataset does not allow for training of models that perform accurately. 

C - I do not understand Figure 2. There are just lots of images, with very little explanation. Since it is referenced as a primary part of the paper and does not have extensive description in the text, I do not understand what it is describing.

D - Overall writing clarity (outside of the appendix) could use some improvement. Explanation seems like it would be sufficient for someone already familiar with the work, but not somebody learning about this for the first time. Additionally, there are some grammatical mistakes which cause confusion (missing three commas in the sentence on line 69-70 for example).

### Questions
1 - In line 36: Transitional methods for what? I assume symmetry identification, though extra clarity would be appreciated.

2 - Line 156 claims that existing symmetry methods rely on 1D CNNs? As it is currently written, it is saying that every technique that has been introduced uses 1D CNNs, which contradicts lines 296-308. 

3 - Lines 296-308: is this supposed to be a comprehensive list of techniques? As it is written, that is what it seems to be saying.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SimXRD, a simulated X-ray diffraction (XRD) pattern dataset for benchmarking crystalline symmetry classification tasks. The patterns are simulated using PySimXRD, a custom software based on diffraction physics, for (filtered) crystal structures in the Materials Project database. Using the dataset, analyses of crystal symmetry data and comparisons of ML models are performed.

### Strengths
The presented large-scale simulated XRD dataset is open-sourced, which could benefit the community.

### Weaknesses
 - The main contribution of this work is unclear. The analyses and benchmarks do not provide much insight into ML research. If the PySimXRD software contains new/better functions than previous XRD simulators, they should be specified; even so, the contributions are in physics or materials science, not ML. Rather than ICLR, venues like *Scientific Data* seem more suitable for this paper.
- The presentation logic and clarity of this paper are poor. Examples are listed in Questions.

- The simulated dataset uses lattice plane distance as the x-axis. How is it related to 2$\theta$ which is more commonly used in XRD data, and what’s the reason for this choice?
- The generalizability of models to experimental data is assessed by training on SimXRD and testing on RRUFF. Is RRUFF representative of experimental data influenced by various factors (materials type, physical condition, equipment, etc.)? How do the authors ensure this is a rigorous assessment?
- Line 157, “almost all related research…due to the lack of easily accessible datasets”, what does this mean?
- Line 345, is “being biased by classes of high frequency” a problem of CNN? It should be more related to the objective/loss function.
- Regarding presentation clarity:
  - Line 48, structure analysis being challenging for domain experts is irrelevant to the search-match method.
  - Line 59, what challenges do introducing large-scale databases present?
  - Line 79, repeated words.
  - Line 216, the details on the Materials Project are irrelevant to this work.

### Questions
- The simulated dataset uses lattice plane distance as the x-axis. How is it related to 2$\theta$ which is more commonly used in XRD data, and what’s the reason for this choice?
- The generalizability of models to experimental data is assessed by training on SimXRD and testing on RRUFF. Is RRUFF representative of experimental data influenced by various factors (materials type, physical condition, equipment, etc.)? How do the authors ensure this is a rigorous assessment?
- Line 157, “almost all related research…due to the lack of easily accessible datasets”, what does this mean?
- Line 345, is “being biased by classes of high frequency” a problem of CNN? It should be more related to the objective/loss function.
- Regarding presentation clarity:
  - Line 48, structure analysis being challenging for domain experts is irrelevant to the search-match method.
  - Line 59, what challenges do introducing large-scale databases present?
  - Line 79, repeated words.
  - Line 216, the details on the Materials Project are irrelevant to this work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Overall, the work presents a valuable dataset and simulation environment for PXRD patterns, which is a great topic of interest in the materials science community.

### Strengths
- Accurate simulation of PXRD patterns is a timely topic of great recent research interest, and actually something I have grappled with in my own work, so I was pleased to read of your work that systematically does this in an easy software package.
- Allows users to simulate PXRD patterns with a wide variety of realistic settings not offered in other packages: grain size, stress, temperature, orientation, background, drift, noise. This is very important for addressing the sim2real gap in computational materials science.
- Some really cool figures (Figure 1, Figure 2) that show that we can simulate PXRD patterns that look like real experimental data. Other leading packages like Pymatgen are known to be unable to do this.
- Validates that models trained on these simulated PXRD patterns can generalize to experiments on real data.
- Well-presented and easily usable open-source code, especially this early in the review process. It gives me faith that this is a reproducible, adaptable contribution to the community.
- Brings to light the weaknesses of previous works (CNN-based) in dealing with the unbalanced symmetry classification task. This is especially important, as it would presumably be more important to analyze the less common symmetry groups.

### Weaknesses
I have a number of important suggestions for improvement, but most of these are easily addressable, rather than fundamental limitations of your work:
- Baseline for Dataset: This work is under the datasets and benchmarks task. You certainly addressed the benchmark part of this, by evaluating multiple space group classification models on your work. However, it is necessary to have baselines for the dataset. In particular, if you simulated PXRD patterns with Pymatgen and GSAS-II [6] and trained models on these, how would it perform on experimental data, as compared to training on SimXRD? The value of the dataset presumably comes from the fact that training on it would reflect real-world conditions with better fidelity, and thus, lead to boosted performance in testing, as compared to training on less realistic patterns. Thus, you need to show that other available datasets/simulators (Pymatgen, GSAS-II) cannot lead to the same sim2real transfer.
- Presentation of Figures: It's really cool that you can simulate PXRD patterns that look like actual experimental data. I'd like to see some more examples of these in a larger diagram. I only saw some small pictures in Figure 1 and Figure 2. I think displaying 4-6 examples of these in a large figure (preferably in the main text) would really drive home the point that your work provides the most realistic simulations of PXRD patterns available. In line with the previous comment, you should also compare to what other simulators (Pymatgen, GSAS-II) can give.
- Simulation Fidelity Evaluation: Can you take maybe 10 experimental patterns with known ground truth structures, and simulate patterns with SimXRD, Pymatgen, and GSAS-II? Then see the R_w goodness of fit value as compared to the experimentally observed? Of course, in this experiment, you'd need to play with the parameters (if available) to get the best fit possible from each software (although I think only GSAS-II, SimXRD, and possibly TOPAS, if you have that; make this possible). I see that you already have the embryo of this in Figure 1, so hopefully it should not be that hard to do on a few patterns. Again, this would emphasize the point that you have the most realistic simulator available.
- Address Structure Solution: Although symmetry classification is important, it's just one step towards the grand challenge of end-to-end structure determination from PXRD. This end-to-end solution paradigm has gained a lot of interest, as of 2024. You seem not to cite the relevant works in the field: please look at them and cite them [1, 2, 3, 4, 5]. It's probably not feasible to train or evaluate such generative structure prediction models in such a short period of time, especially since most of them are very new and not-yet open source. But at least mention them, because I think in the future, this dataset will be very valuable for training the PXRD structure solvers, and you should let the relevant authors see that your work is relevant to them, so that the impact of your work can be maximized!
- Writing: It seems that your intro is fixated on the benchmark part of your contribution, but I think you can emphasize more how this dataset itself is valuable. Again, in my own experience, I have actually been looking for a dataset like this, to address the sim2real gap common in computational crystallography. For instance, out of the bullets on the bold bulleted list at the end of page 2, I actually find the third ("Experimental Data Generalization") more interesting, and I think you could emphasize that direction more in your presentation.

### Questions
- Are you able to generate PXRD patterns of varying Q-ranges and/or x-ray wavelengths?

### Soundness
3

### Presentation
2

### Contribution
3
