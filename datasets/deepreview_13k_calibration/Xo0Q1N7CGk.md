# An Investigation of Conformal Isometry Hypothesis for Grid Cells

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
This paper investigates the conformal isometry hypothesis as a potential explanation for hexagonal periodic patterns in grid cell response maps. The hypothesis posits that grid cell activity forms a high-dimensional vector in neural space, encoding the agent’s position in 2D physical space. As the agent moves, this vector rotates within a 2D manifold in the neural space, driven by a recurrent neural network. The conformal hypothesis suggests that this neural manifold is a conformally isometric embedding of physical space, where local displacements in neural space are proportional to those in physical space. In this paper, we conduct numerical experiments to show that this hypothesis leads to the hexagon periodic patterns of grid cells, agnostic to the choice of transformation models. Furthermore, we present a theoretical understanding that hexagon patterns emerge by minimizing our loss function because hexagon flat torus exhibits minimal deviation from local conformal isometry. In addition, we propose a conformal modulation of the agent's input velocity, enabling the recurrent neural network of grid cells to satisfy the conformal isometry hypothesis automatically. %To summarize, our work provides numerical and theoretical evidences for the conformal isometry hypothesis for grid cells and may serve as a foundation for further development of normative models of grid cells and beyond.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the conformal isometry hypothesis for grid cells. They studied this in a minimal setting, in the isolation of modeling place cells. They show analysis that the hypothesis underlies the hexagonal periodic patterns that the grid cells exhibit. Moreover, they mathematically show that the hexagon patterns are minimal deviations from the local conformal isometry, which can emerge by minimizing the discussed loss function. They perform topological analysis and show the similarities of the arose patterns with their mathematical model to the neural data.

### Strengths
This is of interest to the community. It studies how grid cells encode spatial navigation and how these representations arise in the brain. The paper is written well, and concepts are clearly explained. I enjoyed reading the paper, and the math is thorough.

The proposed framework is novel compared to prior work; it reduces the assumptions required for the emerging hexagonal patterns.

### Weaknesses
I am not an expert in grid cell research; hence, it is a bit hard to fully appreciate and evaluate the significance of their minimalistic assumptions to model grid cells and study the conformal isometry hypothesis. This suggests a more in-depth discussion on why this proposal is better than prior works. Table 1 briefly shows that the framework offers better grid patterns for learning. Moreover, the paper discusses that their assumptions are less strict than prior works. These comparisons should be included in-depth in the main paper (in this version, only the intro discusses). Moreover, the first half of the paper is organized well; however, the theoretical analysis can be organized better. I recommend combining Sections 4 and 5.


I have comments about additional experiments and discussions that can help to improve the paper (see my questions).


minor 

- Some sentences in the abstract are exactly repeated in the intro. I suggest to revise.
- Line 76: Please clarify the "our loss function". Same for line 86.
- Line 126: no need to re-state "D is the 2d Euclidean domain". It has already been stated at the end of page 2.

### Questions
- It would be nice to know the consequence of their model assumptions on what we know about neural representations in the brain; their model seems to have removed some assumptions that the literature seems to think are needed for grid cells to arise.

- Can the authors also discuss what parameter or assumption in the model may break the emergence of hexagonal patterns? For example, can the authors conduct an ablation study where an assumption is violated or added, resulting in no longer optimal hexagons? This study may bring much value. For example, the authors emphasize the importance of the normalization step, which plays a crucial role in finding the correlation between terms in the theoretical analysis. Possible to see numerical analysis in the absence of such constraint?

- It was reported briefly how this work differs from Gao et al. 's. (2021) and Xu et al. (2022) on their study on conformal isometry, please discuss the importance of the difference. Why the proposed approach of only modeling the grid cells is better than the previously studied combined model?

- Could the authors please explain the choice of 1.25 and 3 in the experiment design in Section 3.3.

- Three models are chosen, showing that the grid pattern still emerges. Can the authors clarify if their results are fully independent of the choice of such models?

- More clarifications are needed for Figure 2. How exactly are Figure 2b(ii) and (iii) constructed?

- Is the finding on the proportion of the scale of patterns and the s parameter unique and new from this paper?

