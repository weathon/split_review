## Human Reviewer 1

### Questions
The paper seems to revolve largely around supervised learning only and moreso classification. How do the arguments hold up when going to different supervised learning tasks?

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Questions
- L201L: what does "addition of an Oracle PCA projection (in blue)" mean? Is the 10% increment supposed to be the contribution from indistinguishable features? It is a bit hard for me to follow Figure 2 left and the procedure to generate it. I understand the high level concept that PCA projections on highly discriminating dimensions is supposed to give you higher performance. But not hundred percent sure what that text is saying.
- I am not sure I understand the epistemic uncertainty part completely. Considering the infinite ID data case, the epistemic uncertainty only goes to zero for ID samples. OOD samples may still be unlikely for the distribution learned, resulting in high epistemic uncertainty of the model over those samples. So if I am misunderstanding this: "If measuring epistemic uncertainty were the correct approach to OOD detection, then such low epistemic uncertainty implies that OOD points do not exist in this setting. Therefore, because perfectly capturing epistemic uncertainty is not enough to solve OOD detection, they must answer fundamentally different questions", please explain this more simply. Would also like to see details of the experiment done perhaps in the appendix. The cited reference is a book, maybe a simpler explanation would help the reader.
- Would maybe recommend moving the real generative model experiments to the main text and the 1D example case to the appendix?

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Questions
None at the moment.

### Rating
4

### Confidence
5

---

## Human Reviewer 4

### Questions
None.

### Rating
1

### Confidence
4