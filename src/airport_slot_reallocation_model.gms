sets
t  'Total Time Slots'
i  'Arrival Flights'
j  'Departure Flights'
k  'Downstream Flights'
alias(l,k)
;

set
f_pair1(i,j)    'Flight Connection Sets'
$call gdxxrw.exe Excel_file_conncetion_sample.xlsx set=f_pair1 rng=I,J! rdim=2 cdim=0
$gdxin Excelfile_conncetion.gdx
$load f_pair1
$gdxin

f_pair2(j,i)
$call gdxxrw.exe Excel_file_conncetion_sample.xlsx set=f_pair2 rng=J,I! rdim=2 cdim=0
$gdxin Excel_file_conncetion_sample.gdx
$load f_pair2
$gdxin

f_pair3(j,k)
$call gdxxrw.exe Excel_file_conncetion_sample.xlsx set=f_pair3 rng=J,K! rdim=2 cdim=0
$gdxin Excel_file_conncetion_sample.gdx
$load f_pair3
$gdxin

f_pair4(l,k)
$call gdxxrw.exe Excel_file_conncetion_sample.xlsx set=f_pair4 rng=L,K! rdim=2 cdim=0
$gdxin Excel_file_conncetion_sample.gdx
$load f_pair4
$gdxin

f_pair5(k,i)
$call gdxxrw.exe Excel_file_conncetion_sample.xlsx set=f_pair5 rng=K,I! rdim=2 cdim=0
$gdxin Excel_file_conncetion_sample.gdx
$load f_pair5
$gdxin

parameter
s_arr_i(t,i)       'Scheduled Arrivals of Flights Set i'
$call gdxxrw.exe Original_Schedule_Flights.xlsx par=s_arr_i rng=Arrival_I! rdim=1 cdim=1
$gdxin Original_Schedule_Flights.gdx
$load s_arr_i
$gdxin

s_arr_j(t,j)       'Scheduled Arrivals of Flights Set j'
$call gdxxrw.exe Original_Schedule_Flights.xlsx par=s_arr_j rng=Arrival_j! rdim=1 cdim=1
$gdxin Original_Schedule_Flights.gdx
$load s_arr_j
$gdxin

s_arr_k(t,k)       'Scheduled Arrivals of Flights Set k'
$call gdxxrw.exe Original_Schedule_Flights.xlsx par=s_arr_k rng=Arrival_K! rdim=1 cdim=1
$gdxin Original_Schedule_Flights.gdx
$load s_arr_k
$gdxin

s_dep_i(t,i)       'Scheduled Departures of Flights Set i'
$call gdxxrw.exe Original_Schedule_Flights.xlsx par=s_dep_i rng=Departure_I! rdim=1 cdim=1
$gdxin Original_Schedule_Flights.gdx
$load s_dep_i
$gdxin

s_dep_j(t,j)       'Scheduled Departures of Flights Set j'
$call gdxxrw.exe Original_Schedule_Flights.xlsx par=s_dep_j rng=Departure_J! rdim=1 cdim=1
$gdxin Original_Schedule_Flights.gdx
$load s_dep_j
$gdxin

s_dep_k(t,k)       'Scheduled Departures of Flights Set k'
$call gdxxrw.exe Original_Schedule_Flights.xlsx par=s_dep_k rng=Departure_K! rdim=1 cdim=1
$gdxin Original_Schedule_Flights.gdx
$load s_dep_k
$gdxin

t_min              'Minimum Required Connection Time for Two Connected Flights'
t_max              'Maximum Possible Connection Time for Two Connected Flights'

lambda_X           'Maximum Allowable Number of Flights Arriving at the Central Airport in Each Period'
lambda_Y           'Maximum Allowable Number of Flights Departing From the Central Airport in Each Period'
delta_plus         'Maximum Positive Displacements for Every Flight Operating at the Central Airport'
delta_minus        'Maximum Negative Displacements for Every Flight Operating at the Central Airport'
;

free variable
Z_obj
;

nonnegative variable
pd(k)               'The Amount of Propagated Delays for the Downstream Flight k'
;

positive variable
sumdelta_arr        'Total Displacements For Arrival Flights'
sumdelta_dep        'Total Displacements For Departure Flights'
;

binary variable
w_arr_i(t,i)        'Decision Variables Representing the Rescheduled Arrival Time of Flight i'
w_dep_i(t,i)        'Decision Variables Representing the Rescheduled Departure Time of Flight i'
w_arr_j(t,j)        'Decision Variables Representing the Rescheduled Arrival Time of Flight j'
w_dep_j(t,j)        'Decision Variables Representing the Rescheduled Departure Time of Flight j'
w_arr_k(t,k)        'Decision Variables Representing the Rescheduled Arrival Time of Flight k'
w_dep_k(t,k)        'Decision Variables Vepresenting the Rescheduled Departure Time of Flight k'
;

integer variable
up(i)              'Positive Displacements in Arrival Flights'
vp(j)              'Positive Displacements in Departure Flights'
un(i)              'Negative Displacements in Arrival Flights'
vn(j)              'Negative Displacements in Departure Flights'
;

equation
obj

