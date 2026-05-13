# Unsupervised Detection of Recurrent Patterns in Neural Recordings with Constrained Filters

- Decision: Reject
- Scores: 5, 8, 6

## Abstract
Structured spontaneous neural activity, characterized by the expression of repetitive patterns, is crucial for memory, learning and spatial navigation. However, investigating the functional role of these patterns has been challenging due to a lack of scalable methods for detecting them in large-scale recordings. To address this challenge, we propose an unsupervised approach that utilizes backpropagation to optimize the parameters of a predefined number of spatiotemporal filters, which serve as pattern detectors. We demonstrate the scalability and efficiency of our approach for detecting place cell sequences in biologically plausible synthetic and real datasets obtained from the mouse hippocampus. Our speed benchmarks demonstrate that our method significantly outperforms prior art, enabling the study of spontaneous activity in larger recordings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an unsupervised method for identifying sequences in neural spiking data.   The method learns a set of K filters that summarize the spiking data subject to what seem like some pretty minimal constraints.  The method is applied to ground truth data and recordings from rodent hippocampus.  The method is faster and perhaps more reliable than other competing methods.

### Strengths
Right now, the priors that working neuroscientists bring to analyzing their data has a huge effect on the results they are able to discover.  It would be really very useful to have an unsupervised method to automatically extract sequential information from spiking neurons.  Not only would it be outstanding for analyzing data from freely moving animals (as in Fig 7)  but also would be really impactful for understanding population burst events, theta sequences, etc etc.

Such tools will become increasingly important as recording techniques continue to advance.

### Weaknesses
I am concerned about priors that may be ``baked in'' to the method (perhaps inadvertently).  At mimimum these priors should be made more explicit.  In particular, I'm concerned that the model seems to find ``straighter'' sequences than are present in the data (Fig 7).  The ground truth experiments all use linear sequences, exacerbating this concern.

It's not obvious that the method can generalize to sequences (such as PBEs, theta etc) that unfold over more than 1 continuous dimension.

I remain concerned that there is a scale built in to the method.  Choosing the width M may impose a choice of the experimenter on the results that are not present in the data. Hippocampal neurons (and neurons in other parts of the brain) appear to show reliable sequential firing over many different time scales.  For instance, the ``sequence'' of time cells triggered by an event slows continuously and may extend out to minutes. The time between the peak of time cell n and the peak of time cell n+1 changes systematically with the location in the sequence. If Cao et al., (2022, eLife) are to be believed, the time between cells in the sequence goes up linearly with n.   If the sensitivity of the method depends on the choice M, then any specific window size means that the method would be blind to parts of the sequence slower than that (and perhaps has different resolution for parts of the sequence that are much faster).

### Questions
If ground truth includes sequences that unfold at varying rates can this method identify them?  For instance, suppose that there are place fields along a linear track but they are overrepresented near the ends.   The animal runs at a constant velocity. Now the sequence, rather than appearing as a straight line in, say, Fig 3b, would appear as a hook.  Can this method find those sequences as well?  I think this is a very important question as it seems that these kinds of sequences are very general.  Is there a way to make the filters more or less sensitive to these kinds of sequences?

Suppose we had a set of place cells that tile a 2-D enclosure.  Would this method work?  I'm concerned that the filters will have to cover a 2-D surface with piecewise 1-D filters and this will fail really badly.  

Take the situation in Fig. 7.  Suppose the animal starts out on the linear track at a constant velocity, stops half way through, backtracks for 10 cm, then turns around and continues along its original trajectory to the end.  What filters does this method find?  What should it identify?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a way to find repeating spike patterns in multi-channel neural data. The method uses a novel loss function to learn multiple kernels that respond strongly to different recurring patterns. It is tested and found to perform well on several synthetic datasets as well as a dataset of mouse place-cell responses for which the ground truth is known via the mouse’s position on a track. The method is shown to run more quickly than related past methods.

### Strengths
The paper addresses a substantial issue in analysis of large neural data. It seems to work well and efficiently. The method and the results are clearly presented. 

The loss function seems elegant and well designed, and its explanation is clear. I didn’t find the loss obvious at first but rather felt that reading this section broadened my mind a little.

### Weaknesses
I take it the point of unsupervised detection of neural patterns is to find them even when ground truth isn’t known. However, the method wasn’t applied to such data. Such an application couldn’t be used to test the accuracy of the method, but it would help to illustrate qualitatively what can be expected from it in a realistic scenario, and it might provide an example of downstream use of the results.