- What is the impact of \lambda on the presented analysis and results?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper explores the conformal isometry hypothesis as an explanation for the hexagonal patterns observed in grid cell responses. The authors conduct numerical experiments to show that this hypothesis leads to the hexagon periodic patterns of grid cells, agnostic to the choice of transformation models. Also, a theoretical understanding that hexagon patterns emerge by minimizing the loss function is presented.

### Strengths
- The authors conduct numerical experiments to show that this hypothesis leads to the hexagon periodic patterns of grid cells, agnostic to the choice of transformation models.

- The use of RNN serves as a foundation for further development of normative models of grid cells.

- Some theoretical analysis is presented showing that the hexagonal grid patterns emerge by minimizing the loss function.

### Weaknesses
 - A primary limitation of this paper is that the explored neural networks are restricted to ReLU, GELU, and Tanh activation functions. Could the authors consider extending their framework to support a broader range of activation functions? Specifically, it would be beneficial to see results with activation functions that have different properties, such as those with non-monotonic behavior or different saturation characteristics, to assess the robustness of the findings.

- Could the authors clarify the structure of neural network studied in this paper? There is no mention about the number of layers. Additionally, the reader could benefit from explaining why the authors selected the studied activation functions. The depth of the network is a critical parameter, and its absence makes it difficult to assess the complexity of the model. Furthermore, the rationale behind the choice of ReLU, GELU, and Tanh should be explicitly stated, as these have different properties that could influence the results.

- The paper would benefit from a deeper discussion on how the conformal isometry hypothesis compares to alternative theories of grid cell patterns which are missing in the current submission. A more thorough comparison with existing models, including those based on oscillatory interference or attractor networks, is needed to position the proposed hypothesis within the broader context of grid cell research. This would help to clarify the unique contributions and limitations of the conformal isometry approach.

### Questions
- It would be valuable, however, to see a comparison between the proposed conformal model and other standard models of grid cell activity, as this would provide more context on the advantages or limitations of the proposed approach.

- Could the authors expand on how this hypothesis might be experimentally tested in biological systems or how it could inspire new architectures in machine learning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present numerical and theoretical evidence that the grid cell tuning to 2D position (which follows a hexagonal lattice) would arise whenever the neural representation is (approximately) a conformally isometric embedding of space. This follows up on a select number of previous works that posited the "conformal hypothesis" of grid cell tuning. This paper aims to present a simplified analysis that is stripped down to only the most necessary details.

### Strengths
* The paper is generally well written and self contained. I had not heard of the "conformal hypothesis" before reading this paper, but was able to follow the essential message without reading the prior cited works in detail.

* The paper studies a very simple, minimal model that is nonetheless sufficient to produce striking grid cell firing patterns

* The numerical experiments are convincing (although some additional details on how the simulation is set up would be helpful). I particularly like the ablation experiments in Fig 3e-h.

* The core theoretical insight (which I view as being shown in sections 4.1) is quite interesting. The rest of the theoretical analysis in sections 4.3, 4.4, and 5.2 seems technically sound. However, the contribution of these additional sections is less clear from the presentation.

### Weaknesses
 * As far as I can tell, there is no normative explanation or hypothesis that would explain *why* the neural manifold encoding 2D space *ought* to be a isometric embedding of physical space. What are the potential benefits of this coding scheme? Absent any functional benefit, it is hard to interpret the significance of these results. Is it just a coincidence that this model gives the same grid coding scheme as real networks? Or is there a deeper reason why biological and artificial networks will converge upon a conformal map of space?

* Sections 4.2 - 4.4 are confusing. Because there are three sections, it feels as though the authors are trying to list three different results, but I think all three of these sections are really just supporting the same result (i.e. that hexagonal flat torus results in minimal deviation from local isometry). I suggest that the authors merge these three subsections into one. Furthermore, it would be easier to read if the main result were formally presented as a proposition and, potentially, if the result in section 4.3 were formally presented as a lemma. Overall, I would suggest re-writing this portion of the paper to make the motivation more clear.

* It would be useful to investigate how important assumption 3 (normalization) is to the results. Figure 3f shows that the hexagonal grids do not form when normalization is removed entirely. Real biological networks are likely normalized imperfectly. Is imperfect normalization sufficient to get hexagonal grids? That is, what if $1 - \epsilon \leq \Vert \mathbf{v}(\mathbf{x}) \Vert \leq 1 + \epsilon$ for some $\epsilon > 0$? How big can $\epsilon$ get before the grids fail to form?