eq2
eq3
eq4
eq5
eq6
eq7

eq8
eq9
eq10
eq11
eq12
eq13

eq14
eq15
eq16
eq17

eq18
eq19

eq201
eq202
eq211
eq212
eq221
eq222
eq231
eq232
eq241
eq242

eq25
eq26

eq27

eq281
eq282
eq283
eq284

eq29
eq30
;

obj                         .. Z_obj=e=sum(i,up(i)+un(i))+sum(j,vp(j)+vn(j))+sum(k,pd(k));

********************************* Scheduling Constraints ***************************************
eq2(i)                      ..w_arr_i('1',i)=e=1;
eq3(j)                      ..w_dep_j('1',j)=e=1;
eq4(j)                      ..w_arr_j('1',j)=e=1;
eq5(k)                      ..w_arr_k('1',k)=e=1;
eq6(i)                      ..w_dep_i('1',i)=e=1;
eq7(k)                      ..w_dep_k('1',k)=e=1;

eq8(i,t)                    ..w_arr_i(t,i)=g=w_arr_i(t+1,i);
eq9(j,t)                    ..w_dep_j(t,j)=g=w_dep_j(t+1,j);
eq10(j,t)                   ..w_arr_j(t,j)=g=w_arr_j(t+1,j);
eq11(k,t)                   ..w_arr_k(t,k)=g=w_arr_k(t+1,k);
eq12(i,t)                   ..w_dep_i(t,i)=g=w_dep_i(t+1,i);
eq13(k,t)                   ..w_dep_k(t,k)=g=w_dep_k(t+1,k);

eq14(i)                     ..sum(t,w_arr_i(t,i)-s_arr_i(t,i))=e=up(i)-un(i);
eq15(i)                     ..sum(t,w_dep_i(t,i)-s_dep_i(t,i))=e=up(i)-un(i);
eq16(j)                     ..sum(t,w_dep_j(t,j)-s_dep_j(t,j))=e=vp(j)-vn(j);
eq17(j)                     ..sum(t,w_arr_j(t,j)-s_arr_j(t,j))=e=vp(j)-vn(j);

eq18(t)                     ..sum(i,w_arr_i(t,i)-w_arr_i(t+1,i))=l= lambda_X;
eq19(t)                     ..sum(j,w_dep_j(t,j)-w_dep_j(t+1,j))=l= lambda_Y;

eq201(i,j)$(f_pair1(i,j))   ..sum(t,w_dep_j(t,j)-w_arr_i(t,i))=g= t_min;
eq202(i,j)$(f_pair1(i,j))   ..sum(t,w_dep_j(t,j)-w_arr_i(t,i))=l= t_max;
eq211(j,i)$(f_pair2(j,i))   ..sum(t,w_dep_i(t,i)-w_arr_j(t,j))=g= t_min;
eq212(j,i)$(f_pair2(j,i))   ..sum(t,w_dep_i(t,i)-w_arr_j(t,j))=l= t_max;
eq221(j,k)$(f_pair3(j,k))   ..sum(t,w_dep_k(t,k)-w_arr_j(t,j))=g= t_min;
eq222(j,k)$(f_pair3(j,k))   ..sum(t,w_dep_k(t,k)-w_arr_j(t,j))=l= t_max;
eq231(l,k)$(f_pair4(l,k))   ..sum(t,w_dep_k(t,k)-w_arr_k(t,l))=g= t_min;
eq232(l,k)$(f_pair4(l,k))   ..sum(t,w_dep_k(t,k)-w_arr_k(t,l))=l= t_max;
eq241(k,i)$(f_pair5(k,i))   ..sum(t,w_dep_i(t,i)-w_arr_k(t,k))=g= t_min;
eq242(k,i)$(f_pair5(k,i))   ..sum(t,w_dep_i(t,i)-w_arr_k(t,k))=l= t_max;

eq25(k)                     ..sum(t,w_dep_k(t,k)-s_dep_k(t,k))=l=pd(k);
eq26(k)                     ..sum(t,w_arr_k(t,k)-s_arr_k(t,k))=e=pd(k);

eq27(k)                     ..sum(t,w_dep_k(t,k))=g=sum(t,s_dep_k(t,k));

eq281(i)                    ..up(i)=l=delta_plus;
eq282(i)                    ..un(i)=l=delta_minus;
eq283(j)                    ..vp(j)=l=delta_plus;
eq284(j)                    ..vn(j)=l=delta_minus;

eq29                        ..sum(i,up(i)+un(i))=e=sumdelta_arr;
eq30                        ..sum(j,vp(j)+vn(j))=e=sumdelta_dep;

********************************* Solving **************************************
model Multiple_Airport /all/
option optca=0;
option optcr=0;
option reslim=10000;
option mip=cplex;
solve Multiple_Airport us mip min Z_obj;

up.l(i)$(up.l(i)=0)=eps;
vp.l(j)$(vp.l(j)=0)=eps;
un.l(i)$(un.l(i)=0)=eps;
vn.l(j)$(vn.l(j)=0)=eps;

display Z_obj.l,up.l,vp.l,un.l,vn.l,sumdelta_arr.l, sumdelta_dep.l, pd.l