Line 74: Can “repeating” be defined more clearly? What kinds of variations aside from independent jitter are expected biologically, if any?

What are the spike rates of the background activity?

Figure 3E: Why does it appear that the network learns nothing for 150 epochs and then suddenly converges? This seems inconsistent with the choice of 100 steps in section 4.4, particularly the claim of faster convergence in lines 195-197.

Figure 7: Could the red traces be overlaid on panels C and D as well? Also it appears that the slopes in these panels are smaller than the speed of the mouse. Is that expected? Why? The detections are clear in any case, which is the main point.

Line 204: Is there really a 2D convolution operation? In the neuron dimension maybe you have a non-padded convolution with kernel size equal to input size, but I don’t think it’s standard to call that 2D.

Appendix B.4 & B.5: The comparison with PP-Seq is hard to interpret because both the true and false positive rates of PP-Seq are higher. Can you change a threshold to match one of these measures and compare the other?

The dropout probabilities range from 0.2 to 0.4, and I was not sure how to relate that to spike statistics (e.g. Poisson or otherwise). Can this be clarified?

Figure B.9: The sorted spike sequences look tighter here than in Figure 3. Are they? Why? Does it matter?

Figure B.12: This looks qualitatively quite different than Figure 7 and perhaps more should be said about this in the main text.

The learned kernels seem to include all the neurons, whether or not they participate in the sequence. Is it desirable to ignore non-participating neurons? Figure B.16 seems to suggest one way to do this, i.e. by checking for a Gaussian-like kernel. Are there better ways?

### Questions
Line 74: Can “repeating” be defined more clearly? What kinds of variations aside from independent jitter are expected biologically, if any? 

What are the spike rates of the background activity? 

Figure 3E: Why does it appear that the network learns nothing for 150 epochs and then suddenly converges? This seems inconsistent with the choice of 100 steps in section 4.4, particularly the claim of faster convergence in lines 195-197. 

Figure 7: Could the red traces be overlaid on panels C and D as well? Also it appears that the slopes in these panels are smaller than the speed of the mouse. Is that expected? Why? The detections are clear in any case, which is the main point. 

Line 204: Is there really a 2D convolution operation? In the neuron dimension maybe you have a non-padded convolution with kernel size equal to input size, but I don’t think it’s standard to call that 2D. 

Appendix B.4 & B.5: The comparison with PP-Seq is hard to interpret because both the true and false positive rates of PP-Seq are higher. Can you change a threshold to match one of these measures and compare the other? 

The dropout probabilities range from 0.2 to 0.4, and I was not sure how to relate that to spike statistics (e.g. Poisson or otherwise). Can this be clarified? 

Figure B.9: The sorted spike sequences look tighter here than in Figure 3. Are they? Why? Does it matter? 

Figure B.12: This looks qualitatively quite different than Figure 7 and perhaps more should be said about this in the main text. 

The learned kernels seem to include all the neurons, whether or not they participate in the sequence. Is it desirable to ignore non-participating neurons? Figure B.16 seems to suggest one way to do this, i.e. by checking for a Gaussian-like kernel. Are there better ways?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a convolution dictionary learning method designed for neural data. They also propose a way to assess the statistical significance of their pattern detection and demonstrate speedup compared to other methods.

### Strengths
The paper is clearly written and there is an appreciable progression from experiments on synthetic data to real data. Moreover, the authors present a method to assess the statistical significance of their convolutional pattern detection.

Figures 3.D and 3.E are reassuring in that they seem to show that maximizing the variance in the objective eq.1 (which was motivated intuitively) does indeed correlate with pattern detection. 

Finally, beyond the interpretability of their method, the authors exhibit a speedup compared to other methods.

### Weaknesses
I am surprised in Figure 8 that there are few standard convolutional dictionary learning methods to compare against, given that convolutional dictionary learning is a field with a rich literature. Could the authors explain how their method differs from other convolutional dictionary learning methods used for neural data, e.g. [1]?



### Questions
Can the authors specify in the main text the data modality used in section 4.3.: are these measurements from cell calcium imaging? 

Can the authors explain the main argument for the speed of their method compared to other methods in Figure 8?

What is f, on line 113?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