* There is a question about whether ICLR is the optimal venue for this kind of work, which I think will be primarily interesting to experimental and theoretical neuroscientists. I think this work will have little to no cross-over appeal to machine learning or artificial intelligence communities.

### Questions
* As mentioned above, I would like to know whether there is a normative explanation or theory behind the conformal hypothesis of grid cell coding. Is there a potential benefit (e.g. in terms of energy efficiency or decoding accuracy) for this kind of representation?

* Put differently, is there a justification for why the objective function defined in equations 3 and 4 is a good proxy for the constraints faced by real biological neural systems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work explores the conformal isometry hypothesis (i.e., that grid cells in MEC encode a conformal isometry that may be useful for spatial navigation) in artificial neural networks. The authors take a minimalistic approach, showing that hexagonal grids emerge robustly when optimizing a conformal isometry loss function. They show evidence for conformal isometry in real neural recordings. They analytically probe why hexagonal grid cells would emerge from their optimization, finding them to be optimal among flat tori. Finally, the authors demonstrate that modifying their loss function can lead to the emergence of multiple grid modules.

### Strengths
This paper thoroughly studies different aspects of the conformal isometry hypothesis. The authors' results on: 1) the robustness of grid cells emerging from optimizing a conformal isometry loss function; 2) the connection of the grid scale to the scalar $s$ in the conformal isometry; 3) the analytical results showing why a hexagonal torus is optimal; 4) the demonstration of real neural data satisfying the conformal isometry; 5) the expansion of the authors' results to multiple modules, all are nice additions to the computational study of grid cells.

### Weaknesses
I think there are two points that could be improved upon to increase the quality of this work:

1. While the authors made it clear why a hexagonal torus is local isotropic, it was not clear to me when/if the authors ever showed it was optimal because it "achieve the least deviation from local flatness because it distributes the extrinsic curvature evenly over all directions" (Sec. 4.4). Providing more discussion on this (and explaining why other flat tori do not distribute extrinsic curvature evenly) would make their point of optimality more clear. Specifically, it is not clear how the authors demonstrate that the hexagonal torus minimizes the integral of the squared deviation from local flatness, and how this relates to the even distribution of extrinsic curvature. A more detailed explanation of the mathematical argument, perhaps including a derivation or a more explicit connection to the Cauchy-Schwarz inequality, would be beneficial.

2. While it was interesting to see that the framework developed by the authors could be expanded to include the generation of multiple modules (that were organized approximately $\sqrt(2)$ apart in grid spacing), how exactly the multiple modules tied in to the idea of conformal isometry was lost for me. In an otherwise well structured paper, it felt a little like it was tacked on at the end and the thread was lost. Providing more discussion on how having multiple modules, in addition to the need to decode place responses, affects the kinds of representations that lead to conformal isometry, would be helpful. It would be useful to see a more detailed explanation of how different scaling factors within each module contribute to the overall representation and how this relates to the conformal isometry. The connection between the multiple modules and the ability to decode place responses at different resolutions should be made more explicit.

MINOR POINTS: 

1. What is meant by "$\Delta x$ is constrained to be smaller than 3 grids?" By this do you mean 3 grids of the underlying space discretization? Maybe using a different word would be helpful to keep the reader from confusing this with grid cells. 

2. What is valid rate that is reported in Table 1? 

3. The real neural data analyzed by the authors satisfies conformal isometry (Fig. 5 - up to $|\Delta x|| = 0.2$) for a much larger scale than the grid cells generated by the authors' models (Fig. 4 - up to $|\Delta x|| = 0.08$). Why do the authors think this is? Could this be due to the Gardner et al. data having variability in grid properties (Redman et al., 2024) not present in the authors' model?

4. Which module from the Garnder et al. data set was analyzed? If I remember correctly, none of the modules had 93 grid cells. Did the authors perform some screening on which grid cells to include?

### Questions
1. Why is the hexagonal torus optimal (as compared to other flat tori)? 

2. How does having multiple grid modules affect the conformal isometry? 

3. Why might the neural data satisfy the conformal isometry over a larger scale than the simulations?

4. Which modules was analyzed in Fig. 5 and Fig. 11, and was any pre-processing performed on them?

### Soundness
3

### Presentation
3

### Contribution
3
