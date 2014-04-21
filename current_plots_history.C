{

  TFile *f1 = TFile::Open("Currents_tree.root");
  TTree *t = (TTree*)f1->Get("T1");

  TFile *f2 = new TFile("outfile.root","RECREATE");

  float current;
  int day,hour,minute,second, disk, chamber; 
  t->SetBranchAddress("Current",&current); 
  t->SetBranchAddress("Day",&day); 
  t->SetBranchAddress("Hour",&hour); 
  t->SetBranchAddress("Minute",&minute); 
  t->SetBranchAddress("Second",&second); 
  t->SetBranchAddress("Disk",&disk); 
  t->SetBranchAddress("Chamber",&chamber); 

  double x[10886], y[10886];
  int i =0;
  for(int ient=0; ient< t->GetEntries(); ient++){
    int nbytes = t->GetEntry(ient);
    if( disk == 2 && chamber == 20 ){
      TDatime da1(2014,4,day,hour,minute,second);
      std::cout << "Day " << day << " hour " << hour << " minute " << minute << " second " << second << std::endl; 
    
      x[i] = da1.Convert();
      y[i] = current;

      i++;
    }
  }

  std::cout << "i " << i << std::endl;

  TDatime T0(2014,4,9,00,00,00);
  int X0 = T0.Convert();
  gStyle->SetTimeOffset(X0);
  
  TCanvas *c1 = new TCanvas();
  TGraph gr(1000,x,y);
  gr.SetMarkerStyle(20);
  TAxis *xaxis = gr.GetXaxis();
  xaxis->SetTimeDisplay(1);
  xaxis->SetNdivisions(10);
  xaxis->SetTimeFormat("%Y-%m-%d %H:%M");
  xaxis->SetTimeOffset(1,"gmt");
  gr.Draw("AP");

//  TGaxis *axis = new TGaxis(-8,-0.6,8,-0.6,-200000,200000,2405,"t");
//  axis->SetLabelSize(0.03);
//
//  c1->cd();
//  TDatime da(2014,04,9,12,00,00);
//  axis->SetTimeOffset(da.Convert());
//  axis->SetTimeFormat("%d\/%m\/%Y");
//  axis->Draw("SAME");

  c1->SaveAs("plots/Disk2_C20_history.png");
  gr.Write();
  f2->Close();
  f1->Close();
  
}
