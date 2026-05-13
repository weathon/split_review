# Radial Basis Operator Networks

- Decision: Reject
- Scores: 3, 5, 3, 3, 5

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper deals with operator networks working with radial basis functions.
Time and frequency domain are studied.
A couple of experiments are carried out, mainly on PDEs and TSP.

### Strengths
The paper is well written and the topic is interesting though not mainstream.
The experiments are relevant.

### Weaknesses
The methodological description of the method is too short and not detailed enough, especially for unfamiliar readers.
Some theoretical statements are made but the rest of the methodology would not allow re-implmenting the method. Figs 1 and 2 do not carry any information whatsoever; most equations about the network are implicitly embedded in the theorem.
Part of the problem is that the paper describes a variant of NO/ON and the authors focus on the increment, probably for the sake of space, at the expense of making the paper difficult to read for the average reader.
With the amount of provided details, the proposed method seems to be very simple and very close to classical RBFNs with a product on top. The PDE and TSP tasks are not very convincing if they are not compared to other architecture and methods (X-RBON get compared to LNO only).

### Questions
Can you please reinforce the methodological part and make more self-contained and more detailed.
Can you extend the comparisons (if you think it makes sense)?

### Soundness
3

### Presentation
1

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
Paper proposes a radial basis operator network, an operator network entirely represented with radial basis functions. The RBON can learn in both time and frequency domain. Experiments include comparison with Laplace neural operator on wave, burgers, and Euler-bernoulli beam equations. Paper shows RBON and NRBON forecasting global and local temperatures based on atmospheric CO2.

### Strengths
Paper proposes a new operator network based on radial basis functions. Paper is clearly written. The quantitative results of RBON, NRBON, and F-RBON outperform LNO on the wave, burgers, and Euler-bernoulli beam equations.

### Weaknesses
small set of experiments. CO2 to temperature experiment lacks baseline. other factors than CO2 affect temperature, and overall there's a lot of fluctuation in temperature, so it is hard to tell how good predictions are from the RBONs. another dataset with experiments may be helpful.

### Questions
perhaps authors can include the LNO results on CO2 to temperature experiment? 

What is difference between RBON and NRBON? can authors clarify key architectural or mathematical differences between RBON and NRBON, and how these differences impact performance

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
4

### Summary
This paper presents an extension of DeepONet, where the DNN is replaced with a radial basis neural network, and demonstrates the performance of the extension  through solving some partial differential equations.

### Strengths
Replacing the DNN in DeepONet with the radial basis neural network sounds an interesting idea, leading to improved numerical results.

### Weaknesses
1. The presentation is unclear, making it challenging for readers unfamiliar with DeepONet to follow. For example, it lacks a clear outline (or pseudo) of the training algorithm for the proposed network. What are the training parameters? How should  M and N be selected?

2. Figure 1: what does `x'` represent?  Does the linear transformation L include tunable parameters?

3. In Section 2.3, the authors mentioned computation in the frequency domain, but the algorithm is not detailed. The description lacks specifics on how the frequency domain data is obtained, and how the radial basis functions are adapted for complex-valued inputs. The k-means algorithm, which is typically used with real-valued data, requires further explanation in the context of complex numbers.

4. The comparison with DeepONet is not included in the paper.

5. Theoretical contribution of the paper is marginal.

### Questions
See weakness.

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
2

### Summary
They introduce the Radial Basis Operator Network (RBON) to learn an operator in both the time and frequency domains, with adjustments to handle complex-valued inputs. Experiments on both in-distribution and out-of-distribution (OOD) data are conducted to validate RBON’s effectiveness.

### Strengths
They introduce the Radial Basis Operator Network (RBON) to learn an operator in both the time and frequency domains, with adjustments to handle complex-valued inputs. Experiments on both in-distribution and out-of-distribution (OOD) data are conducted to validate RBON’s effectiveness.

### Weaknesses
1. The experimental comparisons are insufficient, especially lacking comparisons with methods like DeepONet and FNO.
2. Using KNN to select centers may introduce instabilities.
3. The explanation of the experimental results is inadequate; for instance, Table 1 lacks clarity on why different algorithms perform variably across different problems.

### Questions
1. Could you elaborate on the literature review regarding learning operators in either the time domain or frequency domain?
2. What are the advantages of learning an operator simultaneously in both the time and frequency domains, as opposed to learning them separately and then combining the results?
3. Could you provide more details on the network structure?
4. How many centers are chosen using KNN, and what criteria are used for selection?
5. How do you explain the results in Table 1, where different networks show instability on different examples? LNO works better on Burgers?
6. Why some networks work better on OOD data in table 1?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a Radial basis operator network for mapping infinite dimensional spaces like function spaces. This approach can model temporal as well as frequency information. The introduction gives a good motivation for the problem, the literature is vast, and the methods are explained well. The paper shows the efficacy of the proposed approach on a weather dataset.

### Strengths
The paper is written.
Theory enhances the paper.

### Weaknesses
The experiments and comparisons are a bit small and need to be extended to understand the efficacy of RBON.



### Questions
•	Weather data is simple. Can more complex data be added to the comparison as well? There are many time series benchmark data sets (https://arxiv.org/pdf/2303.06053). 
•       More comparison needs to be added. Like LNO, FNO, LSTM, etc. This will give a holistic view wrt performance.
•	Any insights on why the model did not perform as well as global in the local prediction? Is it because of short-term fluctuations or long-term trends?
•	Figures 5 and 6 are too compact and don’t add much information. Can be added to the appendix. A zoomed-in version of the plot would be helpful.
•	A sensitivity study for k means for deciding centers for RBFs would be useful. Showing the effect of varying values of k on model performance will give many insights.

### Soundness
3

### Presentation
2

### Contribution
2
