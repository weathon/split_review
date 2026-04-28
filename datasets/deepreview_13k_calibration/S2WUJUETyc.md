# Integrating Distributed Acoustic Sensing and PINN Frameworks for Enhanced Indoor Sound Source Localization

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Distributed Acoustic Sensing (DAS) is an emerging technology that transforms standard optical fibers into dense arrays of acoustic sensors, offering unprecedented opportunities for smart city applications, indoor monitoring of human activity, and surveillance without compromising privacy. In this paper, we integrate DAS with Physics-Informed Neural Networks (PINNs) for indoor sound source localization. By embedding the acoustic wave equation and impedance boundary conditions into the neural network architecture, we exploit physical laws to guide the learning process, improving accuracy and generalization. We propose two strategies for real-time sound source localization using DAS data. The first strategy involves training the PINN on all available data simultaneously, while the second strategy incrementally feeds data over time, simulating real-time data acquisition. Using real indoor DAS measurements, we demonstrate the effectiveness of our approach in deciphering complex room acoustics and accurately inferring sound source locations under both strategies. Our framework provides a novel solution for real-time indoor positioning and human activity surveillance, offering significant advantages over traditional camera-based systems by preserving individual privacy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a physics-inspired neural network for estimating the location of an acoustical source using the deformations of optical fibres as input. This is an innovative approach, and I have not seen similar approaches before. The physical basis is presented clearly and with appropriate detail. The text and grammar are mostly good, but variables, acronyms and figures are not thoroughly described. The balance between thorough physical modelling and brief experiments feels awkward.

### Strengths
- Contributions of the article are very clearly specified
- The connection between physics and neural networks in the application scenario is a strong contribution

### Weaknesses
Major issues:
First, the correspondence between the real-world location of fibre optic cables and the Halton distribution is weak at best. Second, we probably do not have the accurate location of a fibre optic cable. Yet both the distribution and accurate location of measurement points are required for accurate results. Thus, the correspondence between the experiment and real-world scenarios is weak. More realistic scenarios would have helped.
- This paper claims to be about using fibre optic cables as microphones, but it contains only experiments with piece-wise linear and random arrays. The only connection to fibre optics is the underlying physics model. Experiments closer to fibre optics scenarios would help a lot.
- The balance of the paper is skewed since the physics side is strong, but experiments are brief.

Minor issues:
- All text, and especially equations in Figure 2, are very small.
- Interpretation of symbols in Fig 3-4 are not explained.

### Questions
All my questions have been resolved in the revision.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a source localization method based on distributed acoustic sensing using optical fibers. They propose to use physicals-informed neural networks with a loss function that is based on the sound wave propagation and the boundary conditions. Two strategies for real-time localization are presented, using all the data at once or in an incremental manner. 
Simulation results demonstrate the capabilities of the proposed method.

### Strengths
The paper deals with the emerging field of distributed acoustic sensing through optical fibers, and its use for source localization. Harnessing physics-based deep models is a promising approach. The simulations in 2D and 3D highlight the potential of the proposed method for solving the source localization problem.

### Weaknesses
Overall, the innovation of the paper is more application specific and less in terms of developing a new ML method (which can be specific or general). The use of PINN for sound field reconstruction was already proposed in Olivieri et al. (2024). They state that the main difference is that here they add impedance boundary conditions, which seems like a small addition in terms of innovation, as far as I understand. 
The paper only contains results on simulated data, while the abstract claims: “Using real indoor DAS measurements, we demonstrate the effectiveness of our approach”, and in the intro: “We demonstrate the simultaneous localization of sound sources and recovery of the spatiotemporal acoustic field using *real* DAS measurements”. Additionally, it is unclear why they describe fiber placement (shown in Fig 1.), while they did not apply their method on this data. 
In addition, the results contain no comparison to baselines and no quantitative results.

### Questions
Several questions related to the weaknesses mentioned above:
1.	Is the key contribution of the paper in terms of methodology or the specific application?
2.	How do they deal with the challenges mentioned in the intro (lines 57-64)?
3.	Why aren't there any real-world experiments as stated at the beginning of the paper?
4.	Consider adding comparisons to baselines. 
5.	Consider adding quantitative results in terms of localization error. 
Additional minor questions: 
1.	How are the weights in Eq. (7) chosen?
2.	How does impedance and boundary conditions are determined?
3.	Are Halton and Volume configurations realistic as they require fibers covering the entire space?
4.     Fig. 3  - in the caption, what is the meaning of the acronym FEM?
5.     Fig. 4.  - in the caption, what is presented in the left plot in each subplot?
6.     Figs. 4 and and 7, why are there several final locations?
7.	Consider adding an ablation study comparing to optimization without boundary conditions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper suggests a method for sound source localization using measurements taken from deployed optic fibers inside building structures. The method is based on a physics-informed neural network that is quite small and simple, and does not require labeled data. Thus it has the potential to be used extensively. The authors provide the architecture of the network, but not very clearly. In addition, the method is only studied in computer simulations (not real measurements) and the experiments are limited to a single stationary source.

