package com.example.aaa;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebView;
import android.widget.MediaController;

public class DropBoxActivity extends AppCompatActivity {
    private String s = "https://www.dropbox.com";

    WebView WebView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drop_box);
        WebView = (WebView)findViewById(R.id.view1);

        //JavaScriptを有効化
        WebView.getSettings().setJavaScriptEnabled(true);

        //Web Strageを有効化
        WebView.getSettings().setDomStorageEnabled(true);

        //Hardware Acceleration ON
        getWindow().setFlags(
                WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED,
                WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);

        WebView.loadUrl(s);
    }
}
