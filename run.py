import cv2
import numpy as np
from table import TableRepositories 
TableRepo = TableRepositories('Capture.PNG') 
print(TableRepo.response)
cv2.imwrite ('slate.png', TableRepo.slate)
cv2.imwrite ('mask.png', TableRepo.mask)
cv2.imwrite ('filtered.png', TableRepo.filtered)
kernal = np.ones((2,3),np.uint8)
chg =cv2.morphologyEx(TableRepo.mask,cv2.MORPH_GRADIENT,kernal)
cv2.imshow ("Hii",chg)
cv2.waitKey()
cv2.destroyAllWindows()