### Strengths
* Efficiency - suggesting a method for sound source localization by using already deployed optic fibers
* Simplicity - suggesting a method for sound source localization that does not require a lot of labeled data

### Weaknesses
 * All experiments are based on a single static source, but moving target(s) is very common. It is not clear if this method is applicable to multi-source or moving sources. While showing results just for a single static source is OK, I would expect some explanation whether the method can be used for multi-source or to moving sources. The lack of experiments with moving sources significantly limits the practical applicability of the proposed method. The authors should at least discuss the theoretical limitations of the approach when dealing with dynamic sound sources, and how the assumption of a static source influences the network's ability to learn the underlying physics.
* The clarity of PINN architecture could be improved - while it is presented in Figure 2, I suggest explaining the inputs, outputs, and learned parameters explicitly.
  * Currently I find it difficult to understand how (x,y,z) is used as an input if we do not know the source position.. Are these initialized randomly according to some Gaussian distribution? Please make it clearer. The explanation of how the spatial coordinates are handled within the PINN is insufficient. It is unclear whether these coordinates represent a fixed grid, randomly sampled locations, or something else entirely. The lack of clarity makes it difficult to assess the validity of the approach.
  * In equation (11) we minimize over x_0, but this parameter is not clearly defined in the loss function, instead we have x_pde, x_bc, x_ic, x_data - what is the relation between these parameters? The loss function is not clearly defined, and the relationship between the different terms is ambiguous. The authors should provide a more detailed explanation of how each term contributes to the overall loss and how the optimization process is carried out.
* The presentation of both setup and results of the synthetic tests (section 4) could be improved. The description of the synthetic experiments lacks detail, making it difficult to reproduce the results. The authors should provide more information about the simulation parameters, the geometry of the simulated environment, and the characteristics of the simulated sound source.
* Conclusions from experiments
  * Lacking a clearly defined evaluation criteria (source localization error). The absence of a clear metric for evaluating the source localization performance makes it difficult to compare the proposed method with existing techniques. The authors should define a specific metric, such as the Euclidean distance between the estimated and true source locations, and report the results using this metric.
  * Authors mention the importance of optimal design of DAS array - (a) they did not address optimal source placement, (b) is controlling the placement really possible? Isn’t this given by the structure of the optical fiber array (which is placed according to other constraints)? The discussion of optimal array design is superficial. The authors should provide a more in-depth analysis of how the array geometry affects the localization accuracy and discuss the practical constraints of controlling the fiber placement.
  * It is mentioned that training strategy 1 significantly outperforms strategy 2 but this is not clear from Figure 4. Performance looks very similar. Why did the authors conclude otherwise? Please explain. In addition, if there is such a difference, why is this the case? Can we use this insight to understand when is better to use strategy 1 over 2? The comparison between the two training strategies is not convincing. The authors should provide a more detailed analysis of the performance of each strategy and explain the reasons for the observed differences. The claim that strategy 1 outperforms strategy 2 is not supported by the presented results.
  * Section 4.2 is not presented clearly. In addition, there are many conclusions with no results shown
    * Line 355 - “Strategy 2 converges with the correct 2D source location…” - can you please provide numerical errors? The claim that strategy 2 converges to the correct source location is not supported by quantitative results. The authors should provide numerical errors to validate this claim.
    * Lines 357-359 - where do we see the performance of each strategy? The performance of each strategy is not clearly presented. The authors should provide a more detailed analysis of the results and explain how the performance of each strategy was evaluated.
* While the paper claims it deployed an impressive fiber network (figure 1) - this is not used anywhere in the experiments. All experiments are based on computer simulations of optic fibers behavior. The lack of real-world data in the experiments significantly limits the practical relevance of the proposed method. The authors should validate their approach using real-world measurements to demonstrate its effectiveness in realistic scenarios.

**Minor comments**
* Line 47 - BC and IC abbreviations are not defined (boundary and initial conditions?)
* Line 50 - XPINNs and FBPINNs are defined only later
* Line 199 - p_{data} is defined before equation (10), this is somewhat confusing. Is this the pressure term at the last line of equation (7)?i.e., “...+2p(x,t)E||22”?
* Figure 2 - the two plots below the loss equations are two small and unclear. If they provide some clarity, please incorporate them in a clearer way
* I would suggest to present equation (8) before equation (7) - I think it clearer to understand the strain rate along the axial direction of the fiber before this is used in the los function of the network
* Figure 3
  * Mention what is the the red Gaussian-like distribution (source location)
  * The right-hand side of both plots (a) and (b) are not defined - what do we see there?
