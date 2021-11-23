import Algorithms as A
import matplotlib.pyplot as plt
import numpy as np
import Calc as c

for a in range(50, 1001, 50):
    for b in range(0, 2):
        for c in range(2, 20):
            for d in range(0, 2):
                for e in range(500, 10001, 500):
                    for f in range(0,30,2):
                        A.ga(population_size=a,
                             select=b,
                             div1=c,
                             div2=48 - c,
                             cross=d,
                             iterations=e,
                             file_to_read="dane48.csv",
                             mutations=f)

# dm=np.genfromtxt("dane127.csv", delimiter=",")
# for i in range(0,127):
#     r1 = A.knn(i, "dane127.csv")
#     r1 = [x+1 for x in r1]
#     wynik = c.sequence(r1, dm)
#     save2 = "nn_start127_"+str(i+1)+"_wynik_"+str(wynik)+".csv"
#     np.savetxt(save2,r1, delimiter=",")
#     #save = "map"+str(i+1)+"_"+str(int(wynik))+".jpeg"
#     #c.viz(r1, "points76.csv", save, False)

################################################################
######################IHC
# r1=A.ihc(10,10000,99999,4,"dane48.csv")
# r2=A.ihc(50,10000,99999,4,"dane48.csv")
# r3=A.ihc(100,10000,99999,4,"dane48.csv")
# r4=A.ihc(500,10000,99999,4,"dane48.csv")
# r5=A.ihc(1000,10000,99999,4,"dane48.csv")
# r6=A.ihc(2000,10000,99999,4,"dane48.csv")
# r7=A.ihc(5000,10000,99999,4,"dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "10")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "50")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "100")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "500")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "1000")
# plt.plot(np.linspace(1,len(r6),len(r6)), r6, label = "2000")
# plt.plot(np.linspace(1,len(r7),len(r7)), r7, label = "5000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Multistart")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("IHCITER48.jpeg")
# plt.clf()
#
# r1=A.ihc(500,1000,99999,4,"dane48.csv")
# r2=A.ihc(500,5000,99999,4,"dane48.csv")
# r3=A.ihc(500,10000,99999,4,"dane48.csv")
# r4=A.ihc(500,50000,99999,4,"dane48.csv")
# r5=A.ihc(500,100000,99999,4,"dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "50000")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "100000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Inside iter")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("IHCINSITER48.jpeg")
# plt.clf()
#
# r1=A.ihc(500,10000,99999,1,"dane48.csv")
# r2=A.ihc(500,10000,99999,2,"dane48.csv")
# r3=A.ihc(500,10000,99999,3,"dane48.csv")
# r4=A.ihc(500,10000,99999,4,"dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Neigh")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("IHCNeigh48.jpeg")
# plt.clf()
#
# r1=A.ihc(500,10000,500,4,"dane48.csv")
# r2=A.ihc(500,10000,1000,4,"dane48.csv")
# r3=A.ihc(500,10000,2000,4,"dane48.csv")
# r4=A.ihc(500,10000,3000,4,"dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC No change")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("IHCNOCHENGE48.jpeg")
# plt.clf()
#
# r1=A.ihc(10,10000,99999,4,"dane76.csv")
# r2=A.ihc(50,10000,99999,4,"dane76.csv")
# r3=A.ihc(100,10000,99999,4,"dane76.csv")
# r4=A.ihc(500,10000,99999,4,"dane76.csv")
# r5=A.ihc(1000,10000,99999,4,"dane76.csv")
# r6=A.ihc(2000,10000,99999,4,"dane76.csv")
# r7=A.ihc(5000,10000,99999,4,"dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "10")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "50")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "100")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "500")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "1000")
# plt.plot(np.linspace(1,len(r6),len(r6)), r6, label = "2000")
# plt.plot(np.linspace(1,len(r7),len(r7)), r7, label = "5000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Multistart")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCITER76.jpeg")
# plt.clf()
#
# r1=A.ihc(500,1000,99999,4,"dane76.csv")
# r2=A.ihc(500,5000,99999,4,"dane76.csv")
# r3=A.ihc(500,10000,99999,4,"dane76.csv")
# r4=A.ihc(500,50000,99999,4,"dane76.csv")
# r5=A.ihc(500,100000,99999,4,"dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "50000")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "100000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Inside iter")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCINSITER76.jpeg")
# plt.clf()
#
# r1=A.ihc(500,10000,99999,1,"dane76.csv")
# r2=A.ihc(500,10000,99999,2,"dane76.csv")
# r3=A.ihc(500,10000,99999,3,"dane76.csv")
# r4=A.ihc(500,10000,99999,4,"dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Neigh")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCNeigh76.jpeg")
# plt.clf()
#
# r1=A.ihc(500,10000,500,4,"dane76.csv")
# r2=A.ihc(500,10000,1000,4,"dane76.csv")
# r3=A.ihc(500,10000,2000,4,"dane76.csv")
# r4=A.ihc(500,10000,3000,4,"dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC No change")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCNOCHENGE76.jpeg")
# plt.clf()
#
# r1=A.ihc(10,10000,99999,4,"dane127.csv")
# r2=A.ihc(50,10000,99999,4,"dane127.csv")
# r3=A.ihc(100,10000,99999,4,"dane127.csv")
# r4=A.ihc(500,10000,99999,4,"dane127.csv")
# r5=A.ihc(1000,10000,99999,4,"dane127.csv")
# r6=A.ihc(2000,10000,99999,4,"dane127.csv")
# r7=A.ihc(5000,10000,99999,4,"dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "10")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "50")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "100")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "500")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "1000")
# plt.plot(np.linspace(1,len(r6),len(r6)), r6, label = "2000")
# plt.plot(np.linspace(1,len(r7),len(r7)), r7, label = "5000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Multistart")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCITER127.jpeg")
# plt.clf()
#
# r1=A.ihc(500,1000,99999,4,"dane127.csv")
# r2=A.ihc(500,5000,99999,4,"dane127.csv")
# r3=A.ihc(500,10000,99999,4,"dane127.csv")
# r4=A.ihc(500,50000,99999,4,"dane127.csv")
# r5=A.ihc(500,100000,99999,4,"dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "50000")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "100000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Inside iter")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCINSITER127.jpeg")
# plt.clf()
#
# r1=A.ihc(500,10000,99999,1,"dane127.csv")
# r2=A.ihc(500,10000,99999,2,"dane127.csv")
# r3=A.ihc(500,10000,99999,3,"dane127.csv")
# r4=A.ihc(500,10000,99999,4,"dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC Neigh")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCNeigh127.jpeg")
# plt.clf()
#
# r1=A.ihc(500,10000,500,4,"dane127.csv")
# r2=A.ihc(500,10000,1000,4,"dane127.csv")
# r3=A.ihc(500,10000,2000,4,"dane127.csv")
# r4=A.ihc(500,10000,3000,4,"dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("IHC No change")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("IHCNOCHENGE127.jpeg")
# plt.clf()
################################################################
###############################################################
##############TS
# r1=A.ts(50, 1000, "dane48.csv", "dane48_inside_1000_s_50_allow_T.csv", True)
# r2=A.ts(50, 5000, "dane48.csv", "dane48_inside_5000_s_50_allow_T.csv", True)
# r3=A.ts(50, 10000, "dane48.csv", "dane48_inside_10000_s_50_allow_T.csv", True)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Swaps")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("TSSWAPS48.jpeg")
# plt.clf()
#
# r1=A.ts(5, 500, "dane48.csv", "dane48_inside_500_s_5_allow_T.csv", True)
# r2=A.ts(10, 500, "dane48.csv", "dane48_inside_500_s_10_allow_T.csv", True)
# r3=A.ts(15, 500, "dane48.csv", "dane48_inside_500_s_15_allow_T.csv", True)
# r4=A.ts(25, 500, "dane48.csv", "dane48_inside_500_s_25_allow_T.csv", True)
# r5=A.ts(50, 500, "dane48.csv", "dane48_inside_500_s_50_allow_T.csv", True)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "5")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "10")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "15")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "25")
# plt.plot(np.linspace(1,len(r5),len(r5)),r5 , label = "50")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Tabu List Length")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("TSBLOCK48.jpeg")
# plt.clf()
#
#
# r1=A.ts(50, 5000, "dane48.csv", "dane48_inside_1000_s_50_allow_T.csv", True)
# r2=A.ts(50, 5000, "dane48.csv", "dane48_inside_5000_s_50_allow_T.csv", False)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "allow 0")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Disallow 0")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Allow zeros")
# plt.ylim(10000,15000)
# plt.legend()
# plt.savefig("TSa048.jpeg")
# plt.clf()
#
# r1=A.ts(50, 1000, "dane76.csv", "dane76_inside_1000_s_50_allow_T.csv", True)
# r2=A.ts(50, 5000, "dane76.csv", "dane76_inside_5000_s_50_allow_T.csv", True)
# r3=A.ts(50, 10000, "dane76.csv", "dane76_inside_10000_s_50_allow_T.csv", True)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Swaps")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("TSSWAPS76.jpeg")
# plt.clf()
#
# r1=A.ts(5, 500, "dane76.csv", "dane76_inside_500_s_5_allow_T.csv", True)
# r2=A.ts(10, 500, "dane76.csv", "dane76_inside_500_s_10_allow_T.csv", True)
# r3=A.ts(15, 500, "dane76.csv", "dane76_inside_500_s_15_allow_T.csv", True)
# r4=A.ts(25, 500, "dane76.csv", "dane76_inside_500_s_25_allow_T.csv", True)
# r5=A.ts(50, 500, "dane76.csv", "dane76_inside_500_s_50_allow_T.csv", True)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "5")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "10")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "15")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "25")
# plt.plot(np.linspace(1,len(r5),len(r5)),r5 , label = "50")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Tabu List Length")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("TSBLOCK76.jpeg")
# plt.clf()
#
#
# r1=A.ts(50, 5000, "dane76.csv", "dane76_inside_1000_s_50_allow_T.csv", True)
# r2=A.ts(50, 5000, "dane76.csv", "dane76_inside_5000_s_50_allow_T.csv", False)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "allow 0")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Disallow 0")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Allow zeros")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("TSa076.jpeg")
# plt.clf()
#
# r1=A.ts(50, 1000, "dane127.csv", "dane127_inside_1000_s_50_allow_T.csv", True)
# r2=A.ts(50, 5000, "dane127.csv", "dane127_inside_5000_s_50_allow_T.csv", True)
# r3=A.ts(50, 10000, "dane127.csv", "dane127_inside_10000_s_50_allow_T.csv", True)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Swaps")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("TSSWAPS127.jpeg")
# plt.clf()
#
# r1=A.ts(5, 500, "dane127.csv", "dane127_inside_500_s_5_allow_T.csv", True)
# r2=A.ts(10, 500, "dane127.csv", "dane127_inside_500_s_10_allow_T.csv", True)
# r3=A.ts(15, 500, "dane127.csv", "dane127_inside_500_s_15_allow_T.csv", True)
# r4=A.ts(25, 500, "dane127.csv", "dane127_inside_500_s_25_allow_T.csv", True)
# r5=A.ts(50, 500, "dane127.csv", "dane127_inside_500_s_50_allow_T.csv", True)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "5")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "10")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "15")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "25")
# plt.plot(np.linspace(1,len(r5),len(r5)),r5 , label = "50")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Tabu List Length")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("TSBLOCK127.jpeg")
# plt.clf()
#
#
# r1=A.ts(50, 5000, "dane127.csv", "dane127_inside_1000_s_50_allow_T.csv", True)
# r2=A.ts(50, 5000, "dane127.csv", "dane127_inside_5000_s_50_allow_T.csv", False)
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "allow 0")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Disallow 0")
# plt.xlabel("Swap")
# plt.ylabel("Distance")
# plt.title("TS Allow zeros")
# plt.ylim(90000,150000)
# plt.legend()
# plt.savefig("TSa0127.jpeg")
# plt.clf()


