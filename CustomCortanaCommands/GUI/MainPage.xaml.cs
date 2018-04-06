using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Threading.Tasks;
using Windows.ApplicationModel.Core;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.Storage;
using Windows.System;
using Windows.UI.Popups;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace GUI
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
    }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            CoreApplication.Exit();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string url = "";
            if (cups_text.Text.Length >= 1)
            {
                url = "http://127.0.0.1:5000/api/brew/" + cups_text.Text;
                FetchAsync(url);
            }
            else
            {
                info_box.Text = "Smarter Control " + "Please specify cups of coffee";
            }

            //string url = "http://127.0.0.1:5000/api/brew/" + cups;
            
        }

        public async Task<string> FetchAsync(string url)
        {
            string jsonString;

            using (var httpClient = new System.Net.Http.HttpClient())
            {
                var stream = await httpClient.GetStreamAsync(url);
                StreamReader reader = new StreamReader(stream);
                jsonString = reader.ReadToEnd();
                //stream.Dispose();
            }

            info_box.Text = "Smarter Control " + jsonString;

            //var dialog = new Windows.UI.Popups.MessageDialog(jsonString);
            //dialog.ShowAsync();
            return jsonString;
        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            string url = "";
            url = "http://127.0.0.1:5000/api/reset/";
            FetchAsync(url);

            //info_box.Text = "Smarter Control " + "Default settings applied";

        }
    }
}