* Figure 4 - please describe what we see in the plots, i.e., what are the green boxed, red star, and the difference between the right- and left- hand side plots
* Figure 5 - the colors are very bright and it is difficult to understand the visualization of sound propagation. In addition, the pressure colorbar is missing units.
* Lines 270-271 - I think that you have mistakenly mixed between the two strategy indices, i.e., it should be “the Incremental Time-Stepping Training Strategy (Strategy 2) significantly outperforms the Simultaneous Training with All Data Strategy (Strategy 1) in achieving stable localization”

### Questions
* What are the trade-offs in performance between strategy-1 and strategy-2 training?
* How is training performed when there is a moving source? How fast can the network learn and produce the correct source positions? What about multiple sources? 
* I left additional questions regarding the experiments under “weaknesses” section

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces the combination of distributed acoustic sensing (DAS) and physics-informed neural networks (PINNs). In DAS, observation stations are installed along standard optical fibers. These observation stations capture the anomalous propagation of light along the fibers. The anomaly source can both be internal (e.g., imperfections in the manufacturing process) and external (e.g., acoustic vibrations from the environment) and causes (undesired) backscattering of light. The authors use this deviation from normal light flow for localization of an unknown sound source. They use PINNs and integrate the acoustic wave equation alongside initial and boundary conditions. In model training, the network only uses acoustic pressure over time as input data, no ground-truth location is required. The authors test the combination of DAS+PINNs on synthetic data captured in 2D and 3D space. Qualitative results indicate the feasibility of their approach.

### Strengths
Combination of DAS and PINNs well motivated.

Two strategies of localization (incremental and full-data localization) seem very sensible.

In training for sound source localization, the proposed method does not require labels, possibly making it more widely applicable.

### Weaknesses
Weaknesses:
In my view, the paper has several weaknesses.

First, the paper only uses qualitative evaluation: Judging from the visualizations only (e.g., Fig4c), I cannot appropriately judge how well the approach works. There seems to be multiple possible sound sources identified by the algorithm, so speaking of "stable localization" or "accurately infer[ring] the sound location" seems unwarranted. Similarly, without a comparison to other methods, I cannot judge the performance of the DAS+PINN approach. To alleviate this, I suggest: 1) report MSE between predicted and actual sound source place, and 2) evaluate baseline methods: beamforming, MLP without the PINN part, and if possible also other ML approaches (see e.g. this paper: "Grumiaux et al: A SURVEY OF SOUND SOURCE LOCALIZATION WITH DEEP LEARNING METHODS")

Second, the presentation is lacking: there seems to be a missing paragraph after line 182, the description of the figures are too short, details about the training setup are missing, and mathematical symbols (lines 183ff) are not introduced properly (e.g., N_bc, N_ic, N_pde, x_pde). To alleviate this, I suggest: 1) add standalone figure descriptions on how to interpret them, 2) properly introduce mathematical symbols, 3) explain the network architecture of the PINN in writing, and 4) add a section on the training setup. Please also see my questions and suggestions for improvements further below.

Third, regarding the data, the connection between setting up the fiber cables (section 2, lines 124ff) and the synthetic tests (section 4) is unclear: are the test-spaces part of the overall installment? Or specifically installed? This example is only one of the unclearities that I have after reading the paper, please see my questions below. To alleviate this, I suggest: 1) a clarification on how the installment of the fiber cables relate to the synthetic tests, and 2) describing if the evaluated scenarios are synthetic, real, or idealized ones.

Fourth, the paper does not have paragraphs that I consider essential for (understanding) the paper: no treatment of the background of PINNs, a very short section on related work only, and no ethics statement (this is probably most critical, as the paper repeatedly stresses surveillance without compromising privacy. Alleviate this by: 1) adding a section on PINNs, 2) expanding the related work (on PINNs, but even more so on DAS), and 3) adding an ethics statement.

Fifth, the reference section of the paper includes only 13 references, which do not include other works on DAS (e.g., [1,2,3] found via a quick Google Scholar Search) and PINNs (e.g., [4,5,6]). I suggest you include these references, or others of your choice (this naturally will happen if my previous point is addressed).

Finally, it fails to convince me of the novelty: it appears to describe a trivial combination of DAS and PINNs, and also lacks ablation studies to asses the combinations effects. To alleviate this weakness, I suggest: 1) add a background on DAS, 2) add a background on PINNS, 3) describe the challenges (you had) in combining DAS and PINNs, and 4) discuss how the combination is superior in some way in applications.