# for i in range(3,20):
#      A.ga(population_size=50,
#           select=1,
#           div1=i,
#           div2=48-i,
#           cross=0,
#           iterations=500,
#           file_to_read="dane48.csv",
#           mutations=0)

# for i in range(0,20):
#      A.ga(population_size=50,
#           select=0,
#           div1=23,
#           div2=28,
#           cross=0,
#           iterations=500,
#           file_to_read="dane48.csv",
#           mutations=i)

# a=100
# while a<2000:
#      A.ga(population_size=a,
#           select=1,
#           div1=23,
#           div2=28,
#           cross=0,
#           iterations=500,
#           file_to_read="dane48.csv",
#           mutations=2)
#      a+=100
#

# a=500
# while a<20000:
#      A.ga(population_size=500,
#           select=1,
#           div1=23,
#           div2=28,
#           cross=0,
#           iterations=a,
#           file_to_read="dane48.csv",
#           mutations=2)
#      a+=500
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=1000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=5000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=10000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
#
#
#
# A.ga(population_size=50,
#      select=1,
#      div1=8,
#      div2=40,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=12,
#      div2=36,
#      cross=1,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=10,
#      div2=20,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=30,
#      div2=40,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
#
# A.ga(population_size=50,
#      select=0,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=10,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=20,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=30,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=40,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=100,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=500,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=5)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=10)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=20)
#
#
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=500,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=1000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=5000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=10000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
#
#
#
# A.ga(population_size=50,
#      select=1,
#      div1=8,
#      div2=40,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=12,
#      div2=36,
#      cross=1,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=10,
#      div2=20,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=30,
#      div2=40,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
#
# A.ga(population_size=50,
#      select=0,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=10,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=20,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=30,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=40,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=100,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=500,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=5)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=10)
#
# A.ga(population_size=50,
#      select=1,
#      div1=16,
#      div2=32,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane48.csv",
#      mutations=20)

# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=500,
#      file_to_read="dane76.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=1000,
#      file_to_read="dane76.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=0)
#
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=5000,
#      file_to_read="dane76.csv",
#      mutations=0)
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=10000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
#
#
#
# A.ga(population_size=50,
#      select=1,
#      div1=13,
#      div2=63,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
# A.ga(population_size=50,
#      select=1,
#      div1=19,
#      div2=57,
#      cross=1,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
# A.ga(population_size=50,
#      select=1,
#      div1=15,
#      div2=30,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
# A.ga(population_size=50,
#      select=1,
#      div1=45,
#      div2=61,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
#
# A.ga(population_size=50,
#      select=0,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=10,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=20,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=30,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=40,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=100,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=500,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=3)
#
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=5)
#
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=10)
#
# A.ga(population_size=50,
#      select=1,
#      div1=25,
#      div2=51,
#      cross=0,
#      iterations=2000,
#      file_to_read="dane76.csv",
#      mutations=20)


###############################################################


# route=A.knn(4, "dane48.csv")
# c.viz(route, "points48.csv", True)


#############################################################
########################SA
# r1=A.sa(1,0.75,False,1000, 99999,4, "dane76.csv")
# r2=A.sa(1,0.75,False,5000, 99999,4, "dane76.csv")
# r3=A.sa(1,0.75,False,10000, 99999,4, "dane76.csv")
# r4=A.sa(1,0.75,False,50000, 99999,4, "dane76.csv")
# r5=A.sa(1,0.75,False,100000, 99999,4, "dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "50000")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "100000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Inside Iter")
# plt.ylim(90000,200000)
# plt.legend()
# plt.savefig("SAITER76.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 99999,1, "dane76.csv")
# r2=A.sa(1,0.75,False,10000, 99999,2, "dane76.csv")
# r3=A.sa(1,0.75,False,10000, 99999,3, "dane76.csv")
# r4=A.sa(1,0.75,False,10000, 99999,4, "dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Neigh")
# plt.ylim(90000,200000)
# plt.legend()
# plt.savefig("SANEIGH76.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 500,4, "dane76.csv")
# r2=A.sa(1,0.75,False,10000, 1000,4, "dane76.csv")
# r3=A.sa(1,0.75,False,10000, 2000,4, "dane76.csv")
# r4=A.sa(1,0.75,False,10000, 3000,4, "dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "500")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "100")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "2000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "3000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA No change")
# plt.ylim(90000,200000)
# plt.legend()
# plt.savefig("SANC76.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 999999,4, "dane76.csv")
# r2=A.sa(0.9,0.75,False,10000, 999999,4, "dane76.csv")
# r3=A.sa(0.8,0.75,False,10000, 999999,4, "dane76.csv")
# r4=A.sa(0.6,0.75,False,10000, 999999,4, "dane76.csv")
# r5=A.sa(1.5,0.75,False,10000, 99999,4, "dane76.csv")
# r6=A.sa(2,0.75,False,10000, 999999,4, "dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "0.9")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "0.8")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "0.6")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "1.5")
# plt.plot(np.linspace(1,len(r6),len(r6)), r6, label = "2")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Start temp")
# plt.ylim(90000,200000)
# plt.legend()
# plt.savefig("SASTARTT76.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 999999,4, "dane76.csv")
# r2=A.sa(1,0.9,False,10000, 999999,4, "dane76.csv")
# r3=A.sa(1,0.1,True,10000, 999999,4, "dane76.csv")
# r4=A.sa(1,0.2,True,10000, 999999,4, "dane76.csv")
# r5=A.sa(1,0.3,True,10000, 99999,4, "dane76.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "0.75")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "0.9")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "0.1g")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "0.2g")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "0.3g")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Temp reduction")
# plt.ylim(90000,200000)
# plt.legend()
# plt.savefig("SAREDT76.jpeg")
# plt.clf()
#
#
# r1=A.sa(1,0.75,False,1000, 99999,4, "dane127.csv")
# r2=A.sa(1,0.75,False,5000, 99999,4, "dane127.csv")
# r3=A.sa(1,0.75,False,10000, 99999,4, "dane127.csv")
# r4=A.sa(1,0.75,False,50000, 99999,4, "dane127.csv")
# r5=A.sa(1,0.75,False,100000, 99999,4, "dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "50000")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "100000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Inside Iter")
# plt.ylim(100000,200000)
# plt.legend()
# plt.savefig("SAITER127.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 99999,1, "dane127.csv")
# r2=A.sa(1,0.75,False,10000, 99999,2, "dane127.csv")
# r3=A.sa(1,0.75,False,10000, 99999,3, "dane127.csv")
# r4=A.sa(1,0.75,False,10000, 99999,4, "dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Neigh")
# plt.ylim(100000,200000)
# plt.legend()
# plt.savefig("SANEIGH127.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 500,4, "dane127.csv")
# r2=A.sa(1,0.75,False,10000, 1000,4, "dane127.csv")
# r3=A.sa(1,0.75,False,10000, 2000,4, "dane127.csv")
# r4=A.sa(1,0.75,False,10000, 3000,4, "dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "500")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "100")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "2000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "3000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA No change")
# plt.ylim(100000,200000)
# plt.legend()
# plt.savefig("SANC127.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 999999,4, "dane127.csv")
# r2=A.sa(0.9,0.75,False,10000, 999999,4, "dane127.csv")
# r3=A.sa(0.8,0.75,False,10000, 999999,4, "dane127.csv")
# r4=A.sa(0.6,0.75,False,10000, 999999,4, "dane127.csv")
# r5=A.sa(1.5,0.75,False,10000, 99999,4, "dane127.csv")
# r6=A.sa(2,0.75,False,10000, 999999,4, "dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "0.9")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "0.8")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "0.6")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "1.5")
# plt.plot(np.linspace(1,len(r6),len(r6)), r6, label = "2")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Start temp")
# plt.ylim(100000,200000)
# plt.legend()
# plt.savefig("SASTARTT127.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 999999,4, "dane127.csv")
# r2=A.sa(1,0.9,False,10000, 999999,4, "dane127.csv")
# r3=A.sa(1,0.1,True,10000, 999999,4, "dane127.csv")
# r4=A.sa(1,0.2,True,10000, 999999,4, "dane127.csv")
# r5=A.sa(1,0.3,True,10000, 99999,4, "dane127.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "0.75")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "0.9")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "0.1g")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "0.2g")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "0.3g")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Temp reduction")
# plt.ylim(100000,200000)
# plt.legend()
# plt.savefig("SAREDT127.jpeg")
# plt.clf()
#
# r1=A.sa(1,0.75,False,1000, 99999,4, "dane48.csv")
# r2=A.sa(1,0.75,False,5000, 99999,4, "dane48.csv")
# r3=A.sa(1,0.75,False,10000, 99999,4, "dane48.csv")
# r4=A.sa(1,0.75,False,50000, 99999,4, "dane48.csv")
# r5=A.sa(1,0.75,False,100000, 99999,4, "dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1000")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "5000")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "10000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "50000")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "100000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Inside Iter")
# plt.ylim(10000,14000)
# plt.legend()
# plt.savefig("SAITER48.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 99999,1, "dane48.csv")
# r2=A.sa(1,0.75,False,10000, 99999,2, "dane48.csv")
# r3=A.sa(1,0.75,False,10000, 99999,3, "dane48.csv")
# r4=A.sa(1,0.75,False,10000, 99999,4, "dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "Double swap")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "Reverse")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "Multiswap")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "All")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Neigh")
# plt.ylim(10000,14000)
# plt.legend()
# plt.savefig("SANEIGH48.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 500,4, "dane48.csv")
# r2=A.sa(1,0.75,False,10000, 1000,4, "dane48.csv")
# r3=A.sa(1,0.75,False,10000, 2000,4, "dane48.csv")
# r4=A.sa(1,0.75,False,10000, 3000,4, "dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "500")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "100")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "2000")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "3000")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA No change")
# plt.ylim(10000,14000)
# plt.legend()
# plt.savefig("SANC48.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 999999,4, "dane48.csv")
# r2=A.sa(0.9,0.75,False,10000, 999999,4, "dane48.csv")
# r3=A.sa(0.8,0.75,False,10000, 999999,4, "dane48.csv")
# r4=A.sa(0.6,0.75,False,10000, 999999,4, "dane48.csv")
# r5=A.sa(1.5,0.75,False,10000, 99999,4, "dane48.csv")
# r6=A.sa(2,0.75,False,10000, 999999,4, "dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "1")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "0.9")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "0.8")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "0.6")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "1.5")
# plt.plot(np.linspace(1,len(r6),len(r6)), r6, label = "2")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Start temp")
# plt.ylim(10000,14000)
# plt.legend()
# plt.savefig("SASTARTT48.jpeg")
# plt.clf()
# r1=A.sa(1,0.75,False,10000, 999999,4, "dane48.csv")
# r2=A.sa(1,0.9,False,10000, 999999,4, "dane48.csv")
# r3=A.sa(1,0.1,True,10000, 999999,4, "dane48.csv")
# r4=A.sa(1,0.2,True,10000, 999999,4, "dane48.csv")
# r5=A.sa(1,0.3,True,10000, 99999,4, "dane48.csv")
# plt.plot(np.linspace(1,len(r1),len(r1)),r1 , label = "0.75")
# plt.plot(np.linspace(1,len(r2),len(r2)), r2, label = "0.9")
# plt.plot(np.linspace(1,len(r3),len(r3)),r3 , label = "0.1g")
# plt.plot(np.linspace(1,len(r4),len(r4)), r4, label = "0.2g")
# plt.plot(np.linspace(1,len(r5),len(r5)), r5, label = "0.3g")
# plt.xlabel("Outside iter")
# plt.ylabel("Distance")
# plt.title("SA Temp reduction")
# plt.ylim(10000,14000)
# plt.legend()
# plt.savefig("SAREDT48.jpeg")
# plt.clf()
