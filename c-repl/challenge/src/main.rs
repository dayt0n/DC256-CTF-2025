use std::{
    fs,
    io::{self, Write},
    path::PathBuf,
    process,
};

use colored::Colorize;
use tempfile::TempDir;

const BANNED_WORDS: &[&str] = &[
    "system", "exec", "read", "open", "flag.txt", "scan", "\\x", "write", "fgets", "fprintf",
];

pub fn prompt(text: &str) -> String {
    let mut ret = String::new();
    print!("{}", text);
    let _ = io::stdout().flush();
    io::stdin().read_line(&mut ret).unwrap();
    ret.trim().to_string()
}

fn do_run(source: String) -> Result<(), Box<dyn std::error::Error>> {
    let tdir = TempDir::new()?;
    let tsrc = tdir.path().join("main.c");
    fs::write(&tsrc, source)?;
    // compile
    let program = tdir.path().join("program");
    let compile_result = process::Command::new("/usr/bin/x86_64-linux-gnu-gcc-13")
        .current_dir(tdir.path())
        .arg("-B")
        .arg("/usr/bin")
        .arg("-no-pie")
        .arg(tsrc)
        .arg("-o")
        .arg(&program)
        .output();
    if let Ok(res) = compile_result {
        if !res.status.success() {
            let stderr = String::from_utf8(res.stderr)?;
            return Err(stderr.into());
        }
        if !program.exists() {
            return Err("file was never compiled...".into());
        }
        // run the program
        let file_data = fs::read(&program)?;
        println!("compiled program: {:02X?}", file_data);
        if let Ok(mut run) = process::Command::new(program).spawn() {
            if !run.wait()?.success() {
                return Err("failed!".into());
            }
            return Ok(());
        }
        return Err("couldn't run the program".into());
    }
    Err("compiler error".into())
}

fn main() {
    let mut source_code = vec![
        String::from(
            "#include <stdio.h>
             #include <string.h>
             #include <stdlib.h>
        int main(int argc, char* argv[]) {
            setvbuf(stdin, NULL, _IONBF, 0);
            setvbuf(stdout, NULL, _IONBF, 0);
            setvbuf(stderr, NULL, _IONBF, 0);
            system(\"echo executing...\");",
        ),
        String::new(),
        String::from(
            "   return 0;
        }",
        ),
    ];
    let mut this_source: Vec<String>;
    let mut input: String;
    'main_loop: loop {
        input = prompt("C> ");
        for word in BANNED_WORDS {
            if input.contains(*word) {
                println!("{}", format!("Illegal word '{}'!", word).bright_red());
                continue 'main_loop;
            }
        }
        this_source = source_code.clone();
        this_source[1] = this_source[1].to_owned() + "\n" + &input;

        let result = do_run(this_source.join("\n"));
        if result.is_ok() {
            source_code = this_source;
        } else {
            println!("error!:\n{}", result.err().unwrap().to_string().red())
        }
    }
}