### Questions
Questions:

In my understanding, one needs to place devices along the fiber cables to record the (anomalous) signals. Is that correct? This would probably be a disadvantage, as existing fiber layouts would need to be prepared beforehand and cannot be used as-is.

What are the "1250 distinct monitoring channels" (line 132f)? Are these the total installed recording stations?

Where can I see the channel distribution in Figure 1 (c.f. line 136)? Is each straight red line a channel?

What are the green squares in Fig4?

What is the "image source model" in line 95?

In your work, you repeatedly mention that DAS(+PINN) can be used for surveillance without compromising privacy. How does that work? If we know person X is in a room, we can locate and survey X with the proposed method? How does that relate to maintaining privacy?

Though the qualitative evaluation provided in the paper suggest that the method works, I am not sure how close to the real-world the test-cases are. Only test small rooms (up to 1m x 1m x 1m) are used the Halton-placement seems impractical: the room would then be clogged by fibers and not usable by, e.g., humans.

Figure 1: What is the "interrogator" marked in the figure and how does it relate to the paper?

Suggestions for improvement:

1. General suggestions

Adding a section on the background of PINNS would greatly improve the structure of the paper. Likewise, by expanding the related work on DAS, the paper would be better to comprehend.

Further, I would greatly appreciate a much expanded section on the training setup (epochs, optimizer, batch size, learning rate etc.). In similar spirit, explaining your data and its shape in more detail would improve my understanding of the setup.

For your figures, you could expand the description so they are comprehensible without having read the paper.

2. Specific suggestions
- lines 40ff: add further references to PINNs
- lines 43ff: consider adding more references to the application of PINNS or physical equations into machine learning in general, e.g. [7], [8]
- line 47: BCs and ICs used but not introduced beforehand --> consider introducing the abbreviation beforehand
- lines 48ff: consider adding references for the statement "Even when the loss function is minimized, the BCs and ICs are not strictly satisfied"
- line 49: consider a better transition between the two sentences; for me they do not seem to be related
- lines 57ff (challenges of PINNs): they do not seem to be related to the contributions (lines 75ff)
- lines 178ff: consider using a specific symbol for the neural network instead of the abbreviation NN.
- line 185: consider making the ordering of the equation parts consistent with the ordering of lines 167ff
- lines 270ff: Strategy 1 and Strategy 2 are mixed-up?
- lines 231ff: t_k versus just k in the exponent of the loss
- line 287 (and other places): abbreviation of FEM (for finite elements?) used without prior introduction --> consider introducing the abbreviation beforehand
- line 265: consider adding a short explanation about why the Halton-layout should be used (versus real random placement)
- Figure 2: Consider indicating the direction of data/information flow along the blue lines
- Figure 5: improve readability
- Figures 6, 7: consider improving the placement of the figures, possibly by shrinking Figure 7

Prior work on DAS:

[1]: Cedilnik, Gregor, et al. "Ultra-long reach fiber distributed acoustic sensing for power cable monitoring." Proceedings of the JICABLE. Vol. 19. 2019.

[2]: Jousset, Philippe, et al. "Fibre optic distributed acoustic sensing of volcanic events." Nature communications 13.1 (2022): 1753.

[3]: Lior, Itzhak, et al. "On the detection capabilities of underwater distributed acoustic sensing." Journal of Geophysical Research: Solid Earth 126.3 (2021): e2020JB020925.

Other works on PINNs:

[4]: Krishnapriyan, Aditi, et al. "Characterizing possible failure modes in physics-informed neural networks." Advances in neural information processing systems 34 (2021): 26548-26560.

[5]: Cuomo, Salvatore, et al. "Scientific machine learning through physics–informed neural networks: Where we are and what’s next." Journal of Scientific Computing 92.3 (2022): 88.

[6]: Raissi, M., Perdikaris, P., Karniadakis, G.E.: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. J. Comput. Phys. 378, 686–707 (2019)

Suggested references for the introduction (lines 43ff)

[7]: Salvatore Cuomo, Vincenzo Schiano Di Cola, Fabio Giampaolo, Gianluigi Rozza, Maziar Raissi, and Francesco Piccialli. Scientific machine learning through physics–informed neural networks: Where we are and what’s next. Journal of Scientific Computing, 92(3):88, 2022.

[8]: Yogesh Verma, Markus Heinonen, Vikas Garg. ClimODE: Climate and Weather Forecasting with Physics-informed Neural ODEs. ICLR 2024. 2024

### Soundness
2

### Presentation
2

### Contribution
